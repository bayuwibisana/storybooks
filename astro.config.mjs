import clerk from '@clerk/astro';
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';
// https://astro.build/config
export default defineConfig({
  integrations: [clerk()],
  adapter: vercel()
});