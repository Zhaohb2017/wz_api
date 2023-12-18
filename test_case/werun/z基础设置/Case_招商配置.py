import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_招商配置, Param_楼栋信息, Param_空间信息
from common.Common_Base import write_excel
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_招商配置信息表管理 import Page招商配置信息表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case招商配置(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '招商配置'
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session)
        public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        encrypt_pwd = rsa_encrypt(public_key, feild.get('sword'))
        feild['sword'] = encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(self.session, feild, {})
        self.header = {'traceId': str(uuid.uuid4()), 'Authorization': "Bearer " + res_data.get('data').get('token')}
        pass

    def tearDown(self):
        if hasattr(self, 'zspz_id'):
            Page招商配置信息表管理.api_招商配置信息通过id删除(self.session, str(self.zspz_id), self.header)
        if hasattr(self, 'zspz_id1'):
            Page招商配置信息表管理.api_招商配置信息通过id删除(self.session, str(self.zspz_id1), self.header)
        if hasattr(self,'room_id'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session,str(self.room_id),self.header)
        if hasattr(self, 'space_type_id'):
            Page空间类型表管理.api_空间类型通过id删除(self.session, str(self.space_type_id), self.header)
        if hasattr(self, 'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self,'p_id'):
            Page项目表管理.api_项目通过id删除(self.session,str(self.p_id),self.header)
        self.session.close()
        pass

    def test_招商配置_01(self):
        """
        单接口：1/验证招商下载模板功能正常
        :return:
        """
        #下载导入模版，断言下载成功
        res_data = Page招商配置信息表管理.api_下载招商配置模版(self.session,self.header)
        self.assertEqual(res_data.ok,True)


    def test_招商配置_02(self):
        """
        单接口:2/分页信息查询
        :return:
        """
        # 列表查询招商配置，断言参数正确
        feild_page = Param_招商配置.p_page.get('公司名称')
        res_data = Page招商配置信息表管理.api_招商配置信息分页查询(self.session, feild_page, self.header)
        self.assertEqual(res_data.get("code"),200)


    def test_招商配置_03(self):
        """
        单接口:3/重置功能校验
        :return:
        """
        feild_page = Param_招商配置.p_query.get('重置')
        res_data = Page招商配置信息表管理.api_招商配置信息分页查询(self.session, feild_page, self.header)
        self.assertEqual(res_data.get("code"),200)

    def test_招商管理_04(self):
        """
        单接口:4/通过id删除
        :return:
        """
        Page招商配置信息表管理.api_招商配置信息通过id删除(self.session, str(3541), self.header)

    def test_招商配置_05(self):
        """
        单接口:5/验证招商配置导入模版正常
        :return:
        """
        # 上传
        feild= Param_招商配置.feild_upload_excel_1
        res_data = Page招商配置信息表管理.api_上传导入招商配置(self.session,feild,self.header)
        self.assertEqual(res_data.get('ok'),False)





