import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# ex1. 사이트 요청
# r = requests.get('https://api.github.com/evnets') # 이 url로 정보를 get 하겠다!
# r.raise_for_status() # 에러가 나면 에러를 발생시켜줌.
# print(r.text)

# ex2. 쿠키 전달 -> 규격화, 형식에 맞춰서... 하는 방법 (jar)
# jar = requests.cookies.RequestsCookieJar()
# jar.set('name', 'kim', domain='httpbin.org', path='/cookies')
#
# r = requests.get("http://httpbin.org/cookies", cookies=jar)
# r.raise_for_status()
# print(r.text)
# print()

# ex3. timeout 이용
# r = requests.get('https://github.com', timeout=3)
# 서버가 반응할 때까지 3초까지 대기하겠다. -> 평소엔 괜찮은데 event 등으로 인해 몰릴 때 사용...
# print(r.text)
# print()

# ex4. post형식으로 request (데이터를 서버상에 저장)
# r= requests.post('http://httpbin.org/post', data={'name':'kim'}, cookies=jar)
# print(r.text)


# ex5. payload (data를 서버상에 요청할 때 담을 수 있는 것)
payload1 = {'key1' : 'value1', 'key2' : 'value2'}
payload2 = (('key1', 'value1'), ('key2', 'value2'))
payload3 = {'some':'nice'} # json으로도 보낼 수 있음.

# r = requests.post('http://httpbin.org/post', data=payload1)
# r = requests.post('http://httpbin.org/post', data=payload2)
r = requests.post('http://httpbin.org/post', data=json.dumps(payload3))
# 아까완 달리 form으로 넘어오는게 아니라 json으로 넘어옴... (위의 두개는 form으로 넘어옴.)

print(r.text)

# payload1과 payload2의 결과값은 똑같음.
