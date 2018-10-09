
resultList = None
line1 = None;
line2 = None;
dict = {};
result = []

with open('orderno.md', 'r', encoding='utf-8') as f:
    resultList = f.readlines();
    list = resultList[0].split();
    for i in range(len(list)):
        i_ = list[i]
        str = "orderNos.add(\"%s\");" %(i_[0:32])
        print(str);

