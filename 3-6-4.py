import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import chromedriver_binary

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



driver = webdriver.Chrome('D:/Python/Crawling/Section3/webdriver/chrome/chromedriver')
driver.set_window_size(1920,1200)
driver.implicitly_wait(3)



driver.get('https://www.inflearn.com/')
time.sleep(3)
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="header"]/nav/div[2]/div/div[2]/div[2]/div[2]/a[1]').click()
# driver.find_element_by_xpath('//*[@id="signin"]').click()

driver.find_element_by_class_name('input.email').send_keys('sjh3903@naver.com')
driver.implicitly_wait(1)
driver.find_element_by_class_name('input.pwd').send_keys('cuaf7664')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="root"]/div[4]/section/form/button').click()

# driver.quit()
print('접속 완료')
