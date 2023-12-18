import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_企业档案, Param_项目管理, Param_楼栋信息, Param_空间信息, \
    Param_企业员工
from business.param_config.api_param.werun.设备智管.线上巡检.Param_巡检计划 import p_xmhmc
from common.Common_Base import create_phone, create_email, write_excel_xmhmc
from common.M_Crypto import rsa_encrypt
from page_object.werun.APP.Page_APP登录 import PageAPP登录
from page_object.werun.基础管理.Page_企业员工 import Page企业员工
from page_object.werun.基础管理.Page_企业档案 import Page企业档案
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case企业档案(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '企业档案'
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
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass




    def test_企业档案_01(self):
        """
        单接口：1/新增商户
        :return:
        """
        # 新增企业
        feild_add_qy = Param_企业档案.p_add.get('01')
        Page企业档案.api_新增商户(self.session, feild_add_qy, self.header)


    def test_企业档案_02(self):
        """
        单接口:2/通过id查询商户企业
        :return:
        """
        #通过id查询企业，断言新增参数正常
        Page企业档案.api_通过id查询企业(self.session,str(66565),self.header)

    def test_企业档案_03(self):
        """
        单接口:3/通过id删除企业
        :return:
        """
        #通过id删除企业
        Page企业档案.api_删除企业(self.session,str(6897),self.header)



    def test_企业档案_04(self):
        """
        单接口: 4/修改企业
        :return:
        """
        feild_upd_qy = Param_企业档案.p_add.get('01')
        Page企业档案.api_修改商户(self.session,feild_upd_qy,self.header)

    def test_企业管理_05(self):
        """
        单接口: 5/分页查询企业
        :return:
        """
        feild_page = Param_企业档案.p_page.get('默认')
        Page企业档案.api_分页查询企业(self.session,feild_page,self.header)


    def test_企业管理_06(self):
        """
        单接口：6/重置功能
        :return:
        """
        feild_page = Param_企业档案.p_page.get('重置')
        Page企业档案.api_分页查询企业(self.session,feild_page,self.header)


    def test_企业管理_07(self):
        """
        单接口:7/企业模板下载
        :return:
        """
        Page企业档案.api_企业档案模板(self.session,self.header)



    def test_企业档案_08(self):
        """
        单接口:8/上传模板
        :return:
        """
        qyda = Param_企业档案.p_import.get('01').copy()
        qyda[0] = "3333"
        qyda[1] = '哈尔滨市'
        qyda[2] = '南岗区'

        write_excel_xmhmc(Param_企业档案.file_data.get("02"), qyda)
        # 上传


        res_data = Page企业档案.api_导入企业(self.session,Param_企业档案.file_data.get("01"),self.header)




