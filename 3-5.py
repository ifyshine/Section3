# CSRF : 자동으로 실행되는 걸 막는 것.
# 이걸 막기 위해 브라우져에 CSRF token 값을 내려주고, 이거까지 확인하는 것.. 랜덤으로 발행되기 때문에 브라우져로 실제 접속해야 발행이 됨
# 또한 user agent 모드도 확인함..


import requests
from bs4 import BeautifulSoup
import sys
import io
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 요청 URL
URL = 'https://www.wishket.com/accounts/login/'

# 로그인 Form data를 분석해보면, cssf token값을 요구하고 있으며 이는
# 웹브라우져로 접속시에 랜덤으로 생성하여 쿠키로 제공함.
# 즉, 웹브라우져로 접속해야만 cssf token 쿠키값을 받을 수 있음.

# Fake User-Agent 생성
ua = UserAgent()
# print(ua.chrome)
# 제대로 생성된 것을 확인할 수 있음.

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # URL 연결
    s.get(URL)
    # URL get 없이 연결 요청시 cssf 쿠키값이 없으며, user-info가 없다고 404 됨.
    # 고로, URL 먼저 연결하여 cssf 값을 받아올 수 있음.

    #Login 정보 Payload
    LOGIN_INFO = {
        'identification' : 'ifyshine',
        'password' : 'cuaf7664',
        'csrfmiddlewaretoken' : s.cookies['csrftoken']
    }

    # print('token', s.cookies['csrftoken'])
    # 실행할 때 마다 랜덤으로 바뀌는 것을 확인할 수 있음. 토큰값 get!

    # User-agent 없이 요청 -> 토큰값만으로 안됨.. 왜??
    # response = s.post(URL, data=LOGIN_INFO)

    # print('header', s.headers)
    # 사이트에 Python으로 접속한다고 뻔히 알려주고 있음... 그렇기에 404 당하는 것

    # User-agent 포함하여 요청
    # response = s.post(URL, data=LOGIN_INFO, headers={'User-Agent':str(ua.chrome)})
    # 아직도 안됨... referer header가 더 필요하다고 함..
    # referer headers 는 어디서 이 사이트로 접속했는지 확인 하는 것.

    # Referer header까지 포함하여 요청
    response = s.post(URL, data=LOGIN_INFO, headers={'User-Agent':str(ua.chrome), 'Referer' : 'https://www.wishket.com/accounts/login/'})

    # HTML 결과 확인
    # print('response', response.text)

    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        projectList = soup.select("table.table.table-responsive > tbody > tr")
        # print(projectList)
        for i in projectList:
            print(i.find('th').string, i.find('td').text)
