# Launch Checklist: Hari Hara Serenity Chemical LLP Website

This document records the mandatory verification and configuration steps that must occur prior to deploying the website to production on Cloudflare Pages.

---

## 1. Environment & Configuration Flags
- [ ] **Disable Draft Languages in Production**:
  - In `.env` (or Cloudflare Pages environment variables), set `SHOW_DRAFT_LANGUAGES=false`.
  - Only human-reviewed and AI-validated languages (`en`) will appear in the language switcher. Draft translations remain hidden from production visitors until explicitly verified.
- [ ] **Remove Development Previews & Route Stubs**:
  - Delete `/brand-preview/` (`src/pages/brand-preview/index.astro`).
  - Confirm DEV-only navigation stubs (`isDev` conditionals in `src/pages/index.astro` and `src/pages/[lang]/index.astro`) are excluded from production builds (`astro build` sets `import.meta.env.DEV` to `false`).
- [ ] **Contact Form Deferred**:
  - The contact form has been deferred to a later phase. Direct contact is via verified email (`Purchase@harihara.net`), phone, and WhatsApp (`9427134190`).
- [ ] **Replace Representative Photos with Client's Own Photos**:
  - Review all representative photographs and replace them with the client's verified photos of the Rapar site and operations when available.
- [ ] **Needs a Real Photo Slots**:
  - Review any slots temporarily using fallback brand illustrations and replace them with verified licensed photos.
- [ ] **Google Maps Link / Pins**:
  - Corporate and accounts office link is set to the client-supplied Google Maps place link, and the plant and registered office links are confirmed correct. Client may optionally send custom Google Maps share links or pins for the other two locations if desired.
- [ ] **Preview Safety & Indexing (PUBLIC_NOINDEX)**:
  - Remove PUBLIC_NOINDEX in the production environment and confirm robots.txt and the sitemap are normal.

---

## 2. Brand, Trademark & Client Decisions
- [ ] **Client Decision on Trademark Marks (`SHOW_LOGO_TM`)**:
  - Decide whether the TM mark appears on the reconstructed vector logo (`SHOW_LOGO_TM=true` vs `false` in `src/config.ts`).
  - Note: Per brief hard rules, never use the registered trademark symbol `®` anywhere in copy or design.
- [ ] **Original Client Logo Vector Assets**:
  - If the client delivers official high-resolution vector artwork (`.svg` / `.ai`), swap the files into `public/brand/` and re-verify visual fidelity.
- [ ] **Client Written Approval of Content**:
  - Obtain written client approval for all English source copy across all sections, including the general-background content in all sections.
- [ ] **Image Licences & Internal Audit**:
  - docs/IMAGE_CREDITS.md is complete and every image licence is no-attribution.
- [ ] **Client Legal Approval of Privacy Policy & Disclaimer**:
  - The client must review and approve both `/privacy-policy/` and `/disclaimer/`. Note: The developer is not a lawyer; these pages provide standard DPDP Act 2023 aligned editorial baselines and must be legally verified by the client's legal counsel prior to binding use.

---

## 3. Compliance & Prohibited Claims Audit
Verify that none of the following forbidden claims or representations appear in any language:
- [ ] **No "Startup India" or "DPIIT" mentions**.
- [ ] **No project cost, investment, bank loan, capacity, employment numbers, or financial projections**.
- [ ] **No licence, consent, certification, or approval claims** (State Pollution Control Board, PESO, ISO, etc.).
- [ ] **Plant and products described strictly as planned / under development**:
  - Confirm words like *"we supply"*, *"we manufacture"*, or *"available now"* are absent in all 12 languages.
  - Confirmed phrases: *"planned"*, *"under development"*, *"our aim"*.
- [ ] **Company details strictly match legal filings**:
  - Name: `Hari Hara Serenity Chemical LLP`
  - LLPIN: `ACR-8196`
  - GSTIN: `24AASFH7523H1Z5`
  - Registered and Corporate addresses match project brief exactly.

---

## 4. Internationalisation & Translation Review
- [ ] **Human Review of All 11 Non-English Translations**:
  - Professional review of native translations (`hi`, `gu`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `ar`, `pt`).
  - Update `status` in `src/i18n/languages.config.ts` from `'draft'` to `'human-reviewed'` once approved.
  - Confirm native script place names for Hindi and Gujarati (`રાપર, કચ્છ`, `मानाबा, रापर, कच्छ`) and Latin script for other locales.
- [ ] **Run Internationalisation Parity Checker**:
  - Execute `npm run check:i18n` to confirm zero missing keys, consistent placeholders, and protected term preservation.

---

## 5. Domain, DNS & Email Preservation
- [ ] **DNS Records Migration Strategy**:
  - When configuring DNS records for `harihara.net` on Cloudflare Pages, **preserve existing MX, SPF, DKIM, and DMARC email records** untouched so that business email operations (`Purchase@harihara.net`) experience zero downtime.
  - Create CNAME / Apex records pointing exclusively to the Cloudflare Pages project.
- [ ] **HTTPS & SSL**:
  - Ensure SSL/TLS encryption mode is set to "Full (strict)".
  - Enable Automatic HTTPS Rewrites and HSTS.

---

## 6. Performance, SEO & Accessibility (WCAG AA)
- [ ] **Accessibility Audit**:
  - Verify skip-to-content link functions on initial Tab key press.
  - Verify mobile navigation drawer traps focus while open, closes on `Escape`, and restores focus.
  - Verify color contrast meets WCAG AA standards (Charcoal on Paper = 15.4:1, Crimson on Paper = 4.85:1, Calibrated Grey = 4.54:1).
  - Verify all animations (Hero salt pan drift and shimmer) halt under `prefers-reduced-motion: reduce`.
- [ ] **Search Engine Optimization**:
  - Verify `<link rel="canonical">` and `<link rel="alternate" hreflang="...">` tags for all visible language routes.
  - Verify `robots.txt` and `sitemap-index.xml` generation.
  - Confirm OpenGraph meta tags and preview card (`/brand/social-preview.png`).
- [ ] **Lighthouse Target**:
  - Confirm scores: Performance ≥ 95, Accessibility = 100, Best Practices ≥ 95, SEO = 100.
