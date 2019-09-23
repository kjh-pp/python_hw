# error 처리

import requests as rq

# url 에 http나 https를 명시하지 않으면 에러가 발생함
url = 'ko.wikipedia.org/wiki/파이썬'

#res = rq.get(url)

#print(res)

# 에러 처리 : requests.exceptions.[에러명]
try :
    res = rq.get(url)
except rq.exceptions.MissingSchema:
    print('MissingSchema 발생')