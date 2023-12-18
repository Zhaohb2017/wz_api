import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from business.param_config.api_param.werun.基础管理.排班管理 import Param_班次管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.排班管理.Page_班次管理 import Page班次管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case班次管理(unittest.TestCase):
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
        pass

    def tearDown(self):
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.session.close()
        pass


    def test_班次管理_01(self):
        """
        验证新增班次，通过id查询班次断言比对新建参数正确，通过id删除班次功能正常(一日一班)
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        #新建班次
        feild_add = Param_班次管理.p_add.get('一日一班').copy()
        feild_add['schedulingName'] = 'BanCi'+str(uuid.uuid1())
        feild_add['records'][0]['scheduingName'] = 'BanCiSub'+str(uuid.uuid1())
        res_data = Page班次管理.api_新增或更新班次以及时间安排(self.session,feild_add,self.header)
        b_id = res_data.get('data')
        #通过id查询班次，断言参数正常
        res_data = Page班次管理.api_通过班次id查询班次时间安排(self.session,str(b_id),self.header)
        self.assertEqual(feild_add['records'][0]['scheduingName'],res_data.get('data')[0].get('scheduingName'))
        self.assertEqual(feild_add['records'][0]['schStartTime'],res_data.get('data')[0].get('schStartTime'))
        self.assertEqual(feild_add['records'][0]['schEndTime'],res_data.get('data')[0].get('schEndTime'))
        #通过id删除班次
        res_data = Page班次管理.api_通过id删除班次(self.session,str(b_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #再次通过id查询班次，验证班次不存在
        res_data = Page班次管理.api_通过班次id查询班次时间安排(self.session, str(b_id), self.header)
        self.assertEqual(res_data.get('data'), [])
        pass

    def test_班次管理_02(self):
        """
        验证新增班次，通过id查询班次断言比对新建参数正确，通过id删除班次功能正常(一日两班)
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        #新建班次
        feild_add = Param_班次管理.p_add.get('一日两班').copy()
        feild_add['schedulingName'] = 'BanCi'+str(uuid.uuid1())
        feild_add['records'][0]['scheduingName'] = 'BanCiSub'+str(uuid.uuid1())
        res_data = Page班次管理.api_新增或更新班次以及时间安排(self.session,feild_add,self.header)
        b_id = res_data.get('data')
        #通过id查询班次，断言参数正常
        res_data = Page班次管理.api_通过班次id查询班次时间安排(self.session,str(b_id),self.header)
        self.assertEqual(feild_add['records'][0]['scheduingName'],res_data.get('data')[0].get('scheduingName'))
        self.assertEqual(feild_add['records'][0]['schStartTime'],res_data.get('data')[0].get('schStartTime'))
        self.assertEqual(feild_add['records'][0]['schEndTime'],res_data.get('data')[0].get('schEndTime'))
        self.assertEqual(feild_add['records'][1]['scheduingName'],res_data.get('data')[1].get('scheduingName'))
        self.assertEqual(feild_add['records'][1]['schStartTime'],res_data.get('data')[1].get('schStartTime'))
        self.assertEqual(feild_add['records'][1]['schEndTime'],res_data.get('data')[1].get('schEndTime'))
        #通过id删除班次
        res_data = Page班次管理.api_通过id删除班次(self.session,str(b_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #再次通过id查询班次，验证班次不存在
        res_data = Page班次管理.api_通过班次id查询班次时间安排(self.session, str(b_id), self.header)
        self.assertEqual(res_data.get('data'), [])
        pass

    def test_班次管理_03(self):
        """
        验证班次分页查询功能，查询数据正常(通过名称查询)
        :return:
        """
        #新增项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(p_id)})
        #新建班次
        feild_add = Param_班次管理.p_add.get('一日两班').copy()
        feild_add['schedulingName'] = 'BanCi'+str(uuid.uuid1())
        feild_add['records'][0]['scheduingName'] = 'BanCiSub'+str(uuid.uuid1())
        res_data = Page班次管理.api_新增或更新班次以及时间安排(self.session,feild_add,self.header)
        b_id = res_data.get('data')
        #通过分页查询班次，断言参数正常
        feild_page = Param_班次管理.p_page.get('名称')
        feild_page['schedulingName'] = feild_add.get('schedulingName')
        res_data = Page班次管理.api_分页查询班次信息(self.session,feild_page,self.header)
        self.assertIn(feild_add['schedulingName'],str(res_data.get('data')))
        #通过id删除班次
        res_data = Page班次管理.api_通过id删除班次(self.session,str(b_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        # 删除项目信息
        res_data = Page项目表管理.api_项目通过id删除(self.session, p_id, self.header)
        self.assertEqual(res_data.get('ok'), True)
        pass

    def test_班次管理_04(self):
        """
        验证班次分页查询功能，查询数据正常(重置默认)
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        #新建班次
        feild_add = Param_班次管理.p_add.get('一日两班').copy()
        feild_add['schedulingName'] = 'BanCi'+str(uuid.uuid1())
        feild_add['records'][0]['scheduingName'] = 'BanCiSub'+str(uuid.uuid1())
        res_data = Page班次管理.api_新增或更新班次以及时间安排(self.session,feild_add,self.header)
        b_id = res_data.get('data')
        #通过分页查询班次，断言参数修改成功
        feild_page = Param_班次管理.p_page.get('重置')
        res_data = Page班次管理.api_分页查询班次信息(self.session,feild_page,self.header)
        self.assertNotEqual(res_data.get('data').get('records'),[])
        #通过id删除班次
        res_data = Page班次管理.api_通过id删除班次(self.session,str(b_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        pass

    def test_班次管理_05(self):
        """
        验证修改班次功能，通过id查询班次与修改的内容一致
        :return:
        """
        #新增项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(p_id)})
        #新建班次
        feild_add = Param_班次管理.p_add.get('一日一班').copy()
        feild_add['schedulingName'] = 'BanCi'+str(uuid.uuid1())
        feild_add['records'][0]['scheduingName'] = 'BanCiSub'+str(uuid.uuid1())
        res_data = Page班次管理.api_新增或更新班次以及时间安排(self.session,feild_add,self.header)
        b_id = res_data.get('data')
        #修改班次
        feild_upd = Param_班次管理.p_upd.get('一日两班').copy()
        feild_upd['id'] = b_id
        feild_upd['schedulingName'] = 'BanCi'+str(uuid.uuid1())
        feild_upd['records'][0]['scheduingName'] = 'BanCiSub'+str(uuid.uuid1())
        feild_upd['records'][1]['scheduingName'] = 'BanCiSub'+str(uuid.uuid1())
        res_data = Page班次管理.api_新增或更新班次以及时间安排(self.session, feild_upd, self.header)
        #通过分页查询班次，断言参数不为空
        feild_page = Param_班次管理.p_page.get('名称')
        res_data = Page班次管理.api_分页查询班次信息(self.session,feild_page,self.header)
        self.assertIn(feild_upd['schedulingName'],str(res_data.get('data')))
        #通过id查询班次，断言参数修改正确
        res_data = Page班次管理.api_通过班次id查询班次时间安排(self.session, str(b_id), self.header)
        self.assertEqual(feild_upd['records'][0]['scheduingName'], res_data.get('data')[0].get('scheduingName'))
        self.assertEqual(feild_upd['records'][0]['schStartTime'], res_data.get('data')[0].get('schStartTime'))
        self.assertEqual(feild_upd['records'][0]['schEndTime'], res_data.get('data')[0].get('schEndTime'))
        self.assertEqual(feild_upd['records'][1]['scheduingName'], res_data.get('data')[1].get('scheduingName'))
        self.assertEqual(feild_upd['records'][1]['schStartTime'], res_data.get('data')[1].get('schStartTime'))
        self.assertEqual(feild_upd['records'][1]['schEndTime'], res_data.get('data')[1].get('schEndTime'))
        #通过id删除班次
        res_data = Page班次管理.api_通过id删除班次(self.session,str(b_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        # 删除项目信息
        res_data = Page项目表管理.api_项目通过id删除(self.session, p_id, self.header)
        self.assertEqual(res_data.get('ok'), True)
        pass
