#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_设备类型, Param_项目管理, Param_空间类型
from business.param_config.api_param.werun.设备智管.现场巡检 import Param_巡检标准管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.巡检管理.Page_巡检标准表管理 import Page巡检标准表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case巡检标准管理(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '巡检标准管理'
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

    def test_巡检标准_01(self):
        """
        单接口: 1/新增巡检标准
        :return:
        """
        feild_add_bz = Param_巡检标准管理.p_add.get('仪表类')
        Page巡检标准表管理.api_新增巡检标准表(self.session,feild_add_bz,self.header)

    def test_巡检标准_02(self):
        """
        单接口: 2/通过id查询
        :return:
        """
        Page巡检标准表管理.api_巡检标准通过id查询(self.session,str(4654),self.header)

    def test_巡检标准_03(self):
        """
        单接口: 3/通过id删除
        :return:
        """
        Page巡检标准表管理.api_巡检标准通过id删除(self.session,str(3123),self.header)

    def test_巡检标准_04(self):
        """
        单接口: 4/通过id删除
        :return:
        """
        # 修改设备巡检标准
        feild_upd = Param_巡检标准管理.p_upd.get('01')
        Page巡检标准表管理.api_修改巡检标准表(self.session, feild_upd, self.header)

    def test_巡检标准_05(self):
        """
        单接口: 5/下载导入模板
        :return:
        """
        Page巡检标准表管理.api_巡检标准管理下载导入模板(self.session,self.header)

    def test_巡检标准_06(self):
        """
        单接口: 6/导入模板
        :return:
        """

        feild_upload_hmc = Param_巡检标准管理.feild_upload_hmc.get("01")
        Page巡检标准表管理.api_巡检标准管理上传模板(self.session, feild_upload_hmc, self.header)






