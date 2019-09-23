print()
'''
# break : break 가 붙어있는 가장 가까운 반복문을 탈출
# continue : 이번만 생략 
'''
for i in range(1, 5):
    for j in range(1, 5):
        if i == j :
            #break
            continue
        print('i : ', i, ' j : ', j)

print('--------------------------------------')
# 1부터 사용자가 입력한 숫자까지만 출력해보세요 (단, 1000이하의 숫자)
value = int(input('숫자를 입력하세요 : '))
if value > 1000 :
    print('1000이하로 적어주세요')
else:
    for i in range(1, value+1):
        if i > value:
            break
        print(i)

