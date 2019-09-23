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

'''
# extract() : 실제 크롤링 작업을 해왔을 때 필요한 부분보다 많으면 용량이 많아지므로
                용량을 줄이기 위한 용도
            : 필요없는 javascript 나 style 요소를 제외하고 싶을 때 사용

'''

# 필요없는 요소 제거 : 부모 태그를 삭제하면 자식 태그도 삭제됨에 유의!
# result = soup.body.extract()

# print('--------------------------------')
# print('제거 내역', result)
# print('--------------------------------')
# print(soup)

print('----------------------1-----------------------')
# print(soup.p.extract())  # 없앤 내용을 보여줌

# for tag in soup.select('p'):
#     print(tag.extract())

# print(soup)

print('----------------------2-----------------------')
# find_all()과 조합하면 여러 태그를 동시에 삭제 가능
for tags in soup.find_all(['a','b']):
    print(tags.extract())

print(soup)
