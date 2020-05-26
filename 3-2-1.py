import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

s = requests.Session() # Session이 열림!
# r = s.get('https://naver.com') # PUT(FETCH), DELETE, GET, POST -> 서버에 요청을 보내는 것.
# print('1', r.text) # get방식으로 요청하여 가져 온 것을 확인 가능...


# Cookies 요청 (페이로드 해서 보냄)
r = s.get('http://httpbin.org/cookies', cookies={'from':'myName'})
print(r.text)


# header 요청
url = 'http://httpbin.org/get'
hearder = {'user-agent':'myPythonApp_1.0.0'}

r = s.get(url, headers=hearder)
print(r.text)

s.close() # Session을 열었으면 close로 닫아줘야 함.



# with 문 사용

with requests.Session() as s:
    r = s.get('https://www.naver.com')
    print(r.text)
