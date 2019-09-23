print()
'''
# 조건이 참일 때 실행되는 코드 : if 코드 블록
# 조건이 참이 아닐 때 실행되는 코드 : else 코드 블록

if <조건> :
    <코드 블록>
else :
    <코드 블록>
'''

num1 = 50
num2 = 100

# 두 수 중 큰 수 구하기
if num1 > num2 :
    big = num1

    print(big)
else :
    big = num2

    print(big)

# 두 수 차의 절대값 구하기

if num1 > num2 :
    print(num1 - num2)
else :
    print(num2 - num1)

print('--------------------------------')
'''
if <조건> :
    <코드 블록>
elif <조건> :
    <코드 블록>
else :
    <코드 블록>
'''

# 사용자로부터 입력 받기 : input()
'''
value = input()

print(value)

주의 ! input()을 통해 입력되는 값은 문자열 취급
'''

value = input('점수를 입력하세요 : ')
#print(value)

score = int(value)
if score >= 90 :
    print('당신의 성적은 A 입니다')
elif score >= 80 :
    print('당신의 성적은 B 입니다')
elif score >= 70 :
    print('당신의 성적은 C 입니다')
elif score >= 60 :
    print('당신의 성적은 D 입니다')
else :
    print('당신의 성적은 F 입니다')
