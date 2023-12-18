import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_楼栋信息, Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case楼栋信息(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '楼栋信息'
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session)
        self.public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        self.encrypt_pwd = rsa_encrypt(self.public_key, feild.get('sword'))
        feild['sword'] = self.encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(self.session, feild, {})
        self.header = {'traceId': str(uuid.uuid4()), 'Authorization': "Bearer " + res_data.get('data').get('token')}
        pass

    def tearDown(self):
        if hasattr(self,'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self,'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.session.close()
        pass

    @ddt.data(*Param_楼栋信息.p_add.keys())
    def test_楼栋信息_01(self,key):
        """
        验证新增楼栋、通过Id查询楼栋并断言新增信息正确、通过id删除楼栋功能
        :return:
        """
        #新增项目信息
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目"+str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session,feild_add,self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId':str(self.p_id)})
        #新增楼栋
        feild_add_ld = Param_楼栋信息.p_add.get(key)
        feild_add_ld['propertyId'] = int(self.p_id)
        feild_add_ld['buildingName'] = "楼栋"+str(uuid.uuid1())
        res_data = Page区域或楼栋表管理.api_新增区域或楼栋表(self.session,feild_add_ld,self.header)
        self.f_id = res_data.get('data').get('id')
        #通过id查询楼栋并断言楼栋信息
        res_data = Page区域或楼栋表管理.api_区域或楼栋通过id查询(self.session,str(self.f_id),self.header)
        self.assertEqual(feild_add_ld.get('buildingName'), res_data.get('data').get('buildingName'))
        self.assertEqual(feild_add_ld.get('minFloor'), res_data.get('data').get('minFloor'))
        self.assertEqual(feild_add_ld.get('maxFloor'), res_data.get('data').get('maxFloor'))
        self.assertEqual(feild_add_ld.get('buildingType'), res_data.get('data').get('buildingType'))
        if len(feild_add_ld.get('list')) != 0:
            self.assertEqual(feild_add_ld.get('list')[0].get('floorNum'), res_data.get('data').get('list')[0].get('floorNum'))
            self.assertEqual(feild_add_ld.get('list')[0].get('floorName'), res_data.get('data').get('list')[0].get('floorName'))
            pass
        #通过id删除楼栋信息
        res_data = Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        self.assertEqual(res_data.get('ok'), True)


    def test_楼栋信息_02(self):
        """
        验证分页搜索楼栋功能、断言查询到的楼栋信息与新增的一致
        :return:
        """
        #新增项目信息
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = res_data.get('data').get('id')
        self.header.update({'propertyId': str(self.p_id)})
        #新增楼栋信息
        feild_add_ld = Param_楼栋信息.p_add.get("楼栋")
        feild_add_ld['propertyId'] = self.p_id
        feild_add_ld['buildingName'] = "楼栋"+str(uuid.uuid1())
        res_data = Page区域或楼栋表管理.api_新增区域或楼栋表(self.session,feild_add_ld,self.header)
        self.f_id = res_data.get('data').get('id')
        #分页查询楼栋信息，断言楼栋信息正确
        feild_search = Param_楼栋信息.p_page.get("楼栋")
        feild_search['body']['propertyId'] = self.p_id
        res_data = Page区域或楼栋表管理.api_楼栋信息分页查询(self.session,feild_search,self.header)
        self.assertIn(feild_add_ld.get('buildingName'),str(res_data.get("data")))
        # 通过id删除楼栋信息
        res_data = Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        # 删除项目信息
        res_data = Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

    def test_楼栋信息_03(self):
        """
        验证修改楼栋信息功能、断言修改后的字段与查询到的字段信息一致
        :return:
        """
        # 新增项目信息
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = res_data.get('data').get('id')
        self.header.update({'propertyId': str(self.p_id)})
        # 新增楼栋信息
        feild_add_ld = Param_楼栋信息.p_add.get("楼栋")
        feild_add_ld['propertyId'] = self.p_id
        feild_add_ld['buildingName'] = "楼栋" + str(uuid.uuid1())
        res_data = Page区域或楼栋表管理.api_新增区域或楼栋表(self.session, feild_add_ld, self.header)
        self.f_id = res_data.get('data').get('id')
        # 修改楼栋信息
        feild_upd = Param_楼栋信息.p_upd.get('名称1')
        feild_upd['propertyId'] = self.p_id
        feild_upd['buildingName'] = "楼栋" + str(uuid.uuid1())
        feild_upd['id'] = self.f_id
        res_data = Page区域或楼栋表管理.api_修改区域或楼栋表(self.session,feild_upd,self.header)
        # 通过id查询楼栋信息，断言修改正常
        res_data = Page区域或楼栋表管理.api_区域或楼栋通过id查询(self.session,str(self.f_id),self.header)
        self.assertEqual(feild_upd.get('buildingName'), res_data.get('data').get('buildingName'))
        # 通过id删除楼栋信息
        res_data = Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        # 删除项目信息
        res_data = Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

    def test_楼栋信息_04(self):
        """
        验证楼栋信息页面的项目列表信息查询正常
        :return:
        """
        # 新增项目信息
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = res_data.get('data').get('id')
        self.header.update({'propertyId': str(self.p_id)})
        #查询楼栋的项目列表信息，断言新增的项目在查询的项目中
        res_data = Page项目表管理.api_查询项目下拉列表(self.session,{"propertyName":""},self.header)
        self.assertIn(feild_add.get('propertyName'),str(res_data.get('data')))
        #删除新增项目
        res_data = Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.assertEqual(res_data.get('ok'), True)










