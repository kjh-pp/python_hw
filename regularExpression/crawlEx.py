import requests as rq
from bs4 import BeautifulSoup

base_url = 'http://example.com/'

result = rq.get(base_url)

# print(result)

soup = BeautifulSoup(result.content, 'lxml')

# print(soup)

txts = soup.select('div')

# print(txts)

for txt in txts :
    context = txt.find('h1').text.strip()

    print(context)


    