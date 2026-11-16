from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
r=Path(__file__).parent
with ZipFile(r/'dist/mech-notes-project.zip','w',ZIP_DEFLATED) as z:
 for f in r.rglob('*'):
  rel=f.relative_to(r)
  if f.is_file() and not any(x in rel.parts for x in ['.git','.openai','__pycache__']) and f.suffix!='.zip':z.write(f,rel)
print('Packaged source and website')
