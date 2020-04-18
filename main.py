from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import request
import time

myid = ""
mypswd = ""

def gainList(searchList) :
    i = 1;
    while(i<9) :
        print(i)
        driver.find_element_by_xpath("//table[@class='tab']/tbody/tr/td/div/a["+str(i)+"]").click()
        req = driver.page_source
        src = bs(req, 'html.parser')
        tlist = src.select('.listBody')
        for elem in tlist :
            searchList.append(elem.text)        
        i+=1
    return searchList
    
keywords = {'김영길', 'IGE', 'grace school', '구글', '반기문관', '창조도서관', 'creation library', 'HGCP', }

#히즈넷 자동 로그인
driver = webdriver.Chrome("C:\dev\chromedriver.exe")
driver.get("http://hisnet.handong.edu")
driver.implicitly_wait(2)
driver.switch_to.frame('MainFrame')
driver.find_element_by_css_selector("input[name='id']").send_keys(myid)
driver.find_element_by_css_selector("input[name='password']").send_keys(mypswd)
driver.find_element_by_css_selector("input[src='/2012_images/intro/btn_login.gif']").click()
driver.implicitly_wait(1.5)


#자가검사 통과
try :
    driver.find_element_by_class_name("button3").click()
except:
    print("ok")
    
driver.implicitly_wait(1.5)

#원클릭민원 진입
searchList = []
driver.get("https:///hisnet.handong.edu/myboard/list.php?Board=ONECLICK")
req = driver.page_source
src = bs(req, 'html.parser')
tlist = src.select('.listBody')


for elem in tlist :
    searchList.append(elem.text)


gainList(searchList)

searchList = set(searchList)
for a in keywords :
    for b in searchList :
        if a in b :
            print(a)
    