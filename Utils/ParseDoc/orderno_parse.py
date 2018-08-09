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
        str = "http://localhost/api/valuation/detectionCallBack?orderid=%s" %(list[i][0:32])
        print(str);