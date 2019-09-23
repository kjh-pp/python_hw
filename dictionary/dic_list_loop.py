# 리스트와 비교

# 반복문을 통한 리스트 값 출력
seasons = ['봄', '여름', '가을', '겨울']
print(seasons)
for i in seasons: # 0, 1, 2, 3
    print(i)

print('------------------------------')
# 반복문을 통한 딕셔너리 값 출력 - (이름/값)
score = {'dataType' : 90, 'module' : 90, 'fuction' : 80}

# 딕셔너리는 key 따로, value 따로 가져올 수 있음
for key in score.keys():
    print(key)

print('-------------------')

for value in score.values():
    print(value)

print('-------------------')
# 과목과 점수 모두 출력 - key를 가져오는게 우선
# ~~ 과목 점수는 ~~ 입니다

for key in score.keys():
    print('{}과목 점수는 {} 입니다.'.format(key, score[key]))

# for key in score:  #keys() 는 생략 가능
#    print(key, '과목 점수는',score[key],'입니다')

print('----------------------------')

# 리스트에서 순서, 요소값을 모두 가져오고 싶을 때 : enumrate()
for i, season in enumerate(seasons):
    print('{}번 : {}'.format(i+1, season))

print('----------------------------')
# 딕셔너리에도 enumrate()와 같은 역할을 하는 함수 : items()
for key, val in score.items():
    print('{} 과목 점수는 {} 입니다'.format(key, val))

'''
for ~~ in list : 이미 사용할 값이 정해져 있고 그 목록에서 값을 하나씩 꺼내서 사용할 경우 유용

for ~~ in range : 횟수가 정해져 있거나 단순 증가하는 숫자를 써야 할 때 유용

for ~~ in enumrate() : 순서, 값 모두 가져와야 할 경우 유용

+ 리스트와 달리 딕셔너리는 값을 return 할 때 순서를 지켜주지 않음.(인덱스 번호가 없어서 순서대로 넣지 않기 때문)
  왜냐면 key를 통해 value를 찾으니 순서가 의미가 없음.
  그러므로 순서가 중요할 때는 딕셔너리가 아닌 리스트를 사용

'''