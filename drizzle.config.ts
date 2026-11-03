import { config } from 'dotenv';
import { defineConfig } from 'drizzle-kit';

config();

export default defineConfig({
  schema: './src/db/schema.ts',
  out: './drizzle',
  dialect: 'postgresql',
  dbCredentials: {
    // Migrations must use the direct (unpooled) connection; Neon's pooler
    // drops long-running DDL and advisory locks.
    url: process.env.DATABASE_URL_UNPOOLED ?? process.env.DATABASE_URL!,
  },
});
