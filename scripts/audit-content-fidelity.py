from pathlib import Path
from html.parser import HTMLParser
import json,re,unicodedata,difflib
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'migration/manifest.json').read_text(encoding='utf-8'))
export=json.loads((root/'migration/legacy-export.json').read_text(encoding='utf-8'))
class Text(HTMLParser):
 def __init__(self,original=False):super().__init__(convert_charrefs=True);self.original=original;self.stack=[];self.parts=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);parent=self.stack[-1] if self.stack else ('',self.original,False)
  capture=parent[1] or 'sl-markdown-content' in a.get('class','').split() or (tag=='h1' and a.get('id')=='_top')
  ignore=parent[2] or tag in ['script','style','button'] or 'sr-only' in a.get('class','').split() or a.get('id')=='markdown-toc'
  if tag not in ['br','hr','img','input','link','meta','source','wbr','area','base','col','embed','param','track']:self.stack.append((tag,capture,ignore))
 def handle_endtag(self,tag):
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i][0]==tag:self.stack=self.stack[:i];break
 def handle_data(self,data):
  frame=self.stack[-1] if self.stack else ('',self.original,False)
  if frame[1] and not frame[2]:self.parts.append(data)
def normalized(html,original):
 p=Text(original);p.feed(html);s=unicodedata.normalize('NFKC',''.join(p.parts))
 return re.sub(r'\s+','',s.translate(str.maketrans({'“':'"','”':'"','‘':"'",'’':"'",'–':'-','—':'-','↩':'','\ufe0e':'','\ufe0f':''})))
class Code(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.pre=0;self.capture=False;self.codes=[];self.buffer=[]
 def handle_starttag(self,tag,attrs):
  if tag=='pre':self.pre+=1
  if tag=='code' and self.pre:self.capture=True;self.buffer=[]
 def handle_data(self,data):
  if self.capture:self.buffer.append(data)
 def handle_endtag(self,tag):
  if tag=='code' and self.capture:self.codes.append(re.sub(r'\s+','',''.join(self.buffer)));self.capture=False
  if tag=='pre':self.pre=max(0,self.pre-1)
def code_blocks(text):
 p=Code();p.feed(text);return p.codes
rows=[]
for page in manifest['pages']:
 before=normalized(export[page['source']]['html'],True)
 if page['mode']=='markdown':before=re.sub(r'\{:(?:\.|#|width=|height=)[^}]+\}', '', before)
 after=normalized((root/'dist'/page['slug']/'index.html').read_text(encoding='utf-8'),False)
 coverage=1.0 if not before or before==after or before in after else sum(m.size for m in difflib.SequenceMatcher(None,before,after,autojunk=False).get_matching_blocks())/len(before)
 oldCode=code_blocks(export[page['source']]['html']);newCode=code_blocks((root/'dist'/page['slug']/'index.html').read_text(encoding='utf-8'))
 missingCode=[code for code in oldCode if code and code not in newCode]
 rows.append({'missingCodeBlocks':len(missingCode),'source':page['source'],'slug':page['slug'],'sourceCharacters':len(before),'coverage':round(coverage,6)})
report={'method':'Normalized document title and body text; generated TOCs, assistive labels, copy buttons and regular-Markdown sizing annotations excluded. Original source SHA-256 is verified separately. This is an initial migration audit, not a restriction on future edits.','pages':rows,'minimumCoverage':min(r['coverage'] for r in rows),'belowThreshold':[r for r in rows if r['coverage']<0.99], 'codeBlockFailures':[r for r in rows if r['missingCodeBlocks']]}
(root/'migration/validation/content-fidelity.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'pages':len(rows),'minimumCoverage':report['minimumCoverage'],'belowThreshold':report['belowThreshold'],'codeBlockFailures':report['codeBlockFailures']},ensure_ascii=False))
if report['belowThreshold'] or report['codeBlockFailures']:raise SystemExit(1)
