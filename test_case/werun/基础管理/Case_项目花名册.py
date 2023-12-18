import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_项目花名册
from common.Common_Base import write_excel, create_phone
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_项目花名册管理 import Page项目花名册管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case项目花名册(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '项目花名册'
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
        if hasattr(self,'xmhmc_id'):
            Page项目花名册管理.api_项目花名册通过id删除(self.session, str(self.xmhmc_id), self.header)
        if hasattr(self,'xmhmc_id1'):
            Page项目花名册管理.api_项目花名册通过id删除(self.session, str(self.xmhmc_id1), self.header)
        if hasattr(self,'p_id'):
            Page项目表管理.api_项目通过id删除(self.session,str(self.p_id),self.header)
        self.session.close()
        pass

    def test_项目花名册_01(self):
        """
        验证项目花名册下载模板功能正常
        :return:
        """
        #新增项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        #下载模版
        res_data = Page项目花名册管理.api_下载花名册导入模版(self.session,self.header)
        self.assertEqual(res_data.ok,True)
        pass

    def test_项目花名册_02(self):
        """
        验证导入项目花名册Excel文档，断言查询参数与导入参数一致（单条数据）
        :return:
        """
        #新增项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        #导入花名册
        feild_upload_data = Param_项目花名册.p_upload_data.get('单条数据').copy()
        feild_upload_data[0][0] = feild_add['propertyName']
        feild_upload_data[0][1] = '哈尔滨市'
        feild_upload_data[0][2] = '南岗区'
        feild_upload_data[0][3] = '花名'+str(uuid.uuid4())
        feild_upload_data[0][4] = create_phone()
        feild_upload_data[0][5] = '0'
        write_excel('./test_data/excel/xmhmc1.xlsx', feild_upload_data)
        # 上传
        feild_upload_hmc = {"fileName": 'xmhmc1.xlsx', "file": ('xmhmc1.xlsx', open('./test_data/excel/xmhmc1.xlsx', 'rb'),
                                                               'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
        res_data = Page项目花名册管理.api_导入项目花名册(self.session, feild_upload_hmc, self.header)
        self.assertEqual(res_data.get('ok'),True)
        #分页查询，断言新增的参数一致
        feild_page = Param_项目花名册.p_page.get('员工姓名')
        res_data = Page项目花名册管理.api_项目花名册分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_add['propertyName'],str(res_data))
        self.assertIn(feild_upload_data[0][3],str(res_data))
        self.xmhmc_id = res_data.get('data').get('records')[0]['id']
        #通过id删除花名册
        res_data = Page项目花名册管理.api_项目花名册通过id删除(self.session,str(self.xmhmc_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #分页查询，验证删除正常
        res_data = Page项目花名册管理.api_项目花名册分页查询(self.session, feild_page, self.header)
        self.assertNotIn(feild_add['propertyName'], str(res_data))
        pass

    def test_项目花名册_03(self):
        """
        验证导入项目花名册Excel文档，断言查询参数与导入参数一致（多条数据）
        :return:
        """
        #新增项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        #导入花名册
        feild_upload_data = Param_项目花名册.p_upload_data.get('多条数据').copy()
        feild_upload_data[0][0] = feild_add['propertyName']
        feild_upload_data[0][1] = '哈尔滨市'
        feild_upload_data[0][2] = '南岗区'
        feild_upload_data[0][3] = '花名'+str(uuid.uuid4())
        feild_upload_data[0][4] = create_phone()
        feild_upload_data[0][5] = '0'
        feild_upload_data[1][0] = feild_add['propertyName']
        feild_upload_data[1][1] = '哈尔滨市'
        feild_upload_data[1][2] = '南岗区'
        feild_upload_data[1][3] = '花名'+str(uuid.uuid4())
        feild_upload_data[1][4] = create_phone()
        feild_upload_data[1][5] = '1'
        write_excel('./test_data/excel/xmhmc2.xlsx', feild_upload_data)
        # 上传
        feild_upload_hmc = {"fileName": 'xmhmc2.xlsx', "file": ('xmhmc2.xlsx', open('./test_data/excel/xmhmc2.xlsx', 'rb'),
                                                               'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
        res_data = Page项目花名册管理.api_导入项目花名册(self.session, feild_upload_hmc, self.header)
        self.assertEqual(res_data.get('ok'),True)
        #分页查询，断言新增的参数一致
        feild_page = Param_项目花名册.p_page.get('员工姓名')
        res_data = Page项目花名册管理.api_项目花名册分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_add['propertyName'],str(res_data))
        self.assertIn(feild_upload_data[0][3],str(res_data))
        self.assertIn(feild_upload_data[1][3],str(res_data))
        self.xmhmc_id = res_data.get('data').get('records')[0]['id']
        self.xmhmc_id1 = res_data.get('data').get('records')[1]['id']
        pass

    def test_项目花名册_04(self):
        """
        验证分页查询功能，断言分页查询返回正确（姓名、手机号、重置）
        :return:
        """
        # 新增项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 导入花名册
        feild_upload_data = Param_项目花名册.p_upload_data.get('单条数据').copy()
        feild_upload_data[0][0] = feild_add['propertyName']
        feild_upload_data[0][1] = '哈尔滨市'
        feild_upload_data[0][2] = '南岗区'
        feild_upload_data[0][3] = '花名' + str(uuid.uuid4())
        feild_upload_data[0][4] = create_phone()
        feild_upload_data[0][5] = '0'
        write_excel('./test_data/excel/xmhmc1.xlsx', feild_upload_data)
        # 上传
        feild_upload_hmc = {"fileName": 'xmhmc1.xlsx',
                            "file": ('xmhmc1.xlsx', open('./test_data/excel/xmhmc1.xlsx', 'rb'),
                                     'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
        res_data = Page项目花名册管理.api_导入项目花名册(self.session, feild_upload_hmc, self.header)
        self.assertEqual(res_data.get('ok'), True)
        # 分页查询，断言新增的参数一致
        feild_page = Param_项目花名册.p_page.get('员工姓名')
        res_data = Page项目花名册管理.api_项目花名册分页查询(self.session, feild_page, self.header)
        self.assertIn(feild_add['propertyName'], str(res_data))
        self.assertIn(feild_upload_data[0][3], str(res_data))
        self.xmhmc_id = res_data.get('data').get('records')[0]['id']
        feild_page = Param_项目花名册.p_page.get('重置')
        res_data = Page项目花名册管理.api_项目花名册分页查询(self.session, feild_page, self.header)
        self.assertIn(feild_upload_data[0][3], str(res_data))
        pass

    def test_项目花名册_05(self):
        """
        验证项目花名册导出数据接口返回正常
        :return:
        """
        #新增项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 导入花名册
        feild_upload_data = Param_项目花名册.p_upload_data.get('单条数据').copy()
        feild_upload_data[0][0] = feild_add['propertyName']
        feild_upload_data[0][1] = '哈尔滨市'
        feild_upload_data[0][2] = '南岗区'
        feild_upload_data[0][3] = '花名' + str(uuid.uuid4())
        feild_upload_data[0][4] = create_phone()
        feild_upload_data[0][5] = '0'
        write_excel('./test_data/excel/xmhmc1.xlsx', feild_upload_data)
        # 上传
        feild_upload_hmc = {"fileName": 'xmhmc1.xlsx',
                            "file": ('xmhmc1.xlsx', open('./test_data/excel/xmhmc1.xlsx', 'rb'),
                                     'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
        res_data = Page项目花名册管理.api_导入项目花名册(self.session, feild_upload_hmc, self.header)
        self.assertEqual(res_data.get('ok'), True)
        # 分页查询，断言新增的参数一致
        feild_page = Param_项目花名册.p_page.get('员工姓名')
        res_data = Page项目花名册管理.api_项目花名册分页查询(self.session, feild_page, self.header)
        self.xmhmc_id = res_data.get('data').get('records')[0]['id']
        #导出数据
        res_data = Page项目花名册管理.api_导出花名册(self.session,self.header)
        self.assertEqual(res_data.ok,True)
        pass
