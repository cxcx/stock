# -- coding:utf-8 --
#!/bin/usr/pytgon
# stock_lib.py
# privide some basic fuction for stock data processing

import pandas as pd

'''
fuction name: stock_filter
descripe    : 根据增长率选择股票
parmeter    : dataframe
              filter (years, rate) 表示连续几年增长大于rate增长率 
retaaurn     '''
'''
_________________________________________
name    :   combine_stock_datas
parms   :   DataFrame
return  :   list[]
descri  :   根据增长率选择股票
_________________________________________
author  :   Jack, lplcx@live.com
date    :   2018-03-18
_________________________________________
modify  :
_________________________________________
'''
def stock_caculate_change(frame1):
    is_first = True
    index_list = frame1.index.tolist()
    change_list = {'change' : []}

    for index in index_list:
        data_temp = frame1.loc[index]
        if is_first:
            price_last = data_temp['close']
            is_first = False
            change_list['change'].append(0)
        else:
            change = (data_temp['close'] - price_last) / price_last
            change_list['change'].append(change)
            price_last = data_temp['close']

    dataframe_change = pd.DataFrame(change_list, index = index_list)

    return frame1.join(dataframe_change)


def stock_del_XSHX():
    data_all = pd.read_csv('/home/cx/work/stock/data/stock_data.csv')
    index_list = data_all.index.tolist()

    for index in index_list:
        data_one = data_all.loc[index]
        code_old = data_one['code']
        print(code_old)
        code_new = code_old.split('.')[0]
        data_all.at[index, 'code'] = code_new
        print(data_all.loc[index]['code'])

    data_all.to_csv('/home/cx/work/stock/data/stock_data.csv')


'''
fuction name: stock_filter
descripe    : 根据增长率选择股票
parmeter    : dataframe
              filter (years, rate) 表示连续几年增长大于rate增长率 
retaaurn     '''
'''
_________________________________________
name    :   combine_stock_datas
parms   :   DataFrame
return  :   list[]
descri  :   根据增长率选择股票
_________________________________________
author  :   Jack, lplcx@live.com
date    :   2018-03-18
_________________________________________
modify  :
_________________________________________
'''
def stock_change_fromto(code_df, start, end = None, ndays = 1):
    if end:
        return code_df.query('(@start <= data) | (data <= @end)')
    #else:


'''
fuction name: stock_filter
descripe    : 根据增长率选择股票
parmeter    : dataframe
              filter (years, rate) 表示连续几年增长大于rate增长率 
retaaurn     '''
'''
_________________________________________
name    :   combine_stock_datas
parms   :   DataFrame
return  :   list[]
descri  :   根据增长率选择股票
_________________________________________
author  :   Jack, lplcx@live.com
date    :   2018-03-18
_________________________________________
modify  :
_________________________________________
'''

def stock_filter(dataframe, filter):

    return


if __name__ == '__main__':
    stock_del_XSHX()
