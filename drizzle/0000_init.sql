CREATE TYPE "public"."entitlement_kind" AS ENUM('all_access', 'credit', 'story');--> statement-breakpoint
CREATE TYPE "public"."purchase_status" AS ENUM('pending', 'paid', 'refunded', 'failed');--> statement-breakpoint
CREATE TYPE "public"."scope_kind" AS ENUM('all_access', 'story_count');--> statement-breakpoint
CREATE TYPE "public"."tier" AS ENUM('kecil', 'plus', 'lengkap', 'sahabat');--> statement-breakpoint
CREATE TYPE "public"."webhook_status" AS ENUM('received', 'processed', 'ignored', 'failed');--> statement-breakpoint
CREATE TABLE "entitlements" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"user_id" uuid NOT NULL,
	"purchase_id" uuid NOT NULL,
	"kind" "entitlement_kind" NOT NULL,
	"credits" integer,
	"story_id" text,
	"is_active" boolean DEFAULT true NOT NULL,
	"revoked_at" timestamp with time zone,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "products" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"slug" text NOT NULL,
	"lynk_product_id" text,
	"lynk_checkout_url" text,
	"name" text NOT NULL,
	"price_idr" integer NOT NULL,
	"tier" "tier" NOT NULL,
	"scope_kind" "scope_kind" NOT NULL,
	"scope_count" integer,
	"is_upgrade" boolean DEFAULT false NOT NULL,
	"upgrade_from" "tier",
	"grand_total_hint" integer,
	"is_active" boolean DEFAULT true NOT NULL,
	"sort_order" integer DEFAULT 0 NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "purchases" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"user_id" uuid,
	"ref_id" text NOT NULL,
	"lynk_order_id" text,
	"product_id" uuid,
	"product_slug" text,
	"tier" "tier",
	"granted_scope_kind" "scope_kind",
	"granted_count" integer,
	"buyer_email" text,
	"buyer_name" text,
	"buyer_phone" text,
	"gross_total" integer NOT NULL,
	"fee_bp" integer DEFAULT 500 NOT NULL,
	"net_estimate" integer,
	"status" "purchase_status" DEFAULT 'pending' NOT NULL,
	"paid_at" timestamp with time zone,
	"refunded_at" timestamp with time zone,
	"raw_payload" jsonb,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "stories" (
	"id" text PRIMARY KEY NOT NULL,
	"story_number" integer NOT NULL,
	"title" text NOT NULL,
	"title_en" text,
	"category" text NOT NULL,
	"category_label" text,
	"age_group" text,
	"moral_theme" text,
	"synopsis" text NOT NULL,
	"synopsis_en" text,
	"protagonist" text,
	"companion" text,
	"setting" text,
	"cover_image" text NOT NULL,
	"is_free" boolean DEFAULT false NOT NULL,
	"is_published" boolean DEFAULT false NOT NULL,
	"published_at" timestamp with time zone,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "story_grants" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"user_id" uuid NOT NULL,
	"story_id" text NOT NULL,
	"purchase_id" uuid,
	"entitlement_id" uuid,
	"granted_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "story_pages" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"story_id" text NOT NULL,
	"number" integer NOT NULL,
	"title" text,
	"title_en" text,
	"text_id" text NOT NULL,
	"text_en" text,
	"quote" text,
	"co_reading" text,
	"image" text NOT NULL,
	"audio" text,
	"audio_enabled" boolean DEFAULT false NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "users" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"clerk_user_id" text NOT NULL,
	"email" text,
	"name" text,
	"image_url" text,
	"has_all_access" boolean DEFAULT false NOT NULL,
	"story_credits" integer DEFAULT 0 NOT NULL,
	"granted_story_count" integer DEFAULT 0 NOT NULL,
	"highest_tier" "tier",
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL,
	"deleted_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "webhook_events" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"provider" text DEFAULT 'lynk' NOT NULL,
	"event_key" text NOT NULL,
	"event_type" text,
	"signature" text,
	"headers" jsonb,
	"raw_body" jsonb NOT NULL,
	"status" "webhook_status" DEFAULT 'received' NOT NULL,
	"error" text,
	"purchase_id" uuid,
	"received_at" timestamp with time zone DEFAULT now() NOT NULL,
	"processed_at" timestamp with time zone
);
--> statement-breakpoint
ALTER TABLE "entitlements" ADD CONSTRAINT "entitlements_user_id_users_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "entitlements" ADD CONSTRAINT "entitlements_purchase_id_purchases_id_fk" FOREIGN KEY ("purchase_id") REFERENCES "public"."purchases"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "entitlements" ADD CONSTRAINT "entitlements_story_id_stories_id_fk" FOREIGN KEY ("story_id") REFERENCES "public"."stories"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "purchases" ADD CONSTRAINT "purchases_user_id_users_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("id") ON DELETE set null ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "purchases" ADD CONSTRAINT "purchases_product_id_products_id_fk" FOREIGN KEY ("product_id") REFERENCES "public"."products"("id") ON DELETE restrict ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "story_grants" ADD CONSTRAINT "story_grants_user_id_users_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "story_grants" ADD CONSTRAINT "story_grants_story_id_stories_id_fk" FOREIGN KEY ("story_id") REFERENCES "public"."stories"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "story_grants" ADD CONSTRAINT "story_grants_purchase_id_purchases_id_fk" FOREIGN KEY ("purchase_id") REFERENCES "public"."purchases"("id") ON DELETE set null ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "story_grants" ADD CONSTRAINT "story_grants_entitlement_id_entitlements_id_fk" FOREIGN KEY ("entitlement_id") REFERENCES "public"."entitlements"("id") ON DELETE set null ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "story_pages" ADD CONSTRAINT "story_pages_story_id_stories_id_fk" FOREIGN KEY ("story_id") REFERENCES "public"."stories"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "webhook_events" ADD CONSTRAINT "webhook_events_purchase_id_purchases_id_fk" FOREIGN KEY ("purchase_id") REFERENCES "public"."purchases"("id") ON DELETE set null ON UPDATE no action;--> statement-breakpoint
CREATE INDEX "entitlements_user_active_idx" ON "entitlements" USING btree ("user_id","is_active");--> statement-breakpoint
CREATE INDEX "entitlements_purchase_idx" ON "entitlements" USING btree ("purchase_id");--> statement-breakpoint
CREATE UNIQUE INDEX "products_slug_idx" ON "products" USING btree ("slug");--> statement-breakpoint
CREATE UNIQUE INDEX "products_lynk_id_idx" ON "products" USING btree ("lynk_product_id");--> statement-breakpoint
CREATE INDEX "products_active_idx" ON "products" USING btree ("is_active","sort_order");--> statement-breakpoint
CREATE UNIQUE INDEX "purchases_ref_id_idx" ON "purchases" USING btree ("ref_id");--> statement-breakpoint
CREATE UNIQUE INDEX "purchases_lynk_order_idx" ON "purchases" USING btree ("lynk_order_id");--> statement-breakpoint
CREATE INDEX "purchases_user_idx" ON "purchases" USING btree ("user_id","status");--> statement-breakpoint
CREATE INDEX "purchases_email_idx" ON "purchases" USING btree ("buyer_email");--> statement-breakpoint
CREATE INDEX "purchases_created_idx" ON "purchases" USING btree ("created_at");--> statement-breakpoint
CREATE UNIQUE INDEX "stories_story_number_idx" ON "stories" USING btree ("story_number");--> statement-breakpoint
CREATE INDEX "stories_published_idx" ON "stories" USING btree ("is_published","story_number");--> statement-breakpoint
CREATE INDEX "stories_free_idx" ON "stories" USING btree ("is_free");--> statement-breakpoint
CREATE UNIQUE INDEX "story_grants_user_story_idx" ON "story_grants" USING btree ("user_id","story_id");--> statement-breakpoint
CREATE INDEX "story_grants_user_idx" ON "story_grants" USING btree ("user_id");--> statement-breakpoint
CREATE UNIQUE INDEX "story_pages_story_number_idx" ON "story_pages" USING btree ("story_id","number");--> statement-breakpoint
CREATE INDEX "story_pages_story_idx" ON "story_pages" USING btree ("story_id");--> statement-breakpoint
CREATE UNIQUE INDEX "users_clerk_id_idx" ON "users" USING btree ("clerk_user_id");--> statement-breakpoint
CREATE INDEX "users_email_idx" ON "users" USING btree ("email");--> statement-breakpoint
CREATE UNIQUE INDEX "webhook_events_key_idx" ON "webhook_events" USING btree ("provider","event_key");--> statement-breakpoint
CREATE INDEX "webhook_events_status_idx" ON "webhook_events" USING btree ("status","received_at");