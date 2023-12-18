import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_楼栋信息, Param_空间信息, Param_空间类型, Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case空间信息(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '空间信息'
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
        if hasattr(self,'room_id'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session,str(self.room_id),self.header)
        if hasattr(self, 'space_type_id'):
            Page空间类型表管理.api_空间类型通过id删除(self.session, str(self.space_type_id), self.header)
        if hasattr(self, 'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self,'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass

    # @ddt.data(*Param_楼栋信息.p_add.keys())
    def test_空间信息_01(self):
        """
        验证新增空间、通过Id查询空间并断言新增信息正确、通过id删除空间功能（未选空间类型）
        :return:
        """
        #新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        #新增区域楼栋
        feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
        feild_add_ld['propertyId'] = int(self.p_id)
        feild_add_ld['buildingName'] = "楼栋" + str(uuid.uuid1())
        res_data = Page区域或楼栋表管理.api_新增区域或楼栋表(self.session, feild_add_ld, self.header)
        self.f_id = res_data.get('data').get('id')
        #查询区域或楼栋
        res_data = Page区域或楼栋表管理.api_区域或楼栋通过id查询(self.session, str(self.f_id), self.header)
        floor_id = res_data.get('data').get('list')[0].get('id')
        #新增空间
        feild_add_space = Param_空间信息.p_add.get('空间类型1')
        feild_add_space['propertyId'] = self.p_id
        feild_add_space['buildingId'] = self.f_id
        feild_add_space['buildingFloorId'] = floor_id
        feild_add_space['buildingFloorSpaceName'] = "room "+str(uuid.uuid1())
        res_data = Page楼层房间信息表管理.api_新增楼层房间信息表(self.session,feild_add_space,self.header)
        self.room_id = res_data.get('data').get('id')
        #通过id查询空间信息，断言空间信息
        res_data = Page楼层房间信息表管理.api_楼层房间信息通过id查询(self.session,str(self.room_id),self.header)
        self.assertEqual(feild_add_space.get('buildArea'),res_data.get('data').get('buildArea'))
        self.assertEqual(feild_add_space.get('buildingFloorSpaceName'),res_data.get('data').get('buildingFloorSpaceName'))
        self.assertEqual(str(feild_add_space.get('propertyId')),str(res_data.get('data').get('propertyId')))
        self.assertEqual(str(feild_add_space.get('buildingId')),str(res_data.get('data').get('buildingId')))
        self.assertEqual(str(feild_add_space.get('buildingFloorId')),str(res_data.get('data').get('buildingFloorId')))
        #通过id删除空间信息
        res_data = Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session,str(self.room_id),self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过id查询空间信息
        res_data = Page楼层房间信息表管理.api_楼层房间信息通过id查询(self.session, str(self.room_id), self.header)
        self.assertEqual(res_data.get('data'),None)


    def test_空间信息_02(self):
        """
        验证新增空间、通过Id查询空间并断言新增信息正确、通过id删除空间功能（已选空间类型）
        :return:
        """
        #新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        #新增区域楼栋
        feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
        feild_add_ld['propertyId'] = int(self.p_id)
        feild_add_ld['buildingName'] = "楼栋" + str(uuid.uuid1())
        res_data = Page区域或楼栋表管理.api_新增区域或楼栋表(self.session, feild_add_ld, self.header)
        self.f_id = res_data.get('data').get('id')
        #查询区域或楼栋
        res_data = Page区域或楼栋表管理.api_区域或楼栋通过id查询(self.session, str(self.f_id), self.header)
        floor_id = res_data.get('data').get('list')[0].get('id')
        #新增空间类型
        feild_add_space_type = Param_空间类型.p_add.get('同级')
        feild_add_space_type['spaceCode'] = "room"+str(uuid.uuid1())
        res_data = Page空间类型表管理.api_新增空间类型表(self.session,feild_add_space_type,self.header)
        self.space_type_id = res_data.get('data').get('id')
        #新增空间
        feild_add_space = Param_空间信息.p_add.get('空间类型2')
        feild_add_space['propertyId'] = self.p_id
        feild_add_space['buildingId'] = self.f_id
        feild_add_space['buildingFloorId'] = floor_id
        feild_add_space['buildingFloorSpaceName'] = "room "+str(uuid.uuid1())
        feild_add_space['spaceId'] = self.space_type_id
        res_data = Page楼层房间信息表管理.api_新增楼层房间信息表(self.session,feild_add_space,self.header)
        self.room_id = res_data.get('data').get('id')
        #通过id查询空间信息，断言空间信息
        res_data = Page楼层房间信息表管理.api_楼层房间信息通过id查询(self.session,str(self.room_id),self.header)
        self.assertEqual(feild_add_space.get('buildArea'),res_data.get('data').get('buildArea'))
        self.assertEqual(feild_add_space.get('buildingFloorSpaceName'),res_data.get('data').get('buildingFloorSpaceName'))
        self.assertEqual(str(feild_add_space.get('buildingId')),str(res_data.get('data').get('buildingId')))
        self.assertEqual(str(feild_add_space.get('propertyId')),str(res_data.get('data').get('propertyId')))
        self.assertEqual(str(feild_add_space.get('buildingFloorId')),str(res_data.get('data').get('buildingFloorId')))
        self.assertEqual(str(feild_add_space.get('spaceId')),str(res_data.get('data').get('spaceId')))

    def test_空间信息_03(self):
        """
        验证分页搜索空间功能、断言查询到的空间信息与新增的一致（搜索楼栋）
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        # 新增区域楼栋
        feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
        feild_add_ld['propertyId'] = int(self.p_id)
        feild_add_ld['buildingName'] = "楼栋" + str(uuid.uuid1())
        res_data = Page区域或楼栋表管理.api_新增区域或楼栋表(self.session, feild_add_ld, self.header)
        self.f_id = res_data.get('data').get('id')
        # 查询区域或楼栋
        res_data = Page区域或楼栋表管理.api_区域或楼栋通过id查询(self.session, str(self.f_id), self.header)
        floor_id = res_data.get('data').get('list')[0].get('id')
        # 新增空间
        feild_add_space = Param_空间信息.p_add.get('空间类型1')
        feild_add_space['propertyId'] = self.p_id
        feild_add_space['buildingId'] = self.f_id
        feild_add_space['buildingFloorId'] = floor_id
        feild_add_space['buildingFloorSpaceName'] = "room " + str(uuid.uuid1())
        res_data = Page楼层房间信息表管理.api_新增楼层房间信息表(self.session, feild_add_space, self.header)
        self.room_id = res_data.get('data').get('id')
        # 分页查询信息并断言
        feild_search_page = Param_空间信息.p_page.get('楼栋')
        feild_search_page['body']['propertyId'] = self.p_id
        feild_search_page['body']['buildingId'] = self.f_id
        res_data=Page楼层房间信息表管理.api_楼层房间信息分页查询(self.session,feild_search_page,self.header)
        self.assertIn(feild_add_space.get('buildingFloorSpaceName'),str(res_data.get('data')))

    def test_空间信息_04(self):
        """
        验证分页搜索空间功能、断言查询到的空间信息与新增的一致（搜索房间名称）
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        # 新增区域楼栋
        feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
        feild_add_ld['propertyId'] = int(self.p_id)
        feild_add_ld['buildingName'] = "楼栋" + str(uuid.uuid1())
        res_data = Page区域或楼栋表管理.api_新增区域或楼栋表(self.session, feild_add_ld, self.header)
        self.f_id = res_data.get('data').get('id')
        # 查询区域或楼栋
        res_data = Page区域或楼栋表管理.api_区域或楼栋通过id查询(self.session, str(self.f_id), self.header)
        floor_id = res_data.get('data').get('list')[0].get('id')
        # 新增空间
        feild_add_space = Param_空间信息.p_add.get('空间类型1')
        feild_add_space['propertyId'] = self.p_id
        feild_add_space['buildingId'] = self.f_id
        feild_add_space['buildingFloorId'] = floor_id
        feild_add_space['buildingFloorSpaceName'] = "room " + str(uuid.uuid1())
        res_data = Page楼层房间信息表管理.api_新增楼层房间信息表(self.session, feild_add_space, self.header)
        self.room_id = res_data.get('data').get('id')
        # 分页查询信息并断言
        feild_search_page = Param_空间信息.p_page.get('房间名称')
        feild_search_page['body']['propertyId'] = self.p_id
        feild_search_page['body']['buildingFloorSpaceName'] = "room"
        res_data=Page楼层房间信息表管理.api_楼层房间信息分页查询(self.session,feild_search_page,self.header)
        self.assertIn(feild_add_space.get('buildingFloorSpaceName'),str(res_data.get('data')))

    def test_空间信息_05(self):
        """
        验证分页搜索空间功能、断言查询到的空间信息与新增的一致（搜索楼栋And楼层）
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        # 新增区域楼栋
        feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
        feild_add_ld['propertyId'] = int(self.p_id)
        feild_add_ld['buildingName'] = "楼栋" + str(uuid.uuid1())
        res_data = Page区域或楼栋表管理.api_新增区域或楼栋表(self.session, feild_add_ld, self.header)
        self.f_id = res_data.get('data').get('id')
        # 查询区域或楼栋
        res_data = Page区域或楼栋表管理.api_区域或楼栋通过id查询(self.session, str(self.f_id), self.header)
        floor_id = res_data.get('data').get('list')[0].get('id')
        # 新增空间
        feild_add_space = Param_空间信息.p_add.get('空间类型1')
        feild_add_space['propertyId'] = self.p_id
        feild_add_space['buildingId'] = self.f_id
        feild_add_space['buildingFloorId'] = floor_id
        feild_add_space['buildingFloorSpaceName'] = "room " + str(uuid.uuid1())
        res_data = Page楼层房间信息表管理.api_新增楼层房间信息表(self.session, feild_add_space, self.header)
        self.room_id = res_data.get('data').get('id')
        # 分页查询信息并断言
        feild_search_page = Param_空间信息.p_page.get('楼栋And楼层')
        feild_search_page['body']['propertyId'] = self.p_id
        feild_search_page['body']['buildingId'] = self.f_id
        feild_search_page['body']['buildingFloorId'] = floor_id
        res_data=Page楼层房间信息表管理.api_楼层房间信息分页查询(self.session,feild_search_page,self.header)
        self.assertIn(feild_add_space.get('buildingFloorSpaceName'),str(res_data.get('data')))

    def test_空间信息_06(self):
        """
        验证分页搜索空间功能、断言查询到的空间信息与新增的一致（搜索楼栋And名称）
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        # 新增区域楼栋
        feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
        feild_add_ld['propertyId'] = int(self.p_id)
        feild_add_ld['buildingName'] = "楼栋" + str(uuid.uuid1())
        res_data = Page区域或楼栋表管理.api_新增区域或楼栋表(self.session, feild_add_ld, self.header)
        self.f_id = res_data.get('data').get('id')
        # 查询区域或楼栋
        res_data = Page区域或楼栋表管理.api_区域或楼栋通过id查询(self.session, str(self.f_id), self.header)
        floor_id = res_data.get('data').get('list')[0].get('id')
        # 新增空间
        feild_add_space = Param_空间信息.p_add.get('空间类型1')
        feild_add_space['propertyId'] = self.p_id
        feild_add_space['buildingId'] = self.f_id
        feild_add_space['buildingFloorId'] = floor_id
        feild_add_space['buildingFloorSpaceName'] = "room " + str(uuid.uuid1())
        res_data = Page楼层房间信息表管理.api_新增楼层房间信息表(self.session, feild_add_space, self.header)
        self.room_id = res_data.get('data').get('id')
        # 分页查询信息并断言
        feild_search_page = Param_空间信息.p_page.get('楼栋And房间名称')
        feild_search_page['body']['propertyId'] = self.p_id
        feild_search_page['body']['buildingId'] = self.f_id
        feild_search_page['body']['buildingFloorSpaceName'] = "room"
        res_data=Page楼层房间信息表管理.api_楼层房间信息分页查询(self.session,feild_search_page,self.header)
        self.assertIn(feild_add_space.get('buildingFloorSpaceName'),str(res_data.get('data')))

    # def test_空间信息_07(self):
    #     """
    #     验证批量导入房间功能、断言导入后查询到的项目信息参数与导入的一致
    #     :return:
    #     """
    #     #新增项目,获取项目id
    #     #新增楼栋,获取楼栋id
    #     #重写excel里面项目及楼栋id
    #     #导入房间（导入两个，如返回id则获取id）
    #     #查询房间并断言（有id查则用id查，没有id用名称查）
    #     #通过id删除房间
    #     #通过id删除楼栋
    #     #通过id删除项目
    #     pass
    #
    # def test_空间信息_06(self):
    #     """
    #     验证批量导入房间下载模版功能，断言成功下载
    #     :return:
    #     """
    #     #请求下载模版
    #     #断言下载返回ok
    #     pass