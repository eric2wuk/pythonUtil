import re
resultList = None
with open('resultPathDoc.txt', 'r', encoding='utf-8') as f:
    resultList = f.readlines()

with open('resultPathDoc2.txt', 'w', encoding='utf-8') as f:
    i = 1
    for line in resultList:
        str = '*           1.%d   %s' %(i,line)
        f.write(str)
        i = i+1