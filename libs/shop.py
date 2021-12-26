# -*- coding:utf-8 -*-
# @Time : 2021/12/9 22:38
# Auther : shenyuming
# @File : shop.py
# @Software : PyCharm

from common.baseApi import BaseApi
from configs.config import PAGELIMT,NAMEPASS
from libs.login import Login
from utils.handle_path import testData_path
import os

class Shop(BaseApi):
    # 添加
    def add(self):
        pass

    # 查询
    # def query(self,inData):
    #     pass

    # 修改
    def update(self,inData,shopID,fileinfo):

        # id不存在的情况和id存在的情况
        if inData['id'] == '不存在的':
            inData['id'] == '0011'
        else:
            inData['id'] = shopID

        # inData['id'] = shopID       #更新ID
        inData['image_path'] = fileinfo     #更新文件
        inData['image'] = f'/file/getImgStream?fileName={fileinfo}'
        return super(Shop,self).update(inData) #调用父类

    # 删除
    def delete(self):
        pass

if __name__ == '__main__':
    #获得token
    token_ = Login().login(NAMEPASS,getToken=True)
    # 创建shop实例
    shop = Shop(token_)
    #列出店铺
    res = shop.query(PAGELIMT)
    print(res)

    # 获取店铺id
    shopid = res['data']['records'][0]['id']
    print('店铺id',shopid)

    # 上传文件
    res2 = shop.file_upload(os.path.join(testData_path,'ls-kv-1-2880.jpg'))
    print(res2)
    # 图片信息
    fileinfo = res2['data']['realFileName']
    print('图片信息',fileinfo)

    ## 更新店铺
    shopdata = {
            "name": "dsddsds",
            "address": "上海市静安区秣陵路303号",
            "id": "3269",
            "Phone": "13176876632",
            "rating": "6.0",
            "recent_order_num":100,
            "category": "快餐便当/简餐",
            "description": "满30减5，满60减8",
            "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
            "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
        }
    res3 = shop().update(shopdata,shopid,fileinfo)
    print(res3)

