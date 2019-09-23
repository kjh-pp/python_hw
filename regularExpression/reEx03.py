import re

str = '''
I am Hong Gil-Dong. I lived in YoolDokuk.
I lived in Yooldo for 100 years.
Sample Text for testing :
abcdefghijklmnopqrstuAvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();<>|""
12345 -98.7 3.1415 .5986 9,000 +34
'''
# 숫자 찾기
pattern = re.compile('[0-9]')
num = pattern.findall(str)
print(num)

print('------------------------1---------------------------')
# 0~9 까지 하나 이상 포함되는 것 찾기
pattern = re.compile('[0-9]+')
num = pattern.findall(str)
print(num)


print('------------------------2---------------------------')
# 소문자 찾기
pattern = re.compile('[a-z]')
chars = pattern.findall(str)
print(chars)

# 소문자 하나 이상 포함되는 것 찾기
pattern = re.compile('[a-z]+')
chars = pattern.findall(str)
print(chars)

print('------------------------3---------------------------')
# 대문자 찾기
pattern = re.compile('[A-Z]')
chars = pattern.findall(str)
print(chars)


# 대문자 하나 이상 포함되는 것 찾기
pattern = re.compile('[A-Z]+')
chars = pattern.findall(str)
print(chars)

print('------------------------4---------------------------')
# 대문자 + 소문자
pattern = re.compile('[a-zA-Z]')
chars = pattern.findall(str)
print(chars)

pattern = re.compile('[a-zA-Z]+')
chars = pattern.findall(str)
print(chars)
