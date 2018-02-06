try:
    f = open('./t2est.txt','r')
    print(f.read())
finally:
    f.close()