# Deployment Guide: Hari Hara Serenity Chemical LLP Website

This document outlines the deployment configuration for **Cloudflare Pages** (or any static hosting platform).

---

## 1. Hosting Environment & Build Specifications

| Setting | Value | Notes |
| :--- | :--- | :--- |
| **Framework preset** | None / Astro | Pure static generation (`output: "static"`). |
| **Build command** | `npm run build` | Runs `astro build` (Astro telemetry disabled). |
| **Build output directory** | `dist` | Generated HTML, CSS, JavaScript, assets, and sitemap. |
| **Node.js version** | `22.x` (or `>=22.12.0`) | Specified in `.nvmrc` (`22`) and `package.json` `engines`. |
| **Canonical Site URL** | `https://harihara.net` | Configured in `astro.config.mjs`. |

---

## 2. Environment Variables

All settings work seamlessly without a `.env` file present on Cloudflare Pages. Real process environment variables configured in the Cloudflare dashboard take precedence over any `.env` defaults.

| Variable | Preview Deployments | Production Deployments | Description |
| :--- | :---: | :---: | :--- |
| `PUBLIC_NOINDEX` | `true` | *(unset / empty)* | **Search engine indexing protection:**<br>• When `true`: Injects `<meta name="robots" content="noindex, nofollow">` on every page, disallows all in `robots.txt` (`Disallow: /`), and suppresses the sitemap completely.<br>• When unset or `false`: Permissive indexing (`Allow: /`), standard canonical tags, and generates `sitemap-index.xml`. |
| `SHOW_DRAFT_LANGUAGES` | `true` | *(unset / empty)* | **Language Switcher display:**<br>• When `true`: Displays all 12 languages in the language switcher for QA and stakeholder review.<br>• When unset or `false`: Restricts language switcher strictly to human-reviewed and AI-validated languages (`en`), keeping draft translations hidden from public discovery. |

---

## 3. Self-Contained Zero-Network Build Guarantee

- **Self-Hosted Typography**: All font families (`Newsreader`, `Montserrat`, `Noto Sans/Serif Devanagari`, `Noto Sans/Serif Gujarati`, `Noto Sans/Naskh Arabic`, `Noto Sans/Serif SC`, `Noto Sans/Serif JP`, `Noto Sans/Serif KR`) are packaged and imported via `@fontsource/*` dependencies. Zero runtime or build-time requests to Google Fonts.
- **Local Visual Assets**: All photographic images and vector branding assets reside within `public/images/` and `public/brand/`. No external asset CDNs or hotlinks are contacted.
- **Zero Third-Party Endpoints**: No third-party form processors, runtime telemetry, or external trackers are bundled.
