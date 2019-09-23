'''
+ function 구조
1. 결과값이 '없는' 함수
def 함수명(입력인수) :
    <수행 문장 1>
    <수행 문장 2>
    ....
    ...

2. 결과값(return)이 '있는' 함수
def 함수명(입력인수) :
    <수행 문장 1>
    <수행 문장 2>
    ...
    ....
    return 결과값

'''

def function():
    print('Hello Python World')

# 함수 호출
function()

print('------------------------')

# 입력인수(매개변수 / parameter) 없는 함수
a = 10
b = 20
def sum():
    result = a + b
    print(result)

sum()
# print('sum() : ', sum())
print('------------------------')
# 입력인수가 있는 함수
def sum(c, d):
    result = c + d
    print(result)

sum(20, 30)

print('------------------------')
# 결과값이 있고, 입력 인수 없는 함
def hello():
    return 'hi python'
# 결과 값을 계속 쓸것인지 아닌지 , 변수에 담을 것인지 아닌지, 데이터를 다시 받아서 쓰겠다 할때는 리턴 받는 형식으로

hello = hello() # 함수가 데이터를 가지고 있으니 변수에 담을 수 있다

print(hello)

print('------------------------')
# 결과값이 있고, 입력인수가 있는 함수
def add(e, f):
    result = e + f
    return result

add = add(100, 200) # 추후에 데이터를 쓰고 싶을 때 변수에 담을 수 있다
print(add)

print('------------------------')
# 연봉 5천만원 받는 신입사원의 연봉을 5% 인상한 값으로 돌려주세요
def upsal(annual):
    result = annual * 1.05
    return result
upsal = upsal(50000000)
print(upsal)














