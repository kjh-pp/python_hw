import requests as rq
from bs4 import BeautifulSoup

base_url = 'https://www.culture.go.kr/contest/gallery.do?type=A&year'

page_path = '=%d'

page = 2018

res = rq.get(base_url)
soup = BeautifulSoup(res.content, 'lxml')

while True:
    sub_path = page_path%(page)
    page -= 1

    res = rq.get(base_url+sub_path)

    if(res.status_code != 200):
        break
    soup = BeautifulSoup(res.content, 'lxml')

    posts = soup.select('table.tstyle6 tbody tr')
    # print(posts)

    for post in posts:
        title = post.find('td').text.strip()
        print(title)

    print('----------------------------------')