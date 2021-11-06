># Help the crew home!
>The Xwing had to reboot the system causing coordinates and route-data home to get partly wiped.
>
>Luckily C-3PO always gathers graphical waypoints at all times, which can help the crew regenerate the route!
>We need to analyze where to *Spatial frequency response* is initialized at a certain spots. 
>
>C-3OP has calculated the needed spatial frequency numbers to extract the data, but is unable to do it himself due to poor hardware.
>Hack into C-3OP snapshot-history and analyze his history to gather the last information.
>
>Spatial freq. respons| Lost data|
>--- | --- |
>9898| xxxxxxxx|
>1337|yyyyyyyyyy
>6969|zzzzzzzzzzzzzzzz
>
>Flag | __UiTHack22{*XXXXXXXXYYYYYYYYYYZZZZZZZZZZZZZZZZ*}__|
>---| ---
>
>![C-3PO](https://media.giphy.com/media/xTiIzjS5VKWJzNGIUw/giphy.gif)



The flag is split into three parts located within the exif data of 11337 images. Each image containing a part of the flag has a given spatial frequency response(EXIF-tag). Parsing out the exif of these images reveals a flag parts located in the user_comment.

Images with flags:
```
9899
1339
6970
```


```
UiTHack22{FLAGSHIPMOTHERSHIPRANDOMSTRINGSHIP}
```


    
