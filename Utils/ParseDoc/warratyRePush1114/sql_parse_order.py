resultList = None
line1 = None;
line2 = None;
dict = {};
result = []

with open('order', 'r', encoding='utf-8') as f:
    resultList = f.readlines();
    for i in range(len(resultList)):
        item = resultList[i];
        str = 'list.add("%s");'%(item.strip('\n'))
        print(str);