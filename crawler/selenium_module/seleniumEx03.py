from selenium import webdriver

url = 'https://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp'


driver = webdriver.Chrome('chromedriver')
driver.get(url)

# name 속성을 통한 접근
'''

selected_name = driver.find_element_by_name('SearchCmd_out')

print(selected_name)
print(selected_name.tag_name)
print(selected_name.text)

selected_names = driver.find_elements_by_name('SearchCmd_out')

'''

# a tag의 href 속성을 통한 접근
'''
selected_href = driver.find_element_by_link_text('')
print(selected_href)
print(selected_href.tag_name)
print(selected_href.text)

selected_hrefs = driver.find_elements_by_link_text('')
print(selected_hrefs)
'''

url = 'https://www.python.org/'


driver = webdriver.Chrome('chromedriver')
driver.get(url)




# path를 통한 접근 - href path 중 찾는 단어가 포함될 경우에 접근할 수 있도록 해줌
selected_link = driver.find_element_by_partial_link_text('about')
print(selected_link)
print(selected_link.tag_name)
print(selected_link.text)

# href path를 통해서 접근시 그 이름이 없는 요소를 찾으면 에러 발생






