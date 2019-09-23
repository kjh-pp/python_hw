print()
'''
+ 모듈 : 다른 기능을 가져와서 쓸 수 있도록 해둔 파일
      : 함수나 클래스를 묶어서 누구나 사용할 수 있는 형태로 만든 파일 
    
    - import 모듈 형
'''

import math

# 원의 둘레 : r * 2 * 3.14
r = 10
print(r * 2 * 3.14)
print(r * 2 * math.pi)

# 올림 : ceil
print(math.ceil(3.14))

# 내림 : floor
print(math.floor(3.14))

# 반올림 : round
print(round(3.14))

# 삼각함수, 지수, 로그 .. 기타 등등 다양한 기능이 math 에 있음