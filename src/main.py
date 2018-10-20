# --coding:utf-8 --
#! main.py
# the main function

import stock_data as sd
import stock_lib as slib
import pandas as pd
import sys
from data import data_global

path_config_xml = '../config.xml'

'''
name    :   
parms   :   None
return  :   None
author  :   Jack, lplcx@live.com
_________________________________________
create  :   Jack
date    :   2018-03-18
_________________________________________
modify  :
'''
def change_proc(dataframe):
    data_temp = slib.stock_caculate_change(dataframe)


'''
name    :   
parms   :   None
return  :   None
author  :   Jack, lplcx@live.com
_________________________________________
create  :   Jack
date    :   2018-03-18
_________________________________________
modify  :
'''
def do_all_change_proc():
    df_alldata = sd.data_read_csv(sd.path_pool + 'stock_data.csv')
    b_first = True
    data_frame_ret = pd.DataFrame()
    data_grouped = df_alldata.groupby('code')

    for code in data_grouped.groups.keys():
        data_one_code = data_grouped.get_group(code)
        data_frame = slib.stock_caculate_change(data_one_code)
        if b_first:
            data_frame_ret = data_frame
            b_first = False
        else:
            data_frame_ret = data_frame_ret.append(data_frame, ignore_index = True)

    sd.data_write_csv(data_frame_ret, sd.path_pool + 'stock_data.csv')


'''
name    :   main
parms   :   None
return  :   None
author  :   Jack, lplcx@live.com
_________________________________________
create  :   Jack
date    :   2018-03-18
_________________________________________
modify  :
'''
def main_init():
    data = sd.data_read_csv(sd.path_pool + 'data.csv')
    data_global.set_data_all(data)

'''
name    :   main_menu
parms   :   None
return  :   None
author  :   Jack, lplcx@live.com
descrip :   菜单功能选择
_________________________________________
create  :   Jack
date    :   2018-03-18
_________________________________________
modify  :
'''
def main_print_menu():
    print('1. Input \'s\' to show the datas\n')
    print('2. Input \'u\' to update the datas\n')
    print('3. Input \'q\' to exit!\n')
    print('Please input your task:')


'''
name    :   main_menu
parms   :   None
return  :   None
author  :   Jack, lplcx@live.com
descrip :   菜单功能选择
_________________________________________
create  :   Jack
date    :   2018-03-18
_________________________________________
modify  :
'''
def main_print_option(menu_chioce):
    if 's' == menu_chioce:
        print('1. input \'show all\' to show the datas\n')
        print('2. input \'show xxxxxx\' to show the data of code xxxx\n')
        print('Please input your task:')

'''
name    :   main
parms   :   None
return  :   None
author  :   Jack, lplcx@live.com
_________________________________________
create  :   Jack
date    :   2018-03-21
_________________________________________
modify  :
'''

if __name__ == '__main__':
    main_init()

    # main loop
    while True:
        main_print_menu()
        choice = raw_input()
        if 's' == choice:
            main_print_option(menu_chioce=choice)
            choice = raw_input()
            choice = choice.split()[1]
            if 'all' == choice:
                # 输出当前股票数据
                sd.data_show()
            else:
                sd.data_show(code=choice)
        elif 'u' == choice:
            # 更新股票数据
            sd.data_update()
        elif 'q' == choice:
            # 退出
            sys.exit(0)


