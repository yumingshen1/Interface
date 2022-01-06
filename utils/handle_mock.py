# -*- coding:utf-8 -*-
# @Time : 2022/1/4 22:05
# Auther : shenyuming
# @File : handle_mock.py
# @Software : PyCharm

import requests,json,time,threading

'''
    运行条件：
    启动本地的 .bat文件
    .bat文件有启动moco.jar ，定义端口，读取配置文件 的命令，
    并有配置文件，配置文件中是定义的请求数据和相应数据
'''
Host = 'http://127.0.0.1:9999'

def test1():
    res = requests.get(url = f'{Host}/xintian_1')
    print(res.text)

def test2():
    payload = {
			"key1":"abc",
			"key2":"123"
		  }
    res2 = requests.get(url=f'{Host}/sym',params=payload)
    print(res2.text)

def test3():
    pyload = {
				"key1":"value1",
				"key2":"value2"
			}
    res3 = requests.get(url=f'{Host}/sq3',json=pyload)
    print(res3.text)


def test4(tive=2,timeout=30):
    """
    :param tive:  频率
    :param timeout:  超时
    :return:
    """
    pyload = {
        "key1": "abc"
    }
    start = time.time()
    end = start+timeout
    count = 1
    while time.time() < end:
        res4 = requests.get(url=f'{Host}/sq21',data=pyload)
        if res4.text:
            print(f'第{count}次查询到，跳出循环',res4.text)
            break
        else:
            print(f'第{count}次查询，没有查到继续。。')
        time.sleep(tive)
        count += 1
    print('操作结束！！！')



if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()


    '''
        异步接口
        
        target:你把哪一个函数当成子线程，直接传递函数名
        args：你传递的函数需要使用的变量 ---元组类型
    '''
    start = time.time()

    # # 线程创建
    # T1 = threading.Thread(target=test4,args=())
    # # 主线程停止或异常，子线程强制结束
    # T1.setDaemon(True)
    # # 启动线程
    # T1.start()

    # 创建多个线程
    listThred = []
    for i in range(10):
        listThred.append(threading.Thread(target=test4,args=()))
    for i in listThred:
        b = i
    b.setDaemon(True)
    b.start()

    for one in range(20):
        time.sleep(1)
        print(f'{one}执行其他操作')

    end = time.time()
    print('整个时间：',end-start)