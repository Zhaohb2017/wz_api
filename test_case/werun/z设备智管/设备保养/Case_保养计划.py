#!/usr/bin/env python
# encoding: utf-8
import random
import string
import unittest
import uuid
import ddt
import requests
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_设备类型, Param_组织机构, Param_项目管理, Param_角色权限, \
    Param_用户管理, Param_楼栋信息, Param_空间信息
from business.param_config.api_param.werun.物料管理 import Param_物料管理
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from business.param_config.api_param.werun.设备智管.保养管理 import Param_保养计划
from common.Common_Base import create_phone, create_email
from common.M_Crypto import rsa_encrypt
from page_object.werun.上传下载.Page_附件管理 import Page附件管理
from page_object.werun.保养管理.Page_维保计划表管理 import Page维保计划表管理
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.库存管理.Page_物料分类管理 import Page物料分类管理
from page_object.werun.库存管理.Page_物料管理 import Page物料管理
from page_object.werun.用户权限.Page_用户表管理 import Page用户表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.用户权限.Page_组织架构表管理 import Page组织架构表管理
from page_object.werun.用户权限.Page_角色表管理 import Page角色表管理


@ddt.ddt
class Case保养计划(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '保养计划'
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
        if hasattr(self,'u_id'):
            Page用户表管理.api_用户通过id删除(self.session,str(self.u_id),self.header)
        if hasattr(self,'j_id'):
            Page角色表管理.api_角色通过id删除(self.session,str(self.j_id),self.header)
        if hasattr(self, 'z_id'):
            Page组织架构表管理.api_组织架构通过id删除(self.session, str(self.z_id), self.header)
        if hasattr(self,'bp_id'):
            Page维保计划表管理.api_计划表通过id删除(self.session, str(self.bp_id), self.header)
        if hasattr(self, 'wf_id'):
            Page物料分类管理.api_通过id删除物料分类(self.session, str(self.wf_id), self.header)
        if hasattr(self, 'tz_id'):
            Page设备表管理.api_设备通过id删除(self.session, str(self.tz_id), self.header)
        if hasattr(self, 's_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.s_id), self.header)
        if hasattr(self, 'room_id'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session, str(self.room_id), self.header)
        if hasattr(self, 'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass


    def test_保养计划_01(self):
        """
        单接口: 1/新增保养计划
        :return:
        """
        # 新增保养计划
        feild_add_bp = Param_保养计划.p_add.get('半月And内部处理')
        Page维保计划表管理.api_新增维保计划表(self.session, feild_add_bp, self.header)



    def test_保养计划_02(self):
        """
        单接口: 2/通过id查询
        :return:
        """
        #通过id查询保养计划，断言新增的保养计划
        Page维保计划表管理.api_计划表通过id查询(self.session,str(312412),self.header)

    def test_保养计划_03(self):
        """
        单接口: 3/通过id删除
        :return:
        """
        Page维保计划表管理.api_计划表通过id删除(self.session, str(1564654), self.header)

    def test_保养计划_04(self):
        """
        单接口: 4/分页查询
        :return:
        """
        # 通过分页查询，断言查询的内容正常
        feild_page_byjh = Param_保养计划.p_page.get('设备系统')
        feild_page_byjh['body']['facCateId'] =123412
        res_data = Page维保计划表管理.api_查询保养计划列表(self.session, feild_page_byjh, self.header)


    def test_保养计划_05(self):
        """
        单接口: 5/启动保养计划
        :return:
        """
        # 启用保养计划
        feild_on = Param_保养计划.p_on_off.get('启用')
        feild_on['id'] = 1242132
        res_data = Page维保计划表管理.api_修改定时计划状态(self.session, feild_on, self.header)

    def test_保养计划_06(self):
        """
        单接口: 6/编辑保养计划
        :return:
        """
        #编辑修改保养计划
        feild_upd = Param_保养计划.p_upd.get('01')
        res_data = Page维保计划表管理.api_修改维保计划表(self.session,feild_upd,self.header)

