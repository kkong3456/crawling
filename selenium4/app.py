from selenium import webdriver
import chromedriver_autoinstaller,ssl,time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


ssl._create_default_https_context = ssl._create_unverified_context

chromedriver_autoinstaller.install()
options=Options()
# options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=options)

query=input('검색어를 입력하세요 : ')

print(query)
url=f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={query}'



driver.get(url)
time.sleep(1)

for _ in range(5):
    driver.execute_script('window.scrollBy(0,10000)')
    time.sleep(3)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# time.sleep(3)

items=driver.find_elements(By.CSS_SELECTOR,'a.api_txt_lines.total_tit')

# html=driver.page_source

# soup=BeautifulSoup(html,'html.parser')

# items=soup.select("a.api_txt_lines.total_tit")


for index,item in enumerate(items):
    print(f'{index} : {item.text}')

# driver.find_element(By.CLASS_NAME,'search_input').send_keys('블랙핑크')
# time.sleep(1)
# driver.find_element(By.ID,"query").send_keys('뉴진스')
# time.sleep(1)
# driver.find_element(By.NAME,'query').send_keys('트와이스')
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,'#query').send_keys('SES')
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,'.search_input').send_keys('소녀시대')
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,'[type="search"]').send_keys('원더걸스')
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="query"]').send_keys('에스파')




driver.quit()




