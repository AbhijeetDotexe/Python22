import requests
res=requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
import bs4
soup=bs4.BeautifulSoup(res.text,'lxml')
first= soup.select('.toctext')[0]
for item in soup.select('.toctext'):
    print(item.text)