// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

import fs from 'node:fs';
import path from 'node:path';

// Load .env into process.env if present (process.env takes precedence)
try {
  const envPath = path.resolve('.env');
  if (fs.existsSync(envPath)) {
    const envContent = fs.readFileSync(envPath, 'utf8');
    for (const line of envContent.split('\n')) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('#')) continue;
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        const val = trimmed.slice(idx + 1).trim();
        if (typeof process.env[key] === 'undefined') {
          process.env[key] = val;
        }
      }
    }
  }
} catch {
  // Gracefully continue when no .env exists (e.g. Cloudflare Pages build)
}

const isNoIndex = process.env.PUBLIC_NOINDEX === 'true';

// https://astro.build/config
export default defineConfig({
  site: 'https://harihara.net',
  integrations: isNoIndex ? [] : [sitemap()],
  i18n: {
    defaultLocale: 'en',
    locales: [
      'en',
      'hi',
      'gu',
      'es',
      'fr',
      'de',
      'it',
      {
        path: 'zh',
        codes: ['zh-Hans', 'zh']
      },
      'ja',
      'ko',
      'ar',
      {
        path: 'pt',
        codes: ['pt-BR', 'pt']
      }
    ],
    routing: {
      prefixDefaultLocale: false
    }
  },
  vite: {
    plugins: [tailwindcss()]
  }
});
