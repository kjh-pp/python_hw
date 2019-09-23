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

# select() : find_all()과 비슷 - 리스트로 반환 => CSS 선택자 활용 가능
print(soup.select('p'))
#print(soup.find_all('p'))

print(soup.select('.a')) # 클래스가 a인 요소 전부
print(soup.select('p.a')) # 태그가 p이고 클래스가 a인 요소 전부
print(soup.select('#d')) # id가 d인 요소
print(soup.select('p#d')) # 태그가 p이고 id가 d인 요소 전부

print('------------------------------1-------------------------------')
# 띄어쓰기를 이용해서 자식 태그 표현 가능
print(soup.select('body p'))
print(soup.select('body .a'))
