import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeMemberExr:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") #CLI (User-agent)
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="D:/Python/Crawling/Section3/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

    # 네이버 카페 로그인 && 출석 체크
    def naverLogin(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('sjh3903')
        self.driver.find_element_by_name('pw').send_keys('wacuaf66^^')
        self.driver.find_element_by_xpath('//*[@id="log.login"]').click()
        self.driver.implicitly_wait(30)
        print('login 완료')

    def writeAttendCheck(self):
        self.driver.get('https://cafe.naver.com/AttendanceView.nhn?search.clubid=13764661&search.menuid=278')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('cmtinput').send_keys('반갑습니다!!.')
        self.driver.find_element_by_xpath('//*[@id="btn-submit-attendance"]').click()
        time.sleep(3)

    # 소멸자
    def __del__(self):
        # self.driver.close() 현재 실행 포커스 된 영역을 종료
        self.driver.quit() #Selenium 전체 프로그램 종료
        print("Removed driver Object")

# 실행

if __name__ == '__main__':
    # 객체 생성
    a = NcafeMemberExr()
    # 시작 시간
    start_time = time.time()
    # 프로그램 실행
    a.naverLogin()
    # 종료 시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    # 객체 소멸
    del a
