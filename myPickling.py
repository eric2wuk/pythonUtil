import pickle
d = dict(name='Bob', age=20, score=88)
fff = open('dump.txt','wb')
pickle.dump(d,fff)
fff.close()