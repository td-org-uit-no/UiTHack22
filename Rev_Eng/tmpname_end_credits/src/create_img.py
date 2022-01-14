from PIL import Image, ImageDraw, ImageFont






img = Image.new('RGB', (100, 30), color = (255,255,255))
 
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
d = ImageDraw.Draw(img)
d.text((10,10), "Hello world", font=fnt, fill=(255, 255, 0))
 
img.save('pil_text_font.png')