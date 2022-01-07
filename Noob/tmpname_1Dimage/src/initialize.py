import zipfile
import numpy as np
from PIL import Image

img = Image.open('flag.png').convert('L')
arr = np.array(img)

flat_arr = arr.ravel()
np.savetxt("roughly_1000k_numbers.csv", flat_arr, delimiter=",")



with zipfile.ZipFile("roughly_1000k_numbers.zip", "w", zipfile.ZIP_DEFLATED) as newzip:
    newzip.write("roughly_1000k_numbers.csv")

