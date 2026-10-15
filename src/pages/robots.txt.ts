import type { APIRoute } from 'astro';

export const GET: APIRoute = ({ site }) => {
  const isNoIndex = import.meta.env.PUBLIC_NOINDEX === 'true' || process.env.PUBLIC_NOINDEX === 'true';

  let content = '';
  if (isNoIndex) {
    content = 'User-agent: *\nDisallow: /\n';
  } else {
    const siteUrl = site ? site.toString().replace(/\/$/, '') : 'https://harihara.net';
    content = `User-agent: *\nAllow: /\n\nSitemap: ${siteUrl}/sitemap-index.xml\n`;
  }

  return new Response(content, {
    headers: {
      'Content-Type': 'text/plain; charset=utf-8',
    },
  });
};
