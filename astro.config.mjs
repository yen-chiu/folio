import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { satteri } from '@astrojs/markdown-satteri';
import legacyContent from './src/plugins/legacy-content.mjs';
import { sidebar } from './src/navigation.mjs';
import { legacyRedirects } from './migration/routes.mjs';

export default defineConfig({
  site: 'https://yenchiu.com',
  base: '/folio',
  trailingSlash: 'always',
  output: 'static',
  markdown: { processor: satteri({ features: { smartPunctuation:false }, hastPlugins:[legacyContent] }) },
  redirects: Object.fromEntries(Object.entries(legacyRedirects).map(([from,to]) => [from, `/folio${to}`])),
  integrations: [starlight({
    title: 'Folio',
    description: '把经验写成可查阅的知识。博客指南、建站笔记与日常积累。',
    favicon: '/favicon.svg',
    defaultLocale: 'root',
    locales: { root: { label: '简体中文', lang: 'zh-CN' } },
    social: [{ icon:'github', label:'GitHub', href:'https://github.com/yen-chiu/folio' }],
    editLink: { baseUrl: 'https://github.com/yen-chiu/folio/edit/main/' },
    tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
    sidebar,
    expressiveCode: { frames: { extractFileNameFromCode:false } },
    components: { Footer:'./src/components/Footer.astro' },
    customCss: ['./src/styles/custom.css'],
    head: [{tag:'meta',attrs:{name:'robots',content:'noindex, follow'}}]
  })]
});
