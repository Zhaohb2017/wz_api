#!/usr/bin/env python
# encoding: utf-8
import time
import unittest
import uuid
import ddt
import requests
from business.param_config.api_param.werun.告警中心 import Param_告警记录
from business.param_config.api_param.werun.基础管理 import Param_登录登出
from common.M_Crypto import rsa_encrypt
from page_object.werun.告警中心.Page_告警记录管理 import Page告警记录管理
from page_object.werun.告警中心.Page_安防告警配置管理 import Page安防告警配置管理
from page_object.werun.告警中心.Page_黑名单布控管理 import Page黑名单布控管理
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目花名册管理 import Page项目花名册管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.线上巡检.Page_巡检任务管理 import Page巡检任务管理
from page_object.werun.线上巡检.Page_巡检机房管理 import Page巡检机房管理
from page_object.werun.线上巡检.Page_巡检计划管理 import Page巡检计划管理
from page_object.werun.线上巡检.Page_环境巡检标准管理 import Page环境巡检标准管理


@ddt.ddt
class Case告警记录(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.session_xxl = requests.Session()
        self.case_name = '告警记录'
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
        if hasattr(self,'gjjl_id'):
            Page告警记录管理.api_告警记录通过id删除(self.session,str(self.gjjl_id),self.header)
        if hasattr(self, 'rw_id'):
            Page巡检任务管理.api_通过id删除巡检任务(self.session, str(self.rw_id), self.header)
        if hasattr(self, 'aq_id'):
            Page黑名单布控管理.api_黑名单布控通过id删除(self.session, str(self.aq_id), self.header)
        if hasattr(self, 'xf_id'):
            Page安防告警配置管理.api_安防告警配置通过id删除(self.session, str(self.xf_id), self.header)
        if hasattr(self, 'tz_id'):
            Page设备表管理.api_设备通过id删除(self.session, str(self.tz_id), self.header)
        if hasattr(self, 'sub_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.sub_id), self.header)
        if hasattr(self, 's_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.s_id), self.header)
        if hasattr(self, 'jh_id'):
            Page巡检计划管理.api_通过id删除巡检计划(self.session, str(self.jh_id), self.header)
        if hasattr(self,'jf_id'):
            Page巡检机房管理.api_通过id删除巡检机房(self.session,str(self.jf_id),self.header)
        if hasattr(self, 'sbxj_id'):
            Page环境巡检标准管理.api_通过id删除环境巡检标准(self.session, str(self.sbxj_id), self.header)
        if hasattr(self, 'hmc_u_id'):
            Page项目花名册管理.api_项目花名册通过id删除(self.session, str(self.hmc_u_id), self.header)
        if hasattr(self, 'hmc_u_id1'):
            Page项目花名册管理.api_项目花名册通过id删除(self.session, str(self.hmc_u_id1), self.header)
        if hasattr(self, 'room_id'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session, str(self.room_id), self.header)
        if hasattr(self, 'space_type_id'):
            Page空间类型表管理.api_空间类型通过id删除(self.session, str(self.space_type_id), self.header)
        if hasattr(self, 'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass

    def test_告警记录_01(self):
        """
        单接口：1/ 搜索接口
        :return:
        """
        #分页查询
        feild_page = Param_告警记录.p_page_clz.get('默认查询')
        res_data = Page告警记录管理.api_告警记录分页查询(self.session,feild_page,self.header)
        self.assertEqual(res_data.get('code'),200)

    def test_告警记录_02(self):
        """
        单接口：2/ 统计各类型告警数量
        :return:
        """
        #分页查询
        feild_page = {"alarmStatus":"1"}
        res_data = Page告警记录管理.api_统计各类型告警数量(self.session,feild_page,self.header)
        self.assertEqual(res_data.get('code'),200)




