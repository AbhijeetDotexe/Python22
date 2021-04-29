import requests
import bs4
base = 'https://myanimelist.net/topanime.php?limit='
for page in range(0, 7):
	page_url = base+str(page*50)
	res = requests.get(page_url)
	soup = bs4.BeautifulSoup(res.text,'lxml')
	
	for i in range(0, 50):
		title = soup.select(".hoverinfo_trigger.fl-l.fs14.fw-b.anime_ranking_h3")[i].getText()
		print(i+1, title)