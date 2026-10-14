// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://harihara.net',
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
