#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid
import ddt
import requests
from business.foo_lib.modules_db.werun.Db_设备智管 import Db设备智管
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_设备类型, Param_空间信息, Param_空间类型, Param_楼栋信息, \
    Param_项目管理
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from business.param_config.api_param.werun.设备智管.模式And联动 import Param_联动配置
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.模式联动规则配置.Page_联动模式管理 import Page联动模式管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case联动配置(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '联动配置'
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
        self.session.close()
        pass


    def test_联动配置_01(self):
        """
        单接口: 1/ 新增联动配置
        :return:
        """
        #新增联动配置(依赖设备)
        feild_add_ldpz = Param_联动配置.p_add.get('每周重复')
        Page联动模式管理.api_新增联动模式(self.session,feild_add_ldpz,self.header)


    def test_联动配置_02(self):
        """
        单接口: 2/ 通过id查询
        :return:
        """
        #通过id查询联动配置，断言新增参数
        Page联动模式管理.api_联动模式通过id查询(self.session,str(1231),self.header)


    def test_联动配置_03(self):
        """
        单接口: 3/ 分页查询
        :return:
        """
        #通过分页查询联动配置，断言新增参数
        feild_page = Param_联动配置.p_page.get('名称')
        Page联动模式管理.api_联动模式分页查询(self.session,feild_page,self.header)


    def test_联动配置_04(self):
        """
        单接口: 4/ id删除
        :return:
        """
        #通过id删除联动配置
        Page联动模式管理.api_联动模式通过id删除(self.session,str(12364),self.header)


    def test_联动配置_05(self):
        """
        单接口: 5/ 启用禁用
        :return:
        """
        #禁用联动配置
        feild_off = Param_联动配置.p_on_off.get('禁用')
        feild_off['id'] = 3123
        Page联动模式管理.api_联动模式启用禁用(self.session,feild_off,self.header)



    def test_联动配置_06(self):
        """
        单接口: 6/ 编辑
        :return:
        """
        feild_upd_ldpz = Param_联动配置.p_upd.get('02')
        Page联动模式管理.api_修改联动模式(self.session,feild_upd_ldpz,self.header)
