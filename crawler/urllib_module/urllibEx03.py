from urllib.request import Request, urlopen

# 없는 페이지 요청
url = 'https://www.example.com/%'

req = Request(url)

page = urlopen(req)

print(page)
print(page.url)

'''
+ requests와 urllib
 1. 요청 시 요청 객체를 생성하는 방법이 차이가 있음
 2. 데이터 전달 시 requests는 딕셔너리, urllib는 인코딩을 통해 바이너리 형태로 전송
 3. requests 요청 형태 (get, post) 명시 urllib는 data여부로 구분
 4. 없는 페이지 요청 시 urllib는 에러 코드를 명시
'''