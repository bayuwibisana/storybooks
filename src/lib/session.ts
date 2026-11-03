/**
 * Per-request session resolution. Call `getViewer(Astro)` from a page or an API
 * route; the result is memoised on `Astro.locals` so a layout plus a page plus a
 * nested component all pay for one set of queries.
 */
import type { APIContext } from 'astro';
import { db } from '../db/client';
import { loadViewerAccess, type ViewerAccess } from '../db/entitlements';
import { ensureUser } from '../db/users';

export async function getViewer(ctx: APIContext): Promise<ViewerAccess> {
  const cached = ctx.locals.viewer;
  if (cached) return cached;

  const { userId: clerkUserId } = ctx.locals.auth();

  // Mirror the Clerk user into our table on first sight, so purchases and
  // grants have something to attach to.
  const internalUserId = clerkUserId ? await ensureUser(db, ctx, clerkUserId) : null;
  const viewer = await loadViewerAccess(db, internalUserId);

  ctx.locals.viewer = viewer;
  return viewer;
}
