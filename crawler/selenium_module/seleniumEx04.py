from selenium import webdriver

url = 'https://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp'


driver = webdriver.Chrome('chromedriver')
driver.get(url)

# class를 통한 접근
'''

selected_class = driver.find_element_by_class_name('content_menu')
print(selected_class)
print(selected_class.tag_name)
print(selected_class.text)

selected_class = driver.find_elements_by_class_name('content_menu')
'''

# css 선택자를 통한 접근
'''
selected_css = driver.find_element_by_css_selector('ul.pclist_list2 li.pclist_list_tit42')
print(selected_css)
print(selected_css.tag_name)
print(selected_css.text)

selected_css = driver.find_elements_by_css_selector('ul.pclist_list2 li.pclist_list_tit42')
'''




