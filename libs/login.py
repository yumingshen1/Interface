# -*- coding:utf-8 -*-
# @Time : 2021/12/6 22:27
# Auther : shenyuming
# @File : login.py
# @Software : PyCharm

from common.baseApi import BaseApi
from configs.config import NAMEPASS
import copy
from utils.handle_data import get_MD5_data
'''
    登录业务层
'''
class Login(BaseApi):
    # 登录的token默认false不返回，传入true返回token
    def login(self,inData,getToken=False):
        inData = copy.copy(inData)
        inData['password'] = get_MD5_data(inData['password'])
        respData = self.request_send(data=inData)

        ##获得token
        if getToken:
            return respData['data']['token']
        else:# 获得相应数据
            return respData
        # print('login函数--',resp.text)

    # 退出登录
    def logout(self):
        self.request_send()


if __name__ == '__main__':
    print(Login().login(NAMEPASS,getToken=True))