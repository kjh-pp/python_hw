from bs4 import BeautifulSoup

html = '''<html><head><title class="t" id="ti">test site</title></head><body><p>test1</p><p>test2</p><p>test3</p></body></html>'''

soup = BeautifulSoup(html, 'lxml')

# tag 를 통한 추출 : soup.[태그명]
tag_title = soup.title

#print(tag_title)

# tag 속성을 통한 추출
print(tag_title.attrs) # attrs : 해당 태그 속성 추출 - 딕셔너리 형태로 추출
print(tag_title['class']) # key 값으로 출력
print(tag_title['id'])

print('-----------------------------1-------------------------------')
try :
    print(tag_title['classx']) # 추출해 올 태그에 없는 이름 - 에러 발생
except KeyError as ke:
    print('KeyError', ke)

print('-----------------------------2-------------------------------')
# get()를 통해 tag 속성 추출 - 에러를 방지
print(tag_title.get('class'))
print(tag_title.get('id'))
print(tag_title.get('classx'))

print(tag_title.get('classy', 'none_value'))

