import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# stream data -> json data로 변형해서 그 안에 있는 key 값 모두 출력하기
s = requests.Session()
r = s.get('http://httpbin.org/stream/20') # 20개
# print(r.text) # json 같은데...? json으로 변형 출력해보면?
# print(r.json()) # error

# print(r.encoding) # None -> encoding 설정해줘야 함.
if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    # print(line)
    b = json.loads(line) # json data로 converting
    # print(type(b))
    # print(b['origin']) # json 형태의 dictionary가 된 것을 확인할 수 있음.
    for e in b.keys():
        print("key:", e, "/", "values:",b[e]) # 각 json의 모든 value값 추출 가능


# r = s.get('http://httpbin.org/stream/20', stream=True)  -> 위의 예에서 요렇게 하는게 더 좋음.

# http://www.apistore.co.kr/api/apiList.do
