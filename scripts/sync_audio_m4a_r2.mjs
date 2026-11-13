import fs from 'node:fs/promises';
import path from 'node:path';
import { S3Client, PutObjectCommand, DeleteObjectsCommand, ListObjectsV2Command, HeadObjectCommand } from '@aws-sdk/client-s3';
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

const audioBase = path.resolve(process.cwd(), '../preview/audio');

async function getM4aFiles(dir) {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  let files = [];
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files = files.concat(await getM4aFiles(fullPath));
    } else if (entry.isFile() && entry.name.endsWith('.m4a')) {
      files.push(fullPath);
    }
  }
  return files;
}

async function uploadFile(filePath, r2Key) {
  const stats = await fs.stat(filePath);
  try {
    const head = await client.send(new HeadObjectCommand({ Bucket: bucket, Key: r2Key }));
    if (head.ContentLength === stats.size) {
      return { status: 'skipped', key: r2Key, size: stats.size };
    }
  } catch (err) {
    // Needs upload
  }

  const buffer = await fs.readFile(filePath);
  await client.send(
    new PutObjectCommand({
      Bucket: bucket,
      Key: r2Key,
      Body: buffer,
      ContentType: 'audio/mp4',
      CacheControl: 'public, max-age=31536000, immutable',
    })
  );
  return { status: 'uploaded', key: r2Key, size: stats.size };
}

async function runConcurrently(tasks, limit = 16) {
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

async function syncAndCleanAudio() {
  const m4aFiles = await getM4aFiles(audioBase);
  console.log(`Found ${m4aFiles.length} M4A audio files to upload...`);

  const uploadTasks = m4aFiles.map((filePath) => {
    const rel = path.relative(audioBase, filePath).replace(/\\/g, '/');
    const r2Key = `audio/${rel}`;
    return () => uploadFile(filePath, r2Key);
  });

  let uploadedCount = 0;
  let uploadedBytes = 0;

  const t0 = Date.now();
  await runConcurrently(
    uploadTasks.map((t) => async () => {
      const res = await t();
      if (res.status === 'uploaded') {
        uploadedCount++;
        uploadedBytes += res.size;
        if (uploadedCount % 25 === 0 || uploadedCount === 1) {
          console.log(`[PROGRESS] Uploaded ${uploadedCount} M4A audio files... (${(uploadedBytes / (1024 * 1024)).toFixed(2)} MB)`);
        }
      }
      return res;
    }),
    16
  );

  console.log(`\n✨ Uploaded ${uploadedCount} M4A files (${(uploadedBytes / (1024 * 1024)).toFixed(2)} MB) in ${((Date.now() - t0) / 1000).toFixed(1)}s.`);

  // Clean up old WAV and temporary compressed audio from R2
  console.log('\nCleaning up old WAV files from R2...');
  let token = undefined;
  const toDelete = [];

  do {
    const res = await client.send(
      new ListObjectsV2Command({
        Bucket: bucket,
        Prefix: 'audio/',
        ContinuationToken: token,
      })
    );
    if (res.Contents) {
      for (const obj of res.Contents) {
        if (obj.Key.endsWith('.wav') || obj.Key.includes('story1_compressed/')) {
          toDelete.push({ Key: obj.Key });
        }
      }
    }
    token = res.NextContinuationToken;
  } while (token);

  console.log(`Found ${toDelete.length} obsolete WAV / temporary test objects to delete from R2...`);

  // Batch delete in chunks of 500 (S3 limit is 1000)
  for (let i = 0; i < toDelete.length; i += 500) {
    const chunk = toDelete.slice(i, i + 500);
    await client.send(
      new DeleteObjectsCommand({
        Bucket: bucket,
        Delete: { Objects: chunk },
      })
    );
    console.log(`Deleted ${chunk.length} obsolete objects from R2.`);
  }

  console.log('\n============================================================');
  console.log('✨ CLOUDFLARE R2 AUDIO CLEANUP & M4A SYNC COMPLETE!');
  console.log('============================================================');
}

syncAndCleanAudio().catch(console.error);
