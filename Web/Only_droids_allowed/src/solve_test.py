import requests

s = requests.Session()
url = "http://fire-breathing-unicorn.td.org.uit.no:7500"

while 1:
    r = s.post(url)
    if b'UiTHack22{' in r.content:
        print(r.content)
        break
