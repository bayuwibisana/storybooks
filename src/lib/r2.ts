import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';
import { getEnv } from './env';

let _r2Client: S3Client | null = null;

export function getR2Client(): S3Client {
  if (_r2Client) return _r2Client;
  const accountId = getEnv('R2_ACCOUNT_ID') || '425148ed4de08261ce3f2cdf337752f2';
  const accessKeyId = getEnv('R2_ACCESS_KEY_ID') || getEnv('S3_ACCESS_ID') || '';
  const secretAccessKey = getEnv('R2_SECRET_ACCESS_KEY') || getEnv('S3_SECRET_KEY') || '';

  _r2Client = new S3Client({
    region: 'auto',
    endpoint: `https://${accountId}.r2.cloudflarestorage.com`,
    credentials: {
      accessKeyId,
      secretAccessKey,
    },
  });
  return _r2Client;
}

export async function getR2Object(key: string) {
  try {
    const bucket = getEnv('R2_BUCKET') || 'kisah-krayon';
    const client = getR2Client();
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
