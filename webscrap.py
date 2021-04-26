import requests
import bs4
base_url='https://books.toscrape.com/catalogue/page-{}.html'
res=requests.get(base_url.format(1) )
soup=bs4.BeautifulSoup(res.text,'lxml')
print(len(soup.select('.product_pod')))
product=soup.select('.product_pod')
example=product[0]
#print(str(example))
#print("star-rating Three" in str(example))
#print(example.select(".star-rating.Three"))
print(example.select('a')[1]['title'])
