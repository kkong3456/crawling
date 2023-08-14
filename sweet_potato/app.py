from selenium import webdriver 
import chromedriver_autoinstaller
import time,ssl
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

ssl._create_default_https_context = ssl._create_unverified_context

chromedriver_autoinstaller.install()

crawler=webdriver.Chrome()
crawler.implicitly_wait(10)

crawler.get('https://shopping.naver.com/home')

time.sleep(1)

#!!!!!!!!!!!!!!!! 클릭이후 새로운 탭이 열리면 ind_element는 기존 탭에서 엘리먼트를 찾기때문에 에러가 난다.
#네이버 쇼핑 클릭
#crawler.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[4]/a/span[1]').click()


engine=crawler.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
engine.click()
engine.send_keys('고구마')
engine.send_keys(Keys.ENTER)

crawler.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[1]/div/div[1]/a[4]').click()

names=[]
prices=[]
review_cnts=[]
links=[]

for i in range(1,3):
    crawler.get(f'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EA%B3%A0%EA%B5%AC%EB%A7%88&pagingIndex={i}&pagingSize=40&productSet=total&query=%EA%B3%A0%EA%B5%AC%EB%A7%88&sort=rel&timestamp=&viewType=list')
    print(i)
    
    while True:
        bHeight=crawler.execute_script('return document.body.scrollHeight')
        print(f'bHeight is {bHeight}')
        time.sleep(4)
        crawler.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        aHeight=crawler.execute_script('return document.body.scrollHeight')
        
        if bHeight==aHeight:
            break
        
        bHeigith=aHeight


input()

