/**
 * Kisah Krayon — Drizzle schema (Neon Postgres)
 *
 * Design notes:
 * - Money is INTEGER rupiah. No decimals, no floats. IDR has no cents.
 * - Entitlements are resolved, not stored as a boolean on the user. A user can
 *   hold several purchases (10-pick, then an upgrade), and revoking/refunding
 *   one must not silently keep the others alive.
 * - "Pilih 10 favorit" = credits. A purchase grants N credits; each credit is
 *   burned into a story_grant when the user picks a story. Picks are permanent.
 * - Lynk gives one webhook URL per account, so every event must be traceable to
 *   a product row. If the payload has no product id, `products.grandTotalHint`
 *   is the fallback — see webhookEvents for replay.
 */
import {
  boolean,
  index,
  integer,
  jsonb,
  pgEnum,
  pgTable,
  text,
  timestamp,
  uniqueIndex,
  uuid,
} from 'drizzle-orm/pg-core';

/* ------------------------------------------------------------------ enums */

export const tierEnum = pgEnum('tier', ['kecil', 'plus', 'lengkap', 'sahabat']);

export const scopeKindEnum = pgEnum('scope_kind', [
  'all_access', // every published story, including future ones
  'story_count', // N picks, chosen by the user
]);

export const entitlementKindEnum = pgEnum('entitlement_kind', [
  'all_access', // unlocks the whole library
  'credit', // N remaining story picks
  'story', // one specific story, already chosen
]);

export const purchaseStatusEnum = pgEnum('purchase_status', [
  'pending',
  'paid',
  'refunded',
  'failed',
]);

export const webhookStatusEnum = pgEnum('webhook_status', [
  'received',
  'processed',
  'ignored', // duplicate, or event type we do not act on
  'failed',
]);

/* ---------------------------------------------------------------- stories */

export const stories = pgTable(
  'stories',
  {
    id: text('id').primaryKey(), // slug from stories.json, e.g. 'barnaby-bear'
    storyNumber: integer('story_number').notNull(),
    title: text('title').notNull(),
    titleEn: text('title_en'),
    category: text('category').notNull(),
    categoryLabel: text('category_label'),
    ageGroup: text('age_group'),
    moralTheme: text('moral_theme'),
    synopsis: text('synopsis').notNull(),
    synopsisEn: text('synopsis_en'),
    protagonist: text('protagonist'),
    companion: text('companion'),
    setting: text('setting'),
    coverImage: text('cover_image').notNull(),

    // Access rules. isFree is denormalised from storyNumber for query speed and
    // so the free set can change without a migration. Locked stories still
    // return cover + synopsis — only pages are gated.
    isFree: boolean('is_free').notNull().default(false),
    isPublished: boolean('is_published').notNull().default(false),
    publishedAt: timestamp('published_at', { withTimezone: true }),

    createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
    updatedAt: timestamp('updated_at', { withTimezone: true }).notNull().defaultNow(),
  },
  (t) => [
    uniqueIndex('stories_story_number_idx').on(t.storyNumber),
    index('stories_published_idx').on(t.isPublished, t.storyNumber),
    index('stories_free_idx').on(t.isFree),
  ],
);

export const storyPages = pgTable(
  'story_pages',
  {
    id: uuid('id').primaryKey().defaultRandom(),
    storyId: text('story_id')
      .notNull()
      .references(() => stories.id, { onDelete: 'cascade' }),
    number: integer('number').notNull(), // 1..10
    title: text('title'),
    titleEn: text('title_en'),
    textId: text('text_id').notNull(),
    textEn: text('text_en'),
    quote: text('quote'),
    coReading: text('co_reading'),
    image: text('image').notNull(),

    // Audio is parked: rows stay, the app must not render a player while
    // audioEnabled is false. See audioHidden below for the per-page escape hatch.
    audio: text('audio'),
    audioEnabled: boolean('audio_enabled').notNull().default(false),

    createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
  },
  (t) => [
    uniqueIndex('story_pages_story_number_idx').on(t.storyId, t.number),
    index('story_pages_story_idx').on(t.storyId),
  ],
);

/* --------------------------------------------------------------- products */

/**
 * One row per Lynk product. `slug` is our internal handle used in code and in
 * the UI; `lynkProductId` is what the webhook payload should contain. Register
 * these BEFORE publishing links — the webhook resolves product -> tier here.
 */
export const products = pgTable(
  'products',
  {
    id: uuid('id').primaryKey().defaultRandom(),
    slug: text('slug').notNull(), // 'kecil' | 'plus' | 'lengkap' | 'sahabat' | 'upgrade-lengkap' ...
    lynkProductId: text('lynk_product_id'), // null until the product exists in Lynk
    lynkCheckoutUrl: text('lynk_checkout_url'),

    name: text('name').notNull(),
    priceIdr: integer('price_idr').notNull(),
    tier: tierEnum('tier').notNull(),
    scopeKind: scopeKindEnum('scope_kind').notNull(),
    scopeCount: integer('scope_count'), // required when scopeKind = 'story_count'

    // Upgrades are sold only to entitled users. granted tier replaces the
    // current one; the user's earlier credits are voided, not stacked.
    isUpgrade: boolean('is_upgrade').notNull().default(false),
    upgradeFrom: tierEnum('upgrade_from'),

    grandTotalHint: integer('grand_total_hint'), // fallback matching when the payload lacks a product id
    isActive: boolean('is_active').notNull().default(true),
    sortOrder: integer('sort_order').notNull().default(0),

    createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
    updatedAt: timestamp('updated_at', { withTimezone: true }).notNull().defaultNow(),
  },
  (t) => [
    uniqueIndex('products_slug_idx').on(t.slug),
    uniqueIndex('products_lynk_id_idx').on(t.lynkProductId),
    index('products_active_idx').on(t.isActive, t.sortOrder),
  ],
);

/* ------------------------------------------------------------------ users */

/** Mirror of Clerk's user object. Clerk owns identity; this row owns commerce. */
export const users = pgTable(
  'users',
  {
    id: uuid('id').primaryKey().defaultRandom(),
    clerkUserId: text('clerk_user_id').notNull(),
    email: text('email'),
    name: text('name'),
    imageUrl: text('image_url'),

    // Cached entitlement summary so the nav/lock logic needs one query, not a
    // join. Rebuilt from entitlements whenever a purchase lands.
    hasAllAccess: boolean('has_all_access').notNull().default(false),
    storyCredits: integer('story_credits').notNull().default(0),
    grantedStoryCount: integer('granted_story_count').notNull().default(0),
    highestTier: tierEnum('highest_tier'),

    createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
    updatedAt: timestamp('updated_at', { withTimezone: true }).notNull().defaultNow(),
    deletedAt: timestamp('deleted_at', { withTimezone: true }),
  },
  (t) => [
    uniqueIndex('users_clerk_id_idx').on(t.clerkUserId),
    index('users_email_idx').on(t.email),
  ],
);

/* -------------------------------------------------------------- purchases */

/**
 * One row per Lynk order. `refId` is the identifier we mint and pass to Lynk as
 * the order reference — it is how the webhook finds this row. `userId` is null
 * when the buyer's email matches no account (guest checkout, or they signed up
 * with a different address); those rows wait to be claimed by ref_id from /akun.
 *
 * `grossTotal` is what the buyer actually paid and may include a Lynk payment
 * channel fee or a "kode unik". Never validate it against products.priceIdr.
 * `netEstimate` = grossTotal * (1 - feeBp/10000) — our own accounting, not a
 * number Lynk sends us.
 */
export const purchases = pgTable(
  'purchases',
  {
    id: uuid('id').primaryKey().defaultRandom(),
    userId: uuid('user_id').references(() => users.id, { onDelete: 'set null' }),

    refId: text('ref_id').notNull(),
    lynkOrderId: text('lynk_order_id'),

    productId: uuid('product_id').references(() => products.id, { onDelete: 'restrict' }),
    productSlug: text('product_slug'), // denormalised: survives product deletion
    tier: tierEnum('tier'),
    grantedScopeKind: scopeKindEnum('granted_scope_kind'),
    grantedCount: integer('granted_count'),

    buyerEmail: text('buyer_email'),
    buyerName: text('buyer_name'),
    buyerPhone: text('buyer_phone'),

    grossTotal: integer('gross_total').notNull(),
    feeBp: integer('fee_bp').notNull().default(500), // 500 = 5% Starter, 300 = 3% Pro
    netEstimate: integer('net_estimate'),

    status: purchaseStatusEnum('status').notNull().default('pending'),
    paidAt: timestamp('paid_at', { withTimezone: true }),
    refundedAt: timestamp('refunded_at', { withTimezone: true }),

    rawPayload: jsonb('raw_payload'), // keep forever: replay + dispute evidence
    createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
    updatedAt: timestamp('updated_at', { withTimezone: true }).notNull().defaultNow(),
  },
  (t) => [
    uniqueIndex('purchases_ref_id_idx').on(t.refId),
    uniqueIndex('purchases_lynk_order_idx').on(t.lynkOrderId),
    index('purchases_user_idx').on(t.userId, t.status),
    index('purchases_email_idx').on(t.buyerEmail),
    index('purchases_created_idx').on(t.createdAt),
  ],
);

/* ----------------------------------------------------------- entitlements */

/** What a purchase actually unlocked. Rebuilt on refund/upgrade. */
export const entitlements = pgTable(
  'entitlements',
  {
    id: uuid('id').primaryKey().defaultRandom(),
    userId: uuid('user_id')
      .notNull()
      .references(() => users.id, { onDelete: 'cascade' }),
    purchaseId: uuid('purchase_id')
      .notNull()
      .references(() => purchases.id, { onDelete: 'cascade' }),

    kind: entitlementKindEnum('kind').notNull(),
    credits: integer('credits'), // for kind='credit': picks still unused
    storyId: text('story_id').references(() => stories.id, { onDelete: 'cascade' }),

    isActive: boolean('is_active').notNull().default(true),
    revokedAt: timestamp('revoked_at', { withTimezone: true }),
    createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
  },
  (t) => [
    index('entitlements_user_active_idx').on(t.userId, t.isActive),
    index('entitlements_purchase_idx').on(t.purchaseId),
  ],
);

/**
 * A story the user has actually unlocked. Permanent — revoking a purchase
 * deactivates the entitlement but leaves the grant for audit; access checks
 * require an active entitlement behind the grant.
 */
export const storyGrants = pgTable(
  'story_grants',
  {
    id: uuid('id').primaryKey().defaultRandom(),
    userId: uuid('user_id')
      .notNull()
      .references(() => users.id, { onDelete: 'cascade' }),
    storyId: text('story_id')
      .notNull()
      .references(() => stories.id, { onDelete: 'cascade' }),
    purchaseId: uuid('purchase_id').references(() => purchases.id, { onDelete: 'set null' }),
    entitlementId: uuid('entitlement_id').references(() => entitlements.id, {
      onDelete: 'set null',
    }),
    grantedAt: timestamp('granted_at', { withTimezone: true }).notNull().defaultNow(),
  },
  (t) => [
    uniqueIndex('story_grants_user_story_idx').on(t.userId, t.storyId),
    index('story_grants_user_idx').on(t.userId),
  ],
);

/* --------------------------------------------------------- webhook events */

/**
 * Append-only log of every Lynk callback. Two jobs: idempotency (unique event
 * key) and replay. Until we have captured a real payload we do not know which
 * fields Lynk sends, so storing the raw body is the only way to fix a bad
 * mapping without asking customers to buy again.
 */
export const webhookEvents = pgTable(
  'webhook_events',
  {
    id: uuid('id').primaryKey().defaultRandom(),
    provider: text('provider').notNull().default('lynk'),
    eventKey: text('event_key').notNull(), // ref_id + event type, or the payload's own id
    eventType: text('event_type'),

    signature: text('signature'),
    headers: jsonb('headers'),
    rawBody: jsonb('raw_body').notNull(),

    status: webhookStatusEnum('status').notNull().default('received'),
    error: text('error'),
    purchaseId: uuid('purchase_id').references(() => purchases.id, { onDelete: 'set null' }),

    receivedAt: timestamp('received_at', { withTimezone: true }).notNull().defaultNow(),
    processedAt: timestamp('processed_at', { withTimezone: true }),
  },
  (t) => [
    uniqueIndex('webhook_events_key_idx').on(t.provider, t.eventKey),
    index('webhook_events_status_idx').on(t.status, t.receivedAt),
  ],
);

/* ------------------------------------------------------------------ types */

export type Story = typeof stories.$inferSelect;
export type NewStory = typeof stories.$inferInsert;
export type StoryPage = typeof storyPages.$inferSelect;
export type NewStoryPage = typeof storyPages.$inferInsert;
export type Product = typeof products.$inferSelect;
export type NewProduct = typeof products.$inferInsert;
export type User = typeof users.$inferSelect;
export type NewUser = typeof users.$inferInsert;
export type Purchase = typeof purchases.$inferSelect;
export type NewPurchase = typeof purchases.$inferInsert;
export type Entitlement = typeof entitlements.$inferSelect;
export type NewEntitlement = typeof entitlements.$inferInsert;
export type StoryGrant = typeof storyGrants.$inferSelect;
export type NewStoryGrant = typeof storyGrants.$inferInsert;
export type WebhookEvent = typeof webhookEvents.$inferSelect;
export type NewWebhookEvent = typeof webhookEvents.$inferInsert;
