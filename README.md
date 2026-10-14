# Hari Hara Serenity Chemical LLP — Website

Official landing website for Hari Hara Serenity Chemical LLP, presenting planned bromine recovery and purification operations at Village Manaba, Taluka Rapar, District Kachchh, Gujarat.

Built with [Astro](https://astro.build/) (v5+), Tailwind CSS v4, TypeScript (strict), and multi-locale i18n support across 12 languages.

---

## Supported Locales & URL Structure

- **English (`/`)**: Default locale (no prefix, official binding text)
- **Hindi (`/hi/`)**: हिन्दी (Devanagari)
- **Gujarati (`/gu/`)**: ગુજરાતી (Gujarati)
- **Spanish (`/es/`)**: Español
- **French (`/fr/`)**: Français
- **German (`/de/`)**: Deutsch
- **Italian (`/it/`)**: Italiano
- **Simplified Chinese (`/zh/`)**: 简体中文 (`zh-Hans`)
- **Japanese (`/ja/`)**: 日本語
- **Korean (`/ko/`)**: 한국어
- **Arabic (`/ar/`)**: العربية (Right-to-left layout, `dir="rtl"`)
- **Portuguese (`/pt/`)**: Português (`pt-BR`)

Each non-English locale displays a convenience disclaimer: *"Translated for convenience. The English version is the official version."*

---

## Prerequisites

- Node.js >= 22.12.0
- npm >= 10.0.0

---

## Getting Started

1. **Clone repository and install dependencies:**
   ```bash
   npm install
   ```

2. **Configure environment variables:**
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   Set `SHOW_DRAFT_LANGUAGES=true` in `.env` to preview draft languages in development.

---

## Available Commands

### Development
Starts local development server at `http://localhost:4321/`:
```bash
npm run dev
```

### Build
Runs production build generating static files in `dist/`:
```bash
npm run build
```

### Preview
Serves the generated `dist/` directory locally:
```bash
npm run preview
```

### Validate i18n Translations
Runs automated integrity checks across all 12 locale JSON files:
```bash
npm run check:i18n
```
The check verifies:
- Key presence and non-empty values matching English master (`src/i18n/en.json`).
- Template placeholder synchronization (`{variable}`).
- Protection of un-translatable corporate identifiers (LLPIN, GSTIN, phone, addresses, company name).
- Absence of forbidden registered trademark symbols (`®`, `™`).

### Astro Type Check
Runs strict TypeScript diagnostics on all Astro and TypeScript files:
```bash
npx astro check
```

---

## Design Tokens & Self-Hosted Typography

- **Colours**:
  - Crimson: `#D01A45`
  - Maroon: `#7A1230`
  - Charcoal: `#1C1C1C`
  - Paper: `#F6F3EE` / `#FAF8F5`
  - Grey: `#7A7A7A`
- **Typography**:
  - Headings: `Newsreader` (Latin serif) / Noto Serif per script
  - Body & UI: `Montserrat` (Latin sans) / Noto Sans per script
  - Arabic: `Noto Naskh Arabic` / `Noto Sans Arabic`
  - Non-Latin script font packages are dynamically imported only on their respective language pages.
