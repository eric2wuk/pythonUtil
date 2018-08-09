resultList = None
line1 = None;
line2 = None;
dict = {};
result = []

with open('sql_source.md', 'r', encoding='utf-8') as f:
    resultList = f.readlines();
    for i in range(len(resultList)):
        item = resultList[i];
        itemList = item.split();
        str = "INSERT INTO `db_www`.`t_order_detail` (`order_no`, `code`, `type`, `platform`, `result_code`, `flag_reimburse`, `update_time`, `extends`, `car_no`, `car_no_type`, `driver_name`, `id_no`, `pid`) VALUES ( '%s0', NULL, '7', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '45FF470CBBFB45B0A1F8AB9E909F273F');" %(itemList[0][0:31])
        print(str);