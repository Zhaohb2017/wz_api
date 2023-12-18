import unittest
import uuid
import ddt
import requests
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_项目花名册
from common.Common_Base import write_excel, create_phone
from common.M_Crypto import rsa_encrypt
from business.param_config.api_param.werun.基础管理 import Param_项目日志
from page_object.werun.基础管理.Page_项目日志 import Page项目日志
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case项目日志(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session)
        public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        encrypt_pwd = rsa_encrypt(public_key, feild.get('sword'))
        feild['sword'] = encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(self.session, feild, {})
        self.header = {'traceId': str(uuid.uuid4()), 'Authorization': "Bearer " + res_data.get('data').get('token')}
        pass

    def tearDown(self):
        pass

    def test_项目日志_01(self):
        """
        单接口:1/ 分页查询
        :return:
        """
        #分页查询
        feilds = Param_项目日志.page_search.get('默认查询')
        res_data = Page项目日志.api_项目日志分页查询(self.session,feilds,self.header)
        self.assertEqual(res_data.get('code'),200)







