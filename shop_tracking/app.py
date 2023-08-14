from selenium import webdriver
import chromedriver_autoinstaller,ssl,time
from selenium.webdriver.common.by import By

ssl._create_default_https_context = ssl._create_unverified_context

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()

#Url로 1page부터 방문
query_list=['꿀사과']
shopping_code=['86442895943']
for query,target_code in zip(query_list,shopping_code):
    for page_index in range(1,15):

        shopping_link=f'https://msearch.shopping.naver.com/search/all?frm=NVSHPAG&origQuery=%EA%BF%80%EC%82%AC%EA%B3%BC&pagingIndex={page_index}&pagingSize=40&productSet=total&query={query}&sort=rel&viewType=lst'

        driver.get(shopping_link)
        time.sleep(3)

        # 페이지를 4 ~ 5번 밑으로 내리기
        for _ in range(5):
            driver.execute_script('window.scrollBy(0,10000);')
            time.sleep(2)
            
        #타겟상품이 페이지에 노출되고 있는지 확인하기
        #없다면 Url로 NextPage가기
        try:
            target_selector=f'a[data-i="{target_code}"]'
            print(target_selector)
            target_element=driver.find_element(By.CSS_SELECTOR,target_selector)
            data=target_element.get_attribute('data-nclick')
            total_ranking=data.split(',')[2].split(':')[1]
            ranking=int(total_ranking)-40*int(page_index-1)
            
            
            # allPageRanking=(int(page_index)-1)*40+int(ranking)
            print(f'등수는 {page_index}페이지에서 {ranking}번째에 노출되고 있습니다.')
            break
            
        except Exception as e:
            print(f'{page_index}페이지 찾기 실패')
            page_index+=1
        

input()