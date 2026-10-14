import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const i18nDir = path.resolve(__dirname, '../src/i18n');

const englishFile = path.join(i18nDir, 'en.json');
const glossaryFile = path.join(i18nDir, 'glossary.json');

if (!fs.existsSync(englishFile)) {
  console.error('Error: en.json not found!');
  process.exit(1);
}

const enData = JSON.parse(fs.readFileSync(englishFile, 'utf-8'));
let glossary = { terms: {}, protected_terms: [] };
if (fs.existsSync(glossaryFile)) {
  glossary = JSON.parse(fs.readFileSync(glossaryFile, 'utf-8'));
}

const langFiles = fs.readdirSync(i18nDir).filter(f => f.endsWith('.json') && f !== 'glossary.json');

let hasErrors = false;

function getAllKeys(obj, prefix = '') {
  let keys = [];
  for (const [key, value] of Object.entries(obj)) {
    const fullKey = prefix ? `${prefix}.${key}` : key;
    if (value && typeof value === 'object' && !Array.isArray(value)) {
      keys = keys.concat(getAllKeys(value, fullKey));
    } else {
      keys.push(fullKey);
    }
  }
  return keys;
}

function getValueByPath(obj, pathStr) {
  return pathStr.split('.').reduce((acc, part) => (acc ? acc[part] : undefined), obj);
}

function extractPlaceholders(str) {
  if (typeof str !== 'string') return [];
  const matches = str.match(/\{[a-zA-Z0-9_-]+\}/g) || [];
  return matches.sort();
}

function extractNumbers(str) {
  if (typeof str !== 'string') return [];
  // Match standalone integer/decimal numbers, phone numbers etc.
  const matches = str.match(/\b\d+(\.\d+)?\b/g) || [];
  return matches.sort();
}

const enKeys = getAllKeys(enData);

for (const file of langFiles) {
  const filePath = path.join(i18nDir, file);
  const rawContent = fs.readFileSync(filePath, 'utf-8');

  if (rawContent.includes('®')) {
    console.error(`[FAIL] ${file}: Contains registered trademark symbol '®'.`);
    hasErrors = true;
  }
  if (rawContent.includes('™')) {
    console.error(`[FAIL] ${file}: Contains trademark symbol '™'. The brief states logo image contains TM mark; no text TM allowed.`);
    hasErrors = true;
  }

  let data;
  try {
    data = JSON.parse(rawContent);
  } catch (err) {
    console.error(`[FAIL] ${file}: Invalid JSON syntax.`);
    hasErrors = true;
    continue;
  }

  const currentKeys = getAllKeys(data);

  // Check missing keys
  for (const key of enKeys) {
    const enVal = getValueByPath(enData, key);
    const currVal = getValueByPath(data, key);

    if (currVal === undefined) {
      console.error(`[FAIL] ${file}: Missing key '${key}'.`);
      hasErrors = true;
    } else if (typeof currVal === 'string' && currVal.trim() === '') {
      console.error(`[FAIL] ${file}: Empty value for key '${key}'.`);
      hasErrors = true;
    } else if (typeof currVal === 'string' && typeof enVal === 'string') {
      // Check placeholders
      const enPlaceholders = extractPlaceholders(enVal);
      const currPlaceholders = extractPlaceholders(currVal);
      if (JSON.stringify(enPlaceholders) !== JSON.stringify(currPlaceholders)) {
        console.error(`[FAIL] ${file}: Placeholders mismatch in key '${key}'. Expected ${enPlaceholders.join(', ')}, got ${currPlaceholders.join(', ')}.`);
        hasErrors = true;
      }

      // Check numbers
      const enNumbers = extractNumbers(enVal);
      const currNumbers = extractNumbers(currVal);
      // In Arabic or Indic, numbers might be preserved in ASCII or localized; if ASCII numbers exist in English, check if they exist in translated unless Indic digits are deliberately used.
      // But rule: "numbers differ from English"
      if (enNumbers.length > 0 && currNumbers.length > 0) {
        if (JSON.stringify(enNumbers) !== JSON.stringify(currNumbers)) {
          console.warn(`[WARN] ${file}: Numbers in key '${key}' differ. English: ${enNumbers.join(',')}, Target: ${currNumbers.join(',')}`);
        }
      }
    }
  }

  // Check for extra keys not in en
  for (const key of currentKeys) {
    if (!enKeys.includes(key)) {
      console.warn(`[WARN] ${file}: Extra key '${key}' not found in English template.`);
    }
  }

  // Check protected strings (e.g. company name, LLPIN, GSTIN, phone, etc.)
  if (glossary.protected_terms && Array.isArray(glossary.protected_terms)) {
    // If a key contains a protected string in English, it should maintain it in translation
    for (const key of enKeys) {
      const enVal = getValueByPath(enData, key);
      const currVal = getValueByPath(data, key);
      if (typeof enVal === 'string' && typeof currVal === 'string') {
        for (const protectedStr of glossary.protected_terms) {
          if (enVal.includes(protectedStr) && !currVal.includes(protectedStr)) {
            console.error(`[FAIL] ${file}: Protected string '${protectedStr}' missing in key '${key}'.`);
            hasErrors = true;
          }
        }
      }
    }
  }
}

if (hasErrors) {
  console.error('\n❌ check:i18n failed with errors.');
  process.exit(1);
} else {
  console.log('✅ check:i18n passed! All locale files are valid.');
}
