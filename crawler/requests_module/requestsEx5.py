import requests as rq
'''
url = 'https://ko.wikipedia.org/wiki/파이썬'

# 데이터 보내기 : parameter로 담아서 보내기 (딕셔너리 형태 - 권장)
res = rq.get(url, params={'key1' : 'value', 'key2' : 'value2'})

print(res.url)
'''
# 데이터 보내기 : parameter에 직접 써서 보내기
'''
url = 'https://ko.wikipedia.org/wiki/파이썬?key1=value1'

res = rq.get(url)

print(res.url)
'''
print('---------------------1----------------------')
'''
post 방식으로 데이터 보내기 : 
 post 방식은 데이터가 URL에 포함되지 않고 body에 포함되어 데이터 전달하는 방식
 => params (x)
'''

'''
url = 'https://www.example.com'

res = rq.post(url, data={'key1':'value1', 'key2':'value2'})

print(res.url)
'''

print('---------------------2----------------------')
'''
 data를 전달 할 때 딕셔너리 형태가 권장사항이지만 잘 보내지지
 않을 때가 있습니다. 이럴 때 딕셔너리 형태를 유지한 문자열
 형태로 보내는 방법도 있다. => JSON으로 데이터 전달(권장)
'''

import requests as rq
import json

url = 'https://www.example.com'

res = rq.post(url, data=json.dumps({"key1":"value1", "key2":"value2"}))

print(res.url)

print('---------------------3----------------------')

dict1 = {'key1':'value1', 'key2':'value2'}
dict2 = {"key1":"value1", "key2":"value2"}

print(str(dict1))
print(json.dumps(dict1))
print('-----------------비교------------------')
print(str(dict2))
print(json.dumps(dict2))

'''
딕셔너리 형태 유지하면서 문자열이 될 때는 큰따옴표로 표현하는 것을 권장
str이 작은 따옴표로 표현하므로 에러가 발생할 수 있음
'''