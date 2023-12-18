#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_设备类型, Param_项目管理
from business.param_config.api_param.werun.设备智管.保养管理 import Param_保养标准
from common.M_Crypto import rsa_encrypt
from page_object.werun.保养管理.Page_维保标准表管理 import Page维保标准表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case保养标准(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '保养标准'
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
        if hasattr(self,'by_id'):
            Page维保标准表管理.api_维保标准通过id删除(self.session,str(self.by_id),self.header)
        if hasattr(self, 's_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.s_id), self.header)
        if hasattr(self, 'fs_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.fs_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.session.close()
        pass


    def test_保养标准_01(self):
        """
        单接口: 1/新增保养标准
        :return:
        """
        #新增保养标准
        feild_add_by = Param_保养标准.p_add.get("半月周期")
        Page维保标准表管理.api_新增维保标准表(self.session,feild_add_by,self.header)

    def test_保养标准_02(self):
        """
        单接口: 2/id查询
        :return:
        """
        #通过id查询保养标准
        Page维保标准表管理.api_维保标准通过id查询(self.session,str(231412),self.header)

    def test_保养标准_03(self):
        """
        单接口: 3/id删除
        :return:
        """
        Page维保标准表管理.api_维保标准通过id删除(self.session,str(312312),self.header)

    def test_保养标准_04(self):
        """
        单接口: 4/分页查询
        :return:
        """
        #通过名称分页查询，并断言新增项目存在
        feild_page = Param_保养标准.p_page.get("重置")
        Page维保标准表管理.api_维保标准分页列表(self.session,feild_page,self.header)

    def test_保养标准_05(self):
        """
        单接口: 5/编辑保养标准
        :return:
        """
        #编辑修改保养标准
        feild_upd_by = Param_保养标准.p_upd.get('01')
        Page维保标准表管理.api_修改维保标准表(self.session,feild_upd_by,self.header)

    def test_保养标准_从企业保养手册同步_06(self):
        """
        单接口: 6/企业保养手册数据拉取
        :return:
        """
        feild = {"head":{"total":0,"current":1,"size":10},"body":{"maintenanceStandardType":1}}
        Page维保标准表管理.api_分页查询企业保养手册(self.session,feild,self.header)


