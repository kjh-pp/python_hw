import random
import math

com = [0, 0, 0]

flag = True
flag2 = True

count = 0

while(flag):
    com[0] = math.floor(random.random()*10)
    com[1] = math.floor(random.random()*10)
    com[2] = math.floor(random.random()*10)

    if com[0]!=com[1] and com[0]!=com[2]and com[1]!=com[2]:
        print('',com[0],',',com[1],',',com[2])
        flag = False
strike = 0
ball = 0
count = 0
while(flag2):
    count += 1
    sc = int(input('숫자를 입력하세요 : '))
    print('사용자 입력값 : ', sc)

    user = [0, 0, 0]
    user[0] = sc//100
    user[1] = sc%100//10
    user[2] = sc%10



    for i in range(3):
        if com[i] == user[i]:
            strike += 1
        else:
            for a in range(3):
                if com[a] == user[i]:
                    ball += 1

    print(strike, ' strike', ball, 'ball')

    if strike == 3:
        flag2 = False

print(count, '번 만에 성공')