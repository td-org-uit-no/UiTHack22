import numpy as np
from PIL import Image
import zipfile

with zipfile.ZipFile('roughly_1000k_numbers.zip', 'r') as zip_ref:
    zip_ref.extractall()
   

_1d_np_arr = np.genfromtxt('roughly_1000k_numbers.csv', delimiter=',')
img = Image.fromarray(_1d_np_arr.reshape(1000,1000))
img.show()