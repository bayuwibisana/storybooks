import { clerkMiddleware } from "@clerk/astro/server";
import { sequence } from "astro:middleware";

const initEnv = async (context: any, next: any) => {
  const runtimeEnv = context.locals?.runtime?.env;
  if (runtimeEnv) {
    if (typeof process === 'undefined') {
      (globalThis as any).process = { env: {} };
    }
    if (!process.env) {
      process.env = {};
    }
    Object.assign(process.env, runtimeEnv);
    Object.assign(globalThis, runtimeEnv);
  }
  return next();
};

export const onRequest = sequence(initEnv, clerkMiddleware());
