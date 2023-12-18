#!/usr/bin/env python
# encoding: utf-8
#!/usr/bin/env python
# encoding: utf-8
import unittest
import uuid
import ddt
import requests
from business.param_config.api_param.werun.基础管理 import Param_登录登出
from business.param_config.api_param.werun.设备智管 import Param_空间时态
from common.M_Crypto import rsa_encrypt
from page_object.werun.用户权限.Page_用户表管理 import Page用户表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.模式联动规则配置.Page_设备远程控制 import Page设备远程控制



@ddt.ddt
class Case设备远程控制(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
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


    def test_设备远程控制_01(self):
        """
        单接口: 1/ 分页查询
        :return:
        """
        pagedata = {"body":{"tagType":"fac_control","facCategoryId":None,"spaceId":None,"controlVal":1,"building":[]},"head":{"total":0,"current":1,"size":10}}
        Page设备远程控制.api_设备远程控制page(self.session, pagedata, self.header)

    def test_设备远程控制_02(self):
        """
        单接口: 2/ 左侧标签页查询
        :return:
        """
        feilds = {"tagType":"fac_control"}
        Page设备远程控制.api_设备远程控制左侧标签(self.session, feilds, self.header)


    def test_设备远程控制_03(self):
        """
        单接口: 3/ 新增标签
        :return:
        """
        feilds = {"tagName":"脚本","tagType":"fac_control","propertyId":497}
        Page设备远程控制.api_设备远程控制新增标签(self.session, feilds, self.header)



    def test_设备远程控制_04(self):
        """
        单接口: 4/ 打标签
        :return:
        """
        feilds = {"facIdList":[22124],"tagIdList":[185]}
        Page设备远程控制.api_设备远程控制新增标签(self.session, feilds, self.header)




    def test_设备远程控制_05(self):
        """
        单接口: 5/ 删除标签
        :return:
        """
        Page设备远程控制.api_设备远程控制删除标签(self.session, str(41232), self.header)

    def test_设备远程控制_06(self):
        """
        单接口: 6/ 编辑标签
        :return:
        """
        feilds = {"tagName":"刷卡门禁1111","id":1186,"tagType":"fac_control","propertyId":497}
        Page设备远程控制.api_设备远程控制编辑标签(self.session, feilds, self.header)

    def test_设备远程控制_07(self):
        """
        单接口: 7/ 删除标签
        :return:
        """
        Page设备远程控制.api_设备远程控制删除设备(self.session, str(41232), self.header)



