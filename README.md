# Kisah Krayon Web Platform

Aplikasi web pembaca buku cerita anak bergambar **Kisah Krayon** (105 buku bedtime picture books).

## Stack & Arsitektur
- **Framework**: Astro 5 SSR (`@astrojs/cloudflare`)
- **Runtime**: Cloudflare Workers / Pages dengan `nodejs_compat`
- **Node**: `>=22.23.4` (lihat `.nvmrc`)
- **Database**: Neon Postgres Serverless dengan Drizzle ORM
- **Autentikasi**: Clerk (`@clerk/astro`)
- **Payment Gateway**: Lynk.id (One-time payment packages)
- **Asset Storage**: Cloudflare R2 (`kisah-krayon`) via Astro SSR streaming endpoints (`/covers`, `/pages`, `/audio`)

## Environment Variables Wajib (Cloudflare Settings)
Tambahkan variabel berikut di **Cloudflare Dashboard > Settings > Variables and Secrets**:
- `DATABASE_URL`: Connection string pooled dari Neon Postgres
- `DATABASE_URL_UNPOOLED`: Connection string unpooled dari Neon Postgres
- `PUBLIC_CLERK_PUBLISHABLE_KEY`: Public key Clerk (`pk_test_...`)
- `CLERK_SECRET_KEY`: Secret key Clerk (`sk_test_...`)
- `PUBLIC_SITE_URL`: Domain produksi (misal: `https://storybooks.bayuwibisana15.workers.dev`)
- `R2_ACCOUNT_ID`: Cloudflare Account ID
- `R2_ACCESS_KEY_ID`: R2 Access Key ID
- `R2_SECRET_ACCESS_KEY`: R2 Secret Access Key
- `R2_BUCKET`: `kisah-krayon`
- `PUBLIC_ENABLE_AUDIO`: `true`

## Jalankan Lokal
```bash
npm install
npm run dev
# Buka http://localhost:4321
```
