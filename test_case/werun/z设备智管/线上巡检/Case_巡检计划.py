#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_楼栋信息, Param_空间类型, Param_空间信息
from business.param_config.api_param.werun.设备智管.线上巡检 import Param_巡检计划, Param_线上巡检标准, Param_巡检机房
from business.param_config.api_param.werun.设备智管.线上巡检.Param_巡检计划 import p_xmhmc
from common.Common_Base import write_excel_xmhmc
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_项目花名册管理 import Page项目花名册管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.线上巡检.Page_巡检机房管理 import Page巡检机房管理
from page_object.werun.线上巡检.Page_巡检计划管理 import Page巡检计划管理
from page_object.werun.线上巡检.Page_环境巡检标准管理 import Page环境巡检标准管理


@ddt.ddt
class Case线上巡检计划(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '线上巡检计划'
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
        pass

    def test_巡检计划_01(self):
        """
        单接口: 1/ 新增巡检计划
        :return:
        """
        feild_add_xjjh = Param_巡检计划.p_add.get('自动巡检')
        Page巡检计划管理.api_新增巡检计划(self.session,feild_add_xjjh,self.header)


    def test_巡检计划_02(self):
        """
        单接口: 2/ 分页查询
        :return:
        """
        feild_page = Param_巡检计划.p_page.get('计划名称')
        Page巡检计划管理.api_巡检计划分页查询(self.session,feild_page,self.header)


    def test_巡检计划_03(self):
        """
        单接口: 3/ 启用禁用接口
        :return:
        """
        feild_off = Param_巡检计划.p_on_off.get('禁用')
        feild_off['id'] = 123
        res_data = Page巡检计划管理.api_启用禁用巡检计划(self.session,feild_off,self.header)


    def test_巡检计划_04(self):
        """
        单接口: 4/ 编辑接口
        :return:
        """
        #编辑修改巡检计划
        feild_upd_xjjh = Param_巡检计划.p_upd.get('01')
        Page巡检计划管理.api_修改巡检计划(self.session,feild_upd_xjjh,self.header)

    def test_巡检计划_05(self):
        """
        单接口: 5/ 通过id删除巡检计划
        :return:
        """
        Page巡检计划管理.api_通过id删除巡检计划(self.session,str(123),self.header)

    def test_巡检计划_06(self):
        """
        单接口: 6/ 通过id查看巡检计划
        :return:
        """
        Page巡检计划管理.api_通过id查询巡检计划(self.session,str(456),self.header)





