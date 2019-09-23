print()
'''
# while 반복문

while <조건> :
    수행할 문장 1
    수행할 문장 2
    ...
    ...
 - while문 : 조건이 참일 경우에 코드블록을 반복해서 수행
 - 참인 조건이 끝나지 않으면 계속 반복하므로 주의!
 ex)
while True:
    print('WoW')
    
'''
i = 1
while i <=9 :
    print(9*i)
    i= i+1

print('--------------------------')
# 1부터 99 까지의 합 구하세요
a = 1
sum = 0
while a <= 99 :
    sum = sum + a
    a = a+1
print(sum)

print('--------------------------')
# 100부터 1까지 출력해보세요
i = 100
while i >= 1 :
    print(i)
    i = i-1
