# 데이터 요청

from urllib.request import urlopen, Request
import urllib

url = 'https://www.example.com'

# post 방식으로 요청
# post 방식으로 데이터를 보낼 때는 바이너리 형태로 인코딩하여 보내야 함 : encode()

data = {"key1":"value1", "key2":"value2"}

data = urllib.parse.urlencode(data)
data = data.encode('utf-8')

#print(data)

# post 요청 : Request() 이용 - 첫번째 인자 주소, 두번째 인자 값이 있으면 post/ 없으면 get
'''
req_post = Request(url, data=data)

page = urlopen(req_post)

print(page)
print(page.code)
print(page.url)
'''

print('--------------------1----------------------')
# get 요청
req_get = Request(url+'?key1=value1&key2=value2', None)

page = urlopen(req_get)

print(page)
print(page.url)
print(page.code)