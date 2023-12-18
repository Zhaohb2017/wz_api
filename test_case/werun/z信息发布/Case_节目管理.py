import copy
import time
import unittest
import uuid

import ddt
import requests
import datetime


from business.param_config.api_param.werun.信息发布 import Param_素材管理, Param_节目管理
from page_object.werun.信息发布 import Page_节目管理
from page_object.werun.信息发布.Page_素材管理 import Page素材管理
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块

@ddt.ddt
class Case节目管理(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '节目管理'
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
        self.session.close()
        pass

    def test_节目管理_01(self):
        """
        单接口: 1.新增节目
        :return:
        """
        #新增节目
        feild_add_program = copy.deepcopy(Param_节目管理.p_add_program.get('图片'))
        feild_add_m = feild_add_program.get('materials')
        f_m = feild_add_m[0]
        f_m['materialId'] = "2134"
        feild_add_m[0] = f_m
        feild_add_program['programName'] = self.case_name +str(uuid.uuid4())
        Page_节目管理.Page节目管理.api_新增节目(self.session,feild_add_program,self.header)


    def test_节目管理_02(self):
        """
        单接口:2.修改节目
        :return:
        """
        feild_add_program = copy.deepcopy(Param_节目管理.p_add_program.get('图片'))
        feild_add_m = feild_add_program.get('materials')
        f_m = feild_add_m[0]
        f_m['materialId'] = "2134"
        feild_add_m[0] = f_m
        feild_add_program['programName'] = self.case_name + str(uuid.uuid4())
        Page_节目管理.Page节目管理.api_修改节目(self.session,feild_add_program,self.header)


    def test_节目管理_03(self):
        """
        单接口: 3.节目集合查询
        :return:
        """
        feild_search = copy.deepcopy(Param_节目管理.p_page.get('默认查询'))
        Page_节目管理.Page节目管理.api_节目集合查询(self.session,feild_search,self.header)


    def test_节目管理_04(self):
        """
        单接口: 4.通过id查询
        :return:
        """
        # 删除节目
        Page_节目管理.Page节目管理.api_通过id查询节目(self.session, str(1), self.header)


    def test_节目管理_05(self):
        """
        单接口:5.通过id删除
        :return:
        """
        Page_节目管理.Page节目管理.api_通过id删除节目(self.session, str(3), self.header)




