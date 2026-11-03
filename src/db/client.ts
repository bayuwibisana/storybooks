import { Pool } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-serverless';
import * as schema from './schema';

/**
 * Astro/Vite does not copy `.env` into `process.env` for plain server modules —
 * only into `import.meta.env` — while Vercel injects real environment variables
 * into `process.env` and leaves `import.meta.env` without them. Read both.
 */
const connectionString = import.meta.env.DATABASE_URL ?? process.env.DATABASE_URL;

if (!connectionString) {
  throw new Error(
    'DATABASE_URL is not set. Add the Neon pooled connection string to web/.env (local) or the Vercel project settings (production).',
  );
}

/**
 * Neon serverless driver over WebSockets (not the HTTP driver) because payment
 * flows need interactive transactions: `grantStory` locks an entitlement row,
 * inserts a grant and decrements credits atomically. The HTTP driver cannot do
 * that. Vercel caches the Pool per lambda instance, so this stays cheap.
 */
export const db = drizzle(new Pool({ connectionString }), { schema });

export type Db = typeof db;
