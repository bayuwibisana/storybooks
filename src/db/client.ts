import { neon } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-http';
import * as schema from './schema';
import { getEnv } from '../lib/env';

let _db: any = null;

export function resolveDb() {
  if (_db) return _db;
  const connectionString = getEnv('DATABASE_URL');
  if (!connectionString) {
    throw new Error(
      'DATABASE_URL is not set. Add the Neon connection string in Cloudflare Dashboard (Settings > Variables and Secrets).',
    );
  }
  const sql = neon(connectionString);
  _db = drizzle(sql, { schema });
  return _db;
}

export const db = new Proxy({} as any, {
  get(_target, prop) {
    const instance = resolveDb();
    const value = (instance as any)[prop];
    if (typeof value === 'function') {
      return value.bind(instance);
    }
    return value;
  },
});

export type Db = ReturnType<typeof resolveDb>;
