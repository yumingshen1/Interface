# -*- coding:utf-8 -*-
# @Time : 2021/12/12 09:40
# Auther : shenyuming
# @File : handle_excel.py
# @Software : PyCharm

'''
    获取Excel用例
    目标：
    测试的模块 sheetName 、
    可以传递对应接口 caseNmae 、
    提供扩展使以后可以获取任意列 *args 、
    可以挑选测试用例 单个，连续，复合 ，  runCase 、
    函数调用减少参数传递-->选择配置文件、
'''

import xlrd,os
from utils.handle_path import testData_path

def get_excel_data(excelDir,sheetName,caseName,*args,runCase=['all']) -> list:
    # 定义list存放数据
    resList = []

    # 打开一个Excel，formatting_info 表示保持原样
    workbook = xlrd.open_workbook(excelDir,formatting_info=True)

    # 获得所有的表名
    sheets = workbook.sheet_names()
    # print(sheets)

    # 获得操作的子表
    worksheet = workbook.sheet_by_name(sheetName)

    # 获得一列数据,第一列数据
    # print(worksheet.col_values(0))

    # 获得某个单元格数据
    # print(worksheet.cell(0,0).value)


    # 存放输入的列名的下标 *args
    colIndexList = []
    for i in args:
        # 获得Excel第一行数据的下标
        row_index = worksheet.row_values(0).index(i)
        colIndexList.append(row_index)
    print(colIndexList)

    # 用例筛选 runCase
    runList = []
    if 'all' in runCase:
        runList = worksheet.col_values(0)
    else:
        for i in runCase:
            if '-' in i:
                start,end = i.split('-')
                for one in range(int(start),int(end)+1):
                    runList.append(caseName+f'{one:0>3}')
            else:
                runList.append(caseName+f'{i:0>3}')

    ## 行编号初始值
    rowIndex = 0
    # 循环第一列数据值长度
    for one in worksheet.col_values(0):
        # 判断输入的 caseName 有没有在列中 , 并判断是否在用例筛选中
        if caseName in one and one in runList:
            # 存放每一列数据
            getcolData = []
            # 遍历列编号
            for num in colIndexList:
                tem = worksheet.cell(rowIndex,num).value  # 一行的多列数据
                getcolData.append(tem)        # 每组数据加入list
                print('===',getcolData)
            # respData = worksheet.cell(rowIndex,11).value
            resList.append(list(getcolData))
        rowIndex+=1

    #打印存入list数据
    for i in resList:
        print(i)



if __name__ == '__main__':
    excelpath = os.path.join(testData_path,'test_devolop.xls')
    get_excel_data(excelpath,'登录模块','Login','URL','标题','请求参数','响应预期结果',runCase=['1','5-6','all'])