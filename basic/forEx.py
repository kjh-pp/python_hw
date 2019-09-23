print()
'''
반복문 : for, while 

# for문 기본 구조
for 변수 in range() :
    수행 할 문장 1
    수행 할 문장 2
    .
    .
    
- range() : 숫자 리스트를 자동으로 만들어 주는 함수
'''

list = range(10) # 0부터 10 미만의 숫자를 자동으로 생성
print(list)
print(len(list))

print('------------------')

for i in range(10):
    print('i : ', i)

print('------------------')

list = range(1,11) # (시작, 끝) 숫자를 지정 가능 - 콤마로 구분
print(list)
print(len(list))

print('------------------')

for i in range(1, 11) :
    print('i : ', i)

print('------------------')
# 구구단 5단 출력
dan = 5
for i in range(1, 10) :
    print(dan,' * ', i," = ", (dan*i))

print('------------------')
# 사용자로부터 숫자 하나 입력 받아서 해당 구구단을 출력해 보세요
'''
value = input('숫자를 입력하세요 : ')
dan = int(value)
for i in range(1, 10) :
    print(dan, ' * ', i,' = ', (dan*i))
'''

print('------------------')
# 다중 반복문
# 19단 출력
for dan in range(2, 20) :
    for i in range(1,10) :
        print(dan,' * ', i,' = ', (dan*i))
    print('')

print('------------------')
# 1부터 9까지 출력 - 옆으로 출력
for i in range(1,10) :
    print(i, end=' ') # end : 입력 인수 - 해당 결과값을 다음줄로 안넘기려고 사용

print('\n')
print('------------------')


for i in range(1, 6) :
    for j in range(1, 6) :
        if i >= j :
            print(j, end='')
        print('')

print('------------------')

for i in range(1, 6) :
    print('*'*i)

print('------------------')
# 1부터 100까지의 합
val = 100
sum = 0
for i in range(1, val+1):
    sum = sum + i
    print(sum)

print('------------------')
# 1부터 16까지 짝수 구하기
for i in range(1, 17) :
    if i%2 == 0 :
        print(i, end='')
print('\n')

print('------------------')
'''
1. 구구단 2단부터 9단까지 출력
2. 구구단 짝수단만 출력
3. 2단은 2*2 까지, 4단은 4*4......8단은 8*8까지 출력
'''
'''
for dan in range(2, 10):
    for i in range(1,10):
        print(dan,' * ', i,' = ', (dan*i))
    print('')
'''
print('--------------------------')
'''
for dan in range(2, 10):
    if dan%2 == 0:
        for i in range(1,10):
            print(dan,' * ', i,' = ', (dan*i))
        print('')
print()
'''

print('--------------------------')

for dan in range(2, 10):
    for i in range(1,10):
        if dan%2 == 0 and dan >= i :
            print(dan,' * ', i,' = ', (dan*i))
    print('')
