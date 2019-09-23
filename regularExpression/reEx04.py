import re

mp = 'My phone number is 010-2222-3333'

pattern = re.compile('[0-9]+')

res = pattern.findall(mp)

print(res)

print('-------------------------1---------------------------')
pattern1 = re.compile('[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')
pattern2 = re.compile('\d\d\d-\d\d\d\d-\d\d\d\d') # \d : 숫자를 의미
pattern3 = re.compile('\d{3}-\d{4}-\d{4}') # {} : 반복 횟수

res1 = pattern1.findall(mp)
res2 = pattern2.findall(mp)
res3 = pattern2.findall(mp)

print(res1)
print(res2)
print(res3)

print('-------------------------2---------------------------')

str = '''
I am Hong Gil-Dong. I lived in YoolDokuk.
I lived in Yooldo for 100 years.
Sample Text for testing :
abcdefghijklmnopqrstuAvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();<>|""
12345 -98.7 3.1415 .5986 9,000 +34
'''

# 숫자, 소문자, 대문자 포함된 것 모두 찾아보세요
pattern1 = re.compile('[0-9a-zA-Z]+')
pattern2 = re.compile('\w+')

res1 = pattern1.findall(str)
res2 = pattern2.findall(str)  # _ 는 아무 의미가 없어서 문자열로 나오고 나머지는 의미가 있는 문자로 인식해서 안나옴

print(res1)
print(res2)

print('-------------------------3---------------------------')
pattern = re.compile('[^a-z]+')   # [^] : not / ^시작

res = pattern.findall(str)

print(res)

print('-------------------------4---------------------------')
pattern = re.compile('t..t') # . : 해당 문자 자리수

res = pattern.findall(str)

print(res)

print('-------------------------5---------------------------')
pattern1 = re.compile('t?est\w+')  # ? : ? 앞에 나온 글자가 있어도 되고 없어도 된다
# test나 est로 시작하는 문자 뒤에 문자열이 더 있는 경우

pattern2 = re.compile('t?est\w*')
# test나 est로 시작하는 문자 뒤에 문자열이 있으면 찾고 없으면 안찾는 경우

res1 = pattern1.findall(str)
res2 = pattern2.findall(str)

print(res1)
print(res2)
