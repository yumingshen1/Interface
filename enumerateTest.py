# -*- coding:utf-8 -*-
# @Time : 2021/12/4 16:51
# Auther : shenyuming
# @File : enumerateTest.py
# @Software : PyCharm
'''
enumerate 用法
numerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
'''

i = 0
example_dictsep = [1, 2, 3]

example_dict = {1:'a', 2:'b', 3:'c', 4:'d'}
for i ,ele in enumerate(example_dict.items()):
    print(i,ele)

list1 = ["这","是","一个","测试"]
for i in range(len(list1)):
    print(i,list1[i])
print('----')
for i,ene in enumerate(list1,1):
    print(i,ene)