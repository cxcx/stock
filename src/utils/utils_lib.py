# --coding:utf-8 --
#!/usr/bin/python

from util_xml.util_xml import *

'''
name    :   util_parse_config
parms   :   path
return  :   {'version':version, 'date_update':date}
author  :   Jack, lplcx@live.com
describe:   解析配置文件，返回描述字典
_________________________________________
create  :   Jack
date    :   2018-03-21
_________________________________________
modify  :
'''
def util_parse_config():
    dict_config = {'version':None, 'date_update':None}
    root_element = util_xml_parse('/home/cx/work/stock/config.xml')
    dict_config['version'] = root_element.getElementsByTagName('version')[0].childNodes[0].data
    dict_config['date_update'] = root_element.getElementsByTagName('date_update')[0].childNodes[0].data
    return dict_config
