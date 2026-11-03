import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';
import type { Readable } from 'node:stream';

const accountId = import.meta.env.R2_ACCOUNT_ID || '425148ed4de08261ce3f2cdf337752f2';
const accessKeyId = import.meta.env.R2_ACCESS_KEY_ID || import.meta.env.S3_ACCESS_ID;
const secretAccessKey = import.meta.env.R2_SECRET_ACCESS_KEY || import.meta.env.S3_SECRET_KEY;
export const R2_BUCKET = import.meta.env.R2_BUCKET || 'kisah-krayon';

export const r2Client = new S3Client({
  region: 'auto',
  endpoint: `https://${accountId}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId,
    secretAccessKey,
  },
});

export async function getR2Object(key: string) {
  try {
    const command = new GetObjectCommand({
      Bucket: R2_BUCKET,
      Key: key,
    });
    const res = await r2Client.send(command);
    return res;
  } catch (err: any) {
    if (err.name === 'NoSuchKey' || err.$metadata?.httpStatusCode === 404) {
      return null;
    }
    throw err;
  }
}
