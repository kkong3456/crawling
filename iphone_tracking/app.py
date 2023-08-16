from selenium import webdriver 
import chromedriver_autoinstaller
import time,ssl
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

ssl._create_default_https_context = ssl._create_unverified_context

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1600,1024") 

broswer=webdriver.Chrome(options=chrome_options)
broswer.implicitly_wait(10)

broswer.get('https://shopping.naver.com/home')

time.sleep(1)

#쇼핑 메뉴 클릭
# broswer.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[4]').click()

# tab_handler=broswer.window_handles

#새로운 탭으로 핸들러 위치
# broswer.switch_to.window(tab_handler[1])

#아이폰13 검색 클릭
input_element=broswer.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
time.sleep(1)
input_element.click()
time.sleep(1)
input_element.send_keys('아이폰13')
time.sleep(1)
input_element.send_keys(Keys.ENTER)
time.sleep(2)

before_h=broswer.execute_script('return window.scrollY')
while True:
    broswer.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
    



input()