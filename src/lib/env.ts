let cfEnv: Record<string, any> = {};

try {
  // Dynamic import so it does not crash when bundled or running on Node.js
  const cf = await import('cloudflare:workers');
  if (cf && cf.env) {
    cfEnv = cf.env;
  }
} catch {
  // Not in Cloudflare Workers runtime (e.g. local Node.js)
  try {
    const dotenv = await import('dotenv');
    dotenv.config();
  } catch {}
}

export function getEnv(key: string): string | undefined {
  return (
    cfEnv[key] ||
    (typeof process !== 'undefined' ? process.env?.[key] : undefined) ||
    (globalThis as any)?.[key] ||
    (import.meta.env as any)?.[key]
  );
}

export function syncProcessEnv() {
  if (Object.keys(cfEnv).length > 0) {
    if (typeof process === 'undefined') {
      (globalThis as any).process = { env: {} };
    }
    if (!process.env) {
      process.env = {};
    }
    Object.assign(process.env, cfEnv);
    Object.assign(globalThis, cfEnv);
  }
}
