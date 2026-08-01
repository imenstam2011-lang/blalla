@echo off
cd /d "c:\Users\Mega Pc\Desktop\Napse.vp"
C:\Python314\python.exe -c "from PIL import Image, ImageDraw; import os; os.makedirs('public', exist_ok=True); img=Image.new('RGBA',(512,512),(255,255,255,0)); d=ImageDraw.Draw(img); d.rounded_rectangle((24,24,488,488), radius=160, fill=(168,85,247,255)); d.rounded_rectangle((48,48,464,464), radius=140, outline=(255,255,255,220), width=24); d.line((140,140,140,370), fill=(255,255,255,255), width=30); d.line((140,250,300,370), fill=(255,255,255,255), width=30); d.line((300,140,300,370), fill=(255,255,255,255), width=30); img.save('public/napse-logo.png')"
echo Created public/napse-logo.png
