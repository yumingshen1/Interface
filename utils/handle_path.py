# -*- coding:utf-8 -*-
# @Time : 2021/12/12 09:54
# Auther : shenyuming
# @File : handle_path.py
# @Software : PyCharm
'''
    获取项目绝对路径
'''

import os

# print(__file__)     ## 当前文件路径
 # os.path.dirname  查找上级目录

# 工程路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置路径
config_path = os.path.join(project_path,'configs')

# 测试数据
testData_path = os.path.join(project_path,'data')

# 测试报告
report_path = os.path.join(project_path,r'outFiles/report/temp')
# print(report_path)
# 日志路径
log_path = os.path.join(project_path,r'outFiles/logs')