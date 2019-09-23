# listType = []

# print(listType[0])

# text = 'Python'

# num = int(text)
print()
'''
 프로그램에서 벌어지는 예외적 상황들(예외)
 
 파이썬에서 이러한 예외(에러)들이 발생하면 프로그램을 중단하고
 에러메시지를 보여줌 -> 서비스가 멈추는 단점이 생김
 => 서비스를 멈추지 않고 예외들을 처리하고 싶을 때
   사용하는 방법 : 예외처리

 - 예외 예
 IndexError : 없는 인덱스를 찾을 때
 FileNotFoundError : 파일이 없을 때
 ZeroDivisionError : 숫자를 0으로 나누었을 때
 SyntaxError : 구문 오류
 EOFError : EOF(End Of File) - 파일의 끝 - 읽은 내용이 없을 때

 - 예외 처리
 try :
     수행 로직 ...
 except <발생에러명 [as 별칭]>:
     에러 처리 로직 ...
'''

# 예외 처리
def take(list, index):
    try:
        print(list.pop(index))
        print(list)
    except IndexError:
        print('{} 값이 없습니다'.format(index))

take([1, 2, 3], 1)
print('-----------------------')
take([1, 2, 3], 3)

print('---------------------------------')
# try~except 없이 if 구문으로 처리
def list_pop(list, index):
    if index < len(list):
        print(list.pop(index))
        print(list)
    else :
        print('{} index 값이 없습니다'.format(index))

list_pop([1, 2, 3],2)
list_pop([1, 2, 3],3)

print('---------------------------------')
text = '100%'

try :
    number = int(text)
except ValueError:
    print('{} 는 숫자가 아닙니다.'.format(text))