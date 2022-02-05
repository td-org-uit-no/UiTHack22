> # Only droids allowed
> > Web - 150 pts

> While exploring a trade stop you find a locked door marked with some strange numbers and a button.
> You can hear strange music and beeping noises from within.
>
> Open the door from here: http://fire-breathing-unicorn.td.org.uit.no:7500
> 
> ![droids](https://c.tenor.com/8-NM974OdjMAAAAd/star-wars-droids.gif)
> 
> Hint 1: How high does it go?
> 
> Hint 2: There must be a way to do this faster than just clicking the button.

## Writeup

Every time you click the button the counter increases by one.
After 50k clicks the response contains the flag.
To automate this a simple python script as such could be utilized:
```py
import requests

s = requests.Session()
url = "http://fire-breathing-unicorn.td.org.uit.no:7500"

while 1:
    r = s.post(url)
    if b'UiTHack22{' in r.content:
        print(r.content)
        break
```

```
Flag: UiTHack22{Pressing_Really_really_fast_does_the_trick}
```
