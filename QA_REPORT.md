# Automated QA Test Report

**Execution Date**: 2026-10-15T11:03:30.336Z
**Overall Status**: ✅ PASS

## Summary Table

| Test Check | Description | Status | Evidence / Notes |
| :--- | :--- | :---: | :--- |
| **Check A** | No horizontal overflow & no clipped text (320px–1920px across all 12 languages) | PASS | Zero overflow or text clipping detected across 60 viewport combinations |
| **Check B** | Font audit (minimum 14px anywhere, no tiny micro-labels) | PASS | Smallest measured text: 14.0px (0.875rem on eyebrow, status, caption & facts labels) |
| **Check C** | axe-core & WCAG AA/AAA Contrast Verification | PASS | Zero serious or critical accessibility violations |
| **Check D** | Robustness (200% & 400% zoom, 20px & 24px default font, text-spacing override) | PASS | Remains fully functional with zero clipping or horizontal scroll at 320px |
| **Check E** | Keyboard Navigation & Visible 3px Focus Rings | PASS | All focusables have visible 3px outline with offset & double ring on dark/crimson |
| **Check F** | prefers-reduced-motion Handling | PASS | All animations halted under reduced motion emulation |
| **Check G** | Forbidden-Content Scan (Trademarks, DPIIT, "we supply", certifications) | PASS | Clean scan: zero forbidden claims or DEV stubs in dist/ |
| **Check H** | Content Completeness & Protected Identifiers | PASS | All protected identifiers (LLPIN, GSTIN, Company Name, addresses) verified |
| **Check I** | Internal Links & Security Audit | PASS | All internal anchor targets exist; external links have rel="noopener" |
| **Check J** | Lighthouse Mobile Scores (/ and /ar/) | PASS | English: Perf 99, A11y 100, BP 100, SEO 100; Arabic: Perf 98, A11y 100, BP 96, SEO 100 |
| **Check K** | Visual Screenshots & Review Sheet | PASS | 24 multi-language screenshots captured; qa/review-sheet.png generated |

## 10 Smallest Font Elements (Font Audit)

| Selector | Computed Size | Text Snippet |
| :--- | :---: | :--- |
| `span.text-[0.875rem].text-[var(--color-secondary)]` | 14.0px | "English" |
| `span.text-[0.875rem].text-[var(--color-secondary)]` | 14.0px | "Hindi" |
| `span.text-[0.875rem].text-[var(--color-secondary)]` | 14.0px | "Gujarati" |
| `span.text-[0.875rem].text-[var(--color-secondary)]` | 14.0px | "Spanish" |
| `span.text-[0.875rem].text-[var(--color-secondary)]` | 14.0px | "French" |
| `span.text-[0.875rem].text-[var(--color-secondary)]` | 14.0px | "German" |
| `span.text-[0.875rem].text-[var(--color-secondary)]` | 14.0px | "Italian" |
| `span.text-[0.875rem].text-[var(--color-secondary)]` | 14.0px | "Chinese Simplified" |
| `span.text-[0.875rem].text-[var(--color-secondary)]` | 14.0px | "Japanese" |
| `span.text-[0.875rem].text-[var(--color-secondary)]` | 14.0px | "Korean" |

## Measured Color Contrast Ratios

| Color Pair | Required Ratio | Measured Ratio | Result |
| :--- | :---: | :---: | :---: |
| Charcoal text (#1C1C1C) on Paper (#F6F3EE) | ≥ 7.0:1 | **15.40** | PASS |
| Secondary text (#55524F) on Paper (#F6F3EE) | ≥ 5.5:1 | **7.01** | PASS |
| Paper text (#F6F3EE) on Primary Button (#D01A45) | ≥ 4.5:1 | **4.85** | PASS |
| Paper text (#F6F3EE) on Button Hover (#7A1230) | ≥ 4.5:1 | **9.70** | PASS |
