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

chrome_options.add_argument("--window-size=1600,1024")
chrome_options.add_argument("--headless") 
chrome_options.add_argument("user-agent="+user_agent)

broswer=webdriver.Chrome(options=chrome_options)
broswer.implicitly_wait(10)

broswer.get('http://www.bunyangline.com/app-v2/workspace/pc/')

time.sleep(1)

items=broswer.find_elements(By.CSS_SELECTOR,'.firstGrid > .recruitList')
time.sleep(3)

titles=[]
specs=[]
addresses=[]

cnt=0

for idx,item in enumerate(items):
    try:
        # print(f'item object is : {type(item)}')
        print(f'{idx}번째')
        item.click()
        time.sleep(2)
        
        cnt+=1
        
        if cnt>=100:
            break
        
     
        tbody=item.find_element(By.XPATH,'//*[@id="app"]/div[5]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/table/tbody').find_elements(By.TAG_NAME,'tr')
        # print(f'tbody object is {type(tbody)}')
        for tr in tbody:
            try:  
                # if '현장명' in tr.text:
                #     print(tr.text.split('\n')[0][4:0])
                #     print(f'현장명이 존재합니다.')
                # else:
                #     print(tr.text.split('\n')[0][4:0])   
                #     print(f'현장명이 존재하지 않습니다.')        
                title=tr.find_element(By.XPATH,'//*[@id="app"]/div[5]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/table/tbody/tr[1]/td').text
                titles.append(title)
                spec=tr.find_element(By.XPATH,'//*[@id="app"]/div[5]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/table/tbody/tr[2]/td').text
                specs.append(spec)             
                address=tr.find_element(By.XPATH,'//*[@id="app"]/div[5]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/table/tbody/tr[6]/td')
                print(address.text.split('\n')[-1][:-15])
                addresses.append(address.text.split('\n')[-1][:-15])
                break
            except:
                print('tr error')
        
        broswer.execute_script('window.history.go(-1)')
        time.sleep(1)
    except:
        print('error')
        
df=pd.DataFrame({'제목':titles,'특성':specs,'주소':addresses})
print(df)
df.to_csv('./부동산분양.csv')

wc=WordCloud(font_path='./NanumGothic.ttf',colormap='PuBu',width=500,height=500)
wc.generate(str(df['제목']))
wc.to_file('부동산분양.png')