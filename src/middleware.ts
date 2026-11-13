import type { MiddlewareHandler } from "astro";
import { clerkMiddleware } from "@clerk/astro/server";
import { sequence } from "astro:middleware";
import { syncProcessEnv } from "./lib/env";

const BLOCKED_BOT_REGEX = new RegExp(
  [
    'gptbot',
    'chatgpt-user',
    'claudebot',
    'claude-web',
    'anthropic-ai',
    'bytespider',
    'ccbot',
    'perplexitybot',
    'amazonbot',
    'diffbot',
    'facebookbot',
    'meta-externalagent',
    'google-extended',
    'cohere-ai',
    'omgili',
    'scrapy',
    'python-requests',
    'aiohttp',
    'httpx',
    'phantomjs',
    'selenium',
    'puppeteer',
    'headlesschrome',
  ].join('|'),
  'i'
);

const botBlocker: MiddlewareHandler = async (context, next) => {
  if (context.url.pathname === '/robots.txt') {
    return next();
  }

  const userAgent = context.request.headers.get('user-agent') || '';
  if (BLOCKED_BOT_REGEX.test(userAgent)) {
    return new Response(
      JSON.stringify({
        error: 'Forbidden',
        message: 'Automated scrapers and AI training bots are not permitted.',
      }),
      {
        status: 403,
        headers: {
          'Content-Type': 'application/json',
          'X-Robots-Tag': 'noindex, nofollow',
        },
      }
    );
  }

  return next();
};

const initEnv: MiddlewareHandler = async (_context, next) => {
  syncProcessEnv();
  return next();
};

export const onRequest = sequence(botBlocker, initEnv, clerkMiddleware());
