from PIL import Image
import numpy as np

import numpy as np
from PIL import Image

img = Image.open('dimensions.png').convert('L')
arr = np.array(img)

flat_arr = arr.ravel()
np.savetxt(".csv", flat_arr, delimiter=",")

