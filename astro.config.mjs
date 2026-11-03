import clerk from '@clerk/astro';
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';

// https://astro.build/config
export default defineConfig({
  integrations: [clerk()],
  adapter: cloudflare({
    platformProxy: {
      enabled: true
    }
  })
});