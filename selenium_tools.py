from selenium import webdriver
import chromedriver_autoinstaller,ssl,time
from selenium.webdriver.common.by import By

ssl._create_default_https_context = ssl._create_unverified_context

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()

#1. navigation 관련 툴
#1.1 원하는 페이지로 이동하는 함수
# driver.get('https://naver.com')
# time.sleep(1)
# driver.get('https://daum.net')
# time.sleep(1)

# #1.2 뒤로가기  driver.back()
# driver.back()
# time.sleep(2)

# #1.3 앞으로가기 driver.forward()
# driver.forward()
# time.sleep(2)

# #1.4 리프레시 driver.refresh()
# driver.refresh()
# time.sleep(2)

# input()

#2. brower inforamtion

# driver.get('https://naver.com')
# time.sleep(1)

# #2.1  title을 가져온다
# title=driver.title
# print(title,'이 제목이다')

# #2.2 현재 주소창을 가져온다
# current_url=driver.current_url
# print(current_url,' 이 현재 주소이다')


#3. Driver wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

#3.1  selector 가 10초 안에 찾아지면 10초 기다리지 않고 바로 다음단계로 넘어감

selector1='<a href="https://news.naver.com/" class="link_service" target="_blank"><span class="service_icon type_news"></span><span class="service_name">뉴스</span></a>'
try:
    WebDriverWait(driver,10).until(EC.presence_of_element_located)(
        By.CSS_SELECTOR,selector1
    )
except Exception as e:
    print(e)
print('다음 단계로 넘어감')

input()
