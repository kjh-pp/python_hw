from selenium import webdriver
'''
url = 'http://example.com/'

driver = webdriver.Chrome('chromedriver')

driver.get(url)

selected_selector = driver.find_element_by_css_selector('a')
print(selected_selector)
print(selected_selector.tag_name)
print(selected_selector.text)

# 웹 제어 - 마우스 제어
selected_selector.click()
'''

'''
click()을 통한 페이지 이동을 권장하지는 않음 
- 페이지 이동을 해버리면 이전 페이지의 DOM객체를 더이상 사용할 수
  없기 때문
=> 클릭 했을 때 페이지 이동 없이 해당 페이지 내에서 데이터가
   추가되는 경우에 사용하는 것을 권장
'''
url = 'https://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp'


driver = webdriver.Chrome('chromedriver')
driver.get(url)

# 웹 제어 - 마우스 제어
# 선택한 곳에 커서를 위치해 둘 수도 있음
selected_tag_input = driver.find_element_by_css_selector('input.i_text_m4')

selected_tag_input.click()