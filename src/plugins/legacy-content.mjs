import { htmlToHast } from 'satteri';
import manifest from '../../migration/manifest.json' with { type: 'json' };
import headings from '../../migration/headings.json' with { type: 'json' };
import { legacyRedirects } from '../../migration/routes.mjs';

const assets = new Set(manifest.assets.map(asset => '/' + asset.path));
const hosts = new Set(['yenchiu.com', 'yen-chiu.github.io']);
const routeKey = path => (path.replace(/\.(md|html)$/i, '').replace(/\/index$/, '').replace(/\/+$/, '') || '') + '/';

export function rewriteLegacyUrl(value, legacyUrl) {
  if (!legacyUrl || typeof value !== 'string' || !value || value.startsWith('#') || /^(data:|mailto:|tel:|javascript:)/i.test(value)) return value;
  if (value.startsWith('/folio/')) return value;
  const rawAsset = 'https://raw.githubusercontent.com/yen-chiu/WendellManual/master';
  if (value.startsWith(rawAsset + '/assets/')) {
    const path = value.slice(rawAsset.length);
    if (assets.has(decodeURI(path))) return '/folio' + path;
  }
  let url;
  try { url = new URL(value, 'https://yenchiu.com/WendellManual' + legacyUrl); } catch { return value; }
  if (!hosts.has(url.host)) return value;
  let path = decodeURI(url.pathname);
  const legacy = path === '/WendellManual' || path.startsWith('/WendellManual/');
  if (legacy) path = path.slice('/WendellManual'.length) || '/';
  if (assets.has(path)) return '/folio' + path + url.search + url.hash;
  const key = routeKey(path);
  const target = key === '/' && legacy ? '/' : legacyRedirects[key];
  if (target) return '/folio' + target + url.search + url.hash;
  return value;
}

export default function legacyContent({ fileURL }) {
  if (!fileURL) return;
  const path = decodeURIComponent(fileURL.pathname).replaceAll('\\', '/');
  const page = manifest.pages.find(page => path.endsWith('/' + page.destination));
  if (!page) return;
  const used = new Set();
  let titleRemoved=false;
  const candidates = headings[page.legacyUrl] || [];
  return {
    name: 'folio-legacy-content',
    before(root, ctx) {
      if (page.mode !== 'archived-html') return;
      const source = ctx.source.replace(/^---\s*\n[\s\S]*?\n---\s*\n/, '');
      ctx.replaceNode(root, htmlToHast(source, { fragment:true }));
    },
    element: { filter: [], visit(node, ctx) {
      const properties = { ...node.properties };
      let tagName = node.tagName;
      let changed = false;
      for (const key of ['href', 'src', 'poster']) {
        const rewritten = rewriteLegacyUrl(properties[key], page.legacyUrl);
        if (rewritten !== properties[key]) { properties[key] = rewritten; changed = true; }
      }
      if (page.mode === 'archived-html' && tagName === 'code' && ctx.parent(node)?.tagName === 'pre') {
        // Rouge splits one code block into spans. Expressive Code expects a complete text node.
        let ancestor=node;
        for(let depth=0;depth<4&&ancestor;depth++,ancestor=ctx.parent(ancestor)) {
          const value=ancestor.properties?.class || ancestor.properties?.className || '';
          const language=String(value).match(/language-([a-zA-Z0-9_-]+)/)?.[1];
          if(language) { delete properties.class; properties.className=['language-'+language]; break; }
        }
        return { ...node, properties, children:[{type:'text',value:ctx.textContent(node)}] };
      }
      if (tagName === 'h1' && !titleRemoved && ctx.textContent(node).trim() === page.title) {
        titleRemoved=true;
        const id=properties.id || candidates.find(heading=>heading.text.trim()===page.title)?.id;
        return {type:'element',tagName:'span',properties:{...(id?{id}:{}),'aria-hidden':'true'},children:[]};
      }
      if (/^h[1-6]$/.test(tagName)) {
        if (tagName === 'h1') { tagName = 'h2'; changed = true; }
        if (!properties.id) {
          const text = ctx.textContent(node).replace(/\s+/g, ' ').trim();
          const candidate = candidates.find((heading, index) => !used.has(index) && heading.id && heading.text.replace(/\s+/g, ' ').trim() === text);
          if (candidate) {
            used.add(candidates.indexOf(candidate)); properties.id = candidate.id; changed = true;
          }
        }
      }
      if (changed) return { ...node, tagName, properties };
    } }
  };
}
