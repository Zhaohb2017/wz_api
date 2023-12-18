import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_企业档案, Param_项目管理, Param_楼栋信息, Param_空间信息, \
    Param_企业员工
from business.param_config.api_param.werun.设备智管.线上巡检.Param_巡检计划 import p_xmhmc
from common.Common_Base import create_phone, create_email, write_excel_xmhmc
from common.M_Crypto import rsa_encrypt
from page_object.werun.APP.Page_APP登录 import PageAPP登录
from page_object.werun.基础管理.Page_企业员工 import Page企业员工
from page_object.werun.基础管理.Page_企业档案 import Page企业档案
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case企业档案(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '企业档案'
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
        if hasattr(self, 'yg_id'):
            Page企业员工.api_删除企业员工(self.session, str(self.yg_id), self.header)
        if hasattr(self,'qy_id'):
            Page企业档案.api_删除企业(self.session, str(self.qy_id), self.header)
        if hasattr(self, 'room_id'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session, str(self.room_id), self.header)
        if hasattr(self, 'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass

    def test_企业档案_01(self):
        """
        验证新增企业、通过id查询企业验证新增参数正常、通过id删除企业功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
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
        #新增企业(依赖空间)
        feild_add_qy = Param_企业档案.p_add.get('01')
        feild_add_qy['spaceId'] = str(self.room_id)
        feild_add_qy['businessName'] = '公司名称' + str(uuid.uuid4())
        feild_add_qy['contactInformation'] = create_phone()
        feild_add_qy['contactPerson'] = '联系人'+str(uuid.uuid4())
        feild_add_qy['remark'] = '备注'+str(uuid.uuid4())
        res_data = Page企业档案.api_新增企业(self.session,feild_add_qy,self.header)
        self.qy_id = res_data.get('data').get('id')
        #通过id查询企业，断言新增参数正常
        res_data = Page企业档案.api_通过id查询企业(self.session,str(self.qy_id),self.header)
        self.assertEqual(feild_add_qy.get('spaceId'),res_data.get('data').get('spaceId'))
        self.assertEqual(feild_add_qy.get('businessName'),res_data.get('data').get('businessName'))
        self.assertEqual(feild_add_qy.get('contactInformation'),res_data.get('data').get('contactInformation'))
        self.assertEqual(feild_add_qy.get('contactPerson'),res_data.get('data').get('contactPerson'))
        self.assertEqual(feild_add_qy.get('remark'),res_data.get('data').get('remark'))
        #通过id删除企业
        res_data = Page企业档案.api_删除企业(self.session,str(self.qy_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询企业，验证删除成功
        res_data = Page企业档案.api_通过id查询企业(self.session,str(self.qy_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    def test_企业档案_02(self):
        """
        验证分页查询企业档案功能正常(关键字、所在区域、重置)
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
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
        #新增企业(依赖空间)
        feild_add_qy = Param_企业档案.p_add.get('01')
        feild_add_qy['spaceId'] = str(self.room_id)
        feild_add_qy['businessName'] = '公司名称' + str(uuid.uuid4())
        feild_add_qy['contactInformation'] = create_phone()
        feild_add_qy['contactPerson'] = '联系人'+str(uuid.uuid4())
        feild_add_qy['remark'] = '备注'+str(uuid.uuid4())
        res_data = Page企业档案.api_新增企业(self.session,feild_add_qy,self.header)
        self.qy_id = res_data.get('data').get('id')
        #通过分页查询企业，断言分页查询功能正常
        feild_page_qy = Param_企业档案.p_page.get('关键字')
        res_data = Page企业档案.api_分页查询企业(self.session,feild_page_qy,self.header)
        self.assertIn(feild_add_qy.get('businessName'),str(res_data))
        feild_page_qy = Param_企业档案.p_page.get('所在区域')
        feild_page_qy['body']['spaceId'] = self.room_id
        res_data = Page企业档案.api_分页查询企业(self.session, feild_page_qy, self.header)
        self.assertIn(feild_add_qy.get('businessName'), str(res_data))
        feild_page_qy = Param_企业档案.p_page.get('重置')
        res_data = Page企业档案.api_分页查询企业(self.session, feild_page_qy, self.header)
        self.assertNotEqual(res_data.get('data').get('records'),[])
        self.assertNotEqual(res_data.get('data').get('records'),None)
        #通过id删除企业
        res_data = Page企业档案.api_删除企业(self.session,str(self.qy_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询企业，验证删除成功
        res_data = Page企业档案.api_通过id查询企业(self.session,str(self.qy_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    def test_企业档案_03(self):
        """
        验证编辑修改企业功能,断言比对修改后的内容正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
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
        #新增企业(依赖空间)
        feild_add_qy = Param_企业档案.p_add.get('01')
        feild_add_qy['spaceId'] = str(self.room_id)
        feild_add_qy['businessName'] = '公司名称' + str(uuid.uuid4())
        feild_add_qy['contactInformation'] = create_phone()
        feild_add_qy['contactPerson'] = '联系人'+str(uuid.uuid4())
        feild_add_qy['remark'] = '备注'+str(uuid.uuid4())
        res_data = Page企业档案.api_新增企业(self.session,feild_add_qy,self.header)
        self.qy_id = res_data.get('data').get('id')
        #修改企业
        feild_upd_qy = Param_企业档案.p_upd.get('01')
        feild_upd_qy['spaceId'] = str(self.room_id)
        feild_upd_qy['id'] = self.qy_id
        feild_upd_qy['businessName'] = '公司名称' + str(uuid.uuid4())
        feild_upd_qy['contactPerson'] = '联系人'+str(uuid.uuid4())
        feild_upd_qy['contactInformation'] = create_phone()
        feild_upd_qy['remark'] = '备注'+str(uuid.uuid4())
        feild_upd_qy['spaceVos'][0]['spaceId'] = self.room_id
        feild_upd_qy['spaceVos'][0]['buildingId'] = self.f_id
        feild_upd_qy['spaceVos'][0]['buildingFloorId'] = floor_id
        res_data = Page企业档案.api_修改企业(self.session,feild_upd_qy,self.header)
        self.assertEqual(res_data.get('data'),True)
        #通过id查询企业，断言新增参数正常
        res_data = Page企业档案.api_通过id查询企业(self.session,str(self.qy_id),self.header)
        self.assertEqual(feild_upd_qy.get('spaceId'),res_data.get('data').get('spaceId'))
        self.assertEqual(feild_upd_qy.get('businessName'),res_data.get('data').get('businessName'))
        self.assertEqual(feild_upd_qy.get('contactInformation'),res_data.get('data').get('contactInformation'))
        self.assertEqual(feild_upd_qy.get('contactPerson'),res_data.get('data').get('contactPerson'))
        self.assertEqual(feild_upd_qy.get('remark'),res_data.get('data').get('remark'))
        #通过id删除企业
        res_data = Page企业档案.api_删除企业(self.session,str(self.qy_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询企业，验证删除成功
        res_data = Page企业档案.api_通过id查询企业(self.session,str(self.qy_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    def test_企业档案_04(self):
        """
        验证企业添加员工功能正常，企业添加员工后，员工正常登录
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
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
        #新增企业(依赖空间)
        feild_add_qy = Param_企业档案.p_add.get('01')
        feild_add_qy['spaceId'] = str(self.room_id)
        feild_add_qy['businessName'] = '公司名称' + str(uuid.uuid4())
        feild_add_qy['contactInformation'] = create_phone()
        feild_add_qy['contactPerson'] = '联系人'+str(uuid.uuid4())
        feild_add_qy['remark'] = '备注'+str(uuid.uuid4())
        res_data = Page企业档案.api_新增企业(self.session,feild_add_qy,self.header)
        self.qy_id = res_data.get('data').get('id')
        #添加员工
        feild_add_yg = Param_企业员工.p_add_yg.get('业主')
        feild_add_yg['sword'] = self.encrypt_pwd
        feild_add_yg['confirmSword'] = self.encrypt_pwd
        feild_add_yg['nickName'] = '昵称' + str(uuid.uuid4())
        feild_add_yg['businessIds'] = [self.qy_id]
        feild_add_yg['scabbard'] = 'user' + str(uuid.uuid4()).split('-')[-1]
        feild_add_yg['mobile'] = create_phone()
        feild_add_yg['email'] = create_email()
        res_data = Page企业员工.api_新增企业员工(self.session,feild_add_yg,self.header)
        self.assertEqual(res_data.get('ok'),True)
        self.yg_id = res_data.get('data').get('id')
        #验证员工登录成功
        feild_login_yz = Param_企业档案.p_login_yz.get('01')
        feild_login_yz['scabbard'] = feild_add_yg.get('scabbard')
        feild_login_yz['sword'] = feild_add_yg.get('sword')
        res_data = PageAPP登录.api_业主登录(self.session,feild_login_yz,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #删除员工
        res_data = Page企业员工.api_删除企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id删除企业
        res_data = Page企业档案.api_删除企业(self.session,str(self.qy_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询企业，验证删除成功
        res_data = Page企业档案.api_通过id查询企业(self.session,str(self.qy_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    # def test_企业档案_05(self):
    #     """
    #     验证企业档案，导入企业功能正常
    #     :return:
    #     """
    #     # 新增项目
    #     feild_add_p = Param_项目管理.p_add.get('学校')
    #     feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': str(self.p_id)})
    #     # 新增区域楼栋
    #     feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
    #     feild_add_ld['propertyId'] = int(self.p_id)
    #     feild_add_ld['buildingName'] = "楼栋" + str(uuid.uuid1())
    #     res_data = Page区域或楼栋表管理.api_新增区域或楼栋表(self.session, feild_add_ld, self.header)
    #     self.f_id = res_data.get('data').get('id')
    #     # 查询区域或楼栋
    #     res_data = Page区域或楼栋表管理.api_区域或楼栋通过id查询(self.session, str(self.f_id), self.header)
    #     floor_id = res_data.get('data').get('list')[0].get('id')
    #     # 新增空间
    #     feild_add_space = Param_空间信息.p_add.get('空间类型1')
    #     feild_add_space['propertyId'] = self.p_id
    #     feild_add_space['buildingId'] = self.f_id
    #     feild_add_space['buildingFloorId'] = floor_id
    #     feild_add_space['buildingFloorSpaceName'] = "room " + str(uuid.uuid1())
    #     res_data = Page楼层房间信息表管理.api_新增楼层房间信息表(self.session, feild_add_space, self.header)
    #     self.room_id = res_data.get('data').get('id')
    #
    #     qyda = Param_企业档案.p_import.get('01').copy()
    #     qyda[0] = feild_add_p.get('propertyName')
    #     qyda[1] = '哈尔滨市'
    #     qyda[2] = '南岗区'
    #     write_excel_xmhmc('./test_data/excel/xmhmc.xlsx', qyda)
    #     # 上传
    #     feild_upload_hmc = {"fileName": 'xmhmc.xlsx',"file": ('xmhmc.xlsx',open('./test_data/excel/xmhmc.xlsx', 'rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}        #导入企业
    #     feild_import_qyda = Param_企业档案.p_import.get('01')
    #     res_data = Page企业档案.api_导入企业(self.session,feild_import_qyda,self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #通过分页查询导入的企业，断言导入成功，获取企业的id

