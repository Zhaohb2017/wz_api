#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid
import ddt
import requests
from business.foo_lib.modules_db.werun.Db_设备智管 import Db设备智管
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_设备类型, Param_空间类型, Param_空间信息, \
    Param_楼栋信息
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from business.param_config.api_param.werun.设备智管.模式And联动 import Param_运行模式
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.模式联动规则配置.Page_运行模式管理 import Page运行模式管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case运行模式(unittest.TestCase):
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
        feild_add_yxms = Param_运行模式.p_add.get('每天重复')
        feild_add_yxms['operationInfoList'][0]['facCategoryId'] = 1231
        feild_add_yxms['operationInfoList'][0]['facOperationActionList'][0]['actionValue'] = 'value'+str(uuid.uuid4()).split('-')[0]
        feild_add_yxms['modeName'] = '模式名'+str(uuid.uuid4())
        feild_add_yxms['remark'] = '备注'+ str(uuid.uuid4())
        res_data = Page运行模式管理.api_新增运行模式(self.session,feild_add_yxms,self.header)

    def test_运行模式_02(self):
        """
        单接口: 2/通过id查询
        :return:
        """
        Page运行模式管理.api_运行模式通过id查询(self.session,str(312412),self.header)


    def test_运行模式_03(self):
        """
        单接口: 3/通过id删除
        :return:
        """
        #通过id删除
        res_data = Page运行模式管理.api_运行模式通过id删除(self.session,str(12124),self.header)


    def test_运行模式_04(self):
        """
        单接口: 4/分页查询
        :return:
        """
        #通过分页查询，并断言
        feild_page_yxms = Param_运行模式.p_page.get('名称')
        res_data = Page运行模式管理.api_运行模式分页查询(self.session,feild_page_yxms,self.header)


    def test_运行模式_05(self):
        """
        单接口: 5/启用禁用接口
        :return:
        """
        #设置禁用
        feild_off = Param_运行模式.p_on_off.get('禁用')
        feild_off['id'] = 123134
        res_data = Page运行模式管理.api_运行模式启用禁用(self.session,feild_off,self.header)



    def test_运行模式_06(self):
        """
        单接口: 6/编辑运动模式
        :return:
        """


        #编辑修改运行模试
        feild_upd_yxms = Param_运行模式.p_upd.get('01')
        res_data = Page运行模式管理.api_修改运行模式(self.session,feild_upd_yxms,self.header)



    def test_运行模式_07(self):
        """
        单接口: 7/日历查询集合
        :return:
        """
        #日历list查询
        feild_list = {"modeName":""}
        res_data = Page运行模式管理.api_运行模式集合查询(self.session,feild_list,self.header)


    def test_运行模式_08(self):
        """
        单接口: 8/日历设备运行模式列表
        :return:
        """
        #日历calendar_list
        feild_calendar_list = Param_运行模式.p_calendar_list.get('01')
        feild_calendar_list['idList'] = [12321]
        res_data = Page运行模式管理.api_查询设备运行模式列表(self.session,feild_calendar_list,self.header)
