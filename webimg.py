import requests
import bs4
res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text,'lxml')
computer = soup.select('img')[0]
m = computer['src']
# <img src='//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg'>
image_link=requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
# print(image_link.content)
f = open('mycomputer_img.jpg', 'wb')
f.write(image_link.content)
f.close()
