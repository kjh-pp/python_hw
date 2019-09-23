import random
import math

flag = True
flag2 = True

com = [0, 0, 0]

while flag:
    com[0] = math.floor(random.random()*10)
    com[1] = math.floor(random.random()*10)
    com[2] = math.floor(random.random()*10)

    if com[0]!=com[1] and com[0]!= com[2]and com[1]!=com[2]:
        print('', com[0], ',',com[1], ',',com[2])
        flag = False

while flag2:
    sc = int(input('숫자 입력 : '))
    print('사용자 입력 값 : ', sc)

    user = [0, 0, 0]

    user[0] = sc//100
    user[1] = sc%100//10
    user[2] = sc%10



