print('--------------------------------')

'''
오늘은 목요일
-->
오늘은 금요일
'''
# 같은 문자열에서 특정한 값을 바꿔야 하는 경우
'''
- 문자열 format 기법 : %
- 문자열 format 코드
 %s : 문자열(string)
 %c : 문자 1개(character)
 %d : 정수 (Integer)
 %f : 부동소수(floating-point)
 %o : 8진수
 %x : 16진수
 %% : Literal % (문자 % 자체)
'''
# 1. 숫자 또는 문자열을 바로 대입
print('현재 기온은 20도 입니다.')
print('현재 기온은 %d도 입니다.' %24) # %d : 정수

print('현재 기온은 %s도 입니다.' %'Twenty-four')
# 2. 변수로 대입
char = '1'

msg = '현재 기온은 %c도 입니다.'
# %c : 문자 1개
print(msg %char)
# 3. 두 개 이상의 값을 변환 가능
msg2 = '오늘 미세먼지는 %s입니다. %s를 준비하세요'

print(msg2 %("'좋음'",'우산'))
print(msg2 %("'나쁨'", '마스크'))

print('--------------------------------------')

# 천재는 99%의 노력으로 이루어진다.
txt ='%s는 %d%%의 노력으로 이루어진다.'
print(txt %('천재',99))
print('--------------------------------------')
# 포맷코드와 숫자
print('%15s' % 'hi') # 전체 15인 공간에서 왼쪽부터 공백을 주고 hi를 정렬

print('%-15s' % 'hi') # - 를 이용하면 반대도 가능
print('hi')

# 2. 소수점 표현하기
print('%0.5f' % 3.141536434455445) # 소수점을 원하는 자리까지 표현 (반올림 해줌)
print('%15.5f' % 3.12334435356)