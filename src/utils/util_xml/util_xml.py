# --coding:utf-8 --
#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom as x_minidom

'''
name    :   combine_stock_datas
parms   :   None
return  :   DataFrame
author  :   Jack, lplcx@live.com
describe:   解析'str'路径的xml文件，并返回
_________________________________________
create  :   Jack
date    :   2018-03-21
_________________________________________
modify  :
'''
def util_xml_parse(str):
    return x_minidom.parse(str).documentElement

