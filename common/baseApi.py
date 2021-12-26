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

import requests,inspect,os
from utils.handle_path import config_path
from utils.handle_yml import get_yaml_data
from configs.config import HOST
class BaseApi:
    def __init__(self,inToken = None):
        ## 处理调用token
        if inToken:
            self.header = {'Authorization':inToken}
        else:
            self.header = None

        # 获取继承父类的子类的类名,以获取整个类的数据
        self.data = get_yaml_data(os.path.join(config_path,'apiConfig.yaml'))[self.__class__.__name__]

    # 获取数据
    def request_send(self,data=None,params=None,json=None,file=None,id=''):
        try:
            ## 获得调用该方法的函数名，
            methodName = inspect.stack()[1][3]
            # 获得具体函数方法对应的请求方式和路径
            path,method = self.data[methodName].values()
            #剥离对应每个接口的数据
            resp = requests.request(method=method,url=f'{HOST}{path}{id}',data=data,params=params,
                                    json=json,headers=self.header,files=file)
            # print('request_send请求后的数据',resp.json())
            return resp.json()
        except:
            pass #日志


    # add
    def add(self):
        pass

    # delete
    def delete(self):
        pass

    # update
    def update(self,inData):
        return self.request_send(data = inData)

    # query
    def query(self,inData):
        return self.request_send(data = inData)

    # file update
    # userFile = {'变量名':(文件名，文件对象，文件类型)}  上传文件固定格式
    def file_upload(self,fileDir:str):
        fileName = fileDir.split('/')[-1]
        filetype = fileDir.split('.')[-1]
        userFile = {'file':(fileName,open(fileDir,mode='rb',),filetype)}
        return self.request_send(file = userFile)

# 断言
class ApiAssert:
    @classmethod
    def define_api_assert(self,result,condition,exp_result):
        try:
            if condition == '=':
                assert result == exp_result
            elif condition == 'in':
                assert exp_result in result
        except Exception as e:
            raise e