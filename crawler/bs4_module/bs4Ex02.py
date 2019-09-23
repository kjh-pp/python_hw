from bs4 import BeautifulSoup

html = '''<html><head></head><body><p>test</p></body></html>'''

# 보통 BeautifulSoup을 통해 바뀐 데이터는 관례적으로 soup이라 불림
soup = BeautifulSoup(html, 'lxml')
print(soup)
print(type(soup))

print('-----------------------------1-------------------------------')

html = '''<html><head><title>test site</title></head><body><p>test1</p><p>test2</p><p>test3</p></body></html>'''

soup = BeautifulSoup(html, 'lxml')
print(soup)
print(soup.prettify()) # prettify() : HTML코드 들여쓰기 적용

print('-----------------------------2-------------------------------')
# tag에 접근
tag_p = soup.p

print(tag_p)
print(type(soup),',',type(tag_p))
'''
tag에 접근하면 가장 첫번째 tag 정보만 가져옴에 주의

tag명과 데이터가 모두 추출됨에 유의

bs4.BeautifulSoup --> 문서 전체
bs4.element.Tag   --> 각각의 태그
'''
print('--------------------------------3------------------------------------')
html = '''<html><head><title>test site</title></head><body><p>test1</p><p>test2</p><p>test3</p></body></html>'''

soup = BeautifulSoup(html, 'lxml')

tag_title = soup.title

print(tag_title)
print(tag_title.text)
print(tag_title.string)
print(tag_title.name)
print('--------------------------------4------------------------------------')
html = '''<html><head><title>test site</title></head><body><p><span>test1</span><span>test2</span><span>test3</span></p></body></html>'''

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())

tag_p = soup.p
print('text : ', tag_p.text, type(tag_p.text))
print('string : ', tag_p.string, type(tag_p.string))
print('string2 : ', tag_p.span.string, type(tag_p.span.string))

'''
+ text와 string 차이 : 기본적으로 type이 다름

text : 하위 요소의 데이터도 모두 추출해줌
string : 선택한 태그의 데이터만 추출해줌
       : 정확하게 추출하고 싶으면 하위 요소까지 정확하게 지정해줘야 함!
'''