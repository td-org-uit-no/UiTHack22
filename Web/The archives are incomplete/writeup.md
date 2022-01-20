> # The archives are incomplete!
> 
> Obi wan is researching important jedi matters and has found this article.  
> However, it seems like something is wrong with the page.  
> Can you help him find the information he is looking for?
> 
> "http://url_to_web.td.org.uit.no"
> 
> ![obiwan](https://c.tenor.com/aTB70bcZZKcAAAAd/obi-wan-perhaps-the-archives-are-incomplete.gif)


The page links to a clone of the wikipedia page for the empire strikes back.  
This page is however a tiny bit different, and contains words scattered throughout the page that forms the flag.
To find the flag scrape the html of both pages and find the difference between the two.
Beware that this document and the flag contains duplicate words.

Example from [solve.py](src/solve.py):

```py
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

```
