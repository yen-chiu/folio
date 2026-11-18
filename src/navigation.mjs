import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
const root = fileURLToPath(new URL('./content/docs/', import.meta.url));
function page(path) {
  const text=readFileSync(root + path, 'utf8');
  const frontmatter=parse(text.match(/^---\s*\n([\s\S]*?)\n---/)?.[1] || '') || {};
  return { ...frontmatter, slug:frontmatter.slug || path.replace(/\.mdx?$/, '').replace(/\/index$/, '') };
}
function group(directory, label, collapsed=true) {
  const overviewPath=existsSync(root+directory+'.md') ? directory+'.md' : directory+'/index.md';
  const overview=existsSync(root+overviewPath) ? page(overviewPath) : undefined;
  const entries=readdirSync(root+directory,{withFileTypes:true});
  const directories=entries.filter(entry=>entry.isDirectory());
  const rows=[];
  for(const entry of directories) {
    const child=directory+'/'+entry.name;
    const index=existsSync(root+child+'.md') ? page(child+'.md') : existsSync(root+child+'/index.md') ? page(child+'/index.md') : undefined;
    rows.push({order:index?.sidebar?.order ?? 999, name:index?.title || entry.name, item:group(child,index?.title || entry.name)});
  }
  for(const entry of entries.filter(entry=>entry.isFile()&&/\.mdx?$/.test(entry.name))) {
    if(entry.name==='index.md'||directories.some(dir=>entry.name===dir.name+'.md'))continue;
    const data=page(directory+'/'+entry.name);
    if(data.sidebar?.hidden)continue;
    rows.push({order:data.sidebar?.order ?? 999, name:data.title, item:{slug:data.slug}});
  }
  rows.sort((a,b)=>a.order-b.order||a.name.localeCompare(b.name,'zh-CN'));
  return {label,collapsed,items:[...(overview&&!overview.sidebar?.hidden?[{slug:overview.slug,label:'概览'}]:[]),...rows.map(row=>row.item)]};
}
export const sidebar = [
  {slug:'start-here'},
  group('blog-guide','博客指南',false),
  group('building','建站笔记'),
  group('resources','资料导航'),
  group('notes','其他笔记'),
  group('legacy-guides','旧主题参考')
];
