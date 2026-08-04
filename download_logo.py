from urllib.request import Request, urlopen
import os, sys
from PIL import Image

url = "https://cdn.discordapp.com/attachments/1506255547169640553/1533029157481484328/Napse.vp.jfif?ex=6a6f0029&is=6a6daea9&hm=62501d9117095c205f724a771748f643922fb63cb93de7607b96bdb7a9702b15"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

req = Request(url, headers=headers)
try:
    data = urlopen(req).read()
except Exception as e:
    print('DOWNLOAD_FAILED', e)
    sys.exit(2)

os.makedirs('public', exist_ok=True)
jfif_path = os.path.join('public', 'napse-logo.jfif')
with open(jfif_path, 'wb') as f:
    f.write(data)

try:
    img = Image.open(jfif_path).convert('RGBA')
    png_path = os.path.join('public', 'napse-logo.png')
    img.save(png_path)
    print('SAVED', png_path)
except Exception as e:
    print('CONVERT_FAILED', e)
    sys.exit(3)
