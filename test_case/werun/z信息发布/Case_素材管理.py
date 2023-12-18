import copy
import unittest
import uuid
import ddt
import requests
import datetime
import time
from business.param_config.api_param.werun.信息发布 import Param_素材管理
from page_object.werun.信息发布.Page_素材管理 import Page素材管理
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.上传下载.Page_附件管理 import Page附件管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块

@ddt.ddt
class Case素材管理(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '素材管理'
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
        if hasattr(self, 'pic_id'):
            Page素材管理.api_通过id删除素材(self.session, str(self.spic_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass

    def test_素材管理_01(self):
        """
        单接口: 上传图片素材
        :return:
        """
        #上传图片
        global fid
        feild_upload = Param_素材管理.p_upload.get('图片')
        res_data = Page附件管理.api_上传附件(self.session, feild_upload, self.header)
        fid = res_data.get('data').get('fid')

        # 新增图片素材
        feild_add = Param_素材管理.p_add.get('图片')
        f_add = feild_add[0] #字典
        f_add ['materialName'] = self.case_name+str(uuid.uuid4())
        f_add['fileId'] = fid
        feild_add[0] = f_add
        Page素材管理.api_新增素材(self.session,feild_add,self.header)



    def test_素材管理_02(self):
        """
        单接口: 素材集合查询
        :return:
        """
        feild_add = Param_素材管理.p_set.get('默认')
        res_data = Page素材管理.api_素材集合查询(self.session,feild_add,self.header)
        self.assertEqual(res_data.get('code'), 200)



    def test_素材管理_03(self):
        """
        单接口: 通过id查询
        :return:
        """
        Page素材管理.api_id查询素材(self.session, str(fid), self.header)



    def test_素材管理_04(self):
        """
        单接口: 通过id删除素材表
        :return:
        """
        Page素材管理.api_通过id删除素材(self.session, str(fid), self.header)




   