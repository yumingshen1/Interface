# -*- coding:utf-8 -*-
# @Time : 2021/12/20 21:09
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm

import pytest
from libs.login import Login
from libs.shop import Shop
from configs.config import NAMEPASS

@pytest.fixture(scope='session',autouse=True)
def start_running():
    print('开始执行自动化')

    yield
    print('自动化结束后的运行')


@pytest.fixture(scope='class')
def sym():
    print('无返回值') # 调用--> pytest.mark.usefixture(sym)


'''
    登录
'''
@pytest.fixture(scope='session')
def login_init():
    _token = Login().login(NAMEPASS,getToken=True)
    yield _token       ## 调用--> 直接在需要的函数中传入该函数名
    print('优质')

'''
    店铺实例
'''
@pytest.fixture(scope='class')
def shop_init(login_init):
    shopObject = Shop(login_init)  #调用token
    print('店铺实例----')
    yield shopObject