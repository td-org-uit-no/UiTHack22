
from PIL import Image
from PIL.ExifTags import TAGS
import piexif
import piexif.helper
import random
from datetime import datetime
import io

'''
Generates 11337 images of 20x20px with random white spots(stars), representing space or something.
Each image get random generated exif data, but some are given a flag and data which can be used as clues.
'''
def create_images(num_images, key_list):    
    random.seed(datetime.now())
    
    for x in range(num_images):

  
       
        
        spf = random.randint(66, 1660000)
        fe1 = random.randint(500001, 1500000)
        fe2 = random.randint(50000, 150000)
        spf = bytes(str(spf), 'utf-8')
        user_comment = b"!FLAG"
        date_time = create_date()

        for y in range (len(key_list)):
            if x == key_list[y][0]:
                spf = key_list[y][1]
                spf = bytes(str(spf), 'utf-8')
                fe1 = key_list[0][2]
                fe2 = key_list[0][3]
                user_comment = bytes(str(key_list[0][4]), 'utf-8')
                print(x)
                print(date_time)
           



        zeroth_ifd = {
            piexif.ImageIFD.Artist: u"Phinn Skywalker", 
            piexif.ImageIFD.SpatialFrequencyResponse: spf,
            piexif.ImageIFD.FlashEnergy: (fe1,0),
            piexif.ImageIFD.XResolution: (1, 1),
            piexif.ImageIFD.YResolution: (1, 1),
            piexif.ImageIFD.Software: u"Sta-Vaars OS",
            piexif.ImageIFD.ImageDescription: "THIS IMAGE IS SHOWING HOW BEAUTIFUL SPACE LOOKS AT NIGHT"
            }
        exif_ifd = {
            piexif.ExifIFD.DateTimeOriginal: date_time,
            piexif.ExifIFD.UserComment: user_comment,
            }


        gps_ifd = {
           piexif.GPSIFD.GPSVersionID: (2, 0, 0, 0),
           piexif.GPSIFD.GPSAltitudeRef: 1,
           piexif.GPSIFD.GPSDateStamp: date_time,
               }
  

        exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd, "GPS":gps_ifd}
        exif_bytes = piexif.dump(exif_dict)
        jpgimg1 = Image.new("L", (20,20))

        for _ in range(10):
            pxlx = random.randint(0, 19)
            pxly = random.randint(0, 19)
            clr_R = random.randint(255,255)
            clr_G = random.randint(255,255)
            clr_B = random.randint(250,255)
            jpgimg1.putpixel((pxlx, pxly), (255))

        jpgimg1.save(f"Misc/tmpname_exif/src/C_3PO/history/{x}.jpg", exif=exif_bytes)


def create_date():
    year = str(random.randint(1991, 2091))
    month = str(random.randint(1, 12))
    day = str(random.randint(1,28))
    hour = str(random.randint(0,24))
    min = str(random.randint(0, 59))
    sec = str(random.randint(0,59))

    date_time =f'{year}:{month}:{day}-{hour}:{min}:{sec}'

    return bytes(date_time, 'utf-8')



def print_exif(filename):
    jpgimg2 = Image.open(filename)
    for item in (jpgimg2._getexif()).items():
        print(item)

if __name__ == '__main__':
    '''[index, spf, fe1, fe2, FLAG]'''
    key_list = [
        (8008, 9898, 1555, 88888888, "FLAGSHIP"), 
        #(1337, 7315, 3001, 4001), 
        #(8008, 66600656, 49984, 652214), 
        #(9111,404, 666,5641)
        ]
    
    create_images(11337, key_list)
    #print_exif("C_3PO/history/C-3PO_b'1991:1:1-20:32:1'.jpg")




