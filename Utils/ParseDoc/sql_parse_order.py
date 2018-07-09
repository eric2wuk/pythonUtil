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
        str = "INSERT INTO `db_www`.`t_order` ( `order_no`, `user_id`, `order_status`, `order_money`, `pay_money`, `buy_time`, `confirm_time`, `pay_time`, `pay_type`, `vin`, `source`, `thirdpart_orderid`, `order_type`, `check_time`, `deleted`, `timeout`, `expire_days`, `remark`, `extends`, `check_code`, `engine_no`, `car_no`, `refresh_times`, `order_standard_money`) VALUES ('%s0', '63640', '1000300', '999.00', '999.00', '2018-06-28 18:29:28', '2018-06-28 19:21:54', '2018-06-28 19:21:54', '0', '%s', '8', NULL, '12', NULL, '0', '0', NULL, '测试李白20180629,detection_no:%s', NULL, NULL, NULL, NULL, '0', '999.00');" %(itemList[0][0:31],itemList[1],itemList[0][0:32])
        print(str);