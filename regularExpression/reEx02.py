import re
'''
정규식(정규표현식)
1. 패턴 만들기 : re.compile() 패턴 생성
2. 패턴을 이용하여 찾고자하는 부분을 지정(제한)
3. 찾을 결과물을 리턴
'''

# str = '1 test tlsd test1'
str = 'test tlsd test1'

# 1. 패턴 지정
pattern = re.compile('test')

# 2. 패턴을 통해 찾고자 하는 부분을 지정
'''
1) match() : 문자열의 처음부터 정규식과 매치되는지 조사
2) search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사
3) findall() : 정규식과 매치되는 모든 문자열을 리스트로 리턴
4) finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴
'''

res1 = pattern.match(str)
res2 = pattern.search(str)
res3 = pattern.findall(str)
res4 = pattern.finditer(str)

print(res1)
print(res2)
print(res3)
print(res4)

# 3. 결과물 리턴
'''
1) group() : 매치된 문자열 리턴
2) start() : 매치된 문자열의 시작위치를 리턴
3) end()  : 매치된 문자열의 끝위치를 리턴
4) span() : 매치된 문자열의 (시작, 끝)위치를 튜플로 리턴
'''

print('------------------1-------------------')
print(res1)
print(res1.group(), res1.start(), res1.end(), res1.span())


print('------------------2-------------------')
print(res2)
print(res2.group(), res2.start(), res2.end(), res2.span())

print('------------------3-------------------')
print(res3)
# print(res3.group(), res3.start(), res3.end(), res3.span())
for i in res3:
    print(i)


print('------------------4-------------------')
print(res4)
# print(res4.group(), res4.start(), ..)
for i in res4:
    print(i.group(), i.start(), i.end(), i.span())
