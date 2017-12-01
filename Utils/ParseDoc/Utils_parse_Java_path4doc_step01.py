import re
resultList = None
with open('PathDoc.java', 'r', encoding='utf-8') as f:
    resultList = f.readlines()

with open('resultPathDoc.txt', 'w', encoding='utf-8') as f:
    for line in resultList:
        if re.match(r'.*Path\(', line):
            f.write(line)