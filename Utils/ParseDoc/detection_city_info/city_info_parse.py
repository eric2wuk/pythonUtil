import re
resultList = None
d1 ={};
d2 ={};

with open('city_info.npp', 'r', encoding='utf-8') as f:
    resultList = f.readlines();
    for i in range(len(resultList)):
        line = resultList[i];
        item_list =line.split("XXX")
        str = 'ArrayList<CityInfosVO> cityInfosVOS_%d = new ArrayList<>();' %(i);
        print(str);
        postion = item_list[2].split(',');
        str2 = 'cityInfosVOS_%d.add(new CityInfosVO("%s","%s",%s,%s));'%(i,item_list[0],item_list[1],postion[0],postion[1]);
        print(str2);
        str3 ='maps.put("%s",cityInfosVOS_%d);' %(item_list[0],i);
        print(str3);
