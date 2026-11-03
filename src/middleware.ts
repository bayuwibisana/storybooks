import { clerkMiddleware } from "@clerk/astro/server";
import { sequence } from "astro:middleware";
import { syncProcessEnv } from "./lib/env";

const initEnv = async (_context: any, next: any) => {
  syncProcessEnv();
  return next();
};

export const onRequest = sequence(initEnv, clerkMiddleware());
