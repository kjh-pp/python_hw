from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'http://www.naver.com'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

# 웹 제어 - 키보드 제어
selected_tag = driver.find_element_by_css_selector('input.input_text')
selected_tag.send_keys('날씨')
selected_tag.send_keys(Keys.ENTER)
