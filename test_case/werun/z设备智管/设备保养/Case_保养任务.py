#!/usr/bin/env python
# encoding: utf-8
import random
import string
import time
import unittest
import uuid
import ddt
import requests
from business.foo_lib.modules_biz.werun.Biz_xxl_job import BizXxlJob
from business.foo_lib.modules_db.werun.Db_设备智管 import Db设备智管
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_设备类型, Param_组织机构, Param_项目管理, Param_角色权限, \
    Param_用户管理, Param_楼栋信息, Param_空间信息
from business.param_config.api_param.werun.物料管理 import Param_物料管理
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from business.param_config.api_param.werun.设备智管.保养管理 import Param_保养计划, Param_保养标准, Param_保养任务
from common.Common_Base import create_phone, create_email
from common.M_Crypto import rsa_encrypt
from page_object.werun.上传下载.Page_附件管理 import Page附件管理
from page_object.werun.保养管理.Page_维保任务表管理 import Page维保任务表管理
from page_object.werun.保养管理.Page_维保标准表管理 import Page维保标准表管理
from page_object.werun.保养管理.Page_维保计划表管理 import Page维保计划表管理
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.库存管理.Page_物料分类管理 import Page物料分类管理
from page_object.werun.库存管理.Page_物料管理 import Page物料管理
from page_object.werun.用户权限.Page_用户表管理 import Page用户表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.用户权限.Page_组织架构表管理 import Page组织架构表管理
from page_object.werun.用户权限.Page_角色表管理 import Page角色表管理


@ddt.ddt
class Case保养任务(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.session_xxl = requests.Session()
        self.session_by = requests.Session()
        self.case_name = '保养任务'
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session)
        self.public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        self.encrypt_pwd = rsa_encrypt(self.public_key, feild.get('sword'))
        feild['sword'] = self.encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(self.session, feild, {})
        self.uuid_str = str(uuid.uuid4())
        self.header = {'traceId': self.uuid_str, 'Authorization': "Bearer " + res_data.get('data').get('token')}
        res_data = Page用户表管理.api_获取用户信息(self.session, self.header)
        self.user_info = res_data.get('data')
        pass

    def tearDown(self):
        self.session.close()
        self.session_xxl.close()
        self.session_by.close()
        pass


    def test_保养任务_01(self):
        """
        单接口: 1/ 分页查询
        :return:
        """
        #分页查询保养任务
        feild_page_rw = Param_保养任务.p_page.get('设备系统')
        feild_page_rw['body']['facCateId'] = 4564654
        Page维保任务表管理.api_维保任务表分页查询(self.session,feild_page_rw,self.header)


    def test_保养任务_02(self):
        """
        单接口: 2/ 通过id查询
        :return:
        """
        Page维保任务表管理.api_维保任务表通过id查询(self.session,str(123645),self.header)










