export const prerender = false;

import type { APIRoute } from 'astro';
import { db } from '../../../db/client';
import { grantStory } from '../../../db/entitlements';
import { getViewer } from '../../../lib/session';

export const POST: APIRoute = async (ctx) => {
  const viewer = await getViewer(ctx);
  if (!viewer.signedIn || !viewer.userId) {
    return new Response(JSON.stringify({ error: 'Silakan masuk terlebih dahulu' }), {
      status: 401,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  let storyId: string | null = null;
  const contentType = ctx.request.headers.get('content-type') || '';
  if (contentType.includes('application/json')) {
    const body = await ctx.request.json().catch(() => ({}));
    storyId = body.storyId;
  } else if (contentType.includes('application/x-www-form-urlencoded')) {
    const formData = await ctx.request.formData();
    storyId = formData.get('storyId')?.toString() || null;
  }

  if (!storyId) {
    return new Response(JSON.stringify({ error: 'storyId diperlukan' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  const ok = await grantStory(db, viewer.userId, storyId);
  if (!ok) {
    return new Response(JSON.stringify({ error: 'Kredit cerita tidak mencukupi' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  if (contentType.includes('application/x-www-form-urlencoded')) {
    return ctx.redirect(`/baca/${storyId}`);
  }

  return new Response(JSON.stringify({ success: true }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  });
};
