#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid
import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from business.param_config.api_param.werun.基础管理.排班管理 import Param_班次管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.排班管理.Page_班次管理 import Page班次管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case班次管理(unittest.TestCase):
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
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.session.close()
        pass


    def test_班次管理_01(self):
        """
        单接口: 1/新增班次
        :return:
        """
        #新建班次
        feild_add = Param_班次管理.p_add.get('一日一班').copy()
        res_data = Page班次管理.api_新增或更新班次以及时间安排(self.session,feild_add,self.header)


    def test_班次管理_02(self):
        """
        单接口: 2/通过id查看
        :return:
        """
        #通过id查询班次
        Page班次管理.api_通过班次id查询班次时间安排(self.session,str(665),self.header)


    def test_班次管理_03(self):
        """
        单接口: 3/通过id删除
        :return:
        """
        #通过id删除班次
        Page班次管理.api_通过id删除班次(self.session,str(66987),self.header)


    def test_班次管理_04(self):
        """
        单接口: 4/首页分页查询班次
        :return:
        """
        #通过分页查询班次，断言参数正常
        feild_page = Param_班次管理.p_page.get('默认查询')
        res_data = Page班次管理.api_分页查询班次信息(self.session,feild_page,self.header)
        self.assertEqual(res_data.get('code'),200)

    def test_班次管理_05(self):
        """
        单接口: 5/重置功能
        :return:
        """
        feild_page = Param_班次管理.p_page.get('重置')
        res_data = Page班次管理.api_分页查询班次信息(self.session,feild_page,self.header)
        self.assertEqual(res_data.get('code'),200)

    def test_班次管理_06(self):
        """
        单接口: 6/查询班次集合数据
        :return:
        """
        feild_page = {}
        Page班次管理.api_获取班次名称集合(self.session,feild_page,self.header)


