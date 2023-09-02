import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Slot
from random import choice
from ui_naver_estate_data import Ui_MainWindow

from selenium import webdriver 
import chromedriver_autoinstaller
import time,ssl
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import cairosvg

from PIL import Image
from io import BytesIO

from wordcloud import WordCloud

ssl._create_default_https_context = ssl._create_unverified_context
user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("--headless") 
chrome_options.add_argument("user-agent="+user_agent)

broswer=webdriver.Chrome(options=chrome_options)
broswer.implicitly_wait(10)




class MainWindow(QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super().__init__()      
        self.setupUi(self)
 
        self.단지정보리스트=[]
        self.면적83리스트=[]
        self.면적108리스트=[]
        self.면적141리스트=[]
        
        self.startUrl1()
        self.get_url_button.clicked.connect(self.startUrl1)
        
       
          
    def startUrl1(self):
        # url1=self.url1_line_edit.text()
      
        url1='https://new.land.naver.com/complexes/3277?ms=37.5900862,127.0393113,15&a=APT:PRE&e=RETAIL'
        broswer.get(url1)

        time.sleep(1)
        #단지정보 클릭
        broswer.find_element(By.XPATH,'//*[@id="summaryInfo"]/div[2]/div[2]/button[1]').click()
        time.sleep(1)
        단지정보들=broswer.find_element(By.XPATH,'//*[@id="detailContents1"]/div[1]/table/tbody').find_elements(By.TAG_NAME,'tr')
        time.sleep(1)
        
        for idx in range(len(단지정보들)):
            try:
                # print((단지정보들[idx].text.split(' ')[0]+' : '+단지정보들[idx].text.split(' ')[1:]))
                self.단지정보리스트.append(단지정보들[idx].text)
            except:
                pass
        
        time.sleep(1)
        
        면적83=broswer.find_element(By.XPATH,'//*[@id="tab0"]').click()
        time.sleep(1)   
        면적83정보들=broswer.find_element(By.XPATH,'//*[@id="tabpanel"]/table/tbody').find_elements(By.TAG_NAME,'tr')
        
        for idx in range(len(면적83정보들)):
            try:
                self.면적83리스트.append(면적83정보들[idx].text)
            except:
                print('면적83에러')
        
        time.sleep(1)
        
        
        # inner_scroll_element=broswer.find_element(By.CSS_SELECTOR,'.detail_contents.is-complex') #스크롤부분 찾기
        # broswer.execute_script('arguments[0].scrollTop=0',inner_scroll_element)
        # time.sleep(10)
        
        면적108=broswer.find_element(By.XPATH,'//*[@id="tab1"]').click()
        time.sleep(1)
        면적108정보들=broswer.find_element(By.XPATH,'//*[@id="tabpanel"]/table/tbody').find_elements(By.TAG_NAME,'tr')
        for idx in range(len(면적108정보들)):
            try:
                self.면적108리스트.append(면적108정보들[idx].text)
            except:
                print('면적108에러')
                
        
        면적141=broswer.find_element(By.XPATH,'//*[@id="tab2"]').click()
        time.sleep(1)
        면적141정보들=broswer.find_element(By.XPATH,'//*[@id="tabpanel"]/table/tbody').find_elements(By.TAG_NAME,'tr')
        for idx in range(len(면적141정보들)):
            try:
                self.면적141리스트.append(면적141정보들[idx].text)
            except:
                print('면적141에러')
                
        #.tab_item#detailTab2
        #실거래가 클릭
        broswer.find_element(By.CSS_SELECTOR,'.tab_area_list > .tab_item#detailTab2').click()
        time.sleep(2)
        #83평 클릭
        xxx=broswer.find_elements(By.XPATH,'//*[@id="tab0"]')
        print(xxx[0].text)
        time.sleep(10)    
        broswer.close()
                
       
        
        
            

    

      
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    print(window.면적108리스트)
    data={'단지정보':window.단지정보리스트,'면적83정보': window.면적83리스트,
          '면적108정보':window.면적108리스트,'면적141정보':window.면적141리스트}
    df = pd.DataFrame.from_dict(data, orient='index').transpose()
    df.to_csv('제기한신.csv',sep=',',encoding='utf-8')
    #window.show()

    #app.exec_()