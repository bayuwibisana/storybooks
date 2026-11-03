import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';
import { getEnv } from './env';

export async function getR2Object(key: string) {
  console.log('[r2.ts] getR2Object called for:', key, 'isDev:', import.meta.env.DEV);
  // 1. In production Cloudflare Workers: Use native R2 bucket binding (zero credentials, internal edge speed)
  if (!import.meta.env.DEV) {
    try {
      const cf = await import('cloudflare:workers');
      const binding = (cf.env as any)?.R2_BUCKET_BINDING || (cf.env as any)?.kisah_krayon || (cf.env as any)?.R2;
      if (binding && typeof binding.get === 'function') {
        const object = await binding.get(key);
        if (object) {
          return {
            Body: object.body, // Native ReadableStream
            ContentType: object.httpMetadata?.contentType || (key.endsWith('.wav') ? 'audio/wav' : 'image/jpeg'),
            ContentLength: object.size,
            ETag: object.httpEtag,
          };
        }
      }
    } catch {
      // Fall through to S3 SDK if native binding fails
    }
  }

  // 2. In local dev or fallback: Fetch from Cloudflare R2 via AWS S3 SDK
  try {
    const accountId = getEnv('R2_ACCOUNT_ID') || '425148ed4de08261ce3f2cdf337752f2';
    const accessKeyId = getEnv('R2_ACCESS_KEY_ID') || getEnv('S3_ACCESS_ID') || '';
    const secretAccessKey = getEnv('R2_SECRET_ACCESS_KEY') || getEnv('S3_SECRET_KEY') || '';
    const bucket = getEnv('R2_BUCKET') || 'kisah-krayon';

    if (accessKeyId && secretAccessKey) {
      const client = new S3Client({
        region: 'auto',
        endpoint: `https://${accountId}.r2.cloudflarestorage.com`,
        credentials: {
          accessKeyId,
          secretAccessKey,
        },
      });

      const command = new GetObjectCommand({
        Bucket: bucket,
        Key: key,
      });
      const res = await client.send(command);
      if (res && res.Body) {
        return res;
      }
    }
  } catch (err: any) {
    if (err.name !== 'NoSuchKey' && err.$metadata?.httpStatusCode !== 404) {
      console.warn(`[r2.ts] S3 SDK error for ${key}:`, err?.message || err);
    }
  }

  // 3. Ultimate local fallback: If local file exists on disk in preview/
  if (import.meta.env.DEV) {
    try {
      const fs = await import('node:fs/promises');
      const path = await import('node:path');
      const localFilePath = key.startsWith('covers/') || key.startsWith('pages/')
        ? path.resolve(process.cwd(), '../preview/images', path.basename(key))
        : path.resolve(process.cwd(), '../preview', key);

      const stat = await fs.stat(localFilePath).catch(() => null);
      if (stat && stat.isFile()) {
        const buffer = await fs.readFile(localFilePath);
        return {
          Body: buffer,
          ContentType: key.endsWith('.wav') ? 'audio/wav' : 'image/jpeg',
          ContentLength: stat.size,
          ETag: `"${stat.mtimeMs}"`,
        };
      }
    } catch {}
  }

  return null;
}
