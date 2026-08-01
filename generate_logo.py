from PIL import Image, ImageDraw
from pathlib import Path

out_path = Path('public/napse-logo.png')
out_path.parent.mkdir(exist_ok=True)

size = (512, 512)
img = Image.new('RGBA', size, (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Background circle
circle_bbox = (24, 24, size[0] - 24, size[1] - 24)
draw.rounded_rectangle(circle_bbox, radius=140, fill=(168, 85, 247, 255))

# White ring
ring_bbox = (48, 48, size[0] - 48, size[1] - 48)
draw.rounded_rectangle(ring_bbox, radius=120, outline=(255, 255, 255, 220), width=22)

# Simple monogram N
monogram = [(120, 150), (120, 360), (200, 250), (280, 360), (280, 150)]
draw.line(monogram, fill=(255, 255, 255, 255), width=30)

# Small accent dot
# draw.ellipse((320, 150, 360, 190), fill=(255,255,255,255))

img.save(out_path)
print(f'Created {out_path}')
