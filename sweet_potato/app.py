from selenium import webdriver 
import chromedriver_autoinstaller
import time,ssl,sys
from wordcloud import WordCloud
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

ssl._create_default_https_context = ssl._create_unverified_context

chromedriver_autoinstaller.install()

crawler=webdriver.Chrome()
crawler.implicitly_wait(10)
crawler.set_window_size(1920,1080)

crawler.get('https://shopping.naver.com/home')

time.sleep(1)

#!!!!!!!!!!!!!!!! 클릭이후 새로운 탭이 열리면 ind_element는 기존 탭에서 엘리먼트를 찾기때문에 에러가 난다.
#네이버 쇼핑 클릭
#crawler.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[4]/a/span[1]').click()


query='고구마'
engine=crawler.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
engine.click()
engine.send_keys(query)
engine.send_keys(Keys.ENTER)
time.sleep(2)

#리뷰많은순  //*[@id="content"]/div[1]/div[1]/div[1]/div[1]/a[4]
crawler.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[1]/div/div[1]/a[4]').click()
time.sleep(1)



names=[]
prices=[]
review_cnts=[]
links=[]

for i in range(1,3):
    crawler.get(f'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={query}&pagingIndex={i}&pagingSize=40&productSet=total&query={query}&sort=review&timestamp=&viewType=list#')
    print(i)
    
    while True:
        bHeight=crawler.execute_script('return document.body.scrollHeight')
        
        print(f'bHeight is {bHeight}')
        
        time.sleep(4)
        crawler.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        aHeight=crawler.execute_script('return document.body.scrollHeight')
        print(f'aHeight is {aHeight}')
        
        if bHeight==aHeight:
            break
        
        bHeigith=aHeight

    infos=crawler.find_elements(By.CSS_SELECTOR,".product_info_area__xxCTi")

    for info in infos:
        try:
            name=info.find_element(By.CSS_SELECTOR,'.product_title__Mmw2K').text
            names.append(name)
            price=info.find_element(By.CSS_SELECTOR,'.product_price_area__eTg7I').text
            prices.append(price)
            review_cnt=info.find_element(By.CSS_SELECTOR,'.product_num__fafe5').text
            review_cnts.append(review_cnt)
            
            link=info.find_element(By.CSS_SELECTOR,'.product_link__TrAac.linkAnchor').get_attribute('href')
            links.append(link)
        except Exception as e:
            print(e)
            
df=pd.DataFrame({'name':names,'price':prices,'review_cnt':review_cnts,'link':links})
# print(df)
# df.to_csv('./delicious_sweet_potato.csv',sep=',',encoding='utf-8-sig')

# print(str(df['name']))

# file_name=sys.argv[1]
wc=WordCloud(font_path='./H2GTRE.ttf',colormap='PuBu',width=500,height=500)
wc.generate(str(df['name']))
wc.to_file('고구마.png')
            
input()
# crawler.close()

