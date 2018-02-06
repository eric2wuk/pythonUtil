resultList = None
line1 = None;
line2 = None;
dict = {};

with open('money.md', 'r', encoding='utf-8') as f:
    resultList = f.readlines();
    line1 = resultList[0].split();
    line2 = resultList[1].split();
    for i in range(len(line1)):
        if line2[i] != '0':
            dict[line1[i]]=line2[i];
    print(dict)