# -*- coding:utf-8 -*-
# @Time : 2021/11/30 22:19
# Auther : shenyuming
# @File : logintest.py
# @Software : PyCharm


import requests
import hashlib
import copy

HOST = 'http://121.41.14.39:8082'
NAME_PSW = {"username":"zo0385","password":"44982"}
def login(inData):
    url = f'{HOST}/account/sLogin'
    inData = copy.copy(inData)  ## 浅拷贝下数据
    inData['password'] = get_MD5_data(inData['password']) ## 密码调用加密
    pyload = inData
    res = requests.post(url=url,data=pyload)
    return res.text


def get_MD5_data(pwd:str):
    """
    :param pwd:
    :return:
    """
    ## 创建md5实例
    md5 = hashlib.md5()
    ## 调用加密方法
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest() ## 返回加密的结果

if __name__ == '__main__':
    res = login(NAME_PSW)
    print(res)