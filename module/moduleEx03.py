import random
import math
'''
random, math
로또번호 6개 랜덤하게 추출해보세요

'''

rnd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
       11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
       31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
       41, 42, 43, 44, 45]

# 0.0 부터 1.0 사이의 실수
print(random.random())

# 정수로 변환
print(math.floor(random.random()*10))

# 0부터 44까지의 index 번호가 랜덤하게 출력
print(math.floor(random.random()*45))

# 일종의 중복방지
for i in range(1000):
    first = math.floor(random.random()*45)
    second = math.floor(random.random()*45)

    temp = 0

    temp = rnd[first]

    rnd[first] = rnd[second]

    rnd[second] = temp

# 최종 6개를 숫자를 추출
for j in range(6):
    print(rnd[j], end=' ')
print()

print('---------------------')
scissors = ['가위', '바위', '보']
select = random.choice(scissors)
print(select)

print('------------------------')
# 랜덤한 정수 추출
print(random.randint(1,10))

print('-----------------------')

list = ['빨', '주', '노', '초', '파', '남', '보']
#random 모듈 검색하셔서 list에 있는 요소들을 모두 섞어보세요
random.shuffle(list)
print(list)


'''
for i in range(0,6):
    lotto = random.randrange(1,46)
    print(lotto)
'''
'''
for i in range(0,6):
    lotto = rnd[random.randrange(0,45)]
    print(lotto, end=' ')
'''

# print(random.sample(range(1, 46),6))
'''
# print(random.shuffle(rnd))
for i in range(len(rnd)):
    print(rnd[i])
'''