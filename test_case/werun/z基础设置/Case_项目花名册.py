import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_项目花名册
from common.Common_Base import write_excel, create_phone
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_项目花名册管理 import Page项目花名册管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case项目花名册(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '项目花名册'
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
        if hasattr(self,'xmhmc_id'):
            Page项目花名册管理.api_项目花名册通过id删除(self.session, str(self.xmhmc_id), self.header)
        if hasattr(self,'xmhmc_id1'):
            Page项目花名册管理.api_项目花名册通过id删除(self.session, str(self.xmhmc_id1), self.header)
        if hasattr(self,'p_id'):
            Page项目表管理.api_项目通过id删除(self.session,str(self.p_id),self.header)
        self.session.close()
        pass

    def test_项目花名册_01(self):
        """
        单接口:1/项目花名册下载模板功能正常
        :return:
        """
        #下载模版
        res_data = Page项目花名册管理.api_下载花名册导入模版(self.session,self.header)
        self.assertEqual(res_data.ok,True)


    def test_项目花名册_02(self):
        """
        单接口: 2/上传花名册模板
        :return:
        """
        feild_upload_data = Param_项目花名册.p_upload_data.get('单条数据').copy()
        feild_upload_data[0][0] = "测试"
        feild_upload_data[0][1] = '哈尔滨市'
        feild_upload_data[0][2] = '南岗区'
        feild_upload_data[0][3] = '花名'+str(uuid.uuid4())
        feild_upload_data[0][4] = create_phone()
        feild_upload_data[0][5] = '0'
        write_excel(Param_项目花名册.xlsx.get('01'), feild_upload_data)
        feild_upload_hmc = Param_项目花名册.feild_upload_hmc.get("01")
        Page项目花名册管理.api_导入项目花名册(self.session, feild_upload_hmc, self.header)


    def test_项目花名册_03(self):
        """
        单接口:3/通过id删除花名册
        :return:
        """
        #通过id删除花名册
        Page项目花名册管理.api_项目花名册通过id删除(self.session,str(6564),self.header)



    def test_项目花名册_04(self):
        """
        单接口:4/ 项目花名册-分页查询
        :return:
        """
        #分页查询，验证删除正常
        feild_page = Param_项目花名册.p_page.get('员工姓名')
        res_data = Page项目花名册管理.api_项目花名册分页查询(self.session, feild_page, self.header)



