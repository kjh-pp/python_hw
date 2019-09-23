
# urllib 모듈은 객체를 만들어서 요청하는 모듈

from urllib.request import urlopen, Request

url = 'https://www.naver.com'

# Request 객체를 통해 접근 요청
req = Request(url)

# 만들어진 객체를 이용하여 웹페이지에 요청
page = urlopen(req)

print(page)

print(page.code)

print(page.headers)

print(page.url)

print(page.info().get_content_charset())

print(page.read()) # HTML코드 - 바이너리 형태로 가져옴
