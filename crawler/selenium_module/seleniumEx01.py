# 가상 DOM(Document Of Object) 를 활용한 크롤러
from selenium import webdriver

url = 'https://www.naver.com'

# res = rq.get(url) # 직접 접근

driver = webdriver.Chrome('chromedriver')

driver.get(url)

#driver.execute_script('alert("test")')

