import requests as rq

url = 'https://ko.wikipedia.org/wiki/파이썬'

res = rq.get(url)

#print(res)

# 쿠키 가져오기 : 1) headers 속성 다 여는 대신 cookies 속성으로 바로 접근 가능
cookies = res.cookies

print(type(cookies)) # 2) RequestsCookieJar 형식으로 리턴

print(cookies)

# 3) cookie 속성에 맞게 함수들 이용해서 받으면 됨
print(list(cookies))    # 리스트로 받기

print(tuple(cookies))   # 튜플로 받기

print(dict(cookies))    # 딕셔너리로 받기(단, 딕셔너리로 되어 있는 정보)

