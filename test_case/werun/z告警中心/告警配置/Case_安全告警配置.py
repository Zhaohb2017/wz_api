#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid
import ddt
import requests
from business.param_config.api_param.werun.告警中心.告警配置 import Param_安全告警配置
from business.param_config.api_param.werun.基础管理 import Param_登录登出
from common.M_Crypto import rsa_encrypt
from page_object.werun.告警中心.Page_安全告警配置 import Page安全告警配置
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case安全告警配置(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '安全告警配置'
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
        pass


    def test_安全告警配置_01(self):
        """
        单接口: 1/ 分页默认查询条件
        :return:
        """
        # 新增安全告警配置
        feild_page = Param_安全告警配置.p_page.get('默认查询')
        Page安全告警配置.api_分页查询黑名单告警(self.session,feild_page,self.header)


    def test_安全告警配置_02(self):
        """
        单接口: 2/ 新增布控人员
        :return:
        """
        feild_page = Param_安全告警配置.p_upload.get('01')
        res_data = Page安全告警配置.api_上传图片(self.session,feild_page,self.header)
        fid = res_data.get('data').get('fid')
        add_people = Param_安全告警配置.p_add.get('布控人员')
        add_people['faceUrl'] = fid
        Page安全告警配置.api_新增布控人员(self.session, add_people, self.header)


    def test_安全告警配置_03(self):
        """
        单接口: 3/ 通过id删除
        :return:
        """
        Page安全告警配置.api_删除安全告警配置(self.session, str(4564), self.header)


    def test_安全告警配置_04(self):
        """
        单接口: 4/ 通过id查看
        :return:
        """
        Page安全告警配置.api_布控通过id查询(self.session, str(4564), self.header)

    def test_安全告警配置_05(self):
        """
        单接口: 5/ 布控人员启用禁用
        :return:
        """
        feilds = Param_安全告警配置.p_on_off.get('启用')
        Page安全告警配置.api_黑名单布控启用禁用(self.session, feilds, self.header)

