#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid
import ddt
import requests
from business.param_config.api_param.werun.告警中心 import Param_应急预案
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.告警中心.Page_应急预案 import Page应急预案
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case应急预案(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '应急预案'
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
        if hasattr(self, 'yjya_id'):
            Page应急预案.api_删除应急预案(self.session, str(self.yjya_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass

    def test_应急预案_01(self):
        """
        单接口：1/新增
        :return:
        """
        feild_add = Param_应急预案.p_add.get("一级预案")
        res_data = Page应急预案.api_新增应急预案(self.session,feild_add,self.header)



    def test_应急预案_02(self):
        """
        单接口：2/通过id搜索
        :return:
        """
        #     #通过id查询，并断言
        Page应急预案.api_通过id查询应急预案(self.session, str(23212), self.header)


    def test_应急预案_03(self):
        """
        单接口：3/通过id删除
        :return:
        """
        #通过id删除配置
        res_data = Page应急预案.api_删除应急预案(self.session,str(46564),self.header)

    def test_应急预案_04(self):
        """
        单接口：4/分页查询
        :return:
        """
        #通过分页查询，并断言新增参数
        feild_page = Param_应急预案.p_page.get('预案等级')
        res_data = Page应急预案.api_分页查询应急预案(self.session,feild_page,self.header)

    def test_应急预案_05(self):
        """
        单接口：5/应急方案启用状态
        :return:
        """
        feild_page = Param_应急预案.p_on_off.get('启用')
        Page应急预案.api_分页查询应急预案(self.session,feild_page,self.header)



    def test_应急预案_06(self):
        """
        单接口：5/应急方案禁用状态
        :return:
        """
        feild_page = Param_应急预案.p_on_off.get('禁用')
        Page应急预案.api_分页查询应急预案(self.session,feild_page,self.header)




