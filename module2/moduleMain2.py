'''
import calculator
print(calculator.add(100, 200))
'''
# 특정 함수나 클래스만 불러오기
# from<모듈이름> import<함수, 클래스 이름>

from calculator import add

print(add(100, 200))

print('---------------------------')
# calculator 모듈의 모든 함수를 사용
from calculator import *
print(add(100, 200))
print(mul(100, 200))
print(div(100, 10))

print('---------------------------')
'''
from thisisVeryLongNameModule import hello

hello()
'''

# 별칭 - 사용하려는 모듈 이름이 너무 긴 경우
# ex) numpy -> np, tensorflow -> tf(tw), pandas -> pd
import thisisVeryLongNameModule as t

t.hello()