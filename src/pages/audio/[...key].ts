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

    let body: any = res.Body;
    if (typeof (body as any)?.transformToWebStream === 'function') {
      body = (body as any).transformToWebStream();
    } else if (typeof Readable?.toWeb === 'function' && !(body instanceof ReadableStream) && !(body instanceof Uint8Array) && !(body instanceof Buffer)) {
      body = Readable.toWeb(body as Readable);
    }

    return new Response(body, {
      status: 200,
      headers: {
        'Content-Type': res.ContentType || 'audio/wav',
        ...(res.ContentLength ? { 'Content-Length': String(res.ContentLength) } : {}),
        'Cache-Control': 'public, max-age=31536000, immutable',
        ...(res.ETag ? { 'ETag': res.ETag } : {}),
      },
    });
  } catch (err: any) {
    console.error(`Error streaming ${r2Key}:`, err);
    return new Response(`Error fetching from R2: ${err?.message || String(err)}`, { status: 500 });
  }
};
