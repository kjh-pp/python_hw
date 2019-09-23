from bs4 import BeautifulSoup

html = '''<html><head><title>test site</title></head><body><p><span>test1</span><span>test2</span>test3</p></body></html>'''

soup = BeautifulSoup(html, 'lxml')
# 관계를 이용한 추출 방식

# 자식태그 추출 - contents 속성 - 리스트 형태로 추출
print(soup.p.contents)
# 자식태그 추출 - children 속성 - iterator object 형태로 추출 => 반복문으로 추출
print(soup.p.children)

tag_p_children = soup.p.children

for child in tag_p_children:
    print(child, end=' ')
print()

print('--------------------------------1----------------------------------')
tag_span = soup.span
tag_title = soup.title

# 부모 태그 추출 : parent 속성
span_parent = tag_span.parent
title_parent = tag_title.parent

print('====== 현 재 태 그 ======')
print(tag_span)
print(tag_title)

print('====== 부 모 태 그 ======')
print(span_parent)
print(title_parent)


print('--------------------------------2----------------------------------')

# 부모 태그 추출 : parents 속성
span_parents = tag_span.parents
title_parents = tag_title.parents

print('====== 현 재 태 그 ======')
print(span_parent)
print(title_parent)

print('====== 부 모 태 그 ======')
print(span_parents)         # generator 객체 리턴 => 반복문으로 추출
for parents in span_parents:
    print('span_parents : ',parents)
print()


print(title_parents)
for parents in title_parents:
    print('title_parents : ',parents)


