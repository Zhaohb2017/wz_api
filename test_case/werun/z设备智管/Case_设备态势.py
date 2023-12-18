#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid
import ddt
import requests
from business.param_config.api_param.werun.基础管理 import Param_登录登出
from business.param_config.api_param.werun.设备智管 import Param_空间时态
from common.M_Crypto import rsa_encrypt
from page_object.werun.用户权限.Page_用户表管理 import Page用户表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.设备智管.Page_空间时态 import Page空间时态



@ddt.ddt
class Case设备态势(unittest.TestCase):
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
        res_data = Page用户表管理.api_获取用户信息(self.session, self.header)
        self.user_info = res_data.get('data')
        pass

    def tearDown(self):
        self.session.close()


    def test_该页面没有数据关联接口(self):
        pass