import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.PhantomJS('D:/Python/Crawling/Section3/webdriver/phantomjs/phantomjs')

driver.implicitly_wait(5)
# 암묵적으로 5초를 대기하겠다는 뜻. get으로 받기 전에 모듈 실행하면 에러가 나기 때문..

driver.get('https://google.com')  # 드라이버가 웹브라우져 역할을 해줌.
driver.save_screenshot("c:/website1.png")

driver.implicitly_wait(5)

driver.get('https://www.daum.net')
driver.save_screenshot("c:/website2.png")

driver.quit()
print('스크린샷 완료')
