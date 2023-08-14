from selenium import webdriver
import chromedriver_autoinstaller,ssl,time,random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

ssl._create_default_https_context = ssl._create_unverified_context

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()



business_id_list=['1647015551','1020816080']
query_list=['부산 피부과','서울 카페']



#1. 네이버 검색창 + 키워드 드라이버 get
for business_id,query in zip(business_id_list,query_list):
    rank=1
    try:
        business_id_selector=f'a[href*="{business_id}?entry=pll"]'
        query_link=f'https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query={query}'
        add_view_selector='a.cf8PL'

        driver.get(query_link)

        for _ in range(1,3):
            driver.execute_script('window.scrollBy(0,5000)')
            time.sleep(2)
            
        # 더보기 엘리먼트    
        add_view_element=driver.find_element(By.CSS_SELECTOR,'#place-main-section-root > div > div.M7vfr > a')

        print(add_view_element.text)
        
        #더보기 클릭
        add_view_element.click()
        time.sleep(2)
        
        business_elements=driver.find_elements(By.CSS_SELECTOR,business_id_selector)
        business_element=random.choice(business_elements)
        
        while True:

            mother_element=business_element.find_element(By.XPATH,'./..')
            target_tag_name=mother_element.get_attribute('tagName')
            
            if target_tag_name=='LI':
                print('태그를 찾았습니다.')
                break
        
            business_element=mother_element
            
        total_li_list_selector='#_list_scroll_container > div > div > div:nth-child(2) > ul >li'
        total_li_list_elements=driver.find_elements(By.CSS_SELECTOR,total_li_list_selector)

        for element in total_li_list_elements:
            # print(element,mother_element)
            try:
                element.find_element(By.CSS_SELECTOR,'a.gU6bV')
                continue
            except:
                pass
            if element==mother_element:
                break
            rank+=1
            
  
    except:
        print(f'{query}로 업체의 순위를 알수가 없습니다.')
        continue
    print(f'현재 {query}는 {rank} 번째로 노출되고 있습니다.')

# scrollY=20000  
# for _ in range(0,15):
#     business_elements=driver.find_elements(By.CSS_SELECTOR,business_id_selector)
    
#     if(len(business_elements)<1):
#         print('순위권에 업체가 없어서 스크롤합니다.')
        
      
#         #driver.execute_script('window.scrollBy(0,10000)')  ==> 이 사이트의 경우 지도가 윈도우고 업체명은 플롯트라서 driver scroll이 안된다.
#         # 200,450은 휴대폰 화면 왼쪽위를 기준으로 스크롤 시작점이고, 200,scrollY는 시작점에서 스크롤 해야할 거리
#         ActionChains(driver).scroll_by_amount(0,scrollY)
#         scrollY+=20000
#         print(scrollY)
#     else:
#         business_elements=driver.find_elements(By.CSS_SELECTOR,business_id_selector)
#         break
   
#     time.sleep(3)



    
        

    

input()