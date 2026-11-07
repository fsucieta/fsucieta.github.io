import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

/**
 * Générateur officiel du Sitemap XML Souverain de L'OCHJU (Standard Google & xhtml:link multilingue)
 * Sanctuarise strictement les 9 enquêtes publiques clôturées et exclut toute route confidentielle (noindex).
 */
export const GET: APIRoute = async () => {
  const siteUrl = 'https://fsucieta.github.io';
  const lastMod = '2026-11-07';

  // Liste stricte des 9 enquêtes officiellement finalisées et publiées
  const allowedIds = [27, 7, 23, 28, 26, 4, 18, 11, 22];
  const enquetes = (await getCollection('enquetes')).filter((e) => allowedIds.includes(e.data.id));
  const investigations = (await getCollection('investigations')).filter((e) => allowedIds.includes(e.data.id));

  // Langues supportées par la plateforme
  const langs = ['fr', 'en', 'it', 'es', 'pt', 'ru', 'zh', 'ja'];

  // 1. Pages d'accueil multilingues (Priorité 1.0)
  const homeRoutes = langs.map((lng) => ({
    loc: lng === 'fr' ? `${siteUrl}/` : `${siteUrl}/${lng}/`,
    priority: lng === 'fr' ? '1.0' : '0.9',
    changefreq: 'weekly',
    alternates: langs.map((alt) => ({
      hreflang: alt,
      href: alt === 'fr' ? `${siteUrl}/` : `${siteUrl}/${alt}/`,
    })),
  }));

  // 2. Dossiers publics de sources juridiques et mémorandum global (Priorité 0.9)
  const publicDossiers = [
    '/analyse-globale-finale/',
    '/dossier-sources-cadastre-minier/',
    '/dossier-sources-emprise-militaire/',
    '/dossier-transparence-citoyenne-ajaccio/',
  ].map((path) => ({
    loc: `${siteUrl}${path}`,
    priority: '0.9',
    changefreq: 'monthly',
    alternates: [],
  }));

  // 3. Pages Soutenir multilingues (Priorité 0.7)
  const supportRoutes = langs.map((lng) => ({
    loc: lng === 'fr' ? `${siteUrl}/soutenir/` : `${siteUrl}/${lng}/soutenir/`,
    priority: '0.7',
    changefreq: 'monthly',
    alternates: langs.map((alt) => ({
      hreflang: alt,
      href: alt === 'fr' ? `${siteUrl}/soutenir/` : `${siteUrl}/${alt}/soutenir/`,
    })),
  }));

  // 4. Les 9 grandes enquêtes dans les 8 langues avec correspondance exacte des slugs FR/EN (Priorité 1.0)
  const enqueteRoutes: Array<{
    loc: string;
    priority: string;
    changefreq: string;
    alternates: Array<{ hreflang: string; href: string }>;
  }> = [];

  for (const enq of enquetes) {
    const frSlug = enq.slug;
    const enMatch = investigations.find((inv) => inv.data.id === enq.data.id || inv.slug === frSlug);
    const enSlug = enMatch ? enMatch.slug : frSlug;

    const alternates = langs.map((alt) => {
      if (alt === 'fr') return { hreflang: 'fr', href: `${siteUrl}/enquetes/${frSlug}/` };
      if (alt === 'en') return { hreflang: 'en', href: `${siteUrl}/en/investigations/${enSlug}/` };
      return { hreflang: alt, href: `${siteUrl}/${alt}/enquetes/${frSlug}/` };
    });

    for (const alt of alternates) {
      enqueteRoutes.push({
        loc: alt.href,
        priority: alt.hreflang === 'fr' ? '1.0' : '0.85',
        changefreq: 'monthly',
        alternates,
      });
    }
  }

  const allUrls = [...homeRoutes, ...enqueteRoutes, ...publicDossiers, ...supportRoutes];

  const xmlItems = allUrls
    .map((item) => {
      const altLinks =
        item.alternates.length > 0
          ? [
              ...item.alternates.map(
                (a) => `    <xhtml:link rel="alternate" hreflang="${a.hreflang}" href="${a.href}" />`
              ),
              `    <xhtml:link rel="alternate" hreflang="x-default" href="${item.alternates[0].href}" />`,
            ].join('\n') + '\n'
          : '';

      return [
        '  <url>',
        `    <loc>${item.loc}</loc>`,
        `    <lastmod>${lastMod}</lastmod>`,
        `    <changefreq>${item.changefreq}</changefreq>`,
        `    <priority>${item.priority}</priority>`,
        altLinks ? altLinks.trimEnd() : null,
        '  </url>',
      ]
        .filter(Boolean)
        .join('\n');
    })
    .join('\n');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
${xmlItems}
</urlset>
`;

  return new Response(xml, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
    },
  });
};
