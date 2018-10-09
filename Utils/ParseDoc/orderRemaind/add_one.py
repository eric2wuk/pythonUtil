import requests
url = 'http://lfinance.chaboshi.cn/app/finval/add'
ck = "CBS_UUID=YTI2MjcyMDM3MWU3N2MyYWM1MGYxZDEzNDNjMWJhYTk0OWM5ZmJkZWMwN2FiNzQ4MjVlOTZiNjI5NWQxNzgwMmJjMTBmNTgwYTJkOWUzMDUyMzlhYmNmYTY5NGU1NTllLDcyMCwxNTM1NDUwMTU4NTY3; path=/; domain=.chaboshi.cn; Expires=Thu, 27 Sep 2018 09:55:58 GMT;"
d = {'name': '技术-李白', 'address': '凯旋城1901','mobile':'18500349860','cityid':424,'licensecityid':40,"watchmile":2.5,"plateyear":"2018-08-08","modelid":88485}
r = requests.post(url, data=d,cookies=ck)
print(r)