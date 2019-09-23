from bs4 import BeautifulSoup

html = '''<html><head><title>test site</title></head><body><p><span>test1</span><span>test2</span>test3</p></body></html>'''

soup = BeautifulSoup(html, 'lxml')

tag_span = soup.span

# 형제 찾기 - sibling
a = tag_span.next_sibling

c = a.next_sibling

b = a.previous_sibling

print(a)
print(c) # 없는 형제를 찾으면 None으로 return
print(b)

print('-------------------------------1---------------------------------')

html = '''
<html>
<head>
<title>test site</title>
</head>
<body>
<p>
    <a>test1</a>
    <b>test2</b>
    <c>test3</c>
</p>
</body>
</html>
'''
soup = BeautifulSoup(html, 'lxml')
tag_a = soup.a
tag_b = soup.b
tag_c = soup.c

'''
형제 태그 접근 할 때 꼭 같은 이름일 필요는 없음. 위치가 같으면 형제(들)로 인식
'''

print(tag_a.next_siblings)

tag_a_nexts = tag_a.next_siblings

for sibling in tag_a_nexts:
    print(sibling)

print('-----------------')
tag_c_previous = tag_c.previous_siblings
for sibling in tag_c_previous:
    print(sibling)

print('---------------------------------2-------------------------------------')

# 요소 접근 : 태그도 포함하면서 태그 안에 있는 자식 태그, 문자 모두 포함
tag_p = soup.p
tag_p_nexts = tag_p.next_elements

#print(tag_p_nexts)

for element in tag_p_nexts:
    print(element)