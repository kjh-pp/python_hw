print()
'''
라이브러리(library) : 잘 되어있는 프로그램(모듈)을 모아놓은 것

표준 라이브러리는 파이썬 설치 시 자동으로 설치가 됨

ex) sys 모듈, pickle 모듈, os 모듈, glob모듈, 
  time 모듈, calder 모듈, random 모듈 ....
'''

'''
sys 모듈 : 현재 운영체제에 명령을 내릴 수 있도록 도와주는 모듈
'''
print('--------------1--------------')
''' 
pickle 모듈 : 객체 형태를 그대로 유지해서 파일에 저장하고, 불러올 수 
              있도록 하게 하는 모듈
            : pickle 이용해서 파일에 저장 및 조회 할 때는 반드시
              바이너리(2진수) 형태 이어야 함
            : 전송방식이 스트림 방식이므로
            => b 를 입력해서 바이너리임을 표시해야 함!
'''

import pickle as p

txt = ['a', 'b', 'c']

# fw = open('pickle_txt.txt', 'wb')
# p.dump(txt, fw)   # dump : String return, dumps : Integer return
# fw.close()

print('----------------2-----------------')
fr = open('pickle_txt.txt', 'rb')
result = p.load(fr)
print(result)
fr.close()

print('----------------3------------------')
# dictionary도 가능

data = {1 : 'Hello', 2 : 'Python'}

fw = open('pickle_data.txt', 'wb')
p.dump(data, fw)
fw.close()

fr = open('pickle_data.txt', 'rb')
result = p.load(fr)
print(result)
fr.close()

print('----------------4----------------')
class Hello :
    var = 'Hello'

h = p.dumps(Hello)
print(h)

rs = p.loads(h)
print(rs)

print(rs.var)

print('-------------------5---------------------')
# os 모듈

import os
print(os.environ)  #시스템 환경변수 값 확인 - 딕셔너리 형태로 return

print(os.environ['JAVA_HOME'])  # 인덱싱 가능

print(os.getcwd())    # 현재 위치 확인

#os.chdir('C:\\')

print(os.getcwd())

# os.chdir('C:\\Users\\soldesk\\PycharmProjects\\workspace\\module3')
print(os.getcwd())

#os.system('dir')

fr = os.popen('dir')

print(fr.read())

'''
os.environ : 시스템 환경변수값 확인. 그 정보를 딕셔너리 형태로 리턴
os.chdir :  현재 디렉토리를 변경
os.getcwd : 현재 디렉토리 위치 확인
os.system('명령어') : 시스템의 유틸리티나 dos 명령어를 파이썬에서 호출
os.popen('명령어') : 시스템 명령어를 수행한 결과값을 읽기모드의 파일 객체로 리턴

os.mkdir(디렉토리명) : 내 시스템에 디렉토리 생성
os.rmdir(디렉토리명) : 내 시스템 디렉토리 삭제
                     : 유의 - 디렉토리가 비어있어야 함
os.unlink(파일명) : 파일 삭제
os.rename(src, dst) : src 이름의 파일을, dst로 수정

'''

print('---------------6-----------------')
import shutil

# shutil.copy(src, dst) : src이름의 파일 내용을 dst 이름이 파일로 복사
shutil.copy('test', 'dst.txt')

print('----------------7----------------')
# glob 모듈 : 디렉토리에 있는 파일들을 리스트로 만들 때 사용
import glob

print(glob.glob('C:\\Users\\soldesk\\PycharmProjects\\workspace\\module3\\*'))

print('-----------------8--------------------')
'''
tempfile(임시파일) 모듈
 : 임시적으로 파일을 만들어서 사용할 때 유용한 모듈
 
 - tempfile.mktemp() : 임시로 파일을 만들어서 리턴
                     : 중복되지 않도록 만들어 줌
                     
 - tempfile.TemporaryFile() : 임시적인 저장공간으로 사용될 파일 객체를 리턴하는 함수
                          : w+b 모드를 갖는다
'''

import tempfile

fp = tempfile.mktemp()
print(fp)

fp = tempfile.mktemp()
print(fp)

f = tempfile.TemporaryFile()
f.close()
print(f)

print('-----------9------------')
# TemporaryFile을 이용하려면 방법이 좀 달라야 함
from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    f.write('hello python world \n')
    f.seek(0)  # 포인터 위치 설정
    data = f.read()

print(data)

print('--------------10----------------')
f2 = TemporaryFile('w+t')
print(f2)

f2.write('hi python')

# print(f2.write('hi python'))

f2.seek(0)

txt = f2.read()

f2.close()
f.close()

print(data)
print(txt)

'''
+ file mode

w : 쓰기모드로 파일 열기
r : 읽기모드로 파일 열기
a : 추가모드로 파일 열기
b : 바이너리모드로 파일 열기
------------------------------
w+, r+, a+ : 파일을 업데이트할 용도로 사용
b는 w, r, a 뒤에 붙여서 사용
------------------------------
r : 단지 읽기 위해서 사용하는 모드(default). 포인터위치는 파일 처음에 위치
r+ : 읽기와 쓰기 모드로 파일 열기. 포인터위치는 파일 처음에 위치

w : 파일을 쓰기모드로 열고 파일이 없는 경우 새로 만든다. 포인터위치는 파일 처음에 위치
w+ : 읽기와 쓰기모드로 열고, 파일이 없는 경우 새로만든다. 포인터위치는 파일 처음에 위치

a : 파일을 쓰기모드로 열고 파일이 없는 경우 새로 만든다.
    포인터위치는 파일의 끝에 위치    
a+ : 읽기와 쓰기 모드로 열고. 파일이 없는 경우 새로 만든다.
     포인터위치는 파일의 끝에 위치
     
ex)
 파일을 읽으려면 : r, r+, w+, a+
 파일을 쓰려면   : r+, w, w+, a, a+
 없는 파일을 생성하려면 : w, w+, a, a+
 파일을 덮어쓰려면 : w, w+
 파일을 덧붙이려면 
  - 앞쪽에 덧붙이려면 : r+ 
  - 뒤쪽에 덧붙이려면 : a, a+
  
'''

