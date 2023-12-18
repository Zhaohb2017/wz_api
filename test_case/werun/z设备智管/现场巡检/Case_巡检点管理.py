#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_设备类型, Param_项目管理, Param_空间信息, Param_楼栋信息
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from business.param_config.api_param.werun.设备智管.现场巡检 import Param_巡检标准管理, Param_巡检点管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.巡检管理.Page_巡检标准表管理 import Page巡检标准表管理
from page_object.werun.巡检管理.Page_巡检点表管理 import Page巡检点表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case巡检点管理(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '巡检点管理'
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

    def test_巡检点_01(self):
        """
        单接口: 1/新增巡检点检查
        :return:
        """
        #新增巡检点
        feild_add_xjp = Param_巡检点管理.p_add.get('设备')
        Page巡检点表管理.api_新增巡检点表(self.session,feild_add_xjp,self.header)


    def test_巡检点_02(self):
        """
        单接口: 2/新增巡检点检查
        :return:
        """
        res_data = Page巡检点表管理.api_巡检点通过id查询(self.session,str(123123),self.header)

    def test_巡检点_03(self):
        """
        单接口: 3/通过id删除巡检
        :return:
        """

        Page巡检点表管理.api_巡检点通过id删除(self.session,str(33412),self.header)

    def test_巡检点_04(self):
        """
        单接口: 4/分页查询
        :return:
        """
        #通过分页查询巡检点，并断言新增的参数正确
        feild_page = Param_巡检点管理.p_page.get('名称')
        Page巡检点表管理.api_查询巡检点分页列表(self.session,feild_page,self.header)



    def test_巡检点_05(self):
        """
        单接口: 5/编辑修改
        :return:
        """
        #修改巡检点
        feild_upd = Param_巡检点管理.p_upd.get('01')
        Page巡检点表管理.api_修改巡检点表(self.session,feild_upd,self.header)


