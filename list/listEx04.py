# 리스트나 문자열에서 여러 값을 한번에 가져오기
list1 = [1, 2, 3, 4, 5]

text = 'Hello Python World'

print(list1[1])
print(text[1])

print('------------')
# 슬라이싱 지원
print(list1[1:3])
print(text[1:3])

print('------------')
# 숫자 2부터 끝까지 추출
print(list1[1:])
# 숫자 2까지 추출
print(list1[:2])
# 전부 추출
print(list1[:])
print(list1)
'''
 ex) list1[:] 형태는 프로그램 구조상 원래 값을 돌려주는 것이 아닌
     똑같은 값을 갖는 새로운 리스트를 돌려주고 있는 형태
     => 원리스트를 복사한 결과
     
     파이썬3부터는 위와 같은 코드를 지양(권장 x)
     - anti pattern : 쓸 수도 있고 실제로도 사용하고 있지만 되도록 쓰지
       않기를 권장
'''
# 리스트를 복사 : copy()
list2 = [2, 3, 4, 5, 6]
list3 = list2.copy()

print(list3)

print('--------집중력 UP!!--------')
list4 = list(range(20))
print(list4)

# 요소 5번부터 14번까지 추출
print(list4[5:15])

# 요소 5번부터 14번까지 추출 - 2칸씩 건너뛰면서 추출
print(list4[5:15:2]) #[시작:끝:step]

print(list4[5:15:3])
# list가 5, 9, 13, 17 값을 가지도록 슬라이스 해보세요
print(list4[5:18:4])

print('--------3시53분이다--------')
list5 = list(range(10)); print(list5)

del list5[0]
print(list5)

del list5[:3]
print(list5) # 슬라이싱을 통한 리스트 삭제

print('--------3시56분이다---------')
# slice를 통한 특정 영역 값을 수정
print(list5[1:3])
list5[1:3] = [55, 66]
print(list5)

list5[1:3] = [77, 88, 99] # 기존 값의 개수와 바꾸려는 값의 개수가 같지 않아도 된다
print(list5)

#list5[1:3] = 5 # 바꾸려는 값의 개수가 한개일지라도 대괄호는 필요함에 유의!
print(list5)

print('------------------------')
list6 = list(range(6))

# 1, 2, 3 을 11, 22 ,33으로 수정해보세요
list6[1:4] = [11, 22, 33]
print(list6)

