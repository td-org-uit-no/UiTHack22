from PIL import Image
from PIL.ExifTags import TAGS
import piexif
import piexif.helper
import random
from datetime import datetime
import os

base_addr = 'Misc/tmpname_exif/src/C_3PO/history/'
with os.scandir(base_addr) as entries:
    for entry in entries:
        if entry.is_file():
            address = base_addr+entry.name
            exif_dict = piexif.load(address)
            thumbnail = exif_dict.pop("thumbnail")#Pop the thumbnail, which will be empty and non-iterable
            #nested dicts
            for ifd_name in exif_dict:  
                for key in exif_dict[ifd_name]:
                        if key == 37388:        #37388= tag index for spatial freq. response.
                            if exif_dict[ifd_name][37388] ==b'9898':
                                print('FOUND THAT SHIT')
                                print(exif_dict)
                                
                           
