import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_企业员工, Param_项目管理, Param_楼栋信息, Param_空间信息, \
    Param_企业档案
from common.Common_Base import create_phone, create_email
from common.M_Crypto import rsa_encrypt
from page_object.werun.APP.Page_APP登录 import PageAPP登录
from page_object.werun.基础管理.Page_企业员工 import Page企业员工
from page_object.werun.基础管理.Page_企业档案 import Page企业档案
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case企业员工(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '企业员工'
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
        if hasattr(self, 'yg_id'):
            Page企业员工.api_删除企业员工(self.session, str(self.yg_id), self.header)
        if hasattr(self,'qy_id'):
            Page企业档案.api_删除企业(self.session, str(self.qy_id), self.header)
        if hasattr(self, 'room_id'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session, str(self.room_id), self.header)
        if hasattr(self, 'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.session.close()
        pass

    def test_企业员工_01(self):
        """
        单接口：1/新增用户
        :return:
        """
        #新增企业员工(依赖企业)
        feild_add_yg = Param_企业员工.p_add_yg.get("业主")
        Page企业员工.api_新增企业员工(self.session,feild_add_yg,self.header)

    def test_企业员工_02(self):
        """
        单接口: 2/通过id查询企业员工
        :return:
        """
        Page企业员工.api_通过id查询企业员工(self.session,str(4123),self.header)


    def test_企业员工_03(self):
        """
        单接口: 3/通过id删除企业员工
        :return:
        """
        Page企业员工.api_删除企业员工(self.session,str(45645),self.header)

    def test_企业员工_04(self):
        """
        单接口:4/分页查询员工数据
        :return:
        """
        feild_page_yg = Param_企业员工.p_page_yg.get('企业')
        feild_page_yg['body']['businessId'] = "123141231"
        res_data = Page企业员工.api_分页查询企业员工(self.session, feild_page_yg, self.header)

    def test_企业员工_05(self):
        """
        单接口:5/重置功能
        :return:
        """
        feild_page_yg = Param_企业员工.p_page_yg.get('重置')
        Page企业员工.api_分页查询企业员工(self.session, feild_page_yg, self.header)


    def test_企业员工_06(self):
        """
        单接口:6/禁用功能
        :return:
        """
        #禁用
        feild_off = Param_企业员工.p_on_off.get('禁用')
        feild_off['id'] = "654564564646464654"
        Page企业员工.api_企业员工启用禁用(self.session,feild_off,self.header)

    def test_企业员工_07(self):
        """
        单接口：7/启用功能
        :return:
        """
        #启用
        feild_on = Param_企业员工.p_on_off.get('启用')
        feild_on['id'] = "654564564646464654"
        Page企业员工.api_企业员工启用禁用(self.session,feild_on,self.header)

    def test_企业员工_08(self):
        """
        单接口: 8/重置密码功能
        :return:
        """
        # 重置密码
        feild_reset_pwd = Param_企业员工.p_reset.get('01')
        feild_reset_pwd['id'] = "32141232"
        new_pwd = rsa_encrypt(self.public_key, 'Webuild114')
        feild_reset_pwd['sword'] = new_pwd
        Page企业员工.api_企业员工重置密码(self.session, feild_reset_pwd, self.header)


    def test_企业员工_09(self):
        """
        单接口:9/下载模板
        :return:
        """
        Page企业员工.api_批量导入员工模板(self.session, self.header)
