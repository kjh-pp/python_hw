print()
'''
+ 원하는 요소에 정확하게 접근하기
'''

from bs4 import BeautifulSoup

html = '''
<html>
<head>
<title>test site</title>
</head>
<body>
<p>test1</p>
<p id="d" class="c"> test2 </p>
<p class= "e">test3</p>
<a> a tag</a>
<b> b tag</b>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')

p_element = soup.p

print(p_element) # 첫번째 element만 가져다 줌
# 원하는 요소를 전부 : find_all() - 리스트 형태로 return
print(soup.find_all('title'))
print(soup.find_all('p'))

# id 로 찾아오기
print(soup.find_all(id='d'))

# id 가 존재하는 태그, id 가 존재하지 않는 태그 찾기
print(soup.find_all(id=True))
print(soup.find_all(id=False))

# 찾고싶은 태그 + 원하는 id
print(soup.find_all('p', id='d'))
print('없는 id:',soup.find_all('p', id='c')) # 없는 id 찾으면 빈리스트로 return

print('---------------------------------1----------------------------------')
# class 로 원하는 요소 찾기
# python 에도 class 라는 keyword가 존재하므로 class_ 를 사용하여 충돌 방지(권장)
print(soup.find_all('p', class_='c'))
print(soup.find_all('p', class_='e'))

print('---------------------------------2----------------------------------')
# text 요소로 찾기
print(soup.find_all('p', text='test1'))
print(soup.find_all('p', text='t'))

print('---------------------------------3----------------------------------')
#print(soup.find_all()) # 모든 태그 가져오기 (중복 되어 리턴함에 유의)

# 찾아올 태그 양 제한
print(soup.find_all('p', limit=1))
print(soup.find_all('p', limit=2))
print(soup.find_all('p', limit=3))
print(soup.find_all('p', limit=4))

print('---------------------------------4----------------------------------')

# 여러 태그 가져오기
print(soup.find_all(['a', 'b']))

print('---------------------------------5----------------------------------')
tag_body = soup.find_all('body')
tag_p = tag_body[0].find_all('p')

print(type(tag_body), tag_body)
print(type(tag_p), tag_p)


#print(tag_body[0].find_all('p'))