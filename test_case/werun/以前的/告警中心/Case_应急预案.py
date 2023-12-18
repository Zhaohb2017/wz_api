import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.告警中心 import Param_应急预案
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.告警中心.Page_应急预案 import Page应急预案
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case应急预案(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '应急预案'
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
        if hasattr(self, 'yjya_id'):
            Page应急预案.api_删除应急预案(self.session, str(self.yjya_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass

    @ddt.data(*Param_应急预案.p_add.keys())
    def test_应急预案_01(self,key):
        """
        验证新增应急预案，通过id查询应急预案断言新增参数正确，通过id删除应急预案功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})
        #新增应急预案
        feild_add = Param_应急预案.p_add.get(key)
        feild_add['name'] = '预案名称'+str(uuid.uuid4())
        feild_add['number'] = '预案编号' +str(uuid.uuid4())
        feild_add['content'] = '预案内容' +str(uuid.uuid4())
        res_data = Page应急预案.api_新增应急预案(self.session,feild_add,self.header)
        self.yjya_id = res_data.get('data').get('id')
        #通过id查询，并断言
        res_data = Page应急预案.api_通过id查询应急预案(self.session,str(self.yjya_id),self.header)
        self.assertEqual(feild_add.get('name'),res_data.get('data').get('name'))
        self.assertEqual(feild_add.get('number'),res_data.get('data').get('number'))
        self.assertEqual(feild_add.get('content'),res_data.get('data').get('content'))
        #通过id删除配置
        res_data = Page应急预案.api_删除应急预案(self.session,str(self.yjya_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        # 通过id查询，验证删除正常
        res_data = Page应急预案.api_通过id查询应急预案(self.session, str(self.yjya_id), self.header)
        self.assertEqual(res_data.get('data'),None)

    def test_应急预案_02(self):
        """
        验证应急预案分页查询功能（预案等级、预案名称、启用状态、禁用状态）
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})
        #新增应急预案
        feild_add = Param_应急预案.p_add.get('一级预案')
        feild_add['name'] = '预案名称'+str(uuid.uuid4())
        feild_add['number'] = '预案编号' +str(uuid.uuid4())
        feild_add['content'] = '预案内容' +str(uuid.uuid4())
        res_data = Page应急预案.api_新增应急预案(self.session,feild_add,self.header)
        self.yjya_id = res_data.get('data').get('id')
        #通过分页查询，并断言新增参数
        feild_page = Param_应急预案.p_page.get('预案等级')
        feild_page['body']['level'] = feild_add.get('level')
        res_data = Page应急预案.api_分页查询应急预案(self.session,feild_page,self.header)
        self.assertIn(feild_add.get('name'),str(res_data))
        feild_page = Param_应急预案.p_page.get('预案名称')
        res_data = Page应急预案.api_分页查询应急预案(self.session,feild_page,self.header)
        self.assertIn(feild_add.get('name'),str(res_data))
        feild_page = Param_应急预案.p_page.get('启用状态')
        res_data = Page应急预案.api_分页查询应急预案(self.session,feild_page,self.header)
        self.assertNotIn(feild_add.get('name'),str(res_data))
        feild_page = Param_应急预案.p_page.get('禁用状态')
        res_data = Page应急预案.api_分页查询应急预案(self.session,feild_page,self.header)
        self.assertIn(feild_add.get('name'),str(res_data))
        #通过id删除配置
        res_data = Page应急预案.api_删除应急预案(self.session,str(self.yjya_id),self.header)
        self.assertEqual(res_data.get('ok'),True)

    def test_应急预案_03(self):
        """
        验证应急预案启用禁用功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})
        #新增应急预案
        feild_add = Param_应急预案.p_add.get('一级预案')
        feild_add['name'] = '预案名称'+str(uuid.uuid4())
        feild_add['number'] = '预案编号' +str(uuid.uuid4())
        feild_add['content'] = '预案内容' +str(uuid.uuid4())
        res_data = Page应急预案.api_新增应急预案(self.session,feild_add,self.header)
        self.yjya_id = res_data.get('data').get('id')
        #应急预案启用
        feild_on = Param_应急预案.p_on_off.get('启用')
        feild_on['id'] = self.yjya_id
        res_data = Page应急预案.api_应急预案启用禁用(self.session,feild_on,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过分页查询，并断言新增参数
        feild_page = Param_应急预案.p_page.get('启用状态')
        res_data = Page应急预案.api_分页查询应急预案(self.session,feild_page,self.header)
        self.assertIn(feild_add.get('name'),str(res_data))
        #应急预案禁用
        feild_off = Param_应急预案.p_on_off.get('禁用')
        feild_off['id'] = self.yjya_id
        res_data = Page应急预案.api_应急预案启用禁用(self.session,feild_off,self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过分页查询禁用
        feild_page = Param_应急预案.p_page.get('禁用状态')
        res_data = Page应急预案.api_分页查询应急预案(self.session,feild_page,self.header)
        self.assertIn(feild_add.get('name'),str(res_data))
        #通过id删除配置
        res_data = Page应急预案.api_删除应急预案(self.session,str(self.yjya_id),self.header)
        self.assertEqual(res_data.get('ok'),True)

    def test_应急预案_04(self):
        """
        验证应急预案编辑修改功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})
        #新增应急预案
        feild_add = Param_应急预案.p_add.get('一级预案')
        feild_add['name'] = '预案名称'+str(uuid.uuid4())
        feild_add['number'] = '预案编号' +str(uuid.uuid4())
        feild_add['content'] = '预案内容' +str(uuid.uuid4())
        res_data = Page应急预案.api_新增应急预案(self.session,feild_add,self.header)
        self.yjya_id = res_data.get('data').get('id')
        #编辑修改应急预案
        feild_upd = Param_应急预案.p_upd.get('01')
        feild_upd['id'] = self.yjya_id
        feild_upd['number'] = '预案编号' +str(uuid.uuid4())
        feild_upd['name'] = '预案名称'+str(uuid.uuid4())
        feild_upd['content'] = '预案内容' +str(uuid.uuid4())
        res_data = Page应急预案.api_修改应急预案(self.session,feild_upd,self.header)
        self.assertEqual(res_data.get('ok'),True)
        # 通过id查询，并断言
        res_data = Page应急预案.api_通过id查询应急预案(self.session, str(self.yjya_id), self.header)
        self.assertEqual(feild_upd.get('name'), res_data.get('data').get('name'))
        self.assertEqual(feild_upd.get('number'), res_data.get('data').get('number'))
        self.assertEqual(feild_upd.get('content'), res_data.get('data').get('content'))
        self.assertEqual(feild_upd.get('level'), res_data.get('data').get('level'))
        #通过id删除配置
        res_data = Page应急预案.api_删除应急预案(self.session,str(self.yjya_id),self.header)
        self.assertEqual(res_data.get('ok'),True)

