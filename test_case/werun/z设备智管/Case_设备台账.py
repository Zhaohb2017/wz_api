#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_设备类型, Param_项目管理, Param_空间信息, Param_楼栋信息
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case设备台账(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '设备台账'
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



    def test_设备台账_01(self):
        """
        单接口: 1/新增设备
        :return:
        """

        #新增设备台账
        feild_add_tz = Param_设备台账.p_add.get('使用中')
        res_data = Page设备表管理.api_新增设备表(self.session,feild_add_tz,self.header)


    def test_设备台账_02(self):
        """
        单接口: 2/通过id删除设备
        :return:
        """
        #通过id删除台账
        Page设备表管理.api_设备通过id删除(self.session,str(13213),self.header)

    def test_设备台账_03(self):
        """
        单接口: 3/通过id查询
        :return:
        """
        Page设备表管理.api_设备通过id查询(self.session, str(66565), self.header)

    def test_设备台账_04(self):
        """
        单接口: 4/分页查询
        :return:
        """
        #分页查询新增台账参数正确
        feild_page = Param_设备台账.p_page.get('默认查询')
        Page设备表管理.api_设备分页查询(self.session,feild_page,self.header)

    def test_设备台账_05(self):
        """
        单接口: 5/修改台账
        :return:
        """
        #修改设备台账
        feild_upd = Param_设备台账.p_upd.get('使用中')
        Page设备表管理.api_修改设备表(self.session,feild_upd,self.header)

    def test_设备台账_06(self):
        """
        单接口: 6/左侧设备类型所有数据
        :return:
        """
        Page设备表管理.api_左侧设备类型树状图(self.session,self.header)

    def test_设备台账_07(self):
        """
        单接口: 7/设备模板下载
        :return:
        """
        Page设备表管理.api_设备模板下载(self.session,self.header)

    def test_设备台账_08(self):
        """
        单接口: 8/设备模板导入
        :return:
        """
        # 上传

        file_data = Param_设备台账.feild_upload_hmc.get('01')
        Page设备表管理.api_设备模板导入(self.session,file_data,self.header)


