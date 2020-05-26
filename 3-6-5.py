import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import chromedriver_binary

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



driver = webdriver.Chrome('D:/Python/Crawling/Section3/webdriver/chrome/chromedriver')
# driver.set_window_size(1920,1200)
driver.implicitly_wait(3)



driver.get('http://www.encar.com/index.do')
time.sleep(3)

driver.find_element_by_xpath('//*[@id="manufact"]/a').click()
driver.find_element_by_xpath('//*[@id="manufactListText"]/ul[1]/li[1]/a').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="series"]/a').click()
driver.find_element_by_xpath('//*[@id="seriesItemList"]/li[2]/a').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="md"]/a').click()
driver.find_element_by_xpath('//*[@id="mdlItemList"]/li[2]/a').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="indexSch1"]/div[1]/a').click()
# driver.quit()

print('검색 완료')
