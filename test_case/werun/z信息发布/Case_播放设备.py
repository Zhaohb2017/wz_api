import copy
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.信息发布 import Param_播放设备
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_设备类型, Param_项目管理, Param_空间信息, Param_楼栋信息
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from common.M_Crypto import rsa_encrypt
from page_object.werun.信息发布 import Page_播放设备
from page_object.werun.信息发布.Page_播放设备 import Page播放设备
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case播放设备(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '播放设备'
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
        if hasattr(self,'tz_id'):
            Page播放设备.api_播放设备通过id删除(self.session, str(self.tz_id), self.header)
        if hasattr(self, 's_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.s_id), self.header)
        if hasattr(self, 'sub_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.s_id), self.header)
        if hasattr(self, 'fs_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.fs_id), self.header)
        if hasattr(self, 's_id2'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.s_id2), self.header)
        if hasattr(self, 'room_id'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session, str(self.room_id), self.header)
        if hasattr(self, 'room_id2'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session, str(self.room_id2), self.header)
        if hasattr(self, 'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass

    def test_播放设备_01(self):
        """
        单接口: 1.通过id删除播放
        :return:
        """
        Page播放设备.api_播放设备通过id删除(self.session,str(4123123),self.header)


    def test_播放设备_02(self):
        """
        单接口: 2.通过id查询台账
        :return:
        """
        Page播放设备.api_播放设备通过id查询(self.session, str(651), self.header)
