import type { APIRoute } from 'astro';
import { Readable } from 'node:stream';
import { getR2Object } from '../../lib/r2';

export const prerender = false;

export const GET: APIRoute = async ({ params }) => {
  const filename = params.key;
  if (!filename) {
    return new Response('Not found', { status: 404 });
  }

  const r2Key = `audio/${filename}`;
  try {
    const res = await getR2Object(r2Key);
    if (!res || !res.Body) {
      return new Response(`Audio not found in R2: ${r2Key}`, { status: 404 });
    }

    let body: unknown = res.Body;
    const rawBody: unknown = res.Body;
    if (rawBody && typeof rawBody === 'object' && 'transformToWebStream' in rawBody && typeof (rawBody as { transformToWebStream: () => unknown }).transformToWebStream === 'function') {
      body = (rawBody as { transformToWebStream: () => unknown }).transformToWebStream();
    } else if (typeof Readable?.toWeb === 'function' && rawBody && !(rawBody instanceof Uint8Array) && !(rawBody instanceof ReadableStream)) {
      body = Readable.toWeb(rawBody as Readable);
    }

    const contentType = filename.endsWith('.m4a') ? 'audio/mp4' : (res.ContentType || 'audio/wav');

    return new Response(body as unknown as BodyInit, {
      status: 200,
      headers: {
        'Content-Type': contentType,
        ...(res.ContentLength ? { 'Content-Length': String(res.ContentLength) } : {}),
        'Cache-Control': 'public, max-age=31536000, immutable',
        ...(res.ETag ? { 'ETag': res.ETag } : {}),
      },
    });
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : String(err);
    console.error(`Error streaming ${r2Key}:`, message);
    return new Response(`Error fetching from R2: ${message}`, { status: 500 });
  }
};
