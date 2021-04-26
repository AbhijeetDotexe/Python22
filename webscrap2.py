import requests
import bs4
base='https://books.toscrape.com/catalogue/page-{}.html'


twostar_title=[]
for i in range(1,51):
    scrape_url=base.format(i)
    res=requests.get(scrape_url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    books=soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two'))!=0:
            twostar_title.append(book.select('a')[1]['title'])

for i in twostar_title:
    print(i)