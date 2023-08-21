from selenium import webdriver 
import chromedriver_autoinstaller
import time,ssl
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from wordcloud import WordCloud

ssl._create_default_https_context = ssl._create_unverified_context
user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless") 
chrome_options.add_argument("user-agent="+user_agent)

broswer=webdriver.Chrome(options=chrome_options)
broswer.implicitly_wait(10)

broswer.get('https://new.land.naver.com/complexes/3277?ms=37.5898486,127.037336,16&a=APT:PRE&e=RETAIL')

time.sleep(1)

items=broswer.find_elements(By.CSS_SELECTOR,'.item.false')

donghos=[]
prices=[]
conditions=[]
inner_images=[]
charactors=[]
apt_areas=[]
floor_bathroom_cnts=[]
mgmt_fees=[]
before_moneys=[]
door_directions=[]
door_warm_ways=[]
move_day_parking_cnts=[]
id_apt_home_cnts=[]
comments=[]
brokers=[]
broker_fee_infos=[]
broker_fee_ratios=[]
buy_tax_amts=[]
buy_tax_details=[]
have_tax_amts=[]
have_tas_details=[]

for idx,item in enumerate(items):
    # try:
        item.click()
        print(f'{idx+1}번째')
        time.sleep(2)
        dongho=broswer.find_element(By.CSS_SELECTOR,'.info_title_wrap > .info_title')
        donghos.append(dongho.text)
        
        price=broswer.find_element(By.CSS_SELECTOR,'.info_article_price')
        prices.append(price.text)
        # print(price.text)
        
        condition=broswer.find_element(By.CSS_SELECTOR,'.info_article_feature')
        conditions.append(condition.text)
        
        inner_image=broswer.find_element(By.CSS_SELECTOR,'.floor_plan_img > img').get_attribute('src')
        inner_images.append(inner_image)
    
        #print(inner_image)
        
        charactor=broswer.find_element(By.XPATH,'//*[@id="detailContents1"]/div[1]/table/tbody').find_elements(By.TAG_NAME,'tr')
                                                
        charactors.append(charactor[0].text)
        apt_areas.append(charactor[1].text)
        floor_bathroom_cnts.append(charactor[2].text)
        mgmt_fees.append(charactor[3].text)
        before_moneys.append(charactor[4].text)
        door_directions.append(charactor[5].text)
        door_warm_ways.append(charactor[6].text)
        move_day_parking_cnts.append(charactor[7].text)
        id_apt_home_cnts.append(charactor[8].text)
        comments.append(charactor[9].text)
        try:
            brokers.append(charactor[10].text)
        except:
            brokers.append('중개인정보 없음')
            print('중개인 정보 없음')
        
        tax_fee_info=broswer.find_element(By.XPATH,'//*[@id="detailContents1"]/div[2]/table/tbody').find_elements(By.TAG_NAME,'tr')
        broker_fee_infos.append(tax_fee_info[0].text)
        broker_fee_ratios.append(tax_fee_info[1].text)
        
        
        try:
            buy_tax_amts.append(tax_fee_info[2].text)
        except:
            buy_tax_amts.append("취득세 정보 없음")
            print('취득세 정보 없음')
        try:
            buy_tax_details.append(tax_fee_info[3].text)
        except:
            buy_tax_details.append('취득세 상세정보가 없음')
            print('취득세 상세정보가 없음')
        try:
            
            have_tax_amts.append(tax_fee_info[4].text)
        except:
            print('보유세 정보가 없음')
        try:
            have_tas_details.append(tax_fee_info[5].text)
        except:
            print('보유세 상세 정보가 없음')
        
        
    # except:
    # print('error')
df=pd.DataFrame({'동호수':donghos,'매매가격':prices,'환경':conditions})
print(df)
    

input()