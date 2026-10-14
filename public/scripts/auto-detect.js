(function () {
  try {
    // Only auto-detect on the root URL path '/'
    var currentPath = window.location.pathname;
    if (currentPath !== '/' && currentPath !== '') {
      return;
    }

    // Never override a manual user choice
    var savedChoice = localStorage.getItem('user_selected_lang');
    if (savedChoice) {
      if (savedChoice !== 'en') {
        window.location.replace('/' + savedChoice + '/');
      }
      return;
    }

    // Check navigator language
    var navLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
    if (!navLang) {
      return;
    }

    // Supported target locales mapping
    var target = null;
    if (navLang.startsWith('hi')) {
      target = 'hi';
    } else if (navLang.startsWith('gu')) {
      target = 'gu';
    } else if (navLang.startsWith('zh')) {
      target = 'zh';
    } else if (navLang.startsWith('ja')) {
      target = 'ja';
    } else if (navLang.startsWith('ko')) {
      target = 'ko';
    } else if (navLang.startsWith('ar')) {
      target = 'ar';
    } else if (navLang.startsWith('pt')) {
      target = 'pt';
    } else if (navLang.startsWith('es')) {
      target = 'es';
    } else if (navLang.startsWith('fr')) {
      target = 'fr';
    } else if (navLang.startsWith('de')) {
      target = 'de';
    } else if (navLang.startsWith('it')) {
      target = 'it';
    }

    if (target && target !== 'en') {
      window.location.replace('/' + target + '/');
    }
  } catch (e) {
    // Graceful fallback if cookies or storage are blocked
  }
})();
