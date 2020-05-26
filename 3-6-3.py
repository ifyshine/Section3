import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import chromedriver_binary

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



# driver = webdriver.Chrome('D:/Python/Crawling/Section3/webdriver/chrome/chromedriver')
# driver.set_window_size(1920,1200)
# 사이즈 조정도 가능함.

# 이렇게 작동하는 경우 웹브라우져가 실제로 뜨기 때문에 불편함..
# phantomJS 처럼 CLI(command line interface)으로 작동하게 하는게 좋음.
# 그래서 phantomJS를 많이 썼던 것임.. 하지만 CLI로도 작동가능! Options 사용.

firefox_options = Options()
firefox_options.add_argument("--headless") # CLI, brower를 사용하지 않고 내부적으로
driver = webdriver.Firefox(firefox_options=firefox_options, executable_path= r'D:/Python/Crawling/Section3/webdriver/firefox/geckodriver')



driver.get('https://google.com')  # 드라이버가 웹브라우져 역할을 해줌.
# time.sleep(5)

driver.save_screenshot("c:/website1_ff.png")

# driver.implicitly_wait(5)

driver.get('https://www.daum.net')
# time.sleep(5)

driver.save_screenshot("c:/website2_ff.png")

driver.quit()
print('스크린샷 완료')
