import requests

url1 = "<uithack_url>"
url2 = "https://en.wikipedia.org/wiki/The_Empire_Strikes_Back"

res1 = requests.get(url1).text.split(' ')
res2 = requests.get(url2).text.split(' ')

c1 = c2 = 0

diff = ""

while (c1 < len(res1)) and (c2 < len(res2)):
    if res1[c1] == res2[c2]:
        c1 += 1
        c2 += 1
    else:
        diff += res1[c1]
        c1 += 2
        c2 += 1

print("".join(diff))
