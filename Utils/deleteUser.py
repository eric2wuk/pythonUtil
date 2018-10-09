sql_select='select *  from '
sql_delete='delete  from '
db_name = 'db_www.'
where = '  where user_id= '
for user_id in (312508,314781,381704,346630,365933,336076,354956,376002,369331,380408,361091,341161,344879,364446,380958,381802,370756,353958,344128,343100,360741,352879,342259,377692,358772,375631,343127,375628,331643,338444,326404,374176,330022,371209,359509,356234,374080,361695,359420,341767,380541,335440,341714,344918,337506,341928,379602,379284,338273,334301,363247,363883) :
    for table in ('t_account',
                  't_account_log',
                  't_account_sellprice_log',
                  't_account_snapshot',
                  't_call_log',
                  't_cardealer_seller',
                  't_chart_brand',
                  't_chart_order',
                  't_chart_user',
                  't_chart_vin',
                  't_commission_log',
                  't_gps_detail',
                  't_history_days_api',
                  't_invoice_detail',
                  't_invoice_info',
                  't_login_log',
                  't_match_user_bid',
                  't_news_push',
                  't_order',
                  't_order_check',
                  't_own_user_change_log',
                  't_performance',
                  't_redeem_detail',
                  't_scratchcard',
                  't_seller_recharge',
                  't_seller_user',
                  't_support_brand_acl',
                  't_user_bank',
                  't_user_car_valuation',
                  't_user_detail',
                  't_user_file',
                  't_user_peccancy',
                  't_user_product_blacklist',
                  't_valuation_api',
                  't_we_chat_account',
                  't_withdraw') :
        sql=sql_delete + db_name + table  + where +  str(user_id) + ';'
        print(sql)
        # excel_name=table + '_' + str(user_id)
        # write_excel(db,sql,file_path_base,excel_name)