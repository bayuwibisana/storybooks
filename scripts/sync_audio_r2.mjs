import fs from 'node:fs/promises';
import path from 'node:path';
import { S3Client, PutObjectCommand, HeadObjectCommand } from '@aws-sdk/client-s3';
import dotenv from 'dotenv';

dotenv.config();

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

async function getWavFiles(dir) {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  let files = [];
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files = files.concat(await getWavFiles(fullPath));
    } else if (entry.isFile() && entry.name.endsWith('.wav')) {
      files.push(fullPath);
    }
  }
  return files;
}

async function uploadAudioFiles() {
  const wavFiles = await getWavFiles(audioBase);
  console.log(`Found ${wavFiles.length} audio files in preview/audio/`);

  let uploaded = 0;
  let skipped = 0;
  let errors = 0;

  for (const filePath of wavFiles) {
    const rel = path.relative(audioBase, filePath).replace(/\\/g, '/');
    const r2Key = `audio/${rel}`;
    const stats = await fs.stat(filePath);

    try {
      // Check if already in R2 with same size
      const head = await client.send(new HeadObjectCommand({ Bucket: bucket, Key: r2Key }));
      if (head.ContentLength === stats.size) {
        skipped++;
        continue;
      }
    } catch (err) {
      // Not found, will upload
    }

    try {
      const buffer = await fs.readFile(filePath);
      await client.send(
        new PutObjectCommand({
          Bucket: bucket,
          Key: r2Key,
          Body: buffer,
          ContentType: 'audio/wav',
          CacheControl: 'public, max-age=31536000, immutable',
        })
      );
      console.log(`[UPLOADED] ${r2Key} (${stats.size} bytes)`);
      uploaded++;
    } catch (err) {
      console.error(`[ERROR] ${r2Key}:`, err.message);
      errors++;
    }
  }

  console.log(`\n✨ Selesai sinkronisasi R2 Audio!`);
  console.log(`Total: ${wavFiles.length} | Terupload baru: ${uploaded} | Sudah ada: ${skipped} | Gagal: ${errors}`);
}

uploadAudioFiles().catch(console.error);
