import fs from 'node:fs/promises';
import path from 'node:path';
import { S3Client, PutObjectCommand, HeadObjectCommand } from '@aws-sdk/client-s3';
import dotenv from 'dotenv';

dotenv.config({ path: path.resolve(process.cwd(), '.env') });

const accountId = process.env.R2_ACCOUNT_ID || '425148ed4de08261ce3f2cdf337752f2';
const accessKeyId = process.env.R2_ACCESS_KEY_ID || process.env.S3_ACCESS_ID || '';
const secretAccessKey = process.env.R2_SECRET_ACCESS_KEY || process.env.S3_SECRET_KEY || '';
const bucket = process.env.R2_BUCKET || 'kisah-krayon';

if (!accessKeyId || !secretAccessKey) {
  console.error('R2 credentials missing!');
  process.exit(1);
}

const client = new S3Client({
  region: 'auto',
  endpoint: `https://${accountId}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId,
    secretAccessKey,
  },
});

const imagesBase = path.resolve(process.cwd(), '../preview/images');
const thumbsBase = path.resolve(process.cwd(), '../preview/thumbnails');

async function getFiles(dir, filterFn) {
  try {
    const entries = await fs.readdir(dir, { withFileTypes: true });
    return entries
      .filter((e) => e.isFile() && filterFn(e.name))
      .map((e) => path.join(dir, e.name));
  } catch {
    return [];
  }
}

async function uploadFile(filePath, r2Key, contentType) {
  const stats = await fs.stat(filePath);
  try {
    const head = await client.send(new HeadObjectCommand({ Bucket: bucket, Key: r2Key }));
    if (head.ContentLength === stats.size) {
      return { status: 'skipped', key: r2Key, size: stats.size };
    }
  } catch (err) {
    // File doesn't exist or size mismatch -> proceed to upload
  }

  const buffer = await fs.readFile(filePath);
  await client.send(
    new PutObjectCommand({
      Bucket: bucket,
      Key: r2Key,
      Body: buffer,
      ContentType: contentType,
      CacheControl: 'public, max-age=31536000, immutable',
    })
  );
  return { status: 'uploaded', key: r2Key, size: stats.size };
}

async function runConcurrently(tasks, limit = 12) {
  const results = [];
  let index = 0;

  async function worker() {
    while (index < tasks.length) {
      const cur = index++;
      const res = await tasks[cur]();
      results[cur] = res;
    }
  }

  const workers = Array.from({ length: Math.min(limit, tasks.length) }, () => worker());
  await Promise.all(workers);
  return results;
}

async function syncImages() {
  const coverFiles = await getFiles(imagesBase, (n) => n.endsWith('_cover.jpg'));
  const pageFiles = await getFiles(imagesBase, (n) => n.includes('_page') && n.endsWith('.jpg'));
  const thumbFiles = await getFiles(thumbsBase, (n) => n.endsWith('.jpg') || n.endsWith('.webp'));

  console.log(`Found ${coverFiles.length} covers, ${pageFiles.length} pages, ${thumbFiles.length} thumbnails.`);

  const tasks = [];

  for (const f of coverFiles) {
    const r2Key = `covers/${path.basename(f)}`;
    tasks.push(() => uploadFile(f, r2Key, 'image/jpeg'));
  }

  for (const f of pageFiles) {
    const r2Key = `pages/${path.basename(f)}`;
    tasks.push(() => uploadFile(f, r2Key, 'image/jpeg'));
  }

  for (const f of thumbFiles) {
    const isWebp = f.endsWith('.webp');
    const r2Key = `thumbnails/covers/${path.basename(f)}`;
    tasks.push(() => uploadFile(f, r2Key, isWebp ? 'image/webp' : 'image/jpeg'));
  }

  console.log(`Starting sync for ${tasks.length} objects to R2 bucket "${bucket}" with concurrency 12...`);
  const t0 = Date.now();

  let uploadedCount = 0;
  let skippedCount = 0;
  let uploadedBytes = 0;

  const results = await runConcurrently(
    tasks.map((task) => async () => {
      const res = await task();
      if (res.status === 'uploaded') {
        uploadedCount++;
        uploadedBytes += res.size;
        if (uploadedCount % 25 === 0 || uploadedCount === 1) {
          console.log(`[PROGRESS] Uploaded ${uploadedCount} objects... (last: ${res.key}, ${(res.size / 1024).toFixed(1)} KB)`);
        }
      } else {
        skippedCount++;
      }
      return res;
    }),
    12
  );

  const t1 = Date.now();
  console.log('\n============================================================');
  console.log(`✨ R2 IMAGE SYNC COMPLETED in ${((t1 - t0) / 1000).toFixed(1)}s!`);
  console.log(`Total Objects:    ${results.length}`);
  console.log(`Uploaded/Updated: ${uploadedCount} (${(uploadedBytes / (1024 * 1024)).toFixed(2)} MB transferred)`);
  console.log(`Skipped (Unchanged): ${skippedCount}`);
  console.log('============================================================');
}

syncImages().catch(console.error);
