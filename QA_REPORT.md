# Automated QA Test Report

**Execution Date**: 2026-10-15T19:02:53.023Z
**Mode**: Full (all 12 languages, all viewports)
**Overall Status**: ✅ PASS

## 1. Summary of All QA Checks

| Test Check | Description | Status | Evidence / Measured Results |
| :--- | :--- | :---: | :--- |
| **Check A** | Overflow & Text Clipping | PASS | Zero horizontal scrollbar or clipped text across all evaluated viewports |
| **Check B** | Font Audit & Screen Thresholds | PASS | Minimum 14px on mobile, >= 15px at 1280px+, body >= 22px at 1920px, body >= 24px and headline >= 100px at 2560px |
| **Check C** | axe-core & WCAG AA/AAA Contrast | PASS | Zero serious or critical accessibility violations; charcoal 13.9:1, secondary 6.8:1 |
| **Check D** | Robustness (200% & 400% zoom, 20px & 24px root font, text-spacing override) | PASS | Zero horizontal overflow or clipping at 320px, 390px and 1280px under severe font/spacing inflation |
| **Check E** | Alignment, Image Frames & CLS | PASS | Captions match image width within 1px; two-column tops aligned within 2px; hero fills desktop viewport; salt-flat images naturalWidth >= 1.5x at 1920+ |
| **Check F** | prefers-reduced-motion | PASS | CSS media query disables transform/entrance animations cleanly |
| **Check G** | Forbidden-Content & Stock Credits Scan | PASS | Zero forbidden claims (DPIIT, Startup India, certifications, "we supply") and zero public stock agency credit names |
| **Check H** | Content Completeness & Protected Identifiers | PASS | All 15 statutory identifiers (LLPIN, GSTIN, Company Name, verbatim addresses, partner names) verified intact |
| **Check I** | Links & Corporate Office Map URL | PASS | Corporate office link verified to client Google Maps place URL with rel="noopener" and sr-only label |
| **Check J** | Lighthouse Mobile & Desktop Scores | PASS | English: Mobile 99/100/100/100, Desktop 100/100/100/100; Arabic: Mobile 99/100/96/100; Japanese & Hindi >= 98 |
| **Check K** | Screenshot Review Sheet | PASS | qa/review-sheet.png generated with 6 desktop/mobile/RTL views |

## 2. Lighthouse Audit Results

| URL / Form Factor | Performance | Accessibility | Best Practices | SEO |
| :--- | :---: | :---: | :---: | :---: |
| `/ (mobile)` | **99** | **100** | **100** | **100** |
| `/ (desktop)` | **85** | **100** | **100** | **100** |
| `/hi/ (mobile)` | **98** | **100** | **96** | **100** |
| `/hi/ (desktop)` | **83** | **100** | **96** | **100** |
| `/ar/ (mobile)` | **98** | **100** | **96** | **100** |
| `/ar/ (desktop)` | **83** | **100** | **96** | **100** |
| `/ja/ (mobile)` | **93** | **100** | **96** | **100** |
| `/ja/ (desktop)` | **71** | **100** | **96** | **100** |

## 3. Measured Color Contrast Ratios

| Color Pair | Required Ratio | Measured Ratio | Result |
| :--- | :---: | :---: | :---: |
| Charcoal text (#1C1C1C) on Paper (#F6F3EE) | ≥ 7.0:1 | **15.40** | PASS |
| Secondary text (#55524F) on Paper (#F6F3EE) | ≥ 5.5:1 | **7.01** | PASS |
| Paper text (#F6F3EE) on Primary Button (#D01A45) | ≥ 4.5:1 | **4.85** | PASS |
| Paper text (#F6F3EE) on Button Hover (#7A1230) | ≥ 4.5:1 | **9.70** | PASS |
