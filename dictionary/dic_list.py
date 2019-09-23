# 리스트 비교

# 리스트
list = [1, 2, 3, 4, 5]

print(list)

# 리스트 세번째 요소 값을 수정 - 인덱스 번호 유의
list[2] = 33
print(list)

# 리스트 새 값을 추가
# list[5] = 6 # 없는 인덱스에 값을 추가하면 오류

# append()
list.append(6)
print(list)

print(type(list))

print('-------------------------------')
# 딕셔너리
dict = {'one':1, 'two':2, 'three':3}
print(dict)

# 데이터 수정 - 리스트와 방식은 같음(단, 이름으로 수정)
dict['two'] = 22
print(dict)

# 데이터 추가 - 원하는 자리에 추가하면 됨
dict['four'] = 4
print(dict)
print(type(dict))

print('----------------------------------')

# 데이터 삭제 - 리스트, 딕셔너리 모두 같음(다만 인덱스냐, 이름이냐 차이)
del(list[0])
print(list)

del(dict['one'])
print(dict)

list.pop(0)
print(list)

dict.pop('two')
print(dict)

print('-------------------------------------')

# set형 - 순서가 없고 중복 허용 x
setType = {1, 2, 2, 3, 4, 5}

print(setType)
print(type(setType))

print(set('hello'))
