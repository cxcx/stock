#!/usr/bin/python
#!  get all A share data to /cx/stock/data/stock.csv
import pandas as pd
import tushare as ts
import pandas_datareader as p_data
import numpy as np
import time

path = '/home/cx/work/stock/data/stock.csv'

def save_sh():
    # A share list
    stock_code_list = ts.get_stock_basics().index.tolist()
    stock_list = []
    count = 0

    # traverse all stock code in list
    for code in stock_code_list:
        # get a single stock's data

        data_temp = ts.get_h_data(code, start = '2017-01-01', end = '2008-01-01')
        date_list = data_temp.index.tolist()

        print(data_temp)

        #hanlde the stock's daily data, get data out and instert into the list
        for date in date_list:
            data_sinday = data_temp.loc[date]
            open_price = data_sinday['open']
            high_price = data_sinday['high']
            close_price = data_sinday['close']
            low_price   = data_sinday['low']
            price_change = (close_price - open_price)/open_price

            #add data to list
            stock_list.append({'code': code, 'date' : date, 'open' : open_price, 'high' : high_price, \
                           'low' : low_price, 'close' : close_price, 'change':price_change})

    data_all_sh = pd.DataFrame(stock_list)
    print(data_all_sh)


    #! save data to file

    pd.to_csv(path, data_all_sh)

