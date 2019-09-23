from selenium import webdriver

url = 'https://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp'


driver = webdriver.Chrome('chromedriver')
driver.get(url)

# id를 통한 접근 : find_element_by_id()
'''
selected_id = driver.find_element_by_id('container_sub')
print(selected_id)
print(selected_id.tag_name)
print(selected_id.text)
'''

# tag를 통한 접근 : find_element_by_tag_name()
'''
selected_tag = driver.find_element_by_tag_name('a') # 첫번째 a tag 조회
print(selected_tag)
print(selected_tag.tag_name)
print(selected_tag.text)
'''

selected_tags = driver.find_elements_by_tag_name('a')  # 모든 a 태그 조회
# 리스트로 리턴 - tag 이름과 text를 지원하지 않음
# 반복문으로 출력해야 함
for name, content in enumerate(selected_tags):
    print(name, content)
# print(selected_id.tag_name)
# print(selected_id.text)
