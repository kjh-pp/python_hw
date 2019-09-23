from bs4 import BeautifulSoup

html = '''
<html>
<head>
<title>test site</title>
</head>
<body>
<p class="a">test1</p>
<p id="d" class="a"> test2 </p>
<p class= "e">test3</p>
<a> a tag</a>
<b> b tag</b>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')

# 해당 페이지에 찾고자 하는 요소가 하나만 있는 경우(id로 찾아올 경우) : find() 권장
print(soup.find('p'))
print(soup.find_all('p', limit=1)[0])

print('--------------------------------1-----------------------------------')
print(soup.find('span'))
try:
    print(soup.find_all('span')[0]) # 빈 리스트에 값을 요청하면 error 발생
except IndexError as ie:
    print('IndexError', ie)
print('--------------------------------2-----------------------------------')
# id, class 로 찾기 가능
print(soup.find('p', id='d'))
print(soup.find('p', class_='a'))

print('--------------------------------3-----------------------------------')
print(soup.find('body').find('p', id='d'))
