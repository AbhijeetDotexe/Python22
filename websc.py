import requests
result=requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")
# print(result.text)
import bs4
soup=bs4.BeautifulSoup(result.text,'lxml')
# print(soup)
print(soup.select('title')[0].getText())