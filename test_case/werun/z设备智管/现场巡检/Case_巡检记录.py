#!/usr/bin/env python
# encoding: utf-8
import time
import unittest
import uuid

import ddt
import requests

from business.foo_lib.modules_biz.werun.Biz_xxl_job import BizXxlJob
from business.foo_lib.modules_db.werun.Db_设备智管 import Db设备智管
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_设备类型, Param_项目管理, Param_空间信息, Param_楼栋信息, \
    Param_组织机构, Param_角色权限, Param_用户管理
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from business.param_config.api_param.werun.设备智管.现场巡检 import Param_巡检标准管理, Param_巡检点管理, Param_巡检计划, Param_巡检记录
from common.Common_Base import create_phone, create_email, date_change
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.巡检管理.Page_巡检任务表管理 import Page巡检任务表管理
from page_object.werun.巡检管理.Page_巡检标准表管理 import Page巡检标准表管理
from page_object.werun.巡检管理.Page_巡检点表管理 import Page巡检点表管理
from page_object.werun.巡检管理.Page_巡检计划表管理 import Page巡检计划表管理
from page_object.werun.排班管理.Page_排班计划管理 import Page排班计划管理
from page_object.werun.排班管理.Page_班次管理 import Page班次管理
from page_object.werun.用户权限.Page_用户表管理 import Page用户表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.用户权限.Page_组织架构表管理 import Page组织架构表管理
from page_object.werun.用户权限.Page_角色表管理 import Page角色表管理
from page_object.werun.设备智管.Page_巡检记录 import Page巡检记录

@ddt.ddt
class Case巡检记录(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.session_xxl = requests.Session()
        self.case_name = '巡检记录'
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session)
        public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        self.encrypt_pwd = rsa_encrypt(public_key, feild.get('sword'))
        feild['sword'] = self.encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(self.session, feild, {})
        self.current_user_id = int(res_data.get('msg').split('：')[1])
        self.uuid_str = str(uuid.uuid4())
        self.header = {'traceId': self.uuid_str, 'Authorization': "Bearer " + res_data.get('data').get('token')}
        pass

    def tearDown(self):
        self.session.close()
        pass

    def test_巡检记录_01(self):
        """
        单接口: 1/巡检任务
        :return:
        """
        Page巡检记录.api_获取今日巡检任务状态数量(self.session, self.header)

    def test_巡检记录_02(self):
        """
        单接口: 2/巡检任务执行记录
        :return:
        """
        feilds = {"excuteDate":"2023-03-20"}
        Page巡检记录.api_查询巡检任务执行记录列表(self.session, feilds,self.header)

    def test_巡检记录_03(self):
        """
        单接口: 3/编辑查询选中的巡检任务记录
        :return:
        """
        Page巡检任务表管理.api_编辑查询选中的巡检任务记录(self.session,{'scheduleEqtLogIds':str(312312)},self.header)

    def test_巡检记录_04(self):
        """
        单接口: 4/批量更新查询选中的巡检任务记录
        :return:
        """
        feild_upd_rec = Param_巡检记录.p_upd.get('01')
        res_data = Page巡检任务表管理.api_批量更新查询选中的巡检任务记录(self.session, feild_upd_rec, self.header)


    def test_巡检记录_05(self):
        """
        单接口: 5/获取打印巡检记录
        :return:
        """
        feild_record_detail = Param_巡检记录.p_record_detail.get('01')
        res_data = Page巡检任务表管理.api_获取打印巡检记录(self.session, feild_record_detail, self.header)


