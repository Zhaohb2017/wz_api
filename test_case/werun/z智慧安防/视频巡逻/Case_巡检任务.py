#!/usr/bin/env python
# encoding: utf-8
import time
import unittest
import uuid
import ddt
import requests
from business.foo_lib.modules_biz.werun.Biz_xxl_job import BizXxlJob
from business.foo_lib.modules_db.werun.Db_智慧安防 import Db智慧安防
from business.foo_lib.modules_db.werun.Db_设备智管 import Db设备智管
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_楼栋信息, Param_空间类型, Param_空间信息, \
    Param_设备类型
from business.param_config.api_param.werun.智慧安防.视频巡逻 import Param_巡逻标准, Param_巡逻区域, Param_巡逻计划, Param_巡逻任务
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from business.param_config.api_param.werun.设备智管.线上巡检.Param_巡检计划 import p_xmhmc
from common.Common_Base import write_excel_xmhmc
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目花名册管理 import Page项目花名册管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.视频巡逻.Page_巡逻任务表管理 import Page巡逻任务表管理
from page_object.werun.视频巡逻.Page_巡逻区域配置表管理 import Page巡逻区域配置表管理
from page_object.werun.视频巡逻.Page_巡逻检查项配置表管理 import Page巡逻检查项配置表管理
from page_object.werun.视频巡逻.Page_巡逻计划表管理 import Page巡逻计划表管理


#巡逻任务点击完成告警用例未覆盖，原因：前端功能未通

@ddt.ddt
class Case巡逻任务(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.session_xxl = requests.Session()
        self.case_name = '巡逻任务'
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
        pass

    def tearDown(self):
        pass

    def test_巡逻任务_01(self):
        """
        单接口: 1/分页查询
        :return:
        """
        #通过分页查询到任务id
        feild_page_rw = Param_巡逻任务.p_page.get('任务名称')
        res_data = Page巡逻任务表管理.api_巡逻任务分页查询(self.session, feild_page_rw, self.header)

    def test_巡逻任务_02(self):
        """
        单接口: 2/打印巡逻报表
        :return:
        """
        #执行打
        feild_print = Param_巡逻任务.p_print.get('01')
        res_data = Page巡逻任务表管理.api_打印巡逻报表(self.session,feild_print,self.header)

    def test_巡逻任务_03(self):
        """
        单接口: 3/完成巡逻任务提交
        :return:
        """
        #完成巡逻任务
        feild_finish_mission = Param_巡逻任务.p_finish.get('01')
        feild_finish_mission['id'] = 123312
        res_data = Page巡逻任务表管理.api_执行巡逻任务完成巡逻任务提交(self.session,feild_finish_mission,self.header)

    def test_巡逻任务_04(self):
        """
        单接口: 4/分页查询
        :return:
        """
        #通过分页查询到任务id
        feild_page_rw = Param_巡逻任务.p_page.get('任务名称')
        res_data = Page巡逻任务表管理.api_巡逻任务分页查询(self.session, feild_page_rw, self.header)

    def test_巡逻任务_05(self):
        """
        单接口: 5/变更巡逻人
        :return:
        """
        #任务转派，变更巡逻人
        feild_zprw = Param_巡逻任务.p_zprw.get('01')

        res_data = Page巡逻任务表管理.api_修改巡逻人(self.session,feild_zprw,self.header)

    def test_巡逻任务_06(self):
        """
        单接口: 6/id查询
        :return:
        """
        #通过id查询任务详情
        Page巡逻任务表管理.api_巡逻任务通过id查询(self.session,str(31232),self.header)

    def test_巡逻任务_07(self):
        """
        单接口: 7/ 执行巡逻任务查询巡逻区域
        :return:
        """
        feild_rwqy = Param_巡逻任务.p_rwqy.get('01')
        Page巡逻任务表管理.api_执行巡逻任务查询巡逻区域(self.session,feild_rwqy,self.header)





