# 다른 코드에서 쓸 함수나 모듈 생성 시 디버깅 목적으로 오류를 일으키기

# 가위, 바위, 보 함수로 디버깅

def rsp(x, y):
    allowed = ['가위','바위','보']
    if x not in allowed:
        raise ValueError         # raise : 오류를 일부러 발생시키는 구문
    if y not in allowed:
        raise ValueError

# rsp('가위', '묵')

try :
    rsp('가위','목')
except ValueError:
    print('잘못된 값 입력됨')

print('============1=============')

kbl = {'A구단' : [178, 188, 190, 198, 201], 'B구단': [199, 192, 189, 210, 198]}
# KBL : 2m가 넘는 선수가 있다면 그 구단을 출력하고 구단 활동 멈추기
for id, heights in kbl.items():
    for height in heights:
        print(height)
        if height > 200 :
            print(id, '2M 넘는 선수가 있음')
            break

print('============2=============')
# 두 구단 중 2M 가 넘는 선수가 있으면 바로 구단 활동을 멈추기
try:
    for id, heights in kbl.items():
        for height in heights:
            if height > 200:
                print(id, '2m 넘는 선수 있음')
                raise StopIteration
except StopIteration:
    print(id, '규칙 위반')
    
print('============3=============')
'''
exception을 다루는 방법
1. 예외 처리
2. 파이썬에 미리 정의되어 있는 예외를 일으키는 방법
'''
value = '가'

try :
    if value not in ['A', 'B', 'C']:
        raise ValueError('알파벳 중 하나이어야 함')
except ValueError as ex:
    print('오류가 발생했음', ex)

'''
코드가 길어지고 복잡해지게 되면 함수들을 여러번 호출하게 되고 오류가 발생할 수 
있는 코드도 당연히 많아지게 됨. 더해서 처리하지 말아야 할 오류를 처리해 버린다면
코드 전체가 달라지는 의외의 결과도 생길 수 있음.
=> 위의 경우들을 찾는 것은 처리하지 않은 오류를 찾는 것 보다 더 번거로움

=> 개발자가 직접 예외도 하나의 클래스로 만들어 두고 그걸 공유
'''
print('============4=============')

from exceptionObject import Unexpected_exception

value = '가'
try :
    if value not in ['A', 'B', 'C']:
        raise Unexpected_exception
except Unexpected_exception:
    print('오류가 발생했음')