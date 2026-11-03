import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';
import { getEnv } from './env';

export async function getR2Object(key: string) {
  // 1. First attempt: Native Cloudflare R2 bucket binding (zero credentials, internal edge speed)
  try {
    const cf = await import('cloudflare:workers');
    const binding = (cf.env as any)?.R2_BUCKET_BINDING || (cf.env as any)?.kisah_krayon || (cf.env as any)?.R2;
    if (binding && typeof binding.get === 'function') {
      const object = await binding.get(key);
      if (!object) return null;
      return {
        Body: object.body, // Native ReadableStream
        ContentType: object.httpMetadata?.contentType || (key.endsWith('.wav') ? 'audio/wav' : 'image/jpeg'),
        ContentLength: object.size,
        ETag: object.httpEtag,
      };
    }
  } catch {
    // If not in Cloudflare Worker environment with R2 binding, fallback to AWS S3 SDK
  }

  // 2. Second attempt: AWS S3 SDK (used for local development)
  try {
    const accountId = getEnv('R2_ACCOUNT_ID') || '425148ed4de08261ce3f2cdf337752f2';
    const accessKeyId = getEnv('R2_ACCESS_KEY_ID') || getEnv('S3_ACCESS_ID') || '';
    const secretAccessKey = getEnv('R2_SECRET_ACCESS_KEY') || getEnv('S3_SECRET_KEY') || '';
    const bucket = getEnv('R2_BUCKET') || 'kisah-krayon';

    if (!accessKeyId || !secretAccessKey) {
      throw new Error(`R2 credentials missing (R2_ACCESS_KEY_ID: ${Boolean(accessKeyId)}, R2_SECRET_ACCESS_KEY: ${Boolean(secretAccessKey)})`);
    }

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
    return res;
  } catch (err: any) {
    if (err.name === 'NoSuchKey' || err.$metadata?.httpStatusCode === 404) {
      return null;
    }
    throw err;
  }
}
