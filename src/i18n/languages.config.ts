export type LanguageStatus = 'draft' | 'ai-checked' | 'human-reviewed';
export type TextDirection = 'ltr' | 'rtl';

export interface LanguageConfig {
  code: string;
  path: string;
  name: string;
  nativeName: string;
  direction: TextDirection;
  htmlLang: string;
  status: LanguageStatus;
  fontCategory?: 'latin' | 'devanagari' | 'gujarati' | 'sc' | 'jp' | 'kr' | 'arabic';
}

export const languages: Record<string, LanguageConfig> = {
  en: {
    code: 'en',
    path: '',
    name: 'English',
    nativeName: 'English',
    direction: 'ltr',
    htmlLang: 'en',
    status: 'human-reviewed',
    fontCategory: 'latin',
  },
  hi: {
    code: 'hi',
    path: 'hi',
    name: 'Hindi',
    nativeName: 'हिन्दी',
    direction: 'ltr',
    htmlLang: 'hi',
    status: 'draft',
    fontCategory: 'devanagari',
  },
  gu: {
    code: 'gu',
    path: 'gu',
    name: 'Gujarati',
    nativeName: 'ગુજરાતી',
    direction: 'ltr',
    htmlLang: 'gu',
    status: 'draft',
    fontCategory: 'gujarati',
  },
  es: {
    code: 'es',
    path: 'es',
    name: 'Spanish',
    nativeName: 'Español',
    direction: 'ltr',
    htmlLang: 'es',
    status: 'draft',
    fontCategory: 'latin',
  },
  fr: {
    code: 'fr',
    path: 'fr',
    name: 'French',
    nativeName: 'Français',
    direction: 'ltr',
    htmlLang: 'fr',
    status: 'draft',
    fontCategory: 'latin',
  },
  de: {
    code: 'de',
    path: 'de',
    name: 'German',
    nativeName: 'Deutsch',
    direction: 'ltr',
    htmlLang: 'de',
    status: 'draft',
    fontCategory: 'latin',
  },
  it: {
    code: 'it',
    path: 'it',
    name: 'Italian',
    nativeName: 'Italiano',
    direction: 'ltr',
    htmlLang: 'it',
    status: 'draft',
    fontCategory: 'latin',
  },
  zh: {
    code: 'zh',
    path: 'zh',
    name: 'Chinese Simplified',
    nativeName: '简体中文',
    direction: 'ltr',
    htmlLang: 'zh-Hans',
    status: 'draft',
    fontCategory: 'sc',
  },
  ja: {
    code: 'ja',
    path: 'ja',
    name: 'Japanese',
    nativeName: '日本語',
    direction: 'ltr',
    htmlLang: 'ja',
    status: 'draft',
    fontCategory: 'jp',
  },
  ko: {
    code: 'ko',
    path: 'ko',
    name: 'Korean',
    nativeName: '한국어',
    direction: 'ltr',
    htmlLang: 'ko',
    status: 'draft',
    fontCategory: 'kr',
  },
  ar: {
    code: 'ar',
    path: 'ar',
    name: 'Arabic',
    nativeName: 'العربية',
    direction: 'rtl',
    htmlLang: 'ar',
    status: 'draft',
    fontCategory: 'arabic',
  },
  pt: {
    code: 'pt',
    path: 'pt',
    name: 'Portuguese',
    nativeName: 'Português',
    direction: 'ltr',
    htmlLang: 'pt-BR',
    status: 'draft',
    fontCategory: 'latin',
  },
};

export const defaultLang = 'en';

export function getVisibleLanguages(showDrafts: boolean = false): LanguageConfig[] {
  return Object.values(languages).filter((lang) => {
    if (showDrafts) return true;
    return lang.status === 'ai-checked' || lang.status === 'human-reviewed';
  });
}
