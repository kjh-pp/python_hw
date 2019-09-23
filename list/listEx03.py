print()
'''
리스트와 문자열
 : 리스트와 문자열은 비슷한 점이 많음
'''
list1 = [1, 2, 3, 4, 5, 6]

str1 = 'Hello Python World'

print(list1[0])
print(str1[0])
# 인덱싱 가능
print('-----------------------')
# in 연산자 사용법도 같음
print(6 in list1)
print('d' in str1)
print('D' in str1) # 문자열은 대소문자를 구분

print('-----------------------')
# index()
print(list1.index(3))
print(str1.index('P'))

print('-----------------------')
# 문자열을 리스트로 종종 필요에 따라 변환시켜서 사용 가능 : list()
char = list('Hello')
print(char)

print('-----------------------')
str2 = '오늘은 금요일 내일은 토요일'
str2_list = str2.split() # split() : 괄호 안에 구분자 없으면 공백이 구분자
print(str2_list)

str3 = '2019:08:30:02:59'
str3_list = str3.split(':')
print(str3_list)

print('-----------------------')
# 문자열로 이루어진 리스트를 하나의 문자열로 만들기 : join()
# join은 이어붙이는 구분자가 필요함

print('-'.join(str3_list))
# 구분자 없이 쓰고 싶을 때 : ''
print(''.join(str3_list))
# 구분자를 공백으로 쓰고 싶을 때 : ' '
print(' '.join(str3_list))








