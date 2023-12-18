#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid

import ddt
import requests

from business.foo_lib.modules_db.werun.Db_设备智管 import Db设备智管
from business.param_config.api_param.werun.告警中心.告警配置 import Param_设备告警配置
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_设备类型, Param_空间信息, Param_楼栋信息
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from common.M_Crypto import rsa_encrypt
from page_object.werun.告警中心.Page_设备告警配置管理 import Page设备告警配置管理
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case设备告警配置(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '设备告警配置'
        #获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session)
        self.public_key = res_data.get('data').get('RSA')
        #密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        self.encrypt_pwd = rsa_encrypt(self.public_key,feild.get('sword'))
        feild['sword'] = self.encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(self.session,feild,{})
        self.header = {'traceId': str(uuid.uuid4()),'Authorization':"Bearer "+res_data.get('data').get('token')}
        pass

    def tearDown(self):
        self.session.close()

    def test_设备告警配置_01(self):
        """
        单接口: 1/新增设备告警信息
        :return:
        """
        feild_add_sbgj = Param_设备告警配置.p_add.get('自定义设备类型')
        Page设备告警配置管理.api_新增设备告警配置(self.session, feild_add_sbgj, self.header)


    def test_设备告警配置_02(self):
        """
        单接口: 2/通过id查询
        :return:
        """
        Page设备告警配置管理.api_设备告警配置通过id查询(self.session, str(2131231), self.header)

    def test_设备告警配置_03(self):
        """
        单接口: 3/通过id删除
        :return:
        """
        Page设备告警配置管理.api_设备告警配置通过id删除(self.session,str(456),self.header)


    def test_设备告警配置_04(self):
        """
        单接口: 4/分页查询
        :return:
        """
        feild_page = Param_设备告警配置.p_page.get('默认查询')
        Page设备告警配置管理.api_设备告警配置分页查询(self.session,feild_page,self.header)

    def test_设备告警配置_05(self):
        """
        单接口: 5/启用禁用接口
        :return:
        """
        #禁用设备告警配置
        feild_off = Param_设备告警配置.p_on_off.get('禁用')
        feild_off['id'] = 45646
        Page设备告警配置管理.api_设备告警配置启用禁用(self.session,feild_off,self.header)


