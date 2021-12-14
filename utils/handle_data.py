# -*- coding:utf-8 -*-
# @Time : 2021/12/8 22:47
# Auther : shenyuming
# @File : handle_data.py
# @Software : PyCharm


import hashlib

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
