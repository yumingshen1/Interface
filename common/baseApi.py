# -*- coding:utf-8 -*-
# @Time : 2021/12/6 22:26
# Auther : shenyuming
# @File : baseApi.py
# @Software : PyCharm
'''
    基类封装
    1，加入异常机制
    2，截图操作
    3，常用接口，增删改查
    4，调整
'''

import requests,inspect
from utils.handle_yml import get_yaml_data
from configs.config import HOST
class BaseApi:
    def __init__(self):
        # 获取继承父类的子类的类名,以获取整个类的数据
        self.data = get_yaml_data('../configs/apiConfig.yaml')[self.__class__.__name__]

    def request_send(self,data=None,params=None):
        ## 获得调用该方法的函数名，
        methodName = inspect.stack()[1][3]
        # 获得具体函数方法对应的请求方式和路径
        path,method = self.data[methodName].values()
        resp = requests.request(method=method,url=f'{HOST}{path}',data=data,params=params)
        print('request_send请求后的数据',resp.json())
        return resp.json()

