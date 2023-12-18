#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_空间类型, Param_项目管理
from business.param_config.api_param.werun.设备智管.线上巡检 import Param_线上巡检标准
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.线上巡检.Page_环境巡检标准管理 import Page环境巡检标准管理
from page_object.werun.线上巡检.Page_设备巡检标准管理 import Page设备巡检标准管理




@ddt.ddt
class Case巡检标准(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '巡检标准'
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
        if hasattr(self,'xu_id'):
            Page设备巡检标准管理.api_通过id删除设备巡检标准(self.session, str(self.xu_id), self.header)
        #通过id删除新增空间类型
        if hasattr(self,'t_id'):
            Page空间类型表管理.api_空间类型通过id删除(self.session,str(self.t_id),self.header)
        #删除新增项目
        if hasattr(self,'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.session.close()
        pass

    def test_巡检标准_01(self):
        """
        单接口: 1/ 新增设备标准
        :return:
        """
        feild_add_xsxj = Param_线上巡检标准.p_add.get('通用标准')
        feild_add_xsxj['remark'] = 'remark'+str(uuid.uuid4())
        Page设备巡检标准管理.api_新增设备巡检标准(self.session,feild_add_xsxj,self.header)

    def test_巡检标准_02(self):
        """
        单接口: 2/分页查询
        :return:
        """
        #分页查询标准，验证新增的标准存在（设备类型）
        feild_page_xu = Param_线上巡检标准.p_page.get('设备类型')
        Page设备巡检标准管理.api_设备巡检标准分页查询(self.session,feild_page_xu,self.header)

    def test_巡检标准_03(self):
        """
        单接口: 3/启用禁用接口
        :return:
        """
        feild_off = Param_线上巡检标准.p_on_off.get('禁用')
        feild_off['id'] = 456
        Page设备巡检标准管理.api_启用禁用设备巡检标准(self.session,feild_off,self.header)

    def test_巡检标准_04(self):
        """
        单接口: 4/通过id查询接口
        :return:
        """
        res_data = Page设备巡检标准管理.api_通过id查询设备巡检标准(self.session, str(124213), self.header)


    def test_巡检标准_05(self):
        """
        单接口: 5/通过id删除接口
        :return:
        """
        Page设备巡检标准管理.api_通过id删除设备巡检标准(self.session,str(45612),self.header)

    def test_巡检标准_06(self):
        """
        单接口: 6/修改设备巡检标准
        :return:
        """

        #修改巡检标准
        feild_upd_xsxj = Param_线上巡检标准.p_upd.get('01')
        feild_upd_xsxj['id'] = 41231
        res_data = Page设备巡检标准管理.api_修改设备巡检标准(self.session,feild_upd_xsxj,self.header)



