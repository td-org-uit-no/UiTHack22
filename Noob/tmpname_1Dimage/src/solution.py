import numpy as np
from PIL import Image


my_data = np.genfromtxt('roughly_1000k_numbers.csv', delimiter=',')
img = Image.fromarray(my_data.reshape(1000,1000))
img.show()