#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid

import ddt
import requests

from business.foo_lib.modules_db.werun.Db_设备智管 import Db设备智管
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_设备类型, Param_空间信息, Param_空间类型, Param_楼栋信息, \
    Param_项目管理
from business.param_config.api_param.werun.智慧安防.视频巡逻 import Param_巡逻计划, Param_巡逻区域, Param_巡逻标准
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from business.param_config.api_param.werun.设备智管.线上巡检.Param_巡检计划 import p_xmhmc
from common.Common_Base import write_excel_xmhmc
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目花名册管理 import Page项目花名册管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.视频巡逻.Page_巡逻区域配置表管理 import Page巡逻区域配置表管理
from page_object.werun.视频巡逻.Page_巡逻检查项配置表管理 import Page巡逻检查项配置表管理
from page_object.werun.视频巡逻.Page_巡逻计划表管理 import Page巡逻计划表管理


@ddt.ddt
class Case巡逻计划(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '巡逻计划'
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


    def test_巡逻计划_01(self):
        """
        单接口： 1/新增巡逻计划
        :return:
        """
        #新增巡逻计划
        feild_add_xljh = Param_巡逻计划.p_add.get('每天执行')
        res_data = Page巡逻计划表管理.api_新增巡逻计划(self.session,feild_add_xljh,self.header)

    def test_巡逻计划_02(self):
        """
        单接口： 2/id查询
        :return:
        """
        res_data = Page巡逻计划表管理.api_巡逻计划通过id查询(self.session,str(456978),self.header)

    def test_巡逻计划_03(self):
        """
        单接口： 3/id删除
        :return:
        """
        #通过id删除巡逻计划
        res_data = Page巡逻计划表管理.api_巡逻计划通过id删除(self.session,str(465456),self.header)

    def test_巡逻计划_04(self):
        """
        单接口： 4/分页查询
        :return:
        """
        feild_page = Param_巡逻计划.p_page.get('名称')
        res_data = Page巡逻计划表管理.api_巡逻计划分页查询(self.session,feild_page,self.header)

    def test_巡逻计划_05(self):
        """
        单接口： 5/启用禁用
        :return:
        """
        #禁用计划
        feild_off = Param_巡逻计划.p_on_off.get('禁用')
        feild_off['id'] = 312
        res_data = Page巡逻计划表管理.api_巡逻计划启用禁用(self.session,feild_off,self.header)

    def test_巡逻计划_06(self):
        """
        单接口： 6/编辑
        :return:
        """
        #编辑修改巡逻计划
        feild_upd = Param_巡逻计划.p_upd.get('01')
        res_data = Page巡逻计划表管理.api_修改巡逻计划(self.session,feild_upd,self.header)
