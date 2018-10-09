import requests
import hashlib
import sys

paramid = "2"
token = "aaa"
print(sys.argv)
param = sys.argv[1]
clientid = "1"
str =clientid+param+paramid+token
hl = hashlib.md5()
hl.update(str.encode(encoding='utf-8'))
print('MD5加密后为 ：' + hl.hexdigest())
key = hl.hexdigest()
url = "Https://meizhouapi.58.com/v3/query/chaboshi/push/"+param+"/"+paramid+"?clientid=1"+"&key="+key
r = requests.get(url)
print(r.text)
