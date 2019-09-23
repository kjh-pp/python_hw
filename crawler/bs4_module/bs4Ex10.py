import requests as rq
from bs4 import BeautifulSoup

base_url = "https://www.culture.go.kr/contest/gallery.do?type=A&year=2018"

res = rq.get(base_url)
print(res)

soup = BeautifulSoup(res.content, 'lxml')
#print(soup)

posts = soup.select('table.tstyle6 tbody tr')
#print(posts)

for post in posts:
    title = post.find('td').text.strip()
    print(title)