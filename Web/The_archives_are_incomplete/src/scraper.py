import requests
import random

url = "https://en.wikipedia.org/wiki/The_Empire_Strikes_Back"

content = requests.get(url).text.split(' ')

flag = "UiT Hack 22 { The _ empire _ Will _ Strike _ back _ eventually }".split(' ')

start = 2000
for w in flag:
    content.insert(start, str(w))
    start += random.randint(800,1300)

content = " ".join(content)

with open("templates/index.html", "w") as f:
    f.write(content)