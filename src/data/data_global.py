# --coding:utf-8 --
# data_global.py
# 全局数据


def __init():
    global dict_config
    global data_all
    dict_config = {'version': None, 'date_update': None}    # 配置文件数据字典
    data_all = None                                         # 所有股票数据


def get_config_dic():
    return dict_config


def set_config_dic(key, value = None):
    global dict_config
    try:
        dict_config[key] = value
    except KeyError:
        pass


def get_data_all():
    return data_all


def set_data_all(data):
    global data_all
    data_all = data
