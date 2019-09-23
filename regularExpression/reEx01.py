print()
'''
+ 정규 표현식 (Regular Expression)
 : 복잡한 문자열을 처리할 때 사용하는 기법
 : 문자열을 표현하는 모든 곳에서 사용 가능
 
 - re 모듈 : 정규식(정규표현식)을 지원하는 모듈
 - 메타문자 : 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용되는 문자
   ex) - . ^ $ * ? {} [] \ | () 등등
 - 문자클래스 [] : [] 사이의 문자들과 매치
   ex) [abc] : a, b, c 사이의 한 개의 문자와 매치
       
    Project Interpreter -> pip -> bs4   
    Project Interpreter -> pip -> lxml
                                  requests
'''
from bs4 import BeautifulSoup
import re

# URL 형태로 가져온 것?
html = '''
<html>
<head>
<title>test site</title>
</head>
<body>
<div>
<p id='i' class='a'>test1</p>
<p class='d'>test2</p>
<p class='d'>test3</p>
<a href='/example/test1'>a tag</a>
<b> b tag </b>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
# print(soup)

# re.compile() : 해당 문자열이 포함된 코드를 찾는 함수
# 클래스 속성 값에 d가 포함된 요소
print(soup.find_all(class_=re.compile('d')))

# id 속성 값에 i가 포함된 요소
print(soup.find_all(id=re.compile('i')))

# tag에 t가 포함된 요소 전부를 찾아보세요
print(soup.find_all(re.compile('t')))

# tag가 t로 시작하는 요소찾기
print(soup.find_all(re.compile('^t')))   # ^ : 시작

print(soup.find_all(href=re.compile('/')))
'''
+ 정규표현식 장점
 : 정확한 단어가 아니더라도 특정 단어가 포함되거나 패턴이 일치하는 요소를 더 간편하게 찾을 수 있다.
'''

