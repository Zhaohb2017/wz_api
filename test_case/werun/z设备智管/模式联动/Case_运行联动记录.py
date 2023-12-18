#!/usr/bin/env python
# encoding: utf-8
#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid
import ddt
import requests
from business.param_config.api_param.werun.基础管理 import Param_登录登出
from business.param_config.api_param.werun.设备智管.模式And联动 import Param_运行模式
from page_object.werun.模式联动规则配置.Page_运动联动记录 import Page运行联动记录
from common.M_Crypto import rsa_encrypt
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case运行联动记录(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '运行模式'
        #获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session)
        self.public_key = res_data.get('data').get('RSA')
        #密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        self.encrypt_pwd = rsa_encrypt(self.public_key,feild.get('sword'))
        feild['sword'] = self.encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(self.session,feild,{})
        self.header = {'traceId': str(uuid.uuid4()),'Authorization':"Bearer "+res_data.get('data').get('token')}


    def tearDown(self):
        self.session.close()


    def test_运行模式_01(self):
        """
        单接口: 1/新增运行模式
        :return:
        """
        feild = {"head": {"total": 0, "current": 1, "size": 10}, "body": {"type": 1}}
        Page运行联动记录.api_运动联动模式分页查询(self.session,feild,self.header)


    def test_运行模式_02(self):
        """
        单接口: 2/ID查询
        :return:
        """
        Page运行联动记录.api_运动联动记录ID查询(self.session,str(13213),self.header)

