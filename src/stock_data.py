# --coding:utf-8 --
# utils_stock.py
# providing some basic function for procing stock data

'''
name    :   combine_stock_datas
parms   :   None
return  :   DataFrame
author  :   Jack, lplcx@live.com
_________________________________________
create  :   Jack
date    :   2018-03-18
_________________________________________
modify  :
'''


import pandas as pd
import tushare as ts
import datetime as dt
from data import data_global

# 数据路径
path_pool = '~/work/stock/data/'
# 退市数据
codes_delisted = pd.DataFrame()


'''
_________________________________________
name    :   data_get_stocks_delisted
parms   :   None
return  :   DataFrame
descri  :   Jack, lplcx@live.com
_________________________________________
author  :   Jack, lplcx@live.com
date    :   2018-04-04
_________________________________________
modify  :
_________________________________________
'''
def data_get_stocks_delisted():
    return codes_delisted


# combine two dataframe into one
def data_comb_df(df_a = pd.DataFrame(), df_b = pd.DataFrame()):
    return df_a.append(df_b)


def data_read_csv(path = ''):
    return pd.read_csv(path, dtype={'code': str})


def data_write_csv(datafrme, path = ''):
    return datafrme.to_csv(path, index=False)


# get today's data and merge into the data pool
def data_update_csv(path = path_pool):
    data_poll = data_read_csv(path)
    data_today = ts.get_today_all()
    date_string = dt.datetime.isoformat(dt.datetime.now().date())


'''
_________________________________________
name    :   data_show
parms   :   None
return  :   None
descri  :   Jack, lplcx@live.com
_________________________________________
author  :   Jack, lplcx@live.com
date    :   2018-04-07
_________________________________________
modify  :
_________________________________________
'''
def data_show(code=None):
    data_all = data_global.get_data_all()
    if data_all.empty:
        print('None stock data exist!!!\n')
        return

    if code is None:
        print(data_all)
    else:
        # 数据不存在则catch异常
        try:
            data_code = data_all.groupby('code').get_group(code)
        except KeyError:
            print("Code:" + code + ' no data exists!!!\n')
            return

        # 打印指定代码数据
        print(data_code)


'''
_________________________________________
name    :   combine_stock_datas
parms   :   None
return  :   DataFrame
descri  :   Jack, lplcx@live.com
_________________________________________
author  :   Jack, lplcx@live.com
date    :   2018-03-18
_________________________________________
modify  :
_________________________________________
'''
def data_conbine():
    df17 = data_read_csv(path_pool + '2017data.csv')
    df16 = data_read_csv(path_pool + '2016data.csv')
    df15 = data_read_csv(path_pool + '2015data.csv')
    df14 = data_read_csv(path_pool + '2014data.csv')
    df13 = data_read_csv(path_pool + '2013data.csv')
    df12 = data_read_csv(path_pool + '2012data.csv')
    df11 = data_read_csv(path_pool + '2011data.csv')
    df10 = data_read_csv(path_pool + '2010data.csv')
    df09 = data_read_csv(path_pool + '2009data.csv')
    df08 = data_read_csv(path_pool + '2008data.csv')
    df07 = data_read_csv(path_pool + '2007data.csv')
    df06 = data_read_csv(path_pool + '2006data.csv')

    return df06.append(df07).append(df08).append(df09).append(df10).append(df11).append(df12).append(df13) \
                .append(df14).append(df15).append(df16).append(df17)


'''
_________________________________________
name    :   data_update_fromto
parms   :   None
return  :   None
descri  :   更新指定日期内的数据
_________________________________________
author  :   Jack, lplcx@live.com
date    :   2018-03-31
_________________________________________
modify  :
_________________________________________
'''
def __data_judge_delisted(code):
    b_delisted = False
    global codes_delisted
    # A股退市判断, tushare目前不支持深市退市股票
    if codes_delisted.empty:
        codes_delisted = ts.get_terminated()
    codes = codes_delisted['code']
    for index in codes.index.tolist():
        code_num = codes.get(key=index)
        if code == code_num:
            b_delisted = True

    #####   #####   #####   #####  #####
    # 深圳股市判断, 待完成
    #####   #####   #####   #####  #####

    return b_delisted


'''
_________________________________________
name    :   data_update_fromto
parms   :   None
return  :   None
descri  :   更新指定日期内的数据
_________________________________________
author  :   Jack, lplcx@live.com
date    :   2018-03-31
_________________________________________
modify  :
_________________________________________
'''
def data_update():
    date_now = dt.datetime.now()
    hour_now = date_now.hour
    data_saved = data_global.get_data_all()
    date_end = date_now
    data_to_csv = pd.DataFrame()

    if hour_now < 15:
        date_end = date_now - dt.timedelta(days=1)

    end_str = date_end.strftime('%Y-%m-%d')
    data_grouped = data_saved.groupby('code')

    for key in data_grouped.groups.keys():
        code = str(key)
        data_code = data_grouped.get_group(code)

        # 获取该股票上次更新日期, 并求本次更新的起始时间
        date_last_str = data_code.sort_values(by='date').tail(1).iloc[0]['date']
        date_last = dt.datetime.strptime(date_last_str, '%Y-%m-%d')
        date_start = date_last + dt.timedelta(days=1)

        date_start_str = date_start.strftime('%Y-%m-%d')

        # 获取数据
        data_need_saved = ts.get_k_data(code, start=date_start_str, end=end_str)
        if data_need_saved.empty:
            # 如果数据为空, 判断是否退市
            b_delisted = __data_judge_delisted(code)
            if b_delisted:
                print('code:' + code + ' delisted\n')
                # 退市则删除该股以前所有数据
                continue
            else:
                data_code = data_grouped.get_group(code)
                if data_to_csv.empty:
                    data_to_csv = data_code
                else:
                    data_to_csv = data_to_csv.append(data_code, ignore_index=True)

                continue
        else:
            data_code = data_grouped.get_group(code)
            data_need_saved = data_need_saved.drop('volume', axis=1)
            if data_to_csv.empty:
                data_to_csv = data_code.append(data_need_saved, ignore_index=True)
            else:
                data_code_update = data_code.append(data_need_saved, ignore_index=True)
                data_to_csv = data_to_csv.append(data_code_update, ignore_index=True)

    data_global.set_data_all(data_to_csv)
    # 保存数据到文件
    data_write_csv(data_to_csv, path=path_pool + 'data.csv')

'''
_________________________________________
name    :   data_update_today
parms   :   None
return  :   None
descri  :   更新当日数据，保存数据到文件并返回当日最新数据
_________________________________________
author  :   Jack, lplcx@live.com
date    :   2018-03-21
_________________________________________
modify  :
_________________________________________
'''
def data_update_today():
    date_now = dt.datetime.now()
    hour_now = date_now.hour
    b_first = True
    # 当天已闭市则更新至当天数据，如还在交易则更新至上一交易日数据
    if hour_now < 15:
        return
    data_today = ts.get_today_all()
    data_saved = data_global.get_data_all()
    data_need_save = pd.DataFrame()
    data_grouped = data_saved.groupby('code')
    date_today = date_now.strftime('%Y-%m-%d')
    for code in data_grouped.groups.keys():
        data_today.set_index('code')
        data_code_today = data_today.loc[code]
        close_price = data_code_today['trade']
        open_price = data_code_today['open']
        change = data_code_today['changepercent'] / 100.00
        high_price = data_code_today['high']
        low_price = data_code_today['low']
        df_today = pd.DataFrame({'code': [code], 'close': [close_price], 'date': [date_today], 'open': [open_price], \
                                 'high': [high_price], 'low': [low_price], 'change': [change]})
        data_code = data_grouped.get_group(code)
        data_new = data_code.append(df_today, ignore_index=True)
        if b_first:
            data_need_save = data_new
        else:
            data_need_save.append(data_new, ignore_index=True)

        # 删除data_today中的今日数据
        data_today.drop(code, inplace=True)

    # 更新今天上市的股票
    if data_today.empty:
        for code in data_today.index.tolist():
            data_code_today = data_today.loc[code]
            close_price = data_code_today['trade']
            open_price = data_code_today['open']
            change = data_code_today['changepercent'] / 100.00
            high_price = data_code_today['high']
            low_price = data_code_today['low']
            df_today = pd.DataFrame({'code': [code], 'close': [close_price], 'date': [date_today], 'open': [open_price], \
                                        'high': [high_price], 'low': [low_price], 'change': [change]})
            data_need_save.append(df_today, ignore_index=True)

    data_write_csv(data_need_save, path_pool + 'stock_data.csv')

    return data_need_save
