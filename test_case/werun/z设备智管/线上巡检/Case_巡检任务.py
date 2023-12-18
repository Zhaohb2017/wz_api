#!/usr/bin/env python
# encoding: utf-8
import time
import unittest
import uuid

import ddt
import requests

from business.foo_lib.modules_biz.werun.Biz_xxl_job import BizXxlJob
from business.foo_lib.modules_db.werun.Db_设备智管 import Db设备智管
from business.param_config.api_param.werun.告警中心 import Param_告警记录
from business.param_config.api_param.werun.告警中心.告警配置 import Param_消防告警配置, Param_安全告警配置, Param_设备告警配置
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_楼栋信息, Param_空间类型, Param_空间信息, \
    Param_设备类型
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from business.param_config.api_param.werun.设备智管.线上巡检 import Param_线上巡检标准, Param_巡检机房, Param_巡检计划, Param_巡检任务
from business.param_config.api_param.werun.设备智管.线上巡检.Param_巡检计划 import p_xmhmc
from common.Common_Base import write_excel_xmhmc
from common.M_Crypto import rsa_encrypt
from page_object.werun.上传下载.Page_附件管理 import Page附件管理
from page_object.werun.告警中心.Page_告警记录管理 import Page告警记录管理
from page_object.werun.告警中心.Page_安防告警配置管理 import Page安防告警配置管理
from page_object.werun.告警中心.Page_设备告警配置管理 import Page设备告警配置管理
from page_object.werun.告警中心.Page_黑名单布控管理 import Page黑名单布控管理
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目花名册管理 import Page项目花名册管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.线上巡检.Page_巡检任务管理 import Page巡检任务管理
from page_object.werun.线上巡检.Page_巡检机房管理 import Page巡检机房管理
from page_object.werun.线上巡检.Page_巡检计划管理 import Page巡检计划管理
from page_object.werun.线上巡检.Page_环境巡检标准管理 import Page环境巡检标准管理


@ddt.ddt
class Case巡检任务(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.session_xxl = requests.Session()
        self.case_name = '巡检任务'
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session)
        self.public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        self.encrypt_pwd = rsa_encrypt(self.public_key, feild.get('sword'))
        feild['sword'] = self.encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(self.session, feild, {})
        self.uuid_str = str(uuid.uuid4())
        self.header = {'traceId': self.uuid_str, 'Authorization': "Bearer " + res_data.get('data').get('token')}
        pass

    def tearDown(self):
        self.session.close()
        pass

    def test_巡检任务_01(self):
        """
        单接口: 1/统计任务数量
        :return:
        """
        field_done = {}
        Page巡检任务管理.api_巡检任务根据状态统计任务数量(self.session,field_done,self.header)

    def test_巡检任务_02(self):
        """
        单接口: 2/默认查询分页
        :return:
        """
        field = {"head":{"current":1,"size":10},"body":{"taskStatus":2}}
        Page巡检任务管理.api_分页查询巡检任务(self.session,field,self.header)

    def test_巡检任务_03(self):
        """
        单接口: 3/导出
        :return:
        """
        field = {"page": 1, "rows": 10,"total":0,"taskStatus":2}
        Page巡检任务管理.api_导出巡检任务表(self.session, field, self.header)

    def test_巡检任务_04(self):
        """
        单接口: 4/生成报告-左侧所有建筑空间接口
        :return:
        """
        field = {}
        Page巡检任务管理.api_获取所有建筑房间(self.session, field, self.header)

    def test_巡检任务_05(self):
        """
        单接口: 5/生成报告-中间寻机房列表数据
        :return:
        """
        field = {}
        Page巡检任务管理.api_楼层的寻机房列表(self.session, field, self.header)

    def test_巡检任务_06(self):
        """
        单接口: 6/生成报告-生成报告
        :return:
        """
        field = {"date":"2023-03-20","roomIds":[109,255,604,605,1481,1545]}
        Page巡检任务管理.api_巡检任务生成报告(self.session, field, self.header)


