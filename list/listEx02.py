# 리스트 관련 함수들

# 리스트에 요소 추가 : append
a = [10, 20, 30]

a.append(40)
print(a)

a.append([50,60])
a.append('hello')
print(a)

print('---------------------')
# 리스트에 요소 삽입 : insert(x, y)
# x번째 위치에 y값을 삽입
a = [10, 20, 30, 40, 50]
a.insert(3, 4)
print(a)

print('---------------------')
# 리스트 정렬 : sort
b = [9, 4, 2, 10, 7]
b.sort()
print(b)

# cf) 문자도 정렬 가능 - 알파벳 순으로 정렬
str = ['wow', 'fantastic', 'python']
str.sort()
print(str)

print('---------------------')
# 리스트 역순으로 배치 : reverse
b.reverse()
print(b)

chars = ['a', 'c', 'f', 'd', 'b']
#chars.sort()
print(chars)
# reverse()는 큰수에서 작은수로의 정렬이 아님! 리스트에 들어있는 순서 그대로 역정렬
chars.reverse()
print(chars)

print('--------------------------------')
# 위치값 반환 : index(요소값)
c = [10, 20, 30, 40, 50]
print(c.index(40))
c.insert(3, 4)
print(c.index(40))

print('--------------------------------')
print(c)

# 리스트 요소를 제거 : remove(요소값)
c.remove(4)
print(c)

c.insert(3, 40)
print(c)

c.remove(40) # 중복되는 값이 있어도 첫번째 값만 삭제
print(c)     # 다 삭제하고 싶으면 중복된 횟수만큼 더 삭제명령이 필요함

print('--------------------------------')
# 리스트 요소값 꺼내기 : pop()
d = [1, 2, 3]
d.pop() # 맨 마지막 요소를 꺼내기
print(d)

# x번째 요소를 꺼내기 : pop(x)
e = [1, 2, 3, 4, 5]
e.pop(3)
print(e)

print('--------------------------------')
# 리스트에 있는 특정요소(x) 개수 세기 : count(x)
f = [10, 20, 30, 20, 20, 20, 20]

print(len(f))
print(f.count(20))

print('--------------------------------')
# 리스트 확장 - extend()
g = [1, 2, 3]
#g.insert(3, [4, 5])
g.extend([4, 5]) # 허용 자료형 : 리스트
g.append([6, 7])
g#.extend(8)
print(g)

# extend => +=

g += [8, 9, 10]
print(g)