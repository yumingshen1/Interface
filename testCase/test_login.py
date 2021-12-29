# -*- coding:utf-8 -*-
# @Time : 2021/12/11 15:04
# Auther : shenyuming
# @File : test_login.py
# @Software : PyCharm


import pytest,allure,os
from libs.login import Login
from utils.handle_excel import get_excel_data
from utils.handle_path import report_path,testData_path
from common.baseApi import ApiAssert
from utils.handle_yml import get_yaml_caseData
@allure.epic('项目A')
@allure.feature('登录模块')
class TestLogin:
    # yaml 执行
    @pytest.mark.parametrize('title,inData,expData',get_yaml_caseData(os.path.join(testData_path,'loginCase.yaml')))
    # excel执行
    # @pytest.mark.parametrize('title,inData,expData',get_excel_data('登录模块','Login','标题','请求参数','响应预期结果'))
    @allure.title('{title}')
    def test_login(self,title,inData,expData):
        res = Login().login(inData)
        print('res---',res)
        #断言
        ApiAssert.define_api_assert(res['msg'],'=',expData['msg'])

if __name__ == '__main__':
    pytest.main(['test_login.py','-s','--alluredir',f'{report_path}','--clean-alluredir'])
    # os.system(f'allure serve {report_path}')