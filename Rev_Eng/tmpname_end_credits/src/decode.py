import PIL
import pytesseract




pdf = pytesseract.image_to_pdf_or_hocr('bins.jpg', extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) 


