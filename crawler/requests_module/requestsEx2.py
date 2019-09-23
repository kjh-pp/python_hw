import requests as rq

#url = 'https://www.example.com'
url = 'https://ko.wikipedia.org/wiki/파이썬'

res = rq.get(url)

#print(res)
#print(res.headers)

headers = res.headers

# 특정값 (cookie 값) 가져오기
print(headers['Set-Cookie'])

# 헤더의 모든 요소 출력해 보세요
'''
for key, val in headers.items():
    print('key : ', key,', val : ', val)
'''
for header in headers:
    print(headers[header])