import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.专家知识库 import Param_项目资料库
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.上传下载.Page_附件管理 import Page附件管理
from page_object.werun.专家知识库.Page_资料库 import Page资料库
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case资料库(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '资料库'
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
        if hasattr(self, 'xmzl_id'):
            Page资料库.api_删除项目资料(self.session, str(self.xmzl_id), self.header)
        if hasattr(self,'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        if hasattr(self, 'zlk_id'):
            Page资料库.api_删除资料库(self.session, str(self.zlk_id), self.header)
        self.session.close()
        pass

    def test_资料库_01(self):
        """
        单接口：1.新增资料库
        :return:
        """
        global zlk_id
        feild_add_zlk = Param_项目资料库.p_add_zlk.get('顶级')
        Page资料库.api_新增资料库(self.session,feild_add_zlk,self.header)
        zlk_id = "2023"


    def test_资料库_02(self):
        """
        单接口：2.修改资料库
        :return:
        """
        feild_put_zlk = Param_项目资料库.p_add_zlk.get('顶级')
        feild_put_zlk["id"] = zlk_id
        Page资料库.api_编辑资料库(self.session, feild_put_zlk, self.header)

    def test_资料库_03(self):
        """
        单接口：3.通过id查询
        :return:
        """
        Page资料库.api_id查询资料库(self.session,zlk_id,self.header)


    def test_资料库_04(self):
        """
        单接口：4.通过id删除资料库文件夹
        :return:
        """
        res_data = Page资料库.api_删除资料库(self.session,str(zlk_id),self.header)
        self.assertEqual(res_data.get('msg'),"不存在此目录")

    def test_资料库_05(self):
        """
        单接口：5.查询树状数据
        :return:
        """
        # 5.查询树状数据
        res_data = Page资料库.api_列表查询树状资料库(self.session,self.header)
        self.assertEqual(res_data.get('code'),200)



    def test_新增项目资料_01(self):
        """
        单接口: 1.新增
        :return:
        """
        """上传附件文件"""
        global xmzl_id
        feild_upload = Param_项目资料库.p_upload.get('01')
        res_data = Page附件管理.api_上传附件(self.session,feild_upload,self.header)
        fid = res_data.get('data').get('fid')
        feild_add_xmzl = Param_项目资料库.p_add_xmzl.get('01')
        feild_add_xmzl['folderId'] = "2023"
        feild_add_xmzl['filePath'] = fid
        feild_add_xmzl['fileName'] = '名称'
        feild_add_xmzl['fileVersion'] = '版本'
        feild_add_xmzl['remark'] = '备注'
        res_data = Page资料库.api_新增项目资料(self.session,feild_add_xmzl,self.header)
        xmzl_id = res_data.get('data').get('id')
        self.assertEqual(res_data.get('code'),200)


    def test_新增项目资料_02(self):
        """
        单接口: 2.通过id删除项目资料
        :return:
        """
        try:
            res_data = Page资料库.api_删除项目资料(self.session, str(xmzl_id), self.header)
        except NameError:
            self.assertEqual(res_data.get('ok'),False)
        else:
            self.assertEqual(res_data.get('ok'), True)





