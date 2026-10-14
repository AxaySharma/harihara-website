import en from './en.json';
import hi from './hi.json';
import gu from './gu.json';
import es from './es.json';
import fr from './fr.json';
import de from './de.json';
import it from './it.json';
import zh from './zh.json';
import ja from './ja.json';
import ko from './ko.json';
import ar from './ar.json';
import pt from './pt.json';
import { defaultLang, languages } from './languages.config';

export const translations: Record<string, typeof en> = {
  en,
  hi,
  gu,
  es,
  fr,
  de,
  it,
  zh,
  ja,
  ko,
  ar,
  pt,
};

type NestedKeyOf<ObjectType extends object> = {
  [Key in keyof ObjectType & (string | number)]: ObjectType[Key] extends object
    ? `${Key}` | `${Key}.${NestedKeyOf<ObjectType[Key]>}`
    : `${Key}`;
}[keyof ObjectType & (string | number)];

export type TranslationKey = NestedKeyOf<typeof en>;

export function getLangFromUrl(url: URL): string {
  const [, lang] = url.pathname.split('/');
  if (lang && lang in languages) {
    return lang;
  }
  return defaultLang;
}

export function useTranslations(lang: string = defaultLang) {
  const currentTranslations = translations[lang] || translations[defaultLang];

  return function t(key: string): string {
    const keys = key.split('.');
    let current: unknown = currentTranslations;
    for (const k of keys) {
      if (current && typeof current === 'object' && k in current) {
        current = (current as Record<string, unknown>)[k];
      } else {
        // Fallback to default lang
        let fallback: unknown = translations[defaultLang];
        for (const fk of keys) {
          if (fallback && typeof fallback === 'object' && fk in fallback) {
            fallback = (fallback as Record<string, unknown>)[fk];
          } else {
            return key;
          }
        }
        return typeof fallback === 'string' ? fallback : key;
      }
    }
    return typeof current === 'string' ? current : key;
  };
}
