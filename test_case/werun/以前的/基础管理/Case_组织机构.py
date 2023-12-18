import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_组织机构
from common.M_Crypto import rsa_encrypt
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.用户权限.Page_组织架构表管理 import Page组织架构表管理


@ddt.ddt
class Case组织机构(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '组织机构'
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
        if hasattr(self,'z_id_sub'):
            Page组织架构表管理.api_组织架构通过id删除(self.session, str(self.z_id_sub), self.header)
        if hasattr(self,'z_id'):
            Page组织架构表管理.api_组织架构通过id删除(self.session, str(self.z_id), self.header)
        self.session.close()
        pass


    def test_组织机构_01(self):
        """
        验证新增同级组织机构，并查询组织机构结构列表正常，通过orgCode及id查询新增机构正常，断言包含新建的组织
        :return:
        """
        #新增同级组织机构
        feild_add = Param_组织机构.p_add.get('同级')
        feild_add['orgName'] = "orgName " + self.uuid_str
        res_data = Page组织架构表管理.api_新增组织架构(self.session,feild_add,self.header)
        self.z_id = res_data.get('data').get('id')
        org_code = res_data.get('data').get('orgCode')
        #查询列表，断言新增机构在列表内
        res_data = Page组织架构表管理.api_获取组织架构的树形结构(self.session,self.header)
        self.assertIn(feild_add.get('orgName'),str(res_data.get('data')))
        res_data = Page组织架构表管理.api_通过IdOrgCode查询组织架构(self.session,{'orgId':self.z_id,'orgCode':org_code},self.header)
        self.assertIn(feild_add.get('orgName'), str(res_data.get('data')))
        #删除组织机构
        res_data = Page组织架构表管理.api_组织架构通过id删除(self.session,str(self.z_id),self.header)
        self.assertEqual(res_data.get('ok'),True)

    @ddt.data(*Param_组织机构.p_add_sub.keys())
    def test_组织机构_02(self,key):
        """
        验证新增下级组织机构，并查询组织机构结构列表正常，断言包含新建的组织
        :return:
        """
        #新增同级组织机构
        feild_add = Param_组织机构.p_add.get("同级").copy()
        feild_add['orgName'] = "orgName " + str(uuid.uuid4())
        res_data = Page组织架构表管理.api_新增组织架构(self.session,feild_add,self.header)
        self.z_id = res_data.get('data').get('id')
        #新增下级组织机构
        feild_add_sub = Param_组织机构.p_add_sub.get(key).copy()
        feild_add_sub['parentId'] = self.z_id
        feild_add_sub['orgName'] = "orgName " + str(uuid.uuid4())
        res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_sub, self.header)
        self.z_id_sub = res_data.get('data').get('id')
        #查询列表，断言新增机构在列表内
        res_data = Page组织架构表管理.api_获取组织架构的树形结构(self.session,self.header)
        self.assertIn(feild_add_sub.get('orgName'),str(res_data.get('data')))
        self.assertIn(str(feild_add_sub.get('parentId')),str(res_data.get('data')))
        #删除下级组织机构
        res_data = Page组织架构表管理.api_组织架构通过id删除(self.session,str(self.z_id_sub),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #删除同级组织机构
        res_data = Page组织架构表管理.api_组织架构通过id删除(self.session,str(self.z_id),self.header)
        self.assertEqual(res_data.get('ok'),True)

    def test_组织机构_03(self):
        """
        验证编辑修改同级组织机构，断言修改后的内容与查询的内容一致
        :return:
        """
        #新增同级组织机构
        feild_add = Param_组织机构.p_add.get('同级').copy()
        feild_add['orgName'] = "orgName " + str(uuid.uuid4())
        res_data = Page组织架构表管理.api_新增组织架构(self.session,feild_add,self.header)
        self.z_id = res_data.get('data').get('id')
        #修改同级组织机构
        feild_upd = Param_组织机构.p_upd.get('同级').copy()
        feild_upd['id'] = self.z_id
        feild_upd['orgName'] = "orgName " + str(uuid.uuid4())
        res_data = Page组织架构表管理.api_修改组织架构(self.session,feild_upd,self.header)
        #查询列表，断言修改后的机构在列表内，字段比对正常
        res_data = Page组织架构表管理.api_获取组织架构的树形结构(self.session,self.header)
        self.assertIn(feild_upd.get('orgName'),str(res_data.get('data')))
        self.assertIn(str(feild_upd.get('parentId')),str(res_data.get('data')))
        #删除同级组织机构
        res_data = Page组织架构表管理.api_组织架构通过id删除(self.session,str(self.z_id),self.header)
        self.assertEqual(res_data.get('ok'),True)

    def test_组织机构_04(self):
        """
        验证编辑修改下级组织机构，断言修改后的内容与查询的内容一致
        :return:
        """
        #新增同级组织机构
        feild_add = Param_组织机构.p_add.get('同级')
        feild_add['orgName'] = "orgName " + self.uuid_str
        res_data = Page组织架构表管理.api_新增组织架构(self.session,feild_add,self.header)
        self.z_id = res_data.get('data').get('id')
        #新增下级组织机构
        feild_add_sub = Param_组织机构.p_add.get('下级')
        feild_add_sub['parentId'] = self.z_id
        feild_add_sub['orgName'] = "orgName " + str(uuid.uuid4())
        res_data = Page组织架构表管理.api_新增组织架构(self.session,feild_add_sub,self.header)
        self.z_id_sub = res_data.get('data').get('id')
        #修改下级级组织机构
        feild_upd = Param_组织机构.p_upd.get('下级')
        feild_upd['id'] = self.z_id_sub
        feild_upd['parentId'] = self.z_id
        feild_upd['orgName'] = "orgName " + str(uuid.uuid4())
        res_data = Page组织架构表管理.api_修改组织架构(self.session,feild_upd,self.header)
        #查询列表，断言修改后的机构在列表内，字段比对正常
        res_data = Page组织架构表管理.api_获取组织架构的树形结构(self.session,self.header)
        self.assertIn(feild_upd.get('orgName'),str(res_data.get('data')))
        self.assertIn(str(feild_upd.get('parentId')),str(res_data.get('data')))
        #删除同级组织机构
        res_data = Page组织架构表管理.api_组织架构通过id删除(self.session,str(self.z_id),self.header)
        self.assertEqual(res_data.get('ok'),True)