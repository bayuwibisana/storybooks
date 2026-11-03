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

    let stream: any = res.Body;
    if (typeof (res.Body as any)?.transformToWebStream === 'function') {
      stream = (res.Body as any).transformToWebStream();
    } else if (typeof Readable?.toWeb === 'function' && !(stream instanceof ReadableStream)) {
      stream = Readable.toWeb(res.Body as Readable);
    }

    return new Response(stream, {
      status: 200,
      headers: {
        'Content-Type': res.ContentType || 'audio/wav',
        ...(res.ContentLength ? { 'Content-Length': String(res.ContentLength) } : {}),
        'Cache-Control': 'public, max-age=31536000, immutable',
        ...(res.ETag ? { 'ETag': res.ETag } : {}),
      },
    });
  } catch (err: any) {
    console.error(`Error streaming ${r2Key} from R2:`, err);
    return new Response(`Error fetching from R2: ${err?.message || String(err)}`, { status: 500 });
  }
};
