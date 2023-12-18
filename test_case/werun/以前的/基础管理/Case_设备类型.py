import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_设备类型, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case设备类型(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '设备类型'
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
        if hasattr(self,'sub_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session,str(self.sub_id),self.header)
        if hasattr(self,'s_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session,str(self.s_id),self.header)
        if hasattr(self,'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.session.close()
        pass

    @ddt.data(*Param_设备类型.p_add.keys())
    def test_设备类型_01(self,key):
        """
        验证新增同级设备类型，验证设备树表查询功能正常，通过Id查询新增设备，断言新增参数正确
        :return:
        """
        # 新增项目，设置header的项目id
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        #新增同级设备类型
        feild_add = Param_设备类型.p_add.get(key)
        feild_add['facCateName'] = self.case_name+str(uuid.uuid4())
        feild_add['facCateCode'] = self.case_name+str(uuid.uuid4())
        res_data = Page设备类型表管理.api_新增设备类型表(self.session,feild_add,self.header)
        self.s_id = res_data.get('data').get('id')
        #设备树表查询，断言新增设备存在树表中
        res_data = Page设备类型表管理.api_设备类型树列表查询(self.session,self.header)
        self.assertIn(feild_add.get('facCateName'),str(res_data.get('data')))
        #通过id查询设备信息，断言新增参数正确
        res_data = Page设备类型表管理.api_设备类型通过id查询(self.session,str(self.s_id),self.header)
        self.assertEqual(feild_add.get('facCateCode'),res_data.get('data').get('facCateCode'))
        self.assertEqual(feild_add.get('facCateName'),res_data.get('data').get('facCateName'))
        self.assertEqual(feild_add.get('level'),res_data.get('data').get('level'))
        #通过id删除设备类型
        res_data = Page设备类型表管理.api_设备类型通过id删除(self.session,str(self.s_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询设备类型不存在
        res_data = Page设备类型表管理.api_设备类型通过id查询(self.session,str(self.s_id),self.header)
        self.assertEqual(res_data.get('data'),None)
        pass

    @ddt.data(*Param_设备类型.p_add_sub.keys())
    def test_设备类型_02(self,key):
        """
        验证新增下级设备类型，验证设备树表查询功能正常，通过Id查询新增设备，断言新增参数正确
        :return:
        """
        #新增项目，设置header的项目id
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId':str(self.p_id)})
        #新增同级
        feild_add = Param_设备类型.p_add.get('一级设备')
        feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
        self.s_id = res_data.get('data').get('id')
        #新增下级
        feild_add_sub = Param_设备类型.p_add_sub.get(key)
        feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['parentId'] = self.s_id
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
        self.sub_id = res_data.get('data').get('id')
        #设备树表查询，断言新增设备存在树表中
        res_data = Page设备类型表管理.api_设备类型树列表查询(self.session,self.header)
        self.assertIn(feild_add_sub.get('facCateName'),str(res_data.get('data')))
        #通过id查询设备信息，断言新增参数正确
        res_data = Page设备类型表管理.api_设备类型通过id查询(self.session,str(self.sub_id),self.header)
        self.assertEqual(feild_add_sub.get('facCateCode'),res_data.get('data').get('facCateCode'))
        self.assertEqual(feild_add_sub.get('facCateName'),res_data.get('data').get('facCateName'))
        self.assertEqual(feild_add_sub.get('level'),res_data.get('data').get('level'))
        #通过id删除下级设备类型
        res_data = Page设备类型表管理.api_设备类型通过id删除(self.session,str(self.sub_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id删除同级设备类型
        Page设备类型表管理.api_设备类型通过id删除(self.session,str(self.s_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        pass

    def test_设备类型_03(self):
        """
        验证设备类型编辑修改功能，通过id查询修改的内容正确
        :return:
        """
        #新增项目，设置header的项目id
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId':str(self.p_id)})
        #新增同级
        feild_add = Param_设备类型.p_add.get('一级设备')
        feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
        self.s_id = res_data.get('data').get('id')
        #修改同级
        feild_upd = Param_设备类型.p_upd.get('一级设备')
        feild_upd['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_upd['id'] = self.s_id
        res_data = Page设备类型表管理.api_修改设备类型表(self.session,feild_upd,self.header)
        #通过id查询设备信息，断言新增参数正确
        res_data = Page设备类型表管理.api_设备类型通过id查询(self.session,str(self.s_id),self.header)
        self.assertEqual(feild_upd.get('facCateName'),res_data.get('data').get('facCateName'))
        pass
