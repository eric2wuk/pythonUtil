from collections import OrderedDict
ddd = dict([('a',1), ('b',2), ('c',3)])
print(ddd)
od = OrderedDict([('a',1),('b',2), ('c',3)])
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
print(od)