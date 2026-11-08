import type { APIRoute } from 'astro';
import { db } from '../db/client';
import { stories } from '../db/schema';
import { eq } from 'drizzle-orm';
import { slugifyTitle } from '../lib/story-url';

export const prerender = false;

export const GET: APIRoute = async ({ request }) => {
  const allStories = await db
    .select({
      id: stories.id,
      title: stories.title,
      coverImage: stories.coverImage,
      updatedAt: stories.updatedAt,
    })
    .from(stories)
    .where(eq(stories.isPublished, true));

  const origin = new URL(request.url).origin;

  const staticUrls = [
    { loc: `${origin}/`, priority: '1.0', changefreq: 'daily' },
    { loc: `${origin}/perpustakaan`, priority: '0.9', changefreq: 'daily' },
    { loc: `${origin}/akun`, priority: '0.7', changefreq: 'weekly' },
  ];

  const storyUrls = allStories.map((s) => ({
    loc: `${origin}/baca/${slugifyTitle(s.title)}`,
    lastmod: s.updatedAt ? new Date(s.updatedAt).toISOString() : new Date().toISOString(),
    priority: '0.8',
    changefreq: 'weekly',
    image: `${origin}/${s.coverImage}`,
    title: s.title,
  }));

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
${staticUrls
  .map(
    (u) => `  <url>
    <loc>${u.loc}</loc>
    <changefreq>${u.changefreq}</changefreq>
    <priority>${u.priority}</priority>
  </url>`
  )
  .join('\n')}
${storyUrls
  .map(
    (u) => `  <url>
    <loc>${u.loc}</loc>
    <lastmod>${u.lastmod}</lastmod>
    <changefreq>${u.changefreq}</changefreq>
    <priority>${u.priority}</priority>
    <image:image>
      <image:loc>${u.image}</image:loc>
      <image:title>${u.title.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')}</image:title>
    </image:image>
  </url>`
  )
  .join('\n')}
</urlset>`;

  return new Response(xml, {
    status: 200,
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'Cache-Control': 'public, max-age=86400, s-maxage=86400',
    },
  });
};
