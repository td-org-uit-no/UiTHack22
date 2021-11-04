
All images(#11337) has the possibility to save metadata to them with a standard formating system, EXIF.
Efix uses tags to store and categorize a variety of data which is possible parsed out, but not allway easy to edit.

The info given is there is something to analyze in the image where the "spatial frequency response" is *9898*. The flag is simply put in the user_comment of this image.

There are two approaches to sovling this:
The slow painful one:
    Open every single image in a detailed exif-viewer and examine the pictures manually to look for information.

The fast, but tricky one:
    It is possible to scrape exif data from images, for instance by piExif, and find the specic image with the parameter needed. This is quite tricky as exif consists of dictionaries with different datatype values.


src/solution.py parses through all images's exif data, printing out all data when finding the SPF data ==9898. 
Flag == _FLAGSHIP_, in 8008.jpg


    
