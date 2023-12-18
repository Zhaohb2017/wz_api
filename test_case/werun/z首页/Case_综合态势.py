#!/usr/bin/env python
# encoding: utf-8
#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid
import ddt
import requests
from business.param_config.api_param.werun.基础管理 import Param_登录登出
from common.M_Crypto import rsa_encrypt
from page_object.werun.用户权限.Page_用户表管理 import Page用户表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.能耗管理.Page_能耗分析 import Page能耗分析



@ddt.ddt
class Case综合态势(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '综合态势'
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(session=self.session, header={'traceId': str(uuid.uuid4())})
        public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        self.encrypt_pwd = rsa_encrypt(public_key, feild.get('sword'))
        feild['sword'] = self.encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(session= self.session, feilds= feild, header={'traceId': str(uuid.uuid4())})
        self.uuid_str = str(uuid.uuid4())
        self.header = {'traceId': self.uuid_str, 'Authorization': "Bearer " + res_data.get('data').get('token')}


    def tearDown(self):
        self.session.close()


    def test_查询能耗模块图表接口_01(self):
        """
        首页-综合态势-查询能耗图表接口是否报错(按年搜索)
        :return:
        """

        pagedata = {"cycle": "4"}
        res_data = Page能耗分析.api_查询能耗图表接口( pagedata, self.header)
        self.assertEqual(res_data.get('code'),200,"首页综合态势,能耗图表接口报错,请查看!")
        self.assertGreater(len(res_data.get('data').get('dataset').get('source')), 0,"首页综合态势,能耗图表接口报错,页面无数据返回!")



