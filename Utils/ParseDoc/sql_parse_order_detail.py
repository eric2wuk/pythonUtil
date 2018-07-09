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
        str = "INSERT INTO `db_www`.`t_valuation_detail_finance` ( `order_no`, `vin`, `name`, `address`, `mobile`, `city_id`, `detection_no`, `archive_no`, `history_report_no`, `add_time`, `update_time`, `status`, `extend`, `sub_type`, `license_plate_cityid`, `valuation_finish_time`) VALUES ('%s0', '%s', '技术_李白', '澳门特别行政区澳门市test凯旋城', '18500349860', '424', '%s', NULL, NULL, '2018-06-28 18:29:28', '2018-06-28 19:21:54', '1000310', NULL, '1', '735', NULL);" %(itemList[0][0:31],itemList[1],itemList[0][0:32])
        print(str);