# 딕셔너리 조건 제시법

# 사람 리스트를 생성
people = ['홍길동', '유관순', '이순신', '신사임당', '갑돌이', '갑순이']

# 위 리스트를 이용하여 번호를 키값으로, 이름을 벨류값으로 하는 딕셔너리 생성
# enumrate
for num, name in enumerate(people):
    print('{} 번 이름 : {} '.format(num+1, name))

print('--------------------1----------------------')
# 조건제시법으로 같은 코드
print({'{}번'.format(num+1) : name for num, name in enumerate(people)})

# 리스트 조건제시법 : [] 사용
# 딕셔너리 조건 제시법 : {} 사용

print('--------------------2-----------------------')
# 리스트를 이용해서 딕셔너리를 만들 때 많이 사용하는 함수 : zip()
age = [20, 17, 56, 60, 16, 16]

for x,y in zip(people, age):
    dic = {x:y}
    print(dic)

print('--------------------3----------------------')
# zip()을 조건제시법으로 같은 코드
print({x : y for x, y in zip(people, age)})
