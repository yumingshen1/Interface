# -*- coding:utf-8 -*-
# @Time : 2021/12/20 20:45
# Auther : shenyuming
# @File : test_shop.py
# @Software : PyCharm
import pytest,allure,os
from utils.handle_excel import get_excel_data
from utils.handle_path import testData_path,report_path
from common.baseApi import ApiAssert
from libs.login import Login
from configs.config import PAGELIMT,NAMEPASS

# 调用无返回值的fixture
# @pytest.mark.usefixtures('sym')
no_ready=pytest.mark.skip(reason = '无条件跳过')
ifskip=pytest.mark.skipif(not Login().login(NAMEPASS)['data']['token'],reason='登录结果没有token跳过')
@allure.epic('项目A')
@allure.feature('商品模块')
@pytest.mark.shop #定制mark用例
class TestShop:
    @allure.story('列出商品')
    @allure.title('{title}')
    @pytest.mark.parametrize('title,inBody,expData', get_excel_data('我的商铺', 'listshopping', '标题', '请求参数', '响应预期结果'))
    @pytest.mark.shop_list
    # 列出店铺 ， shop_init有返回值的fixture
    def test_shop_list(self,title,inBody,expData,shop_init):
        res = shop_init.query(inBody)
        print('res--->',res)
        #  - 断言
        ApiAssert.define_api_assert(res["code"],'=',expData["code"])

    # 更新店铺
    @allure.story('修改商品')
    @allure.title('{title}')
    @pytest.mark.parametrize('title,inData,expData', get_excel_data('我的商铺', 'updateshopping', '标题', '请求参数', '响应预期结果'))
    @pytest.mark.shop_update
    # @pytest.mark.skip
    def test_shop_update(self,shop_init,title,inData,expData):
        with allure.step('1-用户登录+创建店铺'):
            pass
        with allure.step('2-获取店铺id'):
            res = shop_init.query({"page": "1", "limit": "10"})
            shopid = res['data']['records'][0]['id']
        with allure.step('3-上传文件'):
            res2 = shop_init.file_upload(os.path.join(testData_path,'ls-kv-1-2880.jpg'))
            fileinfo = res2['data']['realFileName']
        with allure.step('4-更新店铺'):
            res3 = shop_init.update(inData,shopid,fileinfo)
        with allure.step('5-断言'):
            ApiAssert.define_api_assert(res3['code'], '=', expData['code'])


if __name__ == '__main__':
    pytest.main(['test_shop.py','-s','-m','shop_list or shop_update','--alluredir',f'{report_path}','--clean-alluredir'])
    os.system(f'allure serve {report_path}')