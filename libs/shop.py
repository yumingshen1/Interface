# -*- coding:utf-8 -*-
# @Time : 2021/12/9 22:38
# Auther : shenyuming
# @File : shop.py
# @Software : PyCharm

from common.baseApi import BaseApi
from configs.config import PAGELIMT

class Shop(BaseApi):
    def list_shop(self,inData):
       resp =  self.request_send(params=inData)
       print(resp)

       return resp


if __name__ == '__main__':
    Shop().list_shop(PAGELIMT)