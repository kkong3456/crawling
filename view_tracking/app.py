from selenium import webdriver
import chromedriver_autoinstaller
import ssl,time
from selenium.webdriver.common.by import By

ssl._create_default_https_context = ssl._create_unverified_context

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()

query='python flask'
search_link=f'https://search.naver.com/search.naver?query={query}&nso=&where=view&sm=tab_nmr&mode=normal'

driver.get(search_link)

target_blog_link='https://cafe.naver.com/synologynas/194493'
selector=f'a[href^="{target_blog_link}"]'

BLOG_FOUND=False

for _ in range(7):
    try:
        element=driver.find_element(By.CSS_SELECTOR,selector)
        print(f'element is {element}')

        while True:
            new_element=element.find_element(By.XPATH,"./..")
            current_link=new_element.get_attribute('data-cr-rank')
            
            if current_link!=None:
                print('현재 링크 찾음', current_link)
                BLOG_FOUND=True
                break
            element=new_element
            print('현재 링크 못찾음')
        if BLOG_FOUND:
            break
    except Exception as e:
        print(f'타겟 블로그를 못찾은 경우 => 스크롤 필요')
        driver.execute_script('window.scrollBy(1,10000);')
        time.sleep(3)
if BLOG_FOUND:
    print(f'타겟 블로그의 링크를 찾았습니다 : {query}')
else:
    print(f'타겟 블로그를 찾지 못했습니다. : {query}')
input()