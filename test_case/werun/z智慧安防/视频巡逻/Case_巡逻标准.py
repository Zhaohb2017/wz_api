#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from business.param_config.api_param.werun.智慧安防.视频巡逻 import Param_巡逻标准
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.视频巡逻.Page_巡逻检查项配置表管理 import Page巡逻检查项配置表管理


@ddt.ddt
class Case巡逻标准(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '巡逻标准'
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

    def test_巡逻标准_01(self):
        """
        单接口: 1/新增巡逻检查项
        :return:
        """
        #新增巡逻标准（依赖项目）
        feild_add_xlbz = Param_巡逻标准.p_add.get('一条内容')
        Page巡逻检查项配置表管理.api_新增巡逻检查项配置(self.session,feild_add_xlbz,self.header)

    def test_巡逻标准_02(self):
        """
        单接口: 2/通过id查询
        :return:
        """
        #通过id查询巡逻标准并断言
        Page巡逻检查项配置表管理.api_巡逻检查项配置通过id查询(self.session,str(456),self.header)

    def test_巡逻标准_03(self):
        """
        单接口: 3/通过id删除
        :return:
        """
        #通过id删除
        Page巡逻检查项配置表管理.api_巡逻检查项配置通过id删除(self.session,str(132),self.header)

    def test_巡逻标准_04(self):
        """
        单接口: 4/分页查询
        :return:
        """
        #通过分页查询巡逻标准
        feild_page = Param_巡逻标准.p_page.get('名称')
        Page巡逻检查项配置表管理.api_巡逻检查项配置分页查询(self.session,feild_page,self.header)

    def test_巡逻标准_05(self):
        """
        单接口: 5/启用禁用
        :return:
        """
        # 禁用项目
        feild_off = Param_巡逻标准.p_on_off.get('禁用')
        feild_off['id'] = 231
        Page巡逻检查项配置表管理.api_巡逻检查项配置启用禁用(self.session, feild_off, self.header)

    def test_巡逻标准_06(self):
        """
        单接口: 6/编辑
        :return:
        """
        # 编辑修改巡逻标准
        feild_upd = Param_巡逻标准.p_upd.get('01')
        res_data = Page巡逻检查项配置表管理.api_修改巡逻检查项配置(self.session, feild_upd, self.header)



