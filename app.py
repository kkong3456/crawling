from selenium import webdriver
import chromedriver_autoinstaller,ssl,time
from selenium.webdriver.common.by import By

ssl._create_default_https_context = ssl._create_unverified_context

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
driver.get('https://naver.com')
time.sleep(3)

selector='#shortcutArea > ul'
navigation=driver.find_element(By.CSS_SELECTOR,selector)

print(navigation.text)

#click
navigation.click()

input()