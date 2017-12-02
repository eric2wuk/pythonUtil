from collections import Counter
ccc = Counter()
for ch in 'programming, coding, hello world, 中国':
    ccc[ch]= ccc[ch] +1

print(ccc)