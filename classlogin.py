# -*- coding:utf-8 -*-
# @Time : 2021/12/4 15:22
# Auther : shenyuming
# @File : classlogin.py
# @Software : PyCharm

import requests
import json

HOST = 'http://120.55.190.222:7080'

def login(indata):
    url = f'{HOST}/api/mgr/loginReq'
    pyload = indata
    resp = requests.post(url=url,data=pyload,)
    # print('请求头---》',resp.request.headers)
    # print('请求体---》',resp.request.body)
    # print('响应头---》',resp.headers)
    resp.encoding='unicode_escape' ## 设置中文编码格式
    # print('响应体---->',resp.text)
    # print('cookie--->',resp.cookies)
    return resp.cookies


class Lesson:
    def __init__(self,inCookies):
        self.cookie = inCookies

    ## 列出课程
    def list_lesson(self,inData):
        url = f'{HOST}/api/mgr/sq_mgr/?'
        payload = inData
        res = requests.get(url=url,params=payload,cookies=self.cookie)
        res.encoding='unicode_escape'
        return res.text

    ## 添加课程
    def add_lesson(self,inData):
        url = f'{HOST}/api/mgr/sq_mgr/'
        add_data = inData
        res = requests.post(url=url,data=add_data,cookies=self.cookie)
        res.encoding='unicode_escape'
        return res.json()

    ##删除课程
    def dele_lesson(self,inData):
        url = f'{HOST}/api/mgr/sq_mgr/'
        dele_data = inData

        print(dele_data)
        res = requests.delete(url=url,data=dele_data,cookies=self.cookie)
        # res.encoding='unicode_escape'
        print('请求体----',res.request.body)
        print(res)
        return res.json()



if __name__ == '__main__':
    cookies = login({'username':'auto','password':'sdfsdfsdf'})

    # list_data = 'action=list_course&pagenum=1&pagesize=20'
    # res_list = Lesson(cookies).list_lesson(list_data)
    # print(res_list)
    #
    #
    # add_data={
    #     "action":"add_course",
    #     "data": '{"name":"12323","desc":"ceshi","display_idx":1}'
    # }
    # res_add = Lesson(cookies).add_lesson(add_data)
    # print('添加结果---》',res_add)


    inData = {
        'action':'delete_course',
        'id': 2307
    }
    res_dele = Lesson(cookies).dele_lesson(inData)
    print('删除结果----》',res_dele)