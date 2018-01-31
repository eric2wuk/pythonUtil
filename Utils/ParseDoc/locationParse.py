import re
resultList = None
d1 ={};
d2 ={};

with open('locationInfo.txt', 'r', encoding='utf-8') as f:
    resultList = f.readlines();
    for line in resultList:
        d1[line.split("	")[0]]={'cityName':line.split("	")[0],'position':line.split("	")[1].replace('\n','')}

with open('locationInfo2.txt', 'r', encoding='utf-8') as f:
    resultList = f.readlines();
    # maps.put("北京",new CityInfosVO("北京","北京市昌平区亚运村汽车交易市场精品厅二楼——58线下服务中心",40.0947500000,116.4166970000));
    for line in resultList:
        key = line.split("XXX")[0];
        value = line.split("XXX")[1].replace('\n','');
        str = ' maps.put("%s",new CityInfosVO("%s","%s",%s));' %(key,key,value,d1[key]['position']);
        print(str);
        # str = '*           1.%d   %s' %(i,line)
        # d2[line.split("XXX")[0]]=line.split("XXX")[1]
#
# with open('result.txt', 'w', encoding='utf-8') as f:
#     i = 1
#
#
#         print(line.split("	")[0]);
#         # str = '*           1.%d   %s' %(i,line)
#         # f.write(str)
#         # i = i+1
#     print(d);