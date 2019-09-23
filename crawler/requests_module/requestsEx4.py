import requests as rq

url = 'https://ko.wikipedia.org/wiki/파이썬'

res = rq.get(url)

#print(res)

# HTML 코드 가져오기
# print(res.text) # 한글 encoding이 깨질 수 도 있음

# print(res.content)
# content 속성 : 바이너리 코드 형태로 가져오므로 인코딩 문제를
#               방지 할수 있음(권장)

# 인코딩 확인
print(res.encoding)