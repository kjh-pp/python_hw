'''
for pattern in patterns:
print (pattern)
'''
scissors = ['가위','바위','보', '보','가위','바위','보']
print(scissors)
print('-----힘내자------')
for scissor in scissors:
    print(scissor)
    
'''
for ~ in : in 뒤에 쓰인 리스트 크기에 관계없이 항상 모든
           리스트에 대해 코드 실행
'''
print('---------힘을..주세요~!--------')
# 1부터 5까지 출력
list1 = [1, 2, 3, 4, 5]
for i in list1:
    print(i)

print('--------------------------')
# 1부터 100까지 출력
# list2 = [1, 2, 3, 4, 5,.......,100]
list2 = list(range(1,101))
for i in list2:
    print(i)

print('--------------------------')
names = ['봄', '여름', '가을', '겨울']
'''
--출력--
1번 : 봄
2번 : 여름
3번 : 가을
4번 : 겨울
'''
for i in range(4):
    name = names[i]
    print('{}번 : {}'.format(i+1, name))

'''
.format() 함수 : 형식에 맞춰 문자열을 만들어 주는 기능
              : 문자열에서 {}로 값을 비워둔 곳에 format() 괄호 안에 있는 갑을
                차례대로 할당
'''

rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']

# 무지개의 첫번째 색은 빨강이다
print('무지개의 첫번째 색은', rainbow[0],'이다')

# 무지개의 마지막 색은 보라이다
print('무지개의 마지막 색은 {} 이다'.format(rainbow[-1]))

print('----------------------------------')
names = ['봄', '여름', '가을', '겨울', '봄봄']
for i in range(5):
    name = names[i]
    print('{}번 : {}'.format(i+1, name))

print('----------------------------------')
names = ['봄', '여름', '가을', '겨울', '봄봄', '여름여름']
for i in range(len(names)):
    name = names[i]
    print('{}번 : {}'.format(i+1,name))

'''
for i in list : 이미 사용할 값이 정해져 있고 그 목록에서 값을 하나씩
                꺼내서 쓰는 경우 유용
for i in range : 횟수가 정해져 있거나, 단순 증가하는 숫자를 써야 할 경우 유용
'''




