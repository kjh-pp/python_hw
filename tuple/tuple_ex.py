'''
튜플을 이용해서 변수 하나에 여러 값을 대입(패킹, 언패킹)
 - 패킹 : 하나의 변수에 여러 개의 값을 넣는 것
 - 언패킹 : 패킹된 변수에서 여러 개의 값을 꺼내오는 것

'''

a,b = 1, 2

print(type(a))
print(type(b))

print(a,b)

print('--------------------------------')
# 패킹
c = (3, 4)
print(type(c))
print(c)

print('--------------------------------')
# 언패킹
d, e = c # c를 언패킹해서 d, e에 대입
print(d, e) 
print(type(d))

print('--------------------------------')
# 패킹
f = d, e # 변수 d와 e를 f에 패킹
print(f)
print(type(f))

print('--------------------------------')
# 값을 맞바꾸기
x = 5
y = 10
'''
temp = x
x = y
y = temp

print(x, y)
'''

x, y = y, x
print(x, y)

print('--------------------------------')
# 튜플을 이용하여 여러 개의 값을 반환 가능
def tuple_util():
    return 1, 2

num1, num2 = tuple_util()

print(num1, num2)

print(type(tuple_util()))

print('--------------------------------')

listType = [1, 2, 3, 4, 5]
for i, j in enumerate(listType):
    print('idx번호 {}: 요소값 {}'.format(i, j))


print('--------------------------------')
'''
tupleType = (1, 2, 3, 4, 5)
for i, j in enumerate(tupleType):
    print('idx번호 {} : 요소값 {}'.format(i, j))
'''
tupleType = (1, 2, 3, 4, 5)
for i in enumerate(tupleType):
    print('idx번호 {} : 요소값 {}'.format(i[0],i[1]))

print('--------------------------------')
#(*args) : 튜플에 있는 값을 알아서 쪼개서 여러개의 실행인자로 만듦
for i in enumerate(tupleType):
    print('idx번호 {} : 요소값 {}'.format(*i))

print('--------------------------------')
# 딕셔너리 : items
dictType = {'python': 100, 'spring': 90, 'java': 100}

for key, value in dictType.items():
    print("{} 점수는 {} 이다".format(key, value))

print('--------------------------------')
for key in dictType.items():
    print("{} 점수는 {} 이다".format(key[0], key[1]))

print('--------------------------------')
for key in dictType.items():
    print("{} 점수는 {} 이다".format(*key))