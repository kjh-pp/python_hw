# 문자열 내장함수 : 문자열 자료형이 자체적으로 가진 함수
# 사용법 : 문자열 변수명 뒤에 .을 붙인 후 함수명

# 특정 문자 개수 세기 : count
str = 'soldesksoldesksoldesk'
print(len(str))
print(str.count('s'))

print('-------------------------')

# 위치 알려주기 - 1 : find
str = '오늘은 목요일, 내일은 금요일'
print(str.find('내일은')) # 찾고자 하는 단어의 첫번째 글자 위치를 반환
print(str.find('토요일')) # 찾는 문자, 문자열이 없으면 -1 리턴
# 위치 알려주기 - 2 : index
print(str.index('내'))
print(str.index('일')) # 찾는 문자 중 맨 처음 나온 문자 위치 반환
# print(str.index('토')) # index()는 찾는 문자가 없으면 에러 발생시킴

print('-------------------------')
# 문자열 삽입 : join
str1 = ','
str2 = 'abcdefg'
# a,b,c,d,e,f,g
print(str1.join(str2))

print('-------------------------')

# 문자 변환
# 소문자를 대문자로 변환 : upper
str = 'hello python'
print(str.upper())
# 대문자를 소문자로 변환 : lower
str = 'Hello Python'
print(str.lower())

print('-------------------------')
# 공백 지우기 : strip(lstrip, rstrip, strip)

str = ' .hello. '
print(str.lstrip())
print(str.rstrip())
print(str.strip())
print('.hello.')

print('-------------------------')

# 문자열 바꾸기 : replace

str = 'today is wed'
print(str.replace('wed', 'thu'))

print('-------------------------')
# 문자열 나누기 : split

str = '오늘은 목요일, 내일은 금요일'
print(str.split(',')) # 괄호 안의 값(기준값) - 기준값(구분자)로 문자열을 나눔
print(str.split()) # 구분자 없으면 공백을 기준으로 문자열을 나눔

print('-------------------------')

email = 'hwalbindang@yooldokuk.com'

# 아이디만 추출해보세요
print(email[0:email.index('@')])

temp = email.find('@')
print(temp)
print(email[:temp])

temp = email.split('@')
print(temp)
print(temp[0])