import random
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_组织机构, Param_角色权限, Param_用户管理
from business.param_config.api_param.werun.基础管理.排班管理 import Param_班次管理, Param_排班计划
from business.param_config.api_param.werun.工单管理 import Param_工单配置
from common.Common_Base import create_phone, create_email
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.工单管理.Page_工单配置表管理 import Page工单配置表管理
from page_object.werun.排班管理.Page_排班计划管理 import Page排班计划管理
from page_object.werun.排班管理.Page_班次管理 import Page班次管理
from page_object.werun.用户权限.Page_用户表管理 import Page用户表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.用户权限.Page_组织架构表管理 import Page组织架构表管理
from page_object.werun.用户权限.Page_角色表管理 import Page角色表管理


@ddt.ddt
class Case工单配置(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '工单配置'
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

    def test_工单配置_01(self):
        """
        验证修改工单配置功能,查询工单配置断言修改成功（人工派单）
        :return:
        """
        # 查询工单配置
        res_data = Page工单配置表管理.api_工单配置通过id查询(self.session, '1', self.header)
        self.assertEqual(res_data.get('code'),200)


