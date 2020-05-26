import sys
import io
import requests, json

# Rest API : POST, GET, PUT(FETCH), DELETE
# PUT : UPDATE, REPLACE
# FETCH : UPDATE, MODIFY

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

payload1 = {'key1' : 'value1', 'key2' : 'value2'}
payload2 = (('key1', 'value1'), ('key2', 'value2'))
payload3 = {'some':'nice'}

# ex1. put 사용
# r = requests.put('http://httpbin.org/put', data=payload1)
# print(r.text)

# ex2. put by jsonplaceholder
# r = requests.put('https://jsonplaceholder.typicode.com/posts/1', data=payload1)
# print(r.text)
# fake rest API

# ex3
r = requests.post('http://www.kma.go.kr/weather/lifenindustry/sevice_rss.jsp', data=payload1)
print(r.text)
