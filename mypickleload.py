import pickle
fff = open('dump.txt','rb')
ddd = pickle.load(fff)
fff.close()
print(ddd)