from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote,urljoin
import json,hashlib,re,collections
root=Path(__file__).resolve().parents[1];dist=root/'dist';base='/folio'
manifest=json.loads((root/'migration/manifest.json').read_text(encoding='utf-8'))
class Page(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.ids=set();self.refs=[];self.redirect=None;self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  if tag in ['a','link'] and a.get('href'):self.refs.append(a['href'])
  if tag in ['img','script','source','video','iframe'] and a.get('src'):self.refs.append(a['src'])
  if tag=='meta' and a.get('http-equiv','').lower()=='refresh':self.redirect=a.get('content','').split('url=',1)[-1]
pages={}
for p in dist.rglob('*.html'):
 page=Page();page.feed(p.read_text(encoding='utf-8'));pages[p.relative_to(dist).as_posix()]=page
errors=[];refs=0
for row in manifest['pages']:
 original=root/'migration/source'/row['source']
 assert hashlib.sha256(original.read_bytes()).hexdigest()==row['sourceSha256'],row['source']
 key=row['slug']+'/index.html'
 assert key in pages,('Missing migrated page',key)
 assert pages[key].h1==1,('Expected one page title',key,pages[key].h1)
for asset in manifest['assets']:
 assert hashlib.sha256((root/'public'/asset['path']).read_bytes()).hexdigest()==asset['sha256'],asset['path']
 assert (dist/asset['path']).is_file(),asset['path']
for name,page in pages.items():
 current='https://folio.invalid'+base+'/'+name.removesuffix('index.html')
 if page.redirect:
  assert page.redirect.startswith(base+'/'),(name,page.redirect)
  target=unquote(urlsplit(page.redirect).path).removeprefix(base).strip('/')
  assert (dist/target/'index.html').is_file(),(name,target)
 for ref in page.refs:
  if ref.startswith(('data:','mailto:','tel:','javascript:')):continue
  u=urlsplit(urljoin(current,ref))
  if u.netloc!='folio.invalid':continue
  refs+=1
  path=unquote(u.path)
  if not(path==base or path.startswith(base+'/')):
   errors.append({'page':name,'link':ref,'reason':'root path escapes /folio'});continue
  relative=path.removeprefix(base).lstrip('/')
  target=dist/relative
  if target.is_dir():target=target/'index.html'
  elif not target.exists() and not target.suffix:target=target/'index.html'
  if not target.is_file():errors.append({'page':name,'link':ref,'reason':'missing target'});continue
  if u.fragment and target.suffix=='.html':
   key=target.relative_to(dist).as_posix();fragment=unquote(u.fragment)
   if key in pages and fragment not in pages[key].ids:errors.append({'page':name,'link':ref,'reason':'missing anchor'})
diagram_example=(dist/'legacy-guides/index-test/index.html').read_text(encoding='utf-8')
assert 'class="folio-mermaid-source"' in diagram_example and 'data-mermaid-source=' in diagram_example,'Archived Mermaid source marker missing'
assert (dist/'pagefind/pagefind.js').exists(),'Search bundle missing'
assert list((dist/'pagefind').glob('*.pf_meta')),'Search index missing'
report={'sourceCommit':manifest['sourceCommit'],'migratedPages':len(manifest['pages']),'htmlPages':len(pages),'staticAssets':len(manifest['assets']),'localReferences':refs,'errors':errors}
(root/'migration/validation').mkdir(exist_ok=True)
(root/'migration/validation/build.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='errors'},ensure_ascii=False))
if errors:
 print(json.dumps(errors[:35],ensure_ascii=False,indent=2));raise SystemExit(f'{len(errors)} broken references')
print('All migrated destinations, original snapshots, copied assets, local links, anchors and search files verified')
