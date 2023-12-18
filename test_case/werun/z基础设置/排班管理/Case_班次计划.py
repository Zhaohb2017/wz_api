#!/usr/bin/env python
# encoding: utf-8
import datetime
import unittest
import uuid
import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_角色权限, Param_组织机构, Param_用户管理, Param_项目管理
from business.param_config.api_param.werun.基础管理.排班管理 import Param_班次管理, Param_排班计划
from common.Common_Base import create_phone, create_email
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.排班管理.Page_排班计划管理 import Page排班计划管理
from page_object.werun.排班管理.Page_班次管理 import Page班次管理
from page_object.werun.用户权限.Page_用户表管理 import Page用户表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.用户权限.Page_组织架构表管理 import Page组织架构表管理
from page_object.werun.用户权限.Page_角色表管理 import Page角色表管理


@ddt.ddt
class Case排班计划(unittest.TestCase):
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
        if hasattr(self,'b_plan_id'):
            Page排班计划管理.api_通过id删除班次计划(self.session,str(self.b_plan_id),self.header)
        if hasattr(self, 'b_id'):
            Page班次管理.api_通过id删除班次(self.session, str(self.b_id), self.header)
        if hasattr(self, 'u_id'):
            Page用户表管理.api_用户通过id删除(self.session, str(self.u_id), self.header)
        if hasattr(self, 'z_id'):
            Page组织架构表管理.api_组织架构通过id删除(self.session, str(self.z_id), self.header)
        if hasattr(self, 'j_id'):
            Page角色表管理.api_角色通过id删除(self.session, str(self.j_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass


    def test_排班计划_01(self):
        """
        单接口：1/新增接口
        :return:
        """
        feild_add_plan = Param_排班计划.p_add.get('一人').copy()
        Page排班计划管理.api_添加或更新班次及明细信息(self.session,feild_add_plan,self.header)



    def test_排班计划_02(self):
        """
        单接口：2/查询排班计划
        :return:
        """
        feild_search = Param_排班计划.p_search.get('一人')
        feild_search['jspId'] = '123412'
        res_data = Page排班计划管理.api_排班计划明细查询(self.session,feild_search,self.header)

    def test_排班计划_03(self):
        """
        单接口：3/查询排班计划
        :return:
        """
        Page排班计划管理.api_通过id删除班次计划(self.session,str(456456),self.header)


    def test_排班计划_04(self):
        """
        单接口：4/分页查询排班计划
        :return:
        """
        # 分页查询排班计划，断言新增的参数正确
        feild_page = Param_排班计划.p_page.get('重置').copy()
        res_data = Page排班计划管理.api_排班计划分页查询(self.session, feild_page, self.header)

    def test_排班计划_05(self):
        """
        单接口：5/新增排班计划拉取排班部门接口数据
        :return:
        """
        Page排班计划管理.api_获取组织架构的树形结构(self.session, self.header)




    def test_排班计划_05(self):
        pass
