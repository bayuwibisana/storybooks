/**
 * Clerk owns identity; this table owns commerce. We mirror the minimum needed
 * to attach purchases and grants, lazily on first sight of a signed-in user —
 * which is why there is no Clerk user-sync webhook.
 *
 * Note: in @clerk/astro, `clerkClient` is a factory taking the request context,
 * not a shared instance. Hence the `ctx` parameter.
 */
import type { APIContext } from 'astro';
import { eq } from 'drizzle-orm';
import { clerkClient } from '@clerk/astro/server';
import type { Db } from './client';
import { users } from './schema';

/** Our internal user id for a Clerk user, creating the row on first sight. */
export async function ensureUser(
  db: Db,
  ctx: APIContext,
  clerkUserId: string,
): Promise<string> {
  const [existing] = await db
    .select({ id: users.id })
    .from(users)
    .where(eq(users.clerkUserId, clerkUserId))
    .limit(1);

  if (existing) return existing.id;

  const cu = await clerkClient(ctx).users.getUser(clerkUserId);
  const email = (
    cu.emailAddresses.find((e) => e.id === cu.primaryEmailAddressId)?.emailAddress ??
    cu.emailAddresses[0]?.emailAddress ??
    ''
  )
    .toLowerCase()
    .trim() || null;
  const name = [cu.firstName, cu.lastName].filter(Boolean).join(' ') || cu.username || null;

  const [row] = await db
    .insert(users)
    .values({ clerkUserId, email, name, imageUrl: cu.imageUrl ?? null })
    .onConflictDoUpdate({
      target: users.clerkUserId,
      set: { email, name, updatedAt: new Date() },
    })
    .returning({ id: users.id });

  return row.id;
}

/**
 * Used by the Lynk webhook: find the account a paid order belongs to.
 * Email is the join key, which is why the checkout flow insists the buyer uses
 * the same address they signed up with.
 */
export async function findUserByEmail(db: Db, email: string) {
  const [row] = await db
    .select({ id: users.id, clerkUserId: users.clerkUserId })
    .from(users)
    .where(eq(users.email, email.toLowerCase().trim()))
    .limit(1);
  return row ?? null;
}
