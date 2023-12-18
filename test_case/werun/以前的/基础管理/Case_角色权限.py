import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出,Param_角色权限
from common.M_Crypto import rsa_encrypt
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.用户权限.Page_角色表管理 import Page角色表管理


@ddt.ddt
class Case角色权限(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '角色权限'
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
        if hasattr(self,'j_id'):
            Page角色表管理.api_角色通过id删除(self.session, str(self.j_id), self.header)
        self.session.close()
        pass


    def test_角色权限_01(self):
        """
        验证新增角色功能正常，通过分页查询断言新增角色成功,通过id删除角色功能正常
        :return:
        """
        #新增角色
        feild_add = Param_角色权限.p_add.get('01').copy()
        feild_add['name'] = "jiaose"+self.uuid_str
        res_data = Page角色表管理.api_新增角色(self.session,feild_add,self.header)
        self.j_id = res_data.get('data').get('id')
        #通过角色名称分页查询角色，并断言角色参数
        feild_page = Param_角色权限.p_page.get('01')
        feild_page['body']['name'] = feild_add.get('name')
        res_data = Page角色表管理.api_角色分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_add.get('name'),str(res_data.get('data')))
        #删除角色
        res_data = Page角色表管理.api_角色通过id删除(self.session,str(self.j_id),self.header)
        self.assertEqual(res_data.get('ok'),True)


    def test_角色权限_02(self):
        """
        验证新增角色功能正常，通过id查询断言新增角色成功
        :return:
        """
        #新增角色
        feild_add = Param_角色权限.p_add.get('01').copy()
        feild_add['name'] = "jiaose"+self.uuid_str
        res_data = Page角色表管理.api_新增角色(self.session,feild_add,self.header)
        self.j_id = res_data.get('data').get('id')
        #通过id查询角色，断言名称及权限列表,转成str assertIn
        res_data = Page角色表管理.api_角色通过id查询(self.session,str(self.j_id),self.header)
        self.assertIn(feild_add.get('name'),str(res_data.get('data')))
        self.assertIn(str(feild_add.get('resourceIds')),str(res_data.get('data')))
        #删除角色
        res_data = Page角色表管理.api_角色通过id删除(self.session,str(self.j_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询已删除的角色
        res_data = Page角色表管理.api_角色通过id查询(self.session, str(self.j_id), self.header)
        self.assertEqual(res_data.get('data'), None)
        pass

    def test_角色权限_03(self):
        """
        验证角色编辑修改功能正常，通过id查询断言修改角色名称、权限成功
        :return:
        """
        #新增角色
        feild_add = Param_角色权限.p_add.get('01').copy()
        feild_add['name'] = "jiaose" + str(uuid.uuid4())
        res_data = Page角色表管理.api_新增角色(self.session, feild_add, self.header)
        self.j_id = res_data.get('data').get('id')
        #编辑角色
        feild_upd = Param_角色权限.p_upd.get('01').copy()
        feild_upd['id'] = self.j_id
        feild_upd['name'] = "jiaose" + str(uuid.uuid4())
        res_data = Page角色表管理.api_修改角色(self.session,feild_upd,self.header)
        #通过id查询查询并断言修改的角色名称、权限
        res_data = Page角色表管理.api_角色通过id查询(self.session,str(self.j_id),self.header)
        self.assertIn(feild_upd.get('name'),str(res_data.get('data')))
        self.assertIn(str(feild_upd.get('resourceIds')),str(res_data.get('data')))
        #删除角色
        res_data = Page角色表管理.api_角色通过id删除(self.session,str(self.j_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        pass

