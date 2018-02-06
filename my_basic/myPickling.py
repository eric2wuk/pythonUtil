import json
d = dict(name='Bob', age=20, score=88)
fff = open('dump.txt','w')
json.dump(d,fff)
fff.close()