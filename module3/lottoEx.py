# Lotto

import random

# numbers = []
numbers = list()

# 6개 숫자를 랜덤하게 추출
'''
for i in range(0,6):
    numbers.append(random.randint(1, 46))
'''

numbers = random.sample(range(1, 46), 6)

# 중복방지 - 새로운 값을 생성(보너스 번호) -> 원 리스트 안에 있으면 추가하지 않기

while len(numbers) != 7:
    numbers.sort()
    new = random.randint(1, 46)
    if new not in numbers:
        numbers.append(new)

print(numbers)



print('''
    로또 당첨번호 : {}, {}, {}, {}, {}, {} 보너스 번호 {} 
    '''.format(numbers[0], numbers[1],numbers[2],numbers[3],
               numbers[4], numbers[5], numbers[6]))

