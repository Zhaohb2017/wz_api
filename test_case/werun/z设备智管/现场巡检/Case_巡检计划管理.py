#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid
import logging
import time
import ddt
import requests
from business.param_config.api_param.werun.基础管理 import Param_登录登出
from common.M_Crypto import rsa_encrypt
from page_object.werun.巡检管理.Page_巡检计划表管理 import Page巡检计划表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块



@ddt.ddt
class Case巡检计划管理(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '巡检计划'
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(session=self.session, header={'traceId': str(uuid.uuid4())})
        public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        self.encrypt_pwd = rsa_encrypt(public_key, feild.get('sword'))
        feild['sword'] = self.encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(session=self.session, feilds=feild, header={'traceId': str(uuid.uuid4())})
        self.uuid_str = str(uuid.uuid4())
        self.header = {'traceId': self.uuid_str, 'Authorization': "Bearer " + res_data.get('data').get('token')}


    def tearDown(self):
        self.session.close()




    def test_巡检计划管理列表_查询所有数据_01(self):
        """
        查询巡检计划_列表所有数据,判断是否有数据返回
        :return:
        """
        feild_page = {
         "head": {"current": 1, "size": 10},
         "body": {"startDate": "", "endDate": "", "startCreateDate": "", "endCreateDate": "", "planningOrgId": "",
                  "facCateId": "", "totalCount": 0, "total": 35, "scheduleName": "", "personInChargeUserId": "",
                  "statusStr": ""}}
        res_data = Page巡检计划表管理.api_查询定时任务列表(self.session, feild_page, self.header)
        self.assertEqual(res_data.get('code'),200,"默认查询条件,巡检计划管理列表,请求失败,请查看!")
        self.assertGreater(len(res_data.get('data').get('records')), 0,"默认条件, 巡检计划管理,页面无数据返回!")


    def test_巡检计划管理列表_搜索巡检名称数据_02(self):
        """
        搜索巡检名称: 直梯日常数据和弱电巡检夜班数据,早8生成直梯日常数据，凌晨00:15生成弱电巡检夜班数据
        :return:
        """
        feild_page = {
        "head":{"current":1,"size":10},
        "body":{"startDate":"","endDate":"","startCreateDate":"","endCreateDate":"","planningOrgId":"",
                "facCateId":"","totalCount":0,"total":35,"scheduleName":"直梯日常","personInChargeUserId":"",
                "statusStr":""}}
        res_data = Page巡检计划表管理.api_查询定时任务列表(self.session, feild_page, self.header)
        self.assertEqual(res_data.get('code'),200,"巡检名称:直梯日常搜索条件 ,巡检计划管理列表返回数据失败, 请查看!")

        """
        判断当前系统时间是否大于早上8点15分以后,大于则执行断言部分
        """
        # 获取当前时间戳
        current_time = time.time()
        # 获取当天早上8点15分的时间戳
        today = time.strftime('%Y-%m-%d', time.localtime(current_time))
        morning_8_15 = time.mktime(time.strptime(today + ' 08:15:00', '%Y-%m-%d %H:%M:%S'))
        # 判断当前时间戳是否大于早上8点15分的时间戳
        if current_time > morning_8_15:
            logging.info('当前时间大于8:15,开始进行"直梯日常"详情数据校验')
            self.assertGreater(len(res_data.get('data').get('records')), 0, "搜索巡检名称:直梯日常,列表无数据,请检查!")
            #获取当前的ID查看计划的详情
            schedule_id = res_data.get('data').get('records')[0].get('id')
            schedule_res_data = Page巡检计划表管理.api_巡检计划通过id查询(self.session, str(schedule_id), self.header)
            self.assertGreater(len(schedule_res_data.get('data').get('pointList')), 0, "搜索巡检名称:直梯日常,查看详情发现,巡检计划信息无数据!")
            self.assertGreater(len(schedule_res_data.get('data').get('schedule')), 0, "搜索巡检名称:直梯日常,查看详情发现, 巡检计划信息无数据!")
        else:
            logging.info('当前时间小于早8点15分,故不校验"直梯日常"搜索条件返回数据')

        """
        判断当前系统时间是否大于00:20分,大于则执行 搜索巡检名称条件: 弱电巡检夜班
        """
        # 获取当前时间戳
        current_timestamp = int(time.time())
        # 获取今天0点20分整时间戳
        today_start_timestamp = int(time.mktime(time.strptime(time.strftime("%Y-%m-%d") + " 00:20:00", "%Y-%m-%d %H:%M:%S")))
        if current_timestamp > today_start_timestamp:
            logging.info('当前时间大于00:20, 开始准备校验"弱电巡检夜班"数据')
            feild_weeHours_page = {"head": {"current": 1, "size": 10},
                                   "body": {"startDate": "", "endDate": "", "startCreateDate": "", "endCreateDate": "",
                                            "planningOrgId": "","facCateId": "", "totalCount": 0, "total": 1,
                                            "scheduleName": "弱电巡检夜班","personInChargeUserId": "", "statusStr": ""}}

            weeHours_res_data = Page巡检计划表管理.api_查询定时任务列表(self.session, feild_weeHours_page, self.header)
            self.assertEqual(weeHours_res_data.get('code'), 200,"巡检名称:'弱电巡检夜班' ,查询数据为空,请检查!")
            #获取当前的ID查看计划的详情
            schedule_id_rd = weeHours_res_data.get('data').get('records')[0].get('id')
            schedule_res_data = Page巡检计划表管理.api_巡检计划通过id查询(self.session, str(schedule_id_rd), self.header)
            self.assertGreater(len(schedule_res_data.get('data').get('pointList')), 0,"弱电巡检夜班详情数据,查看失败,请检查!")
            self.assertGreater(len(schedule_res_data.get('data').get('schedule')), 0, "弱电巡检夜班详情数据,查看失败,请检查!")

        else:
            logging.info('当前时间小于00:25, 不做"弱电巡检夜班"详情数据查看!')



















