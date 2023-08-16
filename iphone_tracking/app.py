from selenium import webdriver 
import chromedriver_autoinstaller
import time,ssl
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from wordcloud import WordCloud

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

names=[]
prices=[]
links=[]
reviews=[]

for i in range(1,3):
    url=f'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%95%84%EC%9D%B4%ED%8F%B013&pagingIndex={i}&pagingSize=40&productSet=total&query=%EC%95%84%EC%9D%B4%ED%8F%B013&sort=rel&timestamp=&viewType=list'
    broswer.get(url)
    time.sleep(2)
    before_h=broswer.execute_script('return window.scrollY')
    
    while True:
        broswer.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
        time.sleep(1)
        after_h=broswer.execute_script('return window.scrollY')
        
        if after_h==before_h:
            break
        
        before_h=after_h
        time.sleep(1)
    
    items=broswer.find_elements(By.CSS_SELECTOR,'.product_item__MDtDF')

    for index,item in enumerate(items):
        name=item.find_element(By.CSS_SELECTOR,'.product_title__Mmw2K').text
        names.append(name) 
        try:
            price=item.find_element(By.CSS_SELECTOR,'.price_num__S2p_v').text
        except:
            price='판매중단'
        prices.append(price)
        
        link=item.find_element(By.CSS_SELECTOR,'.product_title__Mmw2K > a').get_attribute('href')
        links.append(link)
        
        try:
            review=item.find_element(By.CSS_SELECTOR,'.product_etc_box__ElfVA > .product_etc__LGVaW > .product_num__fafe5').text
        except Exception as e:
            review='리뷰없음'
        reviews.append(review)

        print(index,name,price,link,review)
    
df=pd.DataFrame({'name':names,'price':prices,'link':links,'review':reviews})

df.to_csv('아이폰13.csv')

wc=WordCloud(font_path='./NanumGothic.ttf',colormap='PuBu',width=500,height=500)
wc.generate(str(df['name']))
wc.to_file('아이폰_워드크라우드.png')
