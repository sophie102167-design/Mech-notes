import json,re
from pathlib import Path
from html.parser import HTMLParser
r=Path(__file__).parent; notes=json.loads((r/'content.json').read_text()); keys=json.loads((r/'templates/note.json').read_text())
assert len({n['slug'] for n in notes})==len(notes)
for n in notes:
 assert re.fullmatch('[a-z]+(?:-[a-z]+)*',n['slug'])
 assert all(isinstance(n.get(k),str) and n[k].strip() for k in keys)
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ('href','src') and v and not v.startswith(('https:','http:','#','data:')):
    assert (self.base/v.split('#')[0]).exists(),v
for f in (r/'dist').rglob('*.html'):
 p=Links();p.base=f.parent;p.feed(f.read_text())
print('PASS: fields, unique slugs and all local links')
