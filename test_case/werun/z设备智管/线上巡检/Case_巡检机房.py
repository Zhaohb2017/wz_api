#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_楼栋信息, Param_空间类型, Param_空间信息
from business.param_config.api_param.werun.设备智管.线上巡检 import Param_巡检机房, Param_线上巡检标准
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.线上巡检.Page_巡检机房管理 import Page巡检机房管理
from page_object.werun.线上巡检.Page_环境巡检标准管理 import Page环境巡检标准管理


@ddt.ddt
class Case巡检机房(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '巡检机房'
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
        if hasattr(self, 'sbxj_id'):
            Page环境巡检标准管理.api_通过id删除环境巡检标准(self.session, str(self.sbxj_id), self.header)
        if hasattr(self, 'room_id'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session, str(self.room_id), self.header)
        if hasattr(self, 'space_type_id'):
            Page空间类型表管理.api_空间类型通过id删除(self.session, str(self.space_type_id), self.header)
        if hasattr(self, 'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass





    def test_巡检机房_01(self):
        """
        单接口: 1/新增巡检机房
        :return:
        """
        #新增巡检机房(依赖房间、环境巡检标准)
        feild_add = Param_巡检机房.p_add.get('01')
        Page巡检机房管理.api_新增巡检机房(self.session,feild_add,self.header)

    def test_巡检机房_02(self):
        """
        单接口: 2/分页查询
        :return:
        """
        #通过分页查询巡检机房并断言
        feild_page = Param_巡检机房.p_page.get('机房名称')
        Page巡检机房管理.api_巡检机房分页查询(self.session,feild_page,self.header)

    def test_巡检机房_03(self):
        """
        单接口: 3/通过id删除巡检机房
        :return:
        """
        Page巡检机房管理.api_通过id删除巡检机房(self.session,str(4564),self.header)

    def test_巡检机房_04(self):
        """
        单接口: 4/通过id查询巡检机房
        :return:
        """
        Page巡检机房管理.api_通过id查询巡检机房(self.session, str(45646), self.header)

    def test_巡检机房_05(self):
        """
        单接口: 5/启用禁用
        :return:
        """
        feild_off = Param_巡检机房.p_on_off.get('禁用')
        feild_off['id'] = 4564
        Page巡检机房管理.api_启用禁用巡检机房(self.session,feild_off,self.header)

    def test_巡检机房_06(self):
        """
        单接口: 6/编辑巡检机房
        :return:
        """
        #修改巡检机房
        feild_upd = Param_巡检机房.p_upd.get('01')
        Page巡检机房管理.api_修改巡检机房(self.session,feild_upd,self.header)

    def test_巡检机房_07(self):
        """
        单接口: 7/重置功能
        :return:
        """
        #通过分页查询巡检机房并断言
        feild_page = Param_巡检机房.p_page.get('重置')
        Page巡检机房管理.api_巡检机房分页查询(self.session,feild_page,self.header)

