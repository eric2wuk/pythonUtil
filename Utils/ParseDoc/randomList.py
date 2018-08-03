import random
x = [x for x in range(1000, 9999)]
print(x)
random.seed(7)
random.shuffle(x)
print(x)