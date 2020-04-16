from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from selenium import webdriver

import time

driver = webdriver.Chrome("C:\dev\chromedriver.exe")
driver.get("http://hisnet.handong.edu")
driver.implicitly_wait(2)
driver.switch_to.frame('MainFrame')
driver.find_element_by_css_selector("input[name='id']").send_keys('id')
driver.find_element_by_css_selector("input[name='password']").send_keys('password')
driver.find_element_by_css_selector("input[src='/2012_images/intro/btn_login.gif']").click()
#히즈넷 자동 로그인

driver.implicitly_wait(2)
driver.get("https://hisnet.handong.edu/myboard/list.php?Board=ONECLICK")
