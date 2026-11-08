/**
 * Seed Neon from preview/stories.json.
 *
 * Idempotent: stories upsert on id, pages are replaced per story. Re-running is
 * safe and is how you ship text edits without duplicating rows.
 *
 * IMPORTANT: imagePrompt is deliberately dropped. It is the prompt formula —
 * internal IP — and must never be stored where the app can read it out, let
 * alone shipped to a browser.
 *
 * Image keys are stored as R2 object keys, not URLs:
 *   covers/story1_cover.jpg
 *   pages/story1_page1.jpg
 */
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { config } from 'dotenv';
import { neon } from '@neondatabase/serverless';

config({ path: path.resolve(process.cwd(), '.env') });

if (!process.env.DATABASE_URL) {
  console.error('DATABASE_URL is not set');
  process.exit(1);
}

const sql = neon(process.env.DATABASE_URL);
const REPO = path.resolve(process.cwd(), '..');
const STORIES = JSON.parse(await readFile(path.join(REPO, 'preview/stories.json'), 'utf8'));

const FREE_STORIES = 3;

const PRODUCTS = [
  { slug: 'kecil',   name: 'Paket Kecil — 10 cerita pilihan', priceIdr: 15000, tier: 'kecil',   scopeKind: 'story_count', scopeCount: 10, isUpgrade: false, upgradeFrom: null,      sortOrder: 1, isActive: true },
  { slug: 'plus',    name: 'Paket Plus — 20 cerita pilihan',  priceIdr: 29000, tier: 'plus',    scopeKind: 'story_count', scopeCount: 20, isUpgrade: false, upgradeFrom: null,      sortOrder: 2, isActive: false },
  { slug: 'lengkap', name: 'Paket Lengkap — 40 cerita saat ini', priceIdr: 49000, tier: 'lengkap', scopeKind: 'all_access',  scopeCount: null, isUpgrade: false, upgradeFrom: null,    sortOrder: 3, isActive: true },
  { slug: 'sahabat', name: 'Paket Sahabat — Semua Cerita + Update Tiap Minggu Selamanya', priceIdr: 79000, tier: 'sahabat', scopeKind: 'all_access', scopeCount: null, isUpgrade: false, upgradeFrom: null, sortOrder: 4, isActive: true },
  // Upgrade SKUs: visible only to entitled users. Priced at the difference so
  // an early buyer never pays more than a direct buyer.
  { slug: 'upgrade-kecil-lengkap',   name: 'Upgrade Kecil → Lengkap (40 Cerita)', priceIdr: 34000, tier: 'lengkap', scopeKind: 'all_access', scopeCount: null, isUpgrade: true, upgradeFrom: 'kecil',   sortOrder: 10, isActive: true },
  { slug: 'upgrade-kecil-sahabat',   name: 'Upgrade Kecil → Sahabat (Update Tiap Minggu)', priceIdr: 64000, tier: 'sahabat', scopeKind: 'all_access', scopeCount: null, isUpgrade: true, upgradeFrom: 'kecil',   sortOrder: 11, isActive: true },
  { slug: 'upgrade-plus-lengkap',    name: 'Upgrade Plus → Lengkap (40 Cerita)', priceIdr: 20000, tier: 'lengkap', scopeKind: 'all_access', scopeCount: null, isUpgrade: true, upgradeFrom: 'plus',    sortOrder: 12, isActive: true },
  { slug: 'upgrade-plus-sahabat',    name: 'Upgrade Plus → Sahabat (Update Tiap Minggu)', priceIdr: 50000, tier: 'sahabat', scopeKind: 'all_access', scopeCount: null, isUpgrade: true, upgradeFrom: 'plus',    sortOrder: 13, isActive: true },
  { slug: 'upgrade-lengkap-sahabat', name: 'Upgrade Lengkap → Sahabat (Update Tiap Minggu)', priceIdr: 30000, tier: 'sahabat', scopeKind: 'all_access', scopeCount: null, isUpgrade: true, upgradeFrom: 'lengkap', sortOrder: 14, isActive: true },
];

// "images/story1_page1.jpg" -> "pages/story1_page1.jpg"
const toKey = (p, prefix) => {
  const base = String(p ?? '').replace(/^images\//, '');
  return base ? `${prefix}/${base}` : null;
};

let storyCount = 0;
let pageCount = 0;

for (const s of STORIES) {
  const isFree = s.storyNumber <= FREE_STORIES;

  await sql`
    insert into stories (
      id, story_number, title, title_en, category, category_label, age_group,
      moral_theme, synopsis, synopsis_en, protagonist, companion, setting,
      cover_image, is_free, is_published, published_at, updated_at
    ) values (
      ${s.id}, ${s.storyNumber}, ${s.title}, ${s.englishTitle ?? null},
      ${s.category}, ${s.categoryLabel ?? null}, ${s.ageGroup ?? null},
      ${s.moralTheme ?? null}, ${s.synopsis}, ${s.synopsisEn ?? null},
      ${s.protagonist ?? null}, ${s.companion ?? null}, ${s.setting ?? null},
      ${toKey(s.coverImage ?? s.cover, 'covers')}, ${isFree}, true, now(), now()
    )
    on conflict (id) do update set
      story_number = excluded.story_number,
      title = excluded.title,
      title_en = excluded.title_en,
      category = excluded.category,
      category_label = excluded.category_label,
      age_group = excluded.age_group,
      moral_theme = excluded.moral_theme,
      synopsis = excluded.synopsis,
      synopsis_en = excluded.synopsis_en,
      protagonist = excluded.protagonist,
      companion = excluded.companion,
      setting = excluded.setting,
      cover_image = excluded.cover_image,
      is_free = excluded.is_free,
      is_published = excluded.is_published,
      updated_at = now()
  `;
  storyCount++;

  // Replace pages wholesale so re-seeding never leaves orphaned or stale pages.
  await sql`delete from story_pages where story_id = ${s.id}`;
  for (const p of s.pages ?? []) {
    await sql`
      insert into story_pages (
        story_id, number, title, title_en, text_id, text_en, quote, co_reading,
        image, audio, audio_enabled
      ) values (
        ${s.id}, ${p.number}, ${p.title ?? null}, ${p.titleEn ?? null},
        ${p.textId}, ${p.textEn ?? null}, ${p.quote ?? null}, ${p.coReading ?? null},
        ${toKey(p.image, 'pages')}, ${p.audio ?? null}, ${Boolean(p.audio)}
      )
      on conflict (story_id, number) do update set
        title = excluded.title,
        title_en = excluded.title_en,
        text_id = excluded.text_id,
        text_en = excluded.text_en,
        quote = excluded.quote,
        co_reading = excluded.co_reading,
        image = excluded.image,
        audio = excluded.audio,
        audio_enabled = excluded.audio_enabled
    `;
    pageCount++;
  }
}

for (const p of PRODUCTS) {
  await sql`
    insert into products (slug, name, price_idr, tier, scope_kind, scope_count, is_upgrade, upgrade_from, sort_order, is_active)
    values (${p.slug}, ${p.name}, ${p.priceIdr}, ${p.tier}, ${p.scopeKind}, ${p.scopeCount}, ${p.isUpgrade}, ${p.upgradeFrom}, ${p.sortOrder}, ${p.isActive ?? true})
    on conflict (slug) do update set
      name = excluded.name,
      price_idr = excluded.price_idr,
      tier = excluded.tier,
      scope_kind = excluded.scope_kind,
      scope_count = excluded.scope_count,
      is_upgrade = excluded.is_upgrade,
      upgrade_from = excluded.upgrade_from,
      sort_order = excluded.sort_order,
      is_active = excluded.is_active
  `;
}

const [row] = await sql`
  select
    (select count(*) from stories)::int as stories,
    (select count(*) from story_pages)::int as pages,
    (select count(*) from products)::int as products,
    (select count(*) from stories where is_free)::int as free_stories
`;
console.log(`seeded ${storyCount} stories / ${pageCount} pages / ${PRODUCTS.length} products`);
console.log(`db now: ${row.stories} stories, ${row.pages} pages, ${row.products} products, ${row.free_stories} free`);
