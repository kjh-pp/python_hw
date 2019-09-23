import bs4

html = ""

# BeautifulSoup : 문자열을 파이썬에서 사용 가능한 객체로 만들어 주는 객체
soup = bs4.BeautifulSoup(html, 'lxml')
'''
+ 파이썬에서 사용하는 parser
1. lxml(default) : xml 해석이 가능한 parser. 파이썬 2.x, 3.x 모두 사용
                 : c 기반 - 다른 parser에 비해 빠름
2. html5lib : 웹브라우저 방식으로 HTML 해석
            : 처리 속도가 상대적으로 느림. 2.x 전용
            
3. html.parser : 최신 버전 사용 x


'''

print('----------------------------1-----------------------------')
from bs4 import BeautifulSoup

html = "<p>test</p>"
# lxml parser : html 과 body tag가 포함된 형태로 만들어 줌
soup = BeautifulSoup(html, 'lxml')

print(soup)

html = "<html><p>test</p></html>"
soup = BeautifulSoup(html, 'lxml')

print(soup)


html = "<body><p>test</p></body>"
soup = BeautifulSoup(html, 'lxml')

print(soup)

print('--------------------------2-------------------------------')

html = "<p>test</p>"
# html5lib parser : html, head, body tag가 포함된 형태로 만들어 줌
#                 : HTML document 처럼 해석
soup = BeautifulSoup(html, 'html5lib')

print(soup)


html = "<html><p>test</p></html>"
soup = BeautifulSoup(html, 'html5lib')

print(soup)

