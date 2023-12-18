import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_楼栋信息, Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case楼栋信息(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '楼栋信息'
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session)
        self.public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        self.encrypt_pwd = rsa_encrypt(self.public_key, feild.get('sword'))
        feild['sword'] = self.encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(self.session, feild, {})
        self.header = {'traceId': str(uuid.uuid4()), 'Authorization': "Bearer " + res_data.get('data').get('token')}
        pass

    def tearDown(self):
        if hasattr(self,'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self,'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.session.close()
        pass



    def test_楼栋信息_01(self):
        """
        单接口: 1/楼栋信息- 分页查询
        :return:
        """
        feild_search = Param_楼栋信息.p_page.get("楼栋")
        Page区域或楼栋表管理.api_楼栋信息分页查询(self.session,feild_search,self.header)


    def test_楼栋信息_02(self):
        """
        单接口: 2/通过id删除楼栋信息
        :return:
        """
        Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(2134), self.header)


    def test_楼栋信息_03(self):
        """
        单接口:3/新增楼栋信息
        :return:
        """
        #新增楼栋
        feild_add_ld = Param_楼栋信息.p_add.get("公共区域")
        feild_add_ld['buildingName'] = "楼栋"+str(uuid.uuid1())
        Page区域或楼栋表管理.api_新增区域或楼栋表(self.session,feild_add_ld,self.header)


    def test_楼栋信息_04(self):
        """
        单接口:4/编辑楼栋信息
        :return:
        """
        feild_upd_ld = Param_楼栋信息.p_upd.get("名称1")
        Page区域或楼栋表管理.api_修改区域或楼栋表(self.session,feild_upd_ld,self.header)


