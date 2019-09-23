print()
'''
 + 튜플(tuple) : 순서가 있는 값의 집합
              : 한 번 만들고 나면 변경을 최소화 하고 싶을 때 사용
cf) 리스트 : 대괄호[]
    딕셔너리 : 중괄호{}
    튜플 : 소괄호()
'''
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))

print('-------------------------------')
# 튜플형은 핵심이 괄호 x -> 콤마(,)
tuple2 = 1, 2, 3, 4, 5
print(tuple2)
print(type(tuple2))

print('-------------------------------')
var1 = 1
print(type(var1))
var2 = 1,
print(type(var2))

print('-------------------------------')
# 리스트를 튜플로 변환 가능
list1 = [1, 2, 3, 4, 5]
print(type(list1))

tuple3 = tuple(list1)
print(tuple3)
print(type(tuple3))

print('-------------------------------')
# 튜플 요소값을 가져오기
print(tuple3[0]) # 리스트처럼 인덱스 번호로 가져올 수 있음

print('-------------------------------')
'''
# 튜플 값을 수정
# tuple3[3] = 33
# print(tuple3)

del tuple3[0]
print(tuple3)

: 튜플형은 순서와 값을 모두 고정하고 있는 형태
  값을 변경(수정, 삭제)하려고 하면 모두 오류가 발생함

: 튜플 왜 사용 ?
1) 두 변수의 값을 맞바꿀 때 사용
2) 여러 개의 값을 한꺼번에 전달할 때 사용
3) 딕셔너리의 키에 값을 여러개 넣고 싶을 때 사용
 - 딕셔너리는 키를 통해 벨류를 찾으므로 키가 변경이 되면 곤란하므로
'''

print('-------------------------------')

tuple4 = (11, 22, 33, 44, 55)
#for i in tuple4:
#    print(i)

for i in range(len(tuple4)):
    print(tuple4[i])
