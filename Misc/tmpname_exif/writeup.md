
All images has the possibility to save metadata to them with a standard formating system, EXIF.
Efix uses tags to store and categorize a variety of data, and is possible to be parsed out, but not allway easy to edit.


There are two approaches to sovling this:
The slow painful one:
    Open every single image in a detailed exif-viewer and examine the pictures manually to look for information.

The fast, but tricky one:
    It is possible to scrape exif data from images, for instance by piExif, and find the specic image with the parameter needed. This is quite tricky as exif consists of dictionaries with different datatype values.

should gitignore the images to generated at end user or similar?
    
