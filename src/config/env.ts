/**
 * Helper to read build-time environment flags consistently from both
 * process.env (real shell/Cloudflare environment variables) and
 * import.meta.env (.env file loaded by Vite/Astro), with process.env winning.
 */
export function getEnvFlag(name: string, defaultValue: boolean = false): boolean {
  // 1. Process environment (Cloudflare Pages dashboard, CI, or shell environment)
  if (typeof process !== 'undefined' && process.env && typeof process.env[name] !== 'undefined') {
    const val = process.env[name]?.trim().toLowerCase();
    return val === 'true' || val === '1';
  }

  // 2. Vite / Astro environment (loaded from .env if present)
  try {
    if (typeof import.meta !== 'undefined' && import.meta.env && typeof import.meta.env[name] !== 'undefined') {
      const val = String(import.meta.env[name]).trim().toLowerCase();
      return val === 'true' || val === '1';
    }
  } catch {
    // import.meta may not exist in pure node scripts
  }

  return defaultValue;
}
