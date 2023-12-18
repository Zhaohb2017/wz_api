import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_招商配置, Param_楼栋信息, Param_空间信息
from common.Common_Base import write_excel
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_招商配置信息表管理 import Page招商配置信息表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case招商配置(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '招商配置'
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session)
        public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        encrypt_pwd = rsa_encrypt(public_key, feild.get('sword'))
        feild['sword'] = encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(self.session, feild, {})
        self.header = {'traceId': str(uuid.uuid4()), 'Authorization': "Bearer " + res_data.get('data').get('token')}
        pass

    def tearDown(self):
        if hasattr(self, 'zspz_id'):
            Page招商配置信息表管理.api_招商配置信息通过id删除(self.session, str(self.zspz_id), self.header)
        if hasattr(self, 'zspz_id1'):
            Page招商配置信息表管理.api_招商配置信息通过id删除(self.session, str(self.zspz_id1), self.header)
        if hasattr(self,'room_id'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session,str(self.room_id),self.header)
        if hasattr(self, 'space_type_id'):
            Page空间类型表管理.api_空间类型通过id删除(self.session, str(self.space_type_id), self.header)
        if hasattr(self, 'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self,'p_id'):
            Page项目表管理.api_项目通过id删除(self.session,str(self.p_id),self.header)
        self.session.close()
        pass


    def test_招商配置_01(self):
        """
        验证招商下载模板功能正常、断言响应正常
        :return:
        """
        # 新增项目信息
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        #下载导入模版，断言下载成功
        res_data = Page招商配置信息表管理.api_下载招商配置模版(self.session,self.header)
        self.assertEqual(res_data.ok,True)
        pass

    def test_招商配置_02(self):
        """
        验证招商配置导入模版正常、断言导入参数正常（一条数据）
        :return:
        """
        #新增项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
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
        #导入招商配置
        feild_upload_data = Param_招商配置.p_upload_data.get('一条数据').copy()
        feild_upload_data[0][0] = '公司名称'+str(uuid.uuid4())
        feild_upload_data[0][1] = feild_add['propertyName']
        feild_upload_data[0][2] = '哈尔滨市'
        feild_upload_data[0][3] = '南岗区'
        feild_upload_data[0][4] = feild_add_ld['buildingName']
        feild_upload_data[0][5] = feild_add_space['buildingFloorSpaceName']
        write_excel('./test_data/excel/zspz.xlsx', feild_upload_data)
        # 上传
        feild_upload_excel = {"fileName": 'zspz.xlsx',"file": ('zspz.xlsx',open('./test_data/excel/zspz.xlsx', 'rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
        res_data = Page招商配置信息表管理.api_上传导入招商配置(self.session,feild_upload_excel,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #列表查询招商配置，断言参数正确
        feild_page = Param_招商配置.p_page.get('公司名称')
        res_data = Page招商配置信息表管理.api_招商配置信息分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_upload_data[0][0],str(res_data))
        self.assertIn(feild_upload_data[0][1],str(res_data))
        self.assertIn('Nangang District',str(res_data))
        self.assertIn(feild_upload_data[0][5],str(res_data))
        self.assertIn(feild_upload_data[0][6],str(res_data.get('data')['records'][0]['rentArea']))
        self.assertEqual(feild_upload_data[0][7],str(res_data.get('data')['records'][0]['currYearRevenue']))
        self.assertEqual(feild_upload_data[0][8],str(res_data.get('data')['records'][0]['currYearTax']))
        self.assertEqual(feild_upload_data[0][9],res_data.get('data')['records'][0]['industry'])
        self.assertEqual('merchant_signing',res_data.get('data')['records'][0]['contractStatus'])
        self.zspz_id = res_data.get('data').get('records')[0]['id']
        #通过id删除招商配置
        res_data = Page招商配置信息表管理.api_招商配置信息通过id删除(self.session,str(self.zspz_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #列表查询招商配置，断言删除正常
        res_data = Page招商配置信息表管理.api_招商配置信息分页查询(self.session, feild_page, self.header)
        self.assertNotIn(feild_upload_data[0][0], str(res_data))
        pass

    def test_招商配置_03(self):
        """
        验证招商配置导入模版正常、断言导入参数正常（多条数据）
        :return:
        """
        #新增项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
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
        #导入招商配置
        feild_upload_data = Param_招商配置.p_upload_data.get('多条数据').copy()
        feild_upload_data[0][0] = '公司名称'+str(uuid.uuid4())
        feild_upload_data[0][1] = feild_add['propertyName']
        feild_upload_data[0][2] = '哈尔滨市'
        feild_upload_data[0][3] = '南岗区'
        feild_upload_data[0][4] = feild_add_ld['buildingName']
        feild_upload_data[0][5] = feild_add_space['buildingFloorSpaceName']
        feild_upload_data[1][0] = '公司名称'+str(uuid.uuid4())
        feild_upload_data[1][1] = feild_add['propertyName']
        feild_upload_data[1][2] = '哈尔滨市'
        feild_upload_data[1][3] = '南岗区'
        feild_upload_data[1][4] = feild_add_ld['buildingName']
        feild_upload_data[1][5] = feild_add_space['buildingFloorSpaceName']
        write_excel('./test_data/excel/zspz2.xlsx', feild_upload_data)
        # 上传
        feild_upload_excel = {"fileName": 'zspz2.xlsx',"file": ('zspz2.xlsx',open('./test_data/excel/zspz2.xlsx', 'rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
        res_data = Page招商配置信息表管理.api_上传导入招商配置(self.session,feild_upload_excel,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #列表查询招商配置，断言参数正确
        feild_page = Param_招商配置.p_page.get('公司名称')
        res_data = Page招商配置信息表管理.api_招商配置信息分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_upload_data[0][0],str(res_data))
        self.assertIn(feild_upload_data[1][0],str(res_data))
        self.zspz_id = res_data.get('data').get('records')[0]['id']
        self.zspz_id1 = res_data.get('data').get('records')[1]['id']
        pass

    def test_招商配置_04(self):
        """
        验证招商配置分页查询功能正常（所在地区、行政区、公司名称、重置）
        :return:
        """
        #新增项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
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
        #导入招商配置
        feild_upload_data = Param_招商配置.p_upload_data.get('一条数据').copy()
        feild_upload_data[0][0] = '公司名称'+str(uuid.uuid4())
        feild_upload_data[0][1] = feild_add['propertyName']
        feild_upload_data[0][2] = '哈尔滨市'
        feild_upload_data[0][3] = '南岗区'
        feild_upload_data[0][4] = feild_add_ld['buildingName']
        feild_upload_data[0][5] = feild_add_space['buildingFloorSpaceName']
        write_excel('./test_data/excel/zspz.xlsx', feild_upload_data)
        # 上传
        feild_upload_excel = {"fileName": 'zspz.xlsx',"file": ('zspz.xlsx',open('./test_data/excel/zspz.xlsx', 'rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
        res_data = Page招商配置信息表管理.api_上传导入招商配置(self.session,feild_upload_excel,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #列表查询招商配置，断言参数正确
        feild_page = Param_招商配置.p_page.get('公司名称')
        res_data = Page招商配置信息表管理.api_招商配置信息分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_upload_data[0][0],str(res_data))
        self.zspz_id = res_data.get('data').get('records')[0]['id']
        feild_page = Param_招商配置.p_page.get('所在地区')
        res_data = Page招商配置信息表管理.api_招商配置信息分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_upload_data[0][0],str(res_data))
        feild_page = Param_招商配置.p_page.get('行政区')
        res_data = Page招商配置信息表管理.api_招商配置信息分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_upload_data[0][0],str(res_data))
        feild_page = Param_招商配置.p_page.get('重置')
        res_data = Page招商配置信息表管理.api_招商配置信息分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_upload_data[0][0],str(res_data))
        pass

