import requests
import bs4
base=requests.get('https://myanimelist.net/topanime.php')
soup=bs4.BeautifulSoup(base.text,'lxml')
for i in range(0,50):
    title = soup.select(".hoverinfo_trigger.fl-l.fs14.fw-b.anime_ranking_h3")[i].getText()
    print(i+1, title)
