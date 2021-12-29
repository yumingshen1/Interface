# -*- coding:utf-8 -*-
# @Time : 2021/12/29 21:58
# Auther : shenyuming
# @File : yam1.py
# @Software : PyCharm

import yaml
def get_data_yaml(fidir):
    with open(fidir,encoding='utf-8') as f:
        res = yaml.safe_load(f.read())
        print(res)

## 多类型数据 / 分段写的yaml
def get_data_yaml2(didir):
    with open(didir,encoding='utf-8') as f:
        res2 = yaml.load_all(f,Loader=yaml.FullLoader)
        for i in res2:
            print(i)

if __name__ == '__main__':
    get_data_yaml2('./1.yaml')