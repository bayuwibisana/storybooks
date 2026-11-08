/**
 * Grant full access or tier to a user by email.
 *
 * Usage:
 *   node scripts/grant_access.mjs <email> [tier=sahabat]
 *
 * Example:
 *   node scripts/grant_access.mjs bayuwibisana15@gmail.com sahabat
 */
import path from 'node:path';
import { config } from 'dotenv';
import { neon } from '@neondatabase/serverless';

config({ path: path.resolve(process.cwd(), '.env') });

if (!process.env.DATABASE_URL) {
  console.error('DATABASE_URL is not set in .env');
  process.exit(1);
}

const email = process.argv[2]?.trim().toLowerCase();
const tier = process.argv[3]?.trim().toLowerCase() || 'sahabat';

if (!email) {
  console.error('Harap sertakan email tujuan: node scripts/grant_access.mjs <email> [tier]');
  process.exit(1);
}

const sql = neon(process.env.DATABASE_URL);

console.log(`Mengaktifkan akses penuh (${tier}) untuk email: ${email}...`);

const updated = await sql`
  UPDATE users
  SET has_all_access = true,
      highest_tier = ${tier},
      updated_at = NOW()
  WHERE LOWER(email) = ${email}
  RETURNING id, clerk_user_id, email, name, has_all_access, highest_tier;
`;

if (updated.length === 0) {
  console.log(`⚠️  Pengguna dengan email "${email}" belum terdaftar di tabel users.`);
  console.log('   Pengguna perlu login terlebih dahulu minimal sekali di website agar akun Clerk tersinkron ke database.');
} else {
  console.log(`✅ Berhasil memberikan akses penuh ke ${updated.length} akun:`);
  console.table(updated);
}
