>#  :milky_way:
>Dimensions can be tricky to wrap ones head around, especially >if one interprets them the wrong. The best thing is to keep >things simple. 
>
>:dizzy_face:


Convert the numbers from a 1-dimensional array to a 2-dimensional array and preview it the get the flag. There is a million numbers, and the picture has equally big dimensions, 1000x1000px. 




```
import numpy as np
from PIL import Image
import zipfile

with zipfile.ZipFile('roughly_1000k_numbers.zip', 'r') as zip_ref:
    zip_ref.extractall()
   
_1d_np_arr = np.genfromtxt('roughly_1000k_numbers.csv', delimiter=',')
img = Image.fromarray(_1d_np_arr.reshape(1000,1000))
img.show()
```
```
Flag: UITHACK22{GIBBERISHDIMENSIONS}
```


    
