import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Response 상태 코드
s = requests.Session()
r = s.get('http://httpbin.org/get')
print(r.status_code) # 200
print(r.ok) # True

# json 예제 대표 사이트
# https://jsonplaceholder.typicode.com

r = s.get('https://jsonplaceholder.typicode.com/posts/1')
# print(r.text)
# print(r.json()) # requests 모듈에서 제공함.
# print(r.json().keys())
# print(r.json().values())
# print(r.encoding)
# print(r.content)
# print(r.raw)

# 위의 정도의 method는 알고 있어야 함.
