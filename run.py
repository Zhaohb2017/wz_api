#!/usr/bin/ python
# encoding: utf-8
# 自动化项目的统一入口.  只会运行这个文件
import argparse
import unittest
import HTMLReport
from business.param_config.biz_param import Biz_Param
from test_suite import Complex_Main
import requests
import datetime
import time
from common.sqlalchemy import SQLMain
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 招商
bot_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=78630faa-92ad-42e7-934b-ca637351e42e'  # 发送消息接口地址
# 测试群
# bot_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c987370b-dfc7-4391-9e40-fc2211209523'  # 发送消息接口地址
title = '金茂火炬'


def wx_send_links(report_file_name, state):
    """
    :param report_file_name: 报告文件
    :param state: 报告状态
    :return:
    """
    # report_ip = "121.15.134.37"
    report_ip = "5285-119-145-28-245.ngrok-free.app"
    # 定义图片和描述
    if state:
        image_url = "https://ts1.cn.mm.bing.net/th/id/R-C.b1e7a67f89fb5f6d715a46fa7e618a4d?rik=sc6EWT2ZcdOufw&riu=http%3a%2f%2fbpic.588ku.com%2felement_pic%2f17%2f02%2f11%2f302aa49ce3d59eb9cce751f5f3326a81.jpg&ehk=XEHr2hhSCA%2bf%2fvTr137NF99KFe4QX9ufcs%2fbhTMfjV0%3d&risl=&pid=ImgRaw&r=0"
        description = "大吉大利,接口无报错"
    else:
        image_url = "https://img95.699pic.com/element/40155/1408.png_300.png!/fw/431/clip/0x300a0a0"
        description = "接口报错了!"

    # 构造要发送的消息体
    message = {
        'msgtype': 'news',
        'news': {
            'articles': [
                {
                    'title': f'{title}测试报告',
                    'description': description,
                    'url': f"http://{report_ip}/html/{report_file_name}.html",
                    'picurl': image_url
                }
            ]
        }
    }
    session = requests.Session()
    session.trust_env = False
    response = session.post(
        url=bot_url, json=message,
        verify=False)  # post请求消息
    print(response.text)
    session.close()


def wx_send_msg():
    # 消息内容
    pengfei = "17665250505"
    jiafeng = "18664980290"
    message = {
        "msgtype": "text",
        "text": {
            "content": f"{title}接口报错,请马上查看!",
            # "mentioned_list":["@all"],
            "mentioned_mobile_list": [jiafeng, pengfei]
        }
    }

    session = requests.Session()
    session.trust_env = False
    response = session.post(
        url=bot_url, json=message,
        verify=False)  # post请求消息
    print(response.text)
    session.close()


def Check_execution():
    """
    不输出报告,返回检查执行结果
    :return:
    """
    totalSuite = unittest.TestSuite()  # 总套件
    totalSuite.addTests(Complex_Main.return_suite())
    # 执行测试用例
    result = unittest.TestResult()
    totalSuite.run(result)
    print("执行的测试用例数: %s" % result.testsRun)  # 执行的测试用例数
    print("失败的测试用例结果列表: %s" % result.failures)  # 失败的测试用例结果列表
    print("错误的测试用例结果列表: %s" % result.errors)  # 错误的测试用例结果列表
    print("是否全部测试用例都执行成功: %s" % result.wasSuccessful())  # 是否全部测试用例都执行成功
    return result.wasSuccessful()


def start_run():
    # 读取命令行参数改写文件
    parser = argparse.ArgumentParser(description="重写配置文件")
    parser.add_argument("-islocal", dest="name", choices={"True", "False"}, help="是否为本地浏览器")
    # 获取命令行输入的参数
    args = parser.parse_args()
    if args.name == "False":  # 如果接受到了浏览器名字
        Biz_Param.is_local_browser = False
        # 根据输入的参数值,修改配置文件
    #     write_config("browser.ini","browser","name",args.name)
    # #改写文件end
    report_html = "JinMao%s" % datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # .format(datetime.datetime.now().strftime('"%Y%m%d"')
    online = "/var/lib/jenkins/workspace/flask/report/templates"
    local = "templates/2023"
    # 测试报告路径设置
    output_path = online
    # 获取当前时间戳
    # current_time = time.time()
    # # 获取当天早上8点15分的时间戳,返回发送执行测试报告
    # today = time.strftime('%Y-%m-%d', time.localtime(current_time))
    # morning_8_15 = time.mktime(time.strptime(today + ' 08:15:00', '%Y-%m-%d %H:%M:%S'))

    current_time = time.time()
    current_hour = int(time.strftime("%H", time.localtime(current_time)))
    current_minute = int(time.strftime("%M", time.localtime(current_time)))

    # 这里使用总套件,加载所有的子套件

    totalSuite = unittest.TestSuite()  # 总套件
    totalSuite.addTests(Complex_Main.return_suite())
    description = """
监测账号: 见群公告
"""
    report = HTMLReport.TestRunner(
        title=f"{title}监测服务接口",
        description=description,
        report_file_name=report_html,
        output_path=output_path,
        lang="en",
        # thread_count=1,  # 并行线程数
        # thread_start_wait=1,
        # tries=0
    ).run(totalSuite)
    print("执行的测试用例数: %s" % report.testsRun)  # 执行的测试用例数
    print("失败的测试用例结果列表: %s" % report.failures)  # 失败的测试用例结果列表
    print("错误的测试用例结果列表: %s" % report.errors)  # 错误的测试用例结果列表
    print("是否全部测试用例都执行成功: %s" % report.wasSuccessful())  # 是否全部测试用例都执行成功
    if report.wasSuccessful():
        # 判断当前时间在8点15分~16分之间
        if current_hour == 8 and current_minute >= 15 and current_minute <= 16:
            wx_send_links(report_file_name=report_html, state=True)
        elif current_hour == 18 and current_minute >= 30 and current_minute <= 31:
            wx_send_links(report_file_name=report_html, state=True)

    else:
        if len(report.failures) != 0 or len(report.errors) != 0:
            wx_send_links(report_file_name=report_html, state=False)
            wx_send_msg()
            # SQLMain().sql_main(title)


if __name__ == '__main__':
    start_run()
