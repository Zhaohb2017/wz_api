import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.专家知识库 import Param_标准作业指导书
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_设备类型
from common.M_Crypto import rsa_encrypt
from page_object.werun.专家知识库.Page_标准作业指导书 import Page标准作业指导书
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case标准作业指导书(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '标准作业指导书'
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
        if hasattr(self,'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        if hasattr(self, 's_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session,str(self.s_id),self.header)
        if hasattr(self, 's_id1'):
            Page设备类型表管理.api_设备类型通过id删除(self.session,str(self.s_id1),self.header)
        if hasattr(self, 'fs_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session,str(self.fs_id),self.header)
        self.session.close()
        pass


    def test_标准作业指导书_01(self):
        """
        单接口: 1.新增标准作业指导书
        :return:
        """
        # 1. 新增标准作业指导书
        global zds_id
        feild_add_zds = Param_标准作业指导书.p_add.get('单条')
        res_data = Page标准作业指导书.api_新增标准作业指导书及操作内容(self.session,feild_add_zds,self.header)
        zds_id = res_data.get('data').get('id')
        self.assertEqual(res_data.get("code"),200)

    def test_标准作业指导书_02(self):
        """
        单接口：2.根据sopid获取标准作业指导书内容
        :return:
        """
        res_data = Page标准作业指导书.api_根据sopId获取标准作业指导书操作内容(self.session,str(zds_id),self.header)
        self.assertEqual(res_data.get("code"),200)

    def test_标准作业指导书_03(self):
        """
        单接口：3.编辑标准作业指导书
        :return:
        """
        feild_upd = Param_标准作业指导书.p_upd.get('01')
        feild_upd['sopVo']['id'] = zds_id
        res_data = Page标准作业指导书.api_编辑标准作业指导书及操作内容(self.session, feild_upd, self.header)
        self.assertEqual(res_data.get('ok'), True)


    def test_标准作业指导书_04(self):
        """
        单接口：4.获取标准作业指导书分页列表
        :return:
        """
        # 4.获取标准作业指导书分页列表
        feild_page_zds = Param_标准作业指导书.p_page.get('默认')
        res_data = Page标准作业指导书.api_获取标准作业指导书分页列表(self.session,feild_page_zds,self.header)
        if feild_page_zds is not None:
            self.assertEqual(res_data.get("code"),200)

    def test_标准作业指导书_05(self):
        """
        单接口：5.下载标准作业指导书模板
        :return:
        """
        Page标准作业指导书.api_下载标准作业指导书模板(self.session, self.header)



    def test_标准作业指导书_06(self):
        """
        单接口：6.通过id删除标准作业指导书
        :return:
        """
        # 7.通过id删除标准作业指导书
        res_data = Page标准作业指导书.api_通过id删除标准作业指导书(self.session, str(zds_id), self.header)
        self.assertEqual(res_data.get("code"),200)







