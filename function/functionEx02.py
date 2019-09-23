
'''
입력인수가 몇 개일지 모를 경우

def 함수명(*입력인수)
    수행할 문장
    ...
    ....

'''
def sum(*args):
    sum = 0
    for i in args :
        sum = sum + i

    return sum

result = sum(1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10)

print(result)

print('-----------------------------')

def return_a():
    for i in range(100):
        return i # 리턴이란 키워드는 되돌릴 수 있는 값이 하나 이다. 그래서 최초값만 받고 끝난 것!

print(return_a())
# return : 되돌려 주는 결과값이 오직 한 개임에 유의!
#        : 어떤 상황이 되어서 함수를 빠져 나가고자 할 때에도 자주 쓰임

print('------------------------------')
def avoid(num):
    if num == 5:
        return # 조건에 만족하여 수행할 값이 없을때 빠져나감
    print(num)

avoid(5)
avoid(10)

print('------------------------------')
'''
var = 1
def rangeTest(var):
    var = var + 1
    print(var)

rangeTest(var)
print(var)
'''

print('------------------------------')
var = 1
def rangeTest(var2):
    var2 = var2 + 1
    print(var2)

rangeTest(1)





'''
x=int(input())
def f(x) :
    if x==5 :
        return f(int(input('값')))
    return x

f(x)
'''
