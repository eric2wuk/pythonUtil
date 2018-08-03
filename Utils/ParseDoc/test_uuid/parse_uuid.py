import random
x = [x for x in range(0, 16*16*16*16*16*16)]
# for x in range(16*16*16*16*16*16):
#     list.append(str(uuid.uuid4()).replace("-","")[0:6].upper());
# print(list);
random.seed(7)
random.shuffle(x)
with open('result.txt', 'w', encoding='utf-8') as f:
    for i in range(10000):
        line = "INSERT into t_redeem_codekey (code,STATUS,add_time) VALUES('%s',0,NOW()) ;" %(str(hex(x[i]))[2:].upper())
        f.write(line+"\n")



