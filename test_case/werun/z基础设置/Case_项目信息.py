import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case项目管理(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '项目管理'
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
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass


    def test_项目信息_01(self):
        """
        单接口: 1.项目信息-分页查询
        :return:
        """
        feild_page = Param_项目管理.p_page.get("查询所有")
        res_data = Page项目表管理.api_项目分页查询(self.session,feild_page,self.header)
        self.assertEqual(res_data.get('code'),200)


    def test_项目信息_02(self):
        """
        单接口: 2.通过id查询-项目信息
        :return:
        """
        Page项目表管理.api_项目通过id查询(self.session,"12341",self.header)

    def test_项目信息_03(self):
        """
        单接口: 3.重置功能
        :return:
        """
        feild_page = Param_项目管理.p_page.get("重置")
        res_data = Page项目表管理.api_项目分页查询(self.session,feild_page,self.header)
        self.assertEqual(res_data.get('code'),200)



    # @ddt.data(*Param_项目管理.p_add.keys())
    # def test_项目管理_01(self,key):
    #     """
    #     验证新增项目、通过Id查询项目并断言新增信息正确、通过id删除项目功能
    #     :return:
    #     """
    #     #新增项目信息
    #     feild_add = Param_项目管理.p_add.get(key)
    #     feild_add['propertyName'] = "项目"+str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session,feild_add,self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     #查看项目信息 断言
    #     res_data = Page项目表管理.api_项目通过id查询(self.session,self.p_id,self.header)
    #     self.assertEqual(feild_add.get('propertyName'),res_data.get('data').get('propertyName'))
    #     self.assertEqual(int(feild_add.get('propertyType')),res_data.get('data').get('propertyType'))
    #     self.assertIn(str(feild_add.get('propertyArea')),str(res_data.get('data').get('propertyArea')))
    #     self.assertIn(str(feild_add.get('propertyPublicArea')),str(res_data.get('data').get('propertyPublicArea')))
    #     self.assertEqual(feild_add.get('fullAddress'),res_data.get('data').get('fullAddress'))
    #     self.assertEqual(feild_add.get('city'),res_data.get('data').get('city'))
    #     self.assertEqual(feild_add.get('area'),res_data.get('data').get('area'))
    #     #删除项目信息
    #     res_data = Page项目表管理.api_项目通过id删除(self.session,self.p_id,self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     # 查看项目信息 断言
    #     res_data = Page项目表管理.api_项目通过id查询(self.session, self.p_id, self.header)
    #     self.assertEqual(res_data.get('data'),None)
    #
    # @ddt.data(*Param_项目管理.p_page.keys())
    # def test_项目管理_02(self,key):
    #     """
    #     验证分页查询项目信息功能、断言查询到的项目信息与新增的一致
    #     :return:
    #     """
    #     #新增项目信息
    #     feild_add = Param_项目管理.p_add.get('学校')
    #     feild_add['propertyName'] = "项目"+str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session,feild_add,self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     #按所在地区查询信息 断言
    #     feild_page = Param_项目管理.p_page.get(key)
    #     res_data = Page项目表管理.api_项目分页查询(self.session,feild_page,self.header)
    #     self.assertIn(feild_add.get('propertyName'),str(res_data.get('data')))
    #     # 删除项目信息
    #     res_data = Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #
    # def test_项目管理_03(self):
    #     """
    #     验证修改项目信息功能、断言修改后的字段与查询到的字段信息一致
    #     :return:
    #     """
    #     #新增项目信息
    #     feild_add = Param_项目管理.p_add.get('学校')
    #     feild_add['propertyName'] = "项目"+str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session,feild_add,self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     #修改项目信息
    #     feild_upd = Param_项目管理.p_upd.get('01')
    #     feild_upd['id'] = int(self.p_id)
    #     Page项目表管理.api_修改项目表(self.session,feild_upd,self.header)
    #     # 查看项目信息 断言
    #     res_data = Page项目表管理.api_项目通过id查询(self.session, self.p_id, self.header)
    #     self.assertEqual(feild_upd.get('propertyName'), res_data.get('data').get('propertyName'))
    #     self.assertEqual(int(feild_upd.get('propertyType')), res_data.get('data').get('propertyType'))
    #     self.assertIn(str(feild_upd.get('propertyArea')), str(res_data.get('data').get('propertyArea')))
    #     self.assertIn(str(feild_upd.get('propertyPublicArea')), str(res_data.get('data').get('propertyPublicArea')))
    #     self.assertEqual(feild_upd.get('fullAddress'), res_data.get('data').get('fullAddress'))
    #     self.assertEqual(feild_upd.get('city'), res_data.get('data').get('city'))
    #     self.assertEqual(feild_upd.get('area'), res_data.get('data').get('area'))
    #     # 删除项目信息
    #     res_data = Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #
    # def test_项目管理_04(self):
    #     """
    #     验证修改楼信息功能、断言修改后的字段与查询到的字段信息一致
    #     :return:
    #     """
    #     #新增项目信息
    #     feild_add = Param_项目管理.p_add.get('学校')
    #     feild_add['propertyName'] = "项目"+str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session,feild_add,self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     #修改项目信息
    #     feild_upd = Param_项目管理.p_upd.get('01')
    #     feild_upd['id'] = int(self.p_id)
    #     Page项目表管理.api_修改项目表(self.session,feild_upd,self.header)
    #     # 查看项目信息 断言
    #     res_data = Page项目表管理.api_项目通过id查询(self.session, self.p_id, self.header)
    #     self.assertEqual(feild_upd.get('propertyName'), res_data.get('data').get('propertyName'))
    #     self.assertEqual(int(feild_upd.get('propertyType')), res_data.get('data').get('propertyType'))
    #     self.assertIn(str(feild_upd.get('propertyArea')), str(res_data.get('data').get('propertyArea')))
    #     self.assertIn(str(feild_upd.get('propertyPublicArea')), str(res_data.get('data').get('propertyPublicArea')))
    #     self.assertEqual(feild_upd.get('fullAddress'), res_data.get('data').get('fullAddress'))
    #     self.assertEqual(feild_upd.get('city'), res_data.get('data').get('city'))
    #     self.assertEqual(feild_upd.get('area'), res_data.get('data').get('area'))
    #     # 删除项目信息
    #     res_data = Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
    #     self.assertEqual(res_data.get('ok'), True)

    # def test_项目管理_05(self):
    #     """
    #     验证导入项目导入功能、断言查询项目与导入的信息一致
    #     :return:
    #     """
    #     #导入项目(导入项目两个、导入项目如有返回Id则获取id)
    #     #通过名称查询项目、断言、并获取项目id
    #     #通过id删除项目
    #     pass

    # def test_项目管理_06(self):
    #     """
    #     验证导入项目下载模版功能、断言查询项目与导入的信息一致
    #     :return:
    #     """
    #     #下载项目模版
    #     #断言返回ok
    #     pass






