import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_角色权限, Param_组织机构, Param_用户管理, Param_项目管理
from common.Common_Base import create_phone, create_email
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_用户表管理 import Page用户表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.用户权限.Page_组织架构表管理 import Page组织架构表管理
from page_object.werun.用户权限.Page_角色表管理 import Page角色表管理


@ddt.ddt
class Case用户管理(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '用户管理'
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
        if hasattr(self,'u_id'):
            Page用户表管理.api_用户通过id删除(self.session, str(self.u_id), self.header)
        if hasattr(self,'j_id'):
            Page角色表管理.api_角色通过id删除(self.session, str(self.j_id), self.header)
        if hasattr(self, 'z_id'):
            Page组织架构表管理.api_组织架构通过id删除(self.session, str(self.z_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass

    @ddt.data(*Param_用户管理.p_add.keys())
    def test_用户管理_01(self,key):
        """
        验证新增用户功能，并使用新增的用户登陆成功
        :return:
        """
        # 新增项目，设置header的项目id
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级组织机构，获取id
        feild_add_z = Param_组织机构.p_add.get('同级')
        feild_add_z['orgName'] = "orgName " + self.uuid_str
        res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
        self.z_id = res_data.get('data').get('id')
        #新增角色，获取id
        feild_add_j = Param_角色权限.p_add.get('01').copy()
        feild_add_j['name'] = "jiaose" + self.uuid_str
        res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
        self.j_id = res_data.get('data').get('id')
        #新增用户
        feild_add_u = Param_用户管理.p_add.get(key).copy()
        feild_add_u['orgIds'] = [self.z_id]
        feild_add_u['roleIds'] = [self.j_id]
        feild_add_u['scabbard'] = "user"+str(uuid.uuid4()).split('-')[-1]
        feild_add_u['nickName'] = "nickName" + str(uuid.uuid4()).split('-')[-1]
        feild_add_u['sword'] = self.encrypt_pwd
        feild_add_u['confirmSword'] = self.encrypt_pwd
        feild_add_u['mobile'] = create_phone()
        feild_add_u['email'] = create_email()
        res_data = Page用户表管理.api_创建用户(self.session,feild_add_u,self.header)
        self.u_id = res_data.get('data').get('id')
        #使用新用户加密登陆，断言登录成功
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        feild['sword'] = feild_add_u.get('sword')
        feild['scabbard'] = feild_add_u.get('scabbard')
        res_data = Page登录模块.api_后台管理登录(self.session, feild, {})
        self.assertEqual(res_data.get('data').get('token') is not None,True)
        #删除用户
        res_data = Page用户表管理.api_用户通过id删除(self.session,str(self.u_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #再次登录，验证登陆失败
        res_data = Page登录模块.api_后台管理登录(self.session, feild, {})
        self.assertEqual(res_data.get('data'),None)
        #删除组织
        res_data = Page组织架构表管理.api_组织架构通过id删除(self.session,str(self.z_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #删除角色
        res_data = Page角色表管理.api_角色通过id删除(self.session,str(self.j_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        pass

    # def test_用户管理_02(self):
    #     """
    #     验证分页查询功能，查询用户正常（启用状态）
    #     :return:
    #     """
    #     # 新增项目，设置header的项目id
    #     feild_add = Param_项目管理.p_add.get('学校')
    #     feild_add['propertyName'] = "项目" + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': str(self.p_id)})
    #     # 新增同级组织机构，获取id
    #     feild_add_z = Param_组织机构.p_add.get('同级')
    #     feild_add_z['orgName'] = "orgName " + self.uuid_str
    #     res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
    #     self.z_id = res_data.get('data').get('id')
    #     # 新增角色，获取id
    #     feild_add_j = Param_角色权限.p_add.get('01').copy()
    #     feild_add_j['name'] = "jiaose" + self.uuid_str
    #     res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
    #     self.j_id = res_data.get('data').get('id')
    #     # 新增用户
    #     feild_add_u = Param_用户管理.p_add.get('客服').copy()
    #     feild_add_u['orgIds'] = [self.z_id]
    #     feild_add_u['roleIds'] = [self.j_id]
    #     feild_add_u['scabbard'] = "user" + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_u['nickName'] = "nickName" + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_u['sword'] = self.encrypt_pwd
    #     feild_add_u['confirmSword'] = self.encrypt_pwd
    #     feild_add_u['mobile'] = create_phone()
    #     feild_add_u['email'] = create_email()
    #     res_data = Page用户表管理.api_创建用户(self.session, feild_add_u, self.header)
    #     self.u_id = res_data.get('data').get('id')
    #     #使用分页查询用户，用断言新增的用户存在
    #     feild_page = Param_用户管理.p_page.get('启用')
    #     feild_page['body']['nickName'] = feild_add_u.get('nickName')
    #     feild_page['body']['orgId'] = self.z_id
    #     res_data = Page用户表管理.api_用户分页查询(self.session,feild_page,self.header)
    #     self.assertIn(feild_add_u.get('scabbard'),str(res_data.get('data')))
    #     #用户设置为禁用
    #     feild_on_off = Param_用户管理.p_on_off.get('禁用').copy()
    #     feild_on_off['id'] = self.u_id
    #     res_data = Page用户表管理.api_用户启用禁用(self.session,feild_on_off,self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #再次使用分页查询用户，断言不存在
    #     feild_page = Param_用户管理.p_page.get('启用')
    #     feild_page['body']['nickName'] = feild_add_u.get('nickName')
    #     feild_page['body']['orgId'] = self.z_id
    #     res_data = Page用户表管理.api_用户分页查询(self.session,feild_page,self.header)
    #     self.assertNotIn(feild_add_u.get('scabbard'),str(res_data.get('data')))
    #     #通过id删除用户
    #     res_data = Page用户表管理.api_用户通过id删除(self.session,str(self.u_id),self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #通过id删除组织机构
    #     res_data = Page组织架构表管理.api_组织架构通过id删除(self.session, str(self.z_id), self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     #通过id删除角色
    #     res_data = Page角色表管理.api_角色通过id删除(self.session, str(self.j_id), self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     pass

    def test_用户管理_03(self):
        """
        验证分页查询功能，查询用户正常（禁用状态）
        :return:
        """
        # 新增项目，设置header的项目id
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级组织机构，获取id
        feild_add_z = Param_组织机构.p_add.get('同级')
        feild_add_z['orgName'] = "orgName " + self.uuid_str
        res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
        self.z_id = res_data.get('data').get('id')
        # 新增角色，获取id
        feild_add_j = Param_角色权限.p_add.get('01').copy()
        feild_add_j['name'] = "jiaose" + self.uuid_str
        res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
        self.j_id = res_data.get('data').get('id')
        # 新增用户
        feild_add_u = Param_用户管理.p_add.get('客服').copy()
        feild_add_u['orgIds'] = [self.z_id]
        feild_add_u['roleIds'] = [self.j_id]
        feild_add_u['scabbard'] = "user" + str(uuid.uuid4()).split('-')[-1]
        feild_add_u['nickName'] = "nickName" + str(uuid.uuid4()).split('-')[-1]
        feild_add_u['sword'] = self.encrypt_pwd
        feild_add_u['confirmSword'] = self.encrypt_pwd
        feild_add_u['mobile'] = create_phone()
        feild_add_u['email'] = create_email()
        res_data = Page用户表管理.api_创建用户(self.session, feild_add_u, self.header)
        self.u_id = res_data.get('data').get('id')
        #使用分页查询用户，用断言新增的用户存在
        feild_page = Param_用户管理.p_page.get('禁用')
        feild_page['body']['nickName'] = feild_add_u.get('nickName')
        feild_page['body']['orgId'] = self.z_id
        res_data = Page用户表管理.api_用户分页查询(self.session,feild_page,self.header)
        self.assertNotIn(feild_add_u.get('scabbard'),str(res_data.get('data')))
        #用户设置为禁用
        feild_on_off = Param_用户管理.p_on_off.get('禁用').copy()
        feild_on_off['id'] = self.u_id
        res_data = Page用户表管理.api_用户启用禁用(self.session,feild_on_off,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #再次使用分页查询用户，断言不存在
        feild_page = Param_用户管理.p_page.get('禁用')
        feild_page['body']['nickName'] = feild_add_u.get('nickName')
        feild_page['body']['orgId'] = self.z_id
        res_data = Page用户表管理.api_用户分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_add_u.get('scabbard'),str(res_data.get('data')))
        #通过id删除用户
        res_data = Page用户表管理.api_用户通过id删除(self.session,str(self.u_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id删除组织机构
        res_data = Page组织架构表管理.api_组织架构通过id删除(self.session, str(self.z_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过id删除角色
        res_data = Page角色表管理.api_角色通过id删除(self.session, str(self.j_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        pass


    # def test_用户管理_04(self):
    #     """
    #     验证分页查询功能，查询用户正常（全部状态）
    #     :return:
    #     """
    #     # 新增项目，设置header的项目id
    #     feild_add = Param_项目管理.p_add.get('学校')
    #     feild_add['propertyName'] = "项目" + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': str(self.p_id)})
    #     # 新增同级组织机构，获取id
    #     feild_add_z = Param_组织机构.p_add.get('同级')
    #     feild_add_z['orgName'] = "orgName " + self.uuid_str
    #     res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
    #     self.z_id = res_data.get('data').get('id')
    #     # 新增角色，获取id
    #     feild_add_j = Param_角色权限.p_add.get('01').copy()
    #     feild_add_j['name'] = "jiaose" + self.uuid_str
    #     res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
    #     self.j_id = res_data.get('data').get('id')
    #     # 新增用户
    #     feild_add_u = Param_用户管理.p_add.get('客服').copy()
    #     feild_add_u['orgIds'] = [self.z_id]
    #     feild_add_u['roleIds'] = [self.j_id]
    #     feild_add_u['scabbard'] = "user" + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_u['nickName'] = "nickName" + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_u['sword'] = self.encrypt_pwd
    #     feild_add_u['confirmSword'] = self.encrypt_pwd
    #     feild_add_u['mobile'] = create_phone()
    #     feild_add_u['email'] = create_email()
    #     res_data = Page用户表管理.api_创建用户(self.session, feild_add_u, self.header)
    #     self.u_id = res_data.get('data').get('id')
    #     #使用分页查询用户，用断言新增的用户存在
    #     feild_page = Param_用户管理.p_page.get('全部')
    #     feild_page['body']['orgId'] = self.z_id
    #     res_data = Page用户表管理.api_用户分页查询(self.session,feild_page,self.header)
    #     self.assertIn(feild_add_u.get('scabbard'),str(res_data.get('data')))
    #     #用户设置为禁用
    #     feild_on_off = Param_用户管理.p_on_off.get('禁用').copy()
    #     feild_on_off['id'] = self.u_id
    #     res_data = Page用户表管理.api_用户启用禁用(self.session,feild_on_off,self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #再次使用分页查询用户，断言不存在
    #     feild_page = Param_用户管理.p_page.get('全部')
    #     feild_page['body']['orgId'] = self.z_id
    #     res_data = Page用户表管理.api_用户分页查询(self.session,feild_page,self.header)
    #     self.assertIn(feild_add_u.get('scabbard'),str(res_data.get('data')))
    #     #通过id删除用户
    #     res_data = Page用户表管理.api_用户通过id删除(self.session,str(self.u_id),self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #通过id删除组织机构
    #     res_data = Page组织架构表管理.api_组织架构通过id删除(self.session, str(self.z_id), self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     #通过id删除角色
    #     res_data = Page角色表管理.api_角色通过id删除(self.session, str(self.j_id), self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     pass

    def test_用户管理_05(self):
        """
        验证分页查询功能，查询用户正常（通过姓名）
        :return:
        """
        # 新增项目，设置header的项目id
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级组织机构，获取id
        feild_add_z = Param_组织机构.p_add.get('同级')
        feild_add_z['orgName'] = "orgName " + self.uuid_str
        res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
        self.z_id = res_data.get('data').get('id')
        # 新增角色，获取id
        feild_add_j = Param_角色权限.p_add.get('01').copy()
        feild_add_j['name'] = "jiaose" + self.uuid_str
        res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
        self.j_id = res_data.get('data').get('id')
        # 新增用户
        feild_add_u = Param_用户管理.p_add.get('客服').copy()
        feild_add_u['orgIds'] = [self.z_id]
        feild_add_u['roleIds'] = [self.j_id]
        feild_add_u['scabbard'] = "user" + str(uuid.uuid4()).split('-')[-1]
        feild_add_u['nickName'] = "nickName" + str(uuid.uuid4()).split('-')[-1]
        feild_add_u['sword'] = self.encrypt_pwd
        feild_add_u['confirmSword'] = self.encrypt_pwd
        feild_add_u['mobile'] = create_phone()
        feild_add_u['email'] = create_email()
        res_data = Page用户表管理.api_创建用户(self.session, feild_add_u, self.header)
        self.u_id = res_data.get('data').get('id')
        #使用分页查询用户，用断言新增的用户存在
        feild_page = Param_用户管理.p_page.get('名称')
        feild_page['body']['nickName'] = feild_add_u.get('nickName')
        feild_page['body']['orgId'] = self.z_id
        res_data = Page用户表管理.api_用户分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_add_u.get('scabbard'),str(res_data.get('data')))
        #用户设置为禁用
        feild_on_off = Param_用户管理.p_on_off.get('禁用').copy()
        feild_on_off['id'] = self.u_id
        res_data = Page用户表管理.api_用户启用禁用(self.session,feild_on_off,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #再次使用分页查询用户，断言不存在
        feild_page = Param_用户管理.p_page.get('名称')
        feild_page['body']['nickName'] = feild_add_u.get('nickName')
        feild_page['body']['orgId'] = self.z_id
        res_data = Page用户表管理.api_用户分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_add_u.get('scabbard'),str(res_data.get('data')))
        #通过id删除用户
        res_data = Page用户表管理.api_用户通过id删除(self.session,str(self.u_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id删除组织机构
        res_data = Page组织架构表管理.api_组织架构通过id删除(self.session, str(self.z_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过id删除角色
        res_data = Page角色表管理.api_角色通过id删除(self.session, str(self.j_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        pass

    def test_用户管理_06(self):
        """
        验证用户启用禁用功能，断言用户启用时登录成功，禁用时登录失败
        :return:
        """
        # 新增项目，设置header的项目id
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级组织机构，获取id
        feild_add_z = Param_组织机构.p_add.get('同级')
        feild_add_z['orgName'] = "orgName " + self.uuid_str
        res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
        self.z_id = res_data.get('data').get('id')
        #新增角色，获取id
        feild_add_j = Param_角色权限.p_add.get('01').copy()
        feild_add_j['name'] = "jiaose" + self.uuid_str
        res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
        self.j_id = res_data.get('data').get('id')
        #新增用户
        feild_add_u = Param_用户管理.p_add.get('客服').copy()
        feild_add_u['orgIds'] = [self.z_id]
        feild_add_u['roleIds'] = [self.j_id]
        feild_add_u['scabbard'] = "user"+str(uuid.uuid4()).split('-')[-1]
        feild_add_u['nickName'] = "nickName" + str(uuid.uuid4()).split('-')[-1]
        feild_add_u['sword'] = self.encrypt_pwd
        feild_add_u['confirmSword'] = self.encrypt_pwd
        feild_add_u['mobile'] = create_phone()
        feild_add_u['email'] = create_email()
        res_data = Page用户表管理.api_创建用户(self.session,feild_add_u,self.header)
        self.u_id = res_data.get('data').get('id')
        #禁用用户
        feild_on_off = Param_用户管理.p_on_off.get('禁用').copy()
        feild_on_off['id'] = self.u_id
        res_data = Page用户表管理.api_用户启用禁用(self.session, feild_on_off, self.header)
        self.assertEqual(res_data.get('ok'), True)
        #使用用户登录,断言登录失败
        feild_login = Param_登录登出.p_后台管理登陆.get('01').copy()
        feild_login['sword'] = feild_add_u.get('sword')
        feild_login['scabbard'] = feild_add_u.get('scabbard')
        res_data = Page登录模块.api_后台管理登录(self.session, feild_login, {})
        self.assertEqual(res_data.get('data'), None)
        #启用用户
        feild_on_off = Param_用户管理.p_on_off.get('启用').copy()
        feild_on_off['id'] = self.u_id
        res_data = Page用户表管理.api_用户启用禁用(self.session, feild_on_off, self.header)
        self.assertEqual(res_data.get('ok'), True)
        #使用新用户再次登陆，断言登录成功
        feild_login = Param_登录登出.p_后台管理登陆.get('01').copy()
        feild_login['sword'] = feild_add_u.get('sword')
        feild_login['scabbard'] = feild_add_u.get('scabbard')
        res_data = Page登录模块.api_后台管理登录(self.session, feild_login, {})
        self.assertEqual(res_data.get('data').get('token') is not None,True)
        #删除用户
        res_data = Page用户表管理.api_用户通过id删除(self.session,str(self.u_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #删除组织
        res_data = Page组织架构表管理.api_组织架构通过id删除(self.session,str(self.z_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #删除角色
        res_data = Page角色表管理.api_角色通过id删除(self.session,str(self.j_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        pass

    def test_用户管理_07(self):
        """
        验证用户重置密码功能，断言用户重置密码后，使用新密码登录成功，旧密码登录失败
        :return:
        """
        # 新增项目，设置header的项目id
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级组织机构，获取id
        feild_add_z = Param_组织机构.p_add.get('同级')
        feild_add_z['orgName'] = "orgName " + self.uuid_str
        res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
        z_id = res_data.get('data').get('id')
        # 新增角色，获取id
        feild_add_j = Param_角色权限.p_add.get('01').copy()
        feild_add_j['name'] = "jiaose" + self.uuid_str
        res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
        j_id = res_data.get('data').get('id')
        # 新增用户
        feild_add_u = Param_用户管理.p_add.get('客服').copy()
        feild_add_u['orgIds'] = [z_id]
        feild_add_u['roleIds'] = [j_id]
        feild_add_u['scabbard'] = "user" + str(uuid.uuid4()).split('-')[-1]
        feild_add_u['nickName'] = "nickName" + str(uuid.uuid4()).split('-')[-1]
        feild_add_u['sword'] = self.encrypt_pwd
        feild_add_u['confirmSword'] = self.encrypt_pwd
        feild_add_u['mobile'] = create_phone()
        feild_add_u['email'] = create_email()
        res_data = Page用户表管理.api_创建用户(self.session, feild_add_u, self.header)
        u_id = res_data.get('data').get('id')
        # 重置用户密码
        feild_reset_pwd = Param_用户管理.p_reset_pwd.get('01').copy()
        feild_reset_pwd['id'] = u_id
        new_pwd = rsa_encrypt(self.public_key, 'Webuild114')
        feild_reset_pwd['sword'] = new_pwd
        res_data = Page用户表管理.api_用户重置密码(self.session, feild_reset_pwd, self.header)
        self.assertEqual(res_data.get('ok'), True)
        # 使用新密码登录，断言登录成功
        feild_login = Param_登录登出.p_后台管理登陆.get('01').copy()
        feild_login['sword'] = feild_reset_pwd.get('sword')
        feild_login['scabbard'] = feild_add_u.get('scabbard')
        res_data = Page登录模块.api_后台管理登录(self.session, feild_login, {})
        self.assertEqual(res_data.get('data').get('token') is not None, True)
        # 使用旧密码登录，断言登录失败
        feild_login = Param_登录登出.p_后台管理登陆.get('01').copy()
        feild_login['sword'] = feild_add_u.get('sword')
        feild_login['scabbard'] = feild_add_u.get('scabbard')
        res_data = Page登录模块.api_后台管理登录(self.session, feild_login, {})
        self.assertEqual(res_data.get('data'), None)
        # 删除用户
        res_data = Page用户表管理.api_用户通过id删除(self.session, str(u_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        # 删除组织
        res_data = Page组织架构表管理.api_组织架构通过id删除(self.session, str(z_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        # 删除角色
        res_data = Page角色表管理.api_角色通过id删除(self.session, str(j_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        pass

    # def test_用户管理_08(self):
    #     """
    #     验证新增用户修改密码前，访问内部接口受限，修改密码后，可正常访问
    #     :return:
    #     """
    #     # 新增同级组织机构，获取id
    #     feild_add_z = Param_组织机构.p_add.get('同级')
    #     feild_add_z['orgName'] = "orgName " + self.uuid_str
    #     res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
    #     self.z_id = res_data.get('data').get('id')
    #     # 新增角色，获取id
    #     feild_add_j = Param_角色权限.p_add.get('01').copy()
    #     feild_add_j['name'] = "jiaose" + self.uuid_str
    #     res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
    #     self.j_id = res_data.get('data').get('id')
    #     # 新增用户
    #     feild_add_u = Param_用户管理.p_add.get('客服').copy()
    #     feild_add_u['orgIds'] = [self.z_id]
    #     feild_add_u['roleIds'] = [self.j_id]
    #     feild_add_u['scabbard'] = "user" + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_u['nickName'] = "nickName" + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_u['sword'] = self.encrypt_pwd
    #     feild_add_u['confirmSword'] = self.encrypt_pwd
    #     feild_add_u['mobile'] = create_phone()
    #     feild_add_u['email'] = create_email()
    #     res_data = Page用户表管理.api_创建用户(self.session, feild_add_u, self.header)
    #     self.u_id = res_data.get('data').get('id')
    #     # 使用新用户登录
    #     feild_login = Param_登录登出.p_后台管理登陆.get('01').copy()
    #     feild_login['sword'] = feild_add_u.get('sword')
    #     feild_login['scabbard'] = feild_add_u.get('scabbard')
    #     res_data = Page登录模块.api_后台管理登录(self.session, feild_login, {})
    #     self.header1 = {'traceId': self.uuid_str, 'Authorization': "Bearer " + res_data.get('data').get('token')}
    #     # 新增项目，断言无法新增
    #     feild_add_p = Param_项目管理.p_add.get('写字楼')
    #     feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header1)
    #     self.assertEqual(res_data.get('code'), 500)
        #使用新用户更改密码后登录
        # feild_upd_pwd = Param_登录登出.p_upd.get('01')
        # res_data = Page登录模块.api_新用户密码修改(self.session,feild_upd_pwd,self.header1)
        # self.assertEqual(res_data.get('ok'),True)
        #新增项目，新增成功
        # res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header1)
        # self.assertEqual(res_data.get('code'), 200)
        #登出
        # pass