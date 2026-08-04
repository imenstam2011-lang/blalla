"""
Replaced generator: download the official Discord-hosted Napse logo
so running this script will not overwrite the canonical site logo.
"""
from urllib.request import Request, urlopen
from pathlib import Path
import os

URL = "https://cdn.discordapp.com/attachments/1506255547169640553/1533029157481484328/Napse.vp.jfif?ex=6a6f0029&is=6a6daea9&hm=62501d9117095c205f724a771748f643922fb63cb93de7607b96bdb7a9702b15"
out_path = Path('public/napse-logo.png')
out_path.parent.mkdir(exist_ok=True)

req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
data = urlopen(req).read()
tmp = out_path.with_suffix('.jfif')
with open(tmp, 'wb') as f:
	f.write(data)

# Try convert to PNG if PIL available, else leave jfif
try:
	from PIL import Image
	img = Image.open(tmp).convert('RGBA')
	img.save(out_path)
	tmp.unlink(missing_ok=True)
	print(f'Updated {out_path}')
except Exception:
	print(f'Downloaded logo to {tmp}, PIL not available to convert to PNG.')
