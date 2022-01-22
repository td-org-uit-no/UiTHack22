># May the force be with you!

>Contact Forces	| Non contact Forces| Other Forces|
>--- | ---| ---|
>Muscular force | Magnetic force| Walk on Water
>Frictional force |	Gravitational force| **Brute Force**
>Tension force	| Electrostatic force | *The Force*
>Applied force	|   | Forza Horizon 5  
>Normal force	|   | Turn water into wine 
>Air resistance force |	
>Mechanical force	|
>Spring force	|
>

> ![C-3PO](https://media.giphy.com/media/OMZRxGyZZ6fGo/giphy.gif)

Find any OCR tool online to convert the pixelated image into a document of characters. Then convert from binary to ascii.
Can be done by Tesseract OCR engine, a machine vision model to recognise ascii/letters/numbers or brute force translate.






## Simple solution
```c
import PIL
import pytesseract

pdf = pytesseract.image_to_pdf_or_hocr('bins.jpg', extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) 
```
### Flags
```
Sympathy-flag: UitHack22{BruteForceWarriors<3}
Main flag: UitHack22{IReallyDoHopeYouDidNotbruteForceThis}
```