# json 처리하기 : Dictionary와 유사함

import json


j1 = {"name":"홍길동","birth":"1999.03.23","age":"20"}

print(j1)

d1 = json.dumps(j1) #.encode("utf-8")
print(d1)

json.loads(d1)
