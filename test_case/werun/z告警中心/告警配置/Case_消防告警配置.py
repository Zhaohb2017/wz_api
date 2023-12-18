#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid
import ddt
import requests
from business.param_config.api_param.werun.告警中心.告警配置 import Param_消防告警配置
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.告警中心.Page_安防告警配置管理 import Page安防告警配置管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case消防告警配置(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '消防告警配置'
        #获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session)
        self.public_key = res_data.get('data').get('RSA')
        #密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        self.encrypt_pwd = rsa_encrypt(self.public_key,feild.get('sword'))
        feild['sword'] = self.encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(self.session,feild,{})
        self.header = {'traceId': str(uuid.uuid4()),'Authorization':"Bearer "+res_data.get('data').get('token')}
        pass

    def tearDown(self):
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        if hasattr(self, 'xf_id'):
            Page安防告警配置管理.api_安防告警配置通过id删除(self.session, str(self.xf_id), self.header)
        self.session.close()
        pass

    def test_消防告警配置_01(self):
        """
        单接口: 1/新增
        :return:
        """
        feild_add_xfgj = Param_消防告警配置.p_add.get('新增消防告警')
        Page安防告警配置管理.api_新增安防告警配置(self.session,feild_add_xfgj,self.header)

    def test_消防告警配置_02(self):
        """
        单接口: 2/分页查询
        :return:
        """
        feild_page = Param_消防告警配置.p_page.get('01')
        Page安防告警配置管理.api_分页查询消防告警配置(self.session, feild_page, self.header)


    def test_消防告警配置_03(self):
        """
        单接口: 3/通过id查看
        :return:
        """
        #通过id查询，并断言新增参数正确
        Page安防告警配置管理.api_安防告警配置通过id查询(self.session,str(12315),self.header)

    def test_消防告警配置_04(self):
        """
        单接口: 4/禁用
        :return:
        """
        feild_on = Param_消防告警配置.p_on_off.get('启用')
        feild_on['id'] = 135644
        Page安防告警配置管理.api_安防告警配置启用禁用(self.session, feild_on, self.header)


