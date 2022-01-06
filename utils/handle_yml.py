# -*- coding:utf-8 -*-
# @Time : 2021/12/7 22:38
# Auther : shenyuming
# @File : handle_yml.py
# @Software : PyCharm

'''
    读取apiConfig配置文件信息
'''

import yaml
def get_yaml_data(fileDir):
    with open(fileDir,encoding='utf-8') as f:
        return yaml.safe_load(f.read())

## 用例
def get_yaml_caseData(fileDir):
    resList = []
    res = get_yaml_data(fileDir)
    for i in res:
        resList.append((i['casename'],i['data'],i['expDate']))
    return resList

if __name__ == '__main__':
    # res = get_yaml_data('../configs/apiConfig.yaml')
    res = get_yaml_caseData('../data/loginCase.yaml')
    print(res)