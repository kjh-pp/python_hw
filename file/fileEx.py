print()
'''
open(parameter1, parameter2, ..)
 첫번째 파라미터 : 파일의 경로(상대)
 두번째 파라미터 : 파일을 여는 옵션
 - r : 기본값, 읽기 전용
 - w : 파일 쓰기. 파일이 이미 존재한다면 해당 파일을 비움
 - x : 배타적 생성. 파일이 이미 존재한다면 open() 실패
 - a : 파일 쓰기. 파일이 이미 존재한다면 파일 끝에 내용을 덧붙임
 - b : 바이너리(2진수) 코드로 열기
 - + : 읽기와 쓰기 모두 다 하기
 
 -> 위 옵션들은 2개 이상 같이 쓸 수 있음
 
'''

f = open('good1', 'r')

# 파일 전체 읽기
#read = f.read()
#print(read)

# 파일 한 행만 읽어들이기
#read = f.readline()

# 한행씩 읽어서 모아서 줌 / 하나의 변수에 다량의 데이터 들어있음
# 파일 내용을 전부 읽어들인 후 리스트로 반환
read = f.readlines()

for line in read:
    print(line)

# 파일을 다 읽어들였으면 닫는게 권장사항
f.close()

print('read[2]:',read[2])


print('-------------------------------')
fp = open('good.txt', 'r', encoding='UTF-8')

print(fp.read())

fp.close()

print('--------------------------------')
# with : 파일을 열고 닫는 과정을 자동으로 해줌
#      : 그 과정에서 가벼운 오류가 있다면 그 오류도 알아서 자동으로 처리해 줌

with open('good1', encoding='UTF-8') as f:
    print(f.read())
