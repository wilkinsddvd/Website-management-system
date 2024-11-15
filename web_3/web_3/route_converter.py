'''
@version: v1.0
@author: wilkins_ddvd
@contact: qingsdao_ddvd@163.com
@software: PyCharm
@file: route_converter.py
@desc: 路由路径转换器类型定义模块
'''

class RouteYearConverter:
    '''自定义年份类型转换器'''
    regex = '[0-9]{4}'
    def to_python(self, value):
        return int(value)
    def to_url(self, value):
        return '%04d'%value