import requests
r = requests.get("https://tm.chaboshi.com/app/redeem/add",params={'q':"phthon"});
print(r)
print(r.url)
print(r.json())