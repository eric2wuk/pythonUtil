
resultList = None
line1 = None;
line2 = None;
dict = {};
result = []

with open('orderno.md', 'r', encoding='utf-8') as f:
    resultList = f.readlines();
    list = resultList[0].split();
    for i in range(len(list)):
        # str = '"%s0" ,' %(list[i][0:31])
        str = "orderNos.add(\"%s\");" %(list[i][0:32])
        print(str);


#
# with open('orderno.md', 'r', encoding='utf-8') as f:
#     url = 'http://lfinance.chaboshi.cn/app/finval/add'
#     d = {'name': '技术-李白', 'address': '凯旋城1901','mobile':'18500349860','cityid':424,'licensecityid':40,"watchmile":2.5,"plateyear":"2018-08-08","modelid":88485}
#     r = requests.post(url, data=d)
#     resultList = f.readlines();
#     list = resultList[0].split();
#     for i in range(len(list)):
#         # str = '"%s0" ,' %(list[i][0:31])
#         str = "http://localhost/api/valuation/detectionCallBack?orderid=%s" %(list[i][0:32])
#         print(str);