/**
 * Entitlement resolution — the one place that decides "can this user read this
 * page". Routes must never re-implement this logic; they call these helpers and
 * return 404 (not 403) for gated pages so a locked story is indistinguishable
 * from a missing one to someone poking at the API.
 */
import { and, eq, isNull, sql } from 'drizzle-orm';
import type { Db } from './client';
import { entitlements, stories, storyGrants, users } from './schema';

export type AccessLevel = 'free' | 'granted' | 'locked';

export interface ViewerAccess {
  signedIn: boolean;
  /** our internal users.id — null when signed out */
  userId: string | null;
  hasAllAccess: boolean;
  storyCredits: number;
  grantedStoryIds: Set<string>;
  /** tier of the active all_access entitlement, used to price upgrades */
  highestTier: string | null;
}

export const ANONYMOUS: ViewerAccess = {
  signedIn: false,
  userId: null,
  hasAllAccess: false,
  storyCredits: 0,
  grantedStoryIds: new Set(),
  highestTier: null,
};

/** Call once per request and stash on locals; do not call it per component. */
export async function loadViewerAccess(
  db: Db,
  internalUserId: string | null,
): Promise<ViewerAccess> {
  if (!internalUserId) return ANONYMOUS;

  const [user] = await db
    .select({
      id: users.id,
      hasAllAccess: users.hasAllAccess,
      storyCredits: users.storyCredits,
      highestTier: users.highestTier,
    })
    .from(users)
    .where(and(eq(users.id, internalUserId), isNull(users.deletedAt)))
    .limit(1);

  if (!user) return { ...ANONYMOUS, signedIn: true };

  const [grants, active] = await Promise.all([
    db
      .select({ storyId: storyGrants.storyId })
      .from(storyGrants)
      .where(eq(storyGrants.userId, user.id)),
    db
      .select({ kind: entitlements.kind, credits: entitlements.credits })
      .from(entitlements)
      .where(and(eq(entitlements.userId, user.id), eq(entitlements.isActive, true))),
  ]);

  const credits = active
    .filter((e) => e.kind === 'credit')
    .reduce((sum, e) => sum + (e.credits ?? 0), 0);

  return {
    signedIn: true,
    userId: user.id,
    hasAllAccess: user.hasAllAccess || active.some((e) => e.kind === 'all_access'),
    storyCredits: credits,
    grantedStoryIds: new Set(grants.map((g) => g.storyId)),
    highestTier: user.highestTier ?? null,
  };
}

export function accessLevel(
  story: { id: string; isFree: boolean },
  viewer: ViewerAccess,
): AccessLevel {
  if (story.isFree) return 'free';
  if (!viewer.signedIn) return 'locked';
  if (viewer.hasAllAccess) return 'granted';
  if (viewer.grantedStoryIds.has(story.id)) return 'granted';
  return 'locked';
}

/** Burn one credit into a permanent grant. Returns false when out of credits. */
export async function grantStory(
  db: Db,
  userId: string,
  storyId: string,
): Promise<boolean> {
  return db.transaction(async (tx) => {
    const [credit] = await tx
      .select({ id: entitlements.id, credits: entitlements.credits })
      .from(entitlements)
      .where(
        and(
          eq(entitlements.userId, userId),
          eq(entitlements.kind, 'credit'),
          eq(entitlements.isActive, true),
          sql`${entitlements.credits} > 0`,
        ),
      )
      .orderBy(sql`${entitlements.createdAt} asc`)
      .limit(1)
      .for('update');

    if (!credit) return false;

    const inserted = await tx
      .insert(storyGrants)
      .values({ userId, storyId, entitlementId: credit.id })
      .onConflictDoNothing()
      .returning({ id: storyGrants.id });

    // Already granted: do not spend a second credit.
    if (inserted.length === 0) return true;

    await tx
      .update(entitlements)
      .set({ credits: sql`${entitlements.credits} - 1` })
      .where(eq(entitlements.id, credit.id));

    await tx
      .update(users)
      .set({ storyCredits: sql`${users.storyCredits} - 1`, updatedAt: new Date() })
      .where(eq(users.id, userId));

    return true;
  });
}

/**
 * Which stories a user may read. Free stories are always included; everything
 * else needs all_access or an explicit grant. Returns slugs so a page can gate
 * in one query.
 */
export async function readableStoryIds(
  db: Db,
  viewer: ViewerAccess,
): Promise<Set<string>> {
  if (viewer.hasAllAccess) {
    const all = await db
      .select({ id: stories.id })
      .from(stories)
      .where(eq(stories.isPublished, true));
    return new Set(all.map((s) => s.id));
  }
  const free = await db
    .select({ id: stories.id })
    .from(stories)
    .where(and(eq(stories.isPublished, true), eq(stories.isFree, true)));
  const set = new Set(free.map((s) => s.id));
  for (const id of viewer.grantedStoryIds) set.add(id);
  return set;
}
