#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from business.param_config.api_param.werun.智慧安防 import Param_实时监控
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_监控配置表管理 import Page监控配置表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case安防态势(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
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
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass

    def test_实时监控_01(self):
        """
        单接口: 1/集合查询
        :return:
        """
        #实时监控列表查询
        Page监控配置表管理.api_监控配置集合查询(self.session,self.header)

    def test_实时监控_02(self):
        """
        单接口: 2/分页查询
        :return:
        """
        feild_page_camera = Param_实时监控.p_page_camera.get('01')
        Page监控配置表管理.api_监控设备分页查询(self.session,feild_page_camera,self.header)
