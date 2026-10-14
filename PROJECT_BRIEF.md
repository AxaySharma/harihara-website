# Hari Hara Serenity Chemical LLP - Website Brief

## What this is
A one-page, 12-language landing site for a chemical company that is setting up a plant. It supports registration and grant applications, so credibility and accuracy matter more than sales language. Visitors may come from India and from export markets.

## Hard rules (never break)
- Never add the registered trademark symbol. The logo image contains a TM mark; use the logo exactly as supplied.
- No "Startup India" or "DPIIT" claim anywhere.
- No project cost, investment, bank loan, capacity, employment number or financial projection.
- No licence, consent, certification or approval claims (pollution board, PESO, ISO etc.).
- Describe the plant and products as planned / under development. Never write "we supply", "we manufacture" or "available now". Use "planned", "upcoming", "our aim". This applies to every language.
- Do not invent facts, statistics, testimonials, partner names or certifications. Use only the content below.
- Copy company details, addresses and the footer text exactly as written below.

## Company content (English, source of truth)
Company: Hari Hara Serenity Chemical LLP
Short name for header: HARI HARA SERENITY

About: Hari Hara Serenity Chemical LLP is setting up a plant at Rapar, Kachchh, Gujarat, to recover and purify bromine from bittern, the residual brine left after salt production. Bromine is a key input for the pharmaceutical, agrochemical, flame-retardant, water-treatment and oil-field chemical industries. Our aim is to supply quality bromine to Indian industry and reduce its dependence on imports.

Planned products: 1) Bromine (industrial grade) 2) Bromine compounds and bromide salts

Industries: pharmaceutical, agrochemical, flame retardants, water treatment, oil-field chemicals

Plant: Village Manaba, Taluka Rapar, District Kachchh, Gujarat

Contact: Purchase@harihara.net | 9427134190 (phone and WhatsApp) | Enquiries handled by Ketan Dholu, Partner

Addresses:
- Registered Office: 106, Ruby Monarch Arcade, Saki Vihar Road, Sakinaka, Andheri (East), Mumbai - 400072, Maharashtra
- Corporate and Accounts Office: Plot No. 390, Shiv Residency, Shiv Aaradhana Society, Bhuj Bypass, Bhuj, Kachchh, Gujarat - 370001
- Plant: Village Manaba, Taluka Rapar, District Kachchh, Gujarat

Footer text: Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 | GSTIN: 24AASFH7523H1Z5 | Limited Liability Partnership registered under the LLP Act, 2008

Partners (hidden behind a config flag SHOW_PARTNERS=false until the client confirms):
Dinesh Ratanshi Bhawani (Designated Partner), Ravilal Rasiklal Patel (Designated Partner), Pranav Dharmnath Avhad, Ketan Valji Dholu, Dinesh Manilal Chopda, Bipin Narshibhai Patel

## Page structure (single page, anchor navigation)
Header (logo, anchors, language switcher) > Hero > About > From bittern to bromine (simple 3-step visual: bittern, recovery, purification, labelled as planned) > Planned products > Industries served > Plant and location (link to maps, no embedded map) > Contact (form, details, addresses) > Footer (footer text, Privacy Policy, Disclaimer). Privacy Policy and Disclaimer are separate simple pages.

## Languages
Twelve languages. English (default, served at /), then /hi/ Hindi, /gu/ Gujarati, /es/ Spanish (international), /fr/ French, /de/ German, /it/ Italian, /zh/ Chinese Simplified (html lang zh-Hans), /ja/ Japanese, /ko/ Korean, /ar/ Arabic (Modern Standard, right-to-left), /pt/ Portuguese (Brazilian).
- All text lives in src/i18n/<lang>.json. Never hard-code text in components.
- The English text is the master. It uses short sentences, plain words, no idioms and no wordplay.
- src/i18n/glossary.json holds fixed translations of key terms per language (bromine, bittern, bromide salts, industry names).
- Never translate: company name, "Hari Hara", LLPIN, GSTIN, email address, phone number, street addresses.
- Each language has a status in src/i18n/languages.config.ts: draft, ai-checked or human-reviewed. Draft is hidden in production. The other two appear in the switcher.
- Every non-English page shows a short note, translated into that language: "Translated for convenience. The English version is the official version." The Privacy Policy and Disclaimer are binding in English only.
- Translation workflow: one model drafts, a different model translates it back to English, and any meaning drift is flagged for review before a language moves from draft to ai-checked.
- Auto-detect: on the first visit to "/", if there is no saved choice, map the browser language to a supported one (zh-* to zh, pt-* to pt, and so on) and redirect. Otherwise stay on English. Always save the visitor's manual choice and never override it.
- Right-to-left: Arabic uses dir="rtl". Use CSS logical properties everywhere (margin-inline, padding-inline, text-align: start, inset-inline) so layouts mirror automatically.
- Fonts: Noto families per script. CJK and Arabic fonts load only on their own language pages.
- Add "npm run check:i18n". It fails if any key is missing or empty, placeholders differ, protected strings or numbers differ from English, or the registered-trademark symbol appears.

## Design direction
Elegant, calm, industrial-premium. Not a typical AI/SaaS template. Warm off-white background, charcoal text, crimson used sparingly, generous whitespace, thin rules, large editorial typography. Palette (approximate, sample exact values from design-assets/logo-original.jpg): crimson #D01A45, deep maroon #7A1230, charcoal #1C1C1C, grey #7A7A7A, paper #F6F3EE. Headings: a refined serif (e.g. Newsreader). Labels, nav, buttons: Montserrat, uppercase with wide letter-spacing, echoing the logo. Other scripts: matching Noto Serif / Noto Sans families. Self-host fonts (Fontsource), no Google Fonts requests. The logo's arch shape is used as an image frame and its up-arrow as a scroll cue. Avoid: purple/blue gradients, glassmorphism, emoji icons, identical three-card rows, stock-photo hero, blobs. Motion: subtle fade/translate on scroll, smooth, disabled for prefers-reduced-motion. Layouts must handle long German words, tall Indic scripts, CJK and right-to-left Arabic.

## Tech
Astro (latest stable), TypeScript strict, Tailwind CSS v4, static output. Hosted on Cloudflare Pages. Contact form via Web3Forms (key in env var, never committed) with honeypot and a consent checkbox. Accessible (WCAG AA), mobile-first, Lighthouse 95+, minimal JavaScript, sitemap and robots, social preview image.