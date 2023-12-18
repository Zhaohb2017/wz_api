import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_企业员工, Param_项目管理, Param_楼栋信息, Param_空间信息, \
    Param_企业档案
from common.Common_Base import create_phone, create_email
from common.M_Crypto import rsa_encrypt
from page_object.werun.APP.Page_APP登录 import PageAPP登录
from page_object.werun.基础管理.Page_企业员工 import Page企业员工
from page_object.werun.基础管理.Page_企业档案 import Page企业档案
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case企业员工(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '企业员工'
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
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.session.close()
        pass

    @ddt.data(*Param_企业员工.p_add_yg.keys())
    def test_企业员工_01(self,key):
        """
        验证新增企业员工、通过id查询企业员工断言新增参数正确、删除企业员工功能正常
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
        # 新增企业(依赖空间)
        feild_add_qy = Param_企业档案.p_add.get('01')
        feild_add_qy['spaceId'] = str(self.room_id)
        feild_add_qy['businessName'] = '公司名称' + str(uuid.uuid4())
        feild_add_qy['contactInformation'] = create_phone()
        feild_add_qy['contactPerson'] = '联系人' + str(uuid.uuid4())
        feild_add_qy['remark'] = '备注' + str(uuid.uuid4())
        res_data = Page企业档案.api_新增企业(self.session, feild_add_qy, self.header)
        self.qy_id = res_data.get('data').get('id')
        #新增企业员工(依赖企业)
        feild_add_yg = Param_企业员工.p_add_yg.get(key)
        feild_add_yg['sword'] = self.encrypt_pwd
        feild_add_yg['confirmSword'] = self.encrypt_pwd
        feild_add_yg['nickName'] = '昵称' + str(uuid.uuid4())
        feild_add_yg['businessIds'] = [self.qy_id]
        feild_add_yg['scabbard'] = 'user' + str(uuid.uuid4()).split('-')[-1]
        feild_add_yg['mobile'] = create_phone()
        feild_add_yg['email'] = create_email()
        res_data = Page企业员工.api_新增企业员工(self.session,feild_add_yg,self.header)
        self.yg_id = res_data.get('data').get('id')
        #通过id查询企业员工，断言新增参数
        res_data = Page企业员工.api_通过id查询企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(feild_add_yg.get('nickName'),res_data.get('data').get('nickName'))
        self.assertEqual(str(feild_add_yg.get('businessIds')[0]),res_data.get('data').get('strBusinessIds'))
        self.assertEqual(feild_add_yg.get('mobile'),res_data.get('data').get('mobile'))
        self.assertEqual(feild_add_yg.get('email'),res_data.get('data').get('email'))
        #使用企业员工登陆APP,验证登陆成功
        feild_login_yg = Param_企业员工.p_login_yz.get('01')
        feild_login_yg['scabbard'] = feild_add_yg.get('scabbard')
        feild_login_yg['sword'] = feild_add_yg.get('sword')
        res_data = PageAPP登录.api_业主登录(self.session,feild_login_yg,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id删除企业员工
        res_data = Page企业员工.api_删除企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询企业员工，验证删除成功
        res_data = Page企业员工.api_通过id查询企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    def test_企业员工_02(self):
        """
        验证分页查询企业员工功能正常
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
        # 新增企业(依赖空间)
        feild_add_qy = Param_企业档案.p_add.get('01')
        feild_add_qy['spaceId'] = str(self.room_id)
        feild_add_qy['businessName'] = '公司名称' + str(uuid.uuid4())
        feild_add_qy['contactInformation'] = create_phone()
        feild_add_qy['contactPerson'] = '联系人' + str(uuid.uuid4())
        feild_add_qy['remark'] = '备注' + str(uuid.uuid4())
        res_data = Page企业档案.api_新增企业(self.session, feild_add_qy, self.header)
        self.qy_id = res_data.get('data').get('id')
        #新增企业员工(依赖企业)
        feild_add_yg = Param_企业员工.p_add_yg.get('业主')
        feild_add_yg['sword'] = self.encrypt_pwd
        feild_add_yg['confirmSword'] = self.encrypt_pwd
        feild_add_yg['nickName'] = '昵称' + str(uuid.uuid4())
        feild_add_yg['businessIds'] = [self.qy_id]
        feild_add_yg['scabbard'] = 'user' + str(uuid.uuid4()).split('-')[-1]
        feild_add_yg['mobile'] = create_phone()
        feild_add_yg['email'] = create_email()
        res_data = Page企业员工.api_新增企业员工(self.session,feild_add_yg,self.header)
        self.yg_id = res_data.get('data').get('id')
        #分页查询企业员工，断言新增参数
        feild_page_yg = Param_企业员工.p_page_yg.get('姓名')
        res_data = Page企业员工.api_分页查询企业员工(self.session,feild_page_yg,self.header)
        self.assertIn(feild_add_yg.get('nickName'),str(res_data))
        # feild_page_yg = Param_企业员工.p_page_yg.get('手机号')
        # feild_page_yg['body']['employee'] = feild_add_yg.get('mobile')
        # res_data = Page企业员工.api_分页查询企业员工(self.session, feild_page_yg, self.header)
        # self.assertIn(feild_add_yg.get('nickName'), str(res_data))
        feild_page_yg = Param_企业员工.p_page_yg.get('企业')
        feild_page_yg['body']['businessId'] = self.qy_id
        res_data = Page企业员工.api_分页查询企业员工(self.session, feild_page_yg, self.header)
        self.assertIn(feild_add_yg.get('nickName'), str(res_data))
        feild_page_yg = Param_企业员工.p_page_yg.get('重置')
        res_data = Page企业员工.api_分页查询企业员工(self.session, feild_page_yg, self.header)
        self.assertNotEqual(res_data.get('data').get('records'), None)
        self.assertNotEqual(res_data.get('data').get('records'), [])
        #通过id删除企业员工
        res_data = Page企业员工.api_删除企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询企业员工，验证删除成功
        res_data = Page企业员工.api_通过id查询企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    def test_企业员工_03(self):
        """
        验证编辑修改企业员工功能、通过id查询企业员工断言修改参数正确
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = res_data.get('data').get('id')
        self.header.update({'propertyId': str(self.p_id)})
        # 新增区域楼栋
        feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
        feild_add_ld['propertyId'] = self.p_id
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
        # 新增企业(依赖空间)
        feild_add_qy = Param_企业档案.p_add.get('01')
        feild_add_qy['spaceId'] = str(self.room_id)
        feild_add_qy['businessName'] = '公司名称' + str(uuid.uuid4())
        feild_add_qy['contactInformation'] = create_phone()
        feild_add_qy['contactPerson'] = '联系人' + str(uuid.uuid4())
        feild_add_qy['remark'] = '备注' + str(uuid.uuid4())
        res_data = Page企业档案.api_新增企业(self.session, feild_add_qy, self.header)
        self.qy_id = res_data.get('data').get('id')
        #新增企业员工(依赖企业)
        feild_add_yg = Param_企业员工.p_add_yg.get('业主')
        feild_add_yg['sword'] = self.encrypt_pwd
        feild_add_yg['confirmSword'] = self.encrypt_pwd
        feild_add_yg['nickName'] = '昵称' + str(uuid.uuid4())
        feild_add_yg['businessIds'] = [self.qy_id]
        feild_add_yg['scabbard'] = 'user' + str(uuid.uuid4()).split('-')[-1]
        feild_add_yg['mobile'] = create_phone()
        feild_add_yg['email'] = create_email()
        res_data = Page企业员工.api_新增企业员工(self.session,feild_add_yg,self.header)
        self.yg_id = res_data.get('data').get('id')
        #修改企业员工
        feild_upd_yg = Param_企业员工.p_upd_yg.get('01')
        feild_upd_yg['id'] = self.yg_id
        feild_upd_yg['scabbard'] = feild_add_yg.get('scabbard')
        feild_upd_yg['nickName'] = '昵称' + str(uuid.uuid4()).split('-')[-1]
        feild_upd_yg['email'] = create_email()
        feild_upd_yg['mobile'] = create_phone()
        feild_upd_yg['propertyId'] = self.p_id
        feild_upd_yg['businessName'] = feild_add_qy['businessName']
        feild_upd_yg['businessIds'] = [self.qy_id]
        feild_upd_yg['strBusinessIds'] = str(self.qy_id)
        res_data = Page企业员工.api_修改企业员工(self.session,feild_upd_yg,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询企业员工，断言新增参数
        res_data = Page企业员工.api_通过id查询企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(feild_upd_yg.get('nickName'),res_data.get('data').get('nickName'))
        self.assertEqual(str(feild_upd_yg.get('businessIds')[0]),res_data.get('data').get('strBusinessIds'))
        self.assertEqual(feild_upd_yg.get('mobile'),res_data.get('data').get('mobile'))
        self.assertEqual(feild_upd_yg.get('email'),res_data.get('data').get('email'))
        #通过id删除企业员工
        res_data = Page企业员工.api_删除企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询企业员工，验证删除成功
        res_data = Page企业员工.api_通过id查询企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    def test_企业员工_04(self):
        """
        验证新增企业员工启用禁用功能，启用时登录成功，禁用时登录失败
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
        # 新增企业(依赖空间)
        feild_add_qy = Param_企业档案.p_add.get('01')
        feild_add_qy['spaceId'] = str(self.room_id)
        feild_add_qy['businessName'] = '公司名称' + str(uuid.uuid4())
        feild_add_qy['contactInformation'] = create_phone()
        feild_add_qy['contactPerson'] = '联系人' + str(uuid.uuid4())
        feild_add_qy['remark'] = '备注' + str(uuid.uuid4())
        res_data = Page企业档案.api_新增企业(self.session, feild_add_qy, self.header)
        self.qy_id = res_data.get('data').get('id')
        #新增企业员工(依赖企业)
        feild_add_yg = Param_企业员工.p_add_yg.get('业主')
        feild_add_yg['sword'] = self.encrypt_pwd
        feild_add_yg['confirmSword'] = self.encrypt_pwd
        feild_add_yg['nickName'] = '昵称' + str(uuid.uuid4())
        feild_add_yg['businessIds'] = [self.qy_id]
        feild_add_yg['scabbard'] = 'user' + str(uuid.uuid4()).split('-')[-1]
        feild_add_yg['mobile'] = create_phone()
        feild_add_yg['email'] = create_email()
        res_data = Page企业员工.api_新增企业员工(self.session,feild_add_yg,self.header)
        self.yg_id = res_data.get('data').get('id')
        #通过id查询企业员工，断言新增参数
        res_data = Page企业员工.api_通过id查询企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(feild_add_yg.get('nickName'),res_data.get('data').get('nickName'))
        self.assertEqual(str(feild_add_yg.get('businessIds')[0]),res_data.get('data').get('strBusinessIds'))
        self.assertEqual(feild_add_yg.get('mobile'),res_data.get('data').get('mobile'))
        self.assertEqual(feild_add_yg.get('email'),res_data.get('data').get('email'))
        #禁用
        feild_off = Param_企业员工.p_on_off.get('禁用')
        feild_off['id'] = self.yg_id
        res_data = Page企业员工.api_企业员工启用禁用(self.session,feild_off,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #登录失败
        feild_login_yg = Param_企业员工.p_login_yz.get('01')
        feild_login_yg['scabbard'] = feild_add_yg.get('scabbard')
        feild_login_yg['sword'] = feild_add_yg.get('sword')
        res_data = PageAPP登录.api_业主登录(self.session, feild_login_yg, self.header)
        self.assertEqual(res_data.get('ok'), False)
        #启用
        feild_on = Param_企业员工.p_on_off.get('启用')
        feild_on['id'] = self.yg_id
        res_data = Page企业员工.api_企业员工启用禁用(self.session,feild_on,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #使用企业员工登陆APP,验证登陆成功
        res_data = PageAPP登录.api_业主登录(self.session,feild_login_yg,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id删除企业员工
        res_data = Page企业员工.api_删除企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(res_data.get('ok'),True)

    def test_企业员工_05(self):
        """
        验证企业员工重置密码功能，使用新密码登陆成功
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
        # 新增企业(依赖空间)
        feild_add_qy = Param_企业档案.p_add.get('01')
        feild_add_qy['spaceId'] = str(self.room_id)
        feild_add_qy['businessName'] = '公司名称' + str(uuid.uuid4())
        feild_add_qy['contactInformation'] = create_phone()
        feild_add_qy['contactPerson'] = '联系人' + str(uuid.uuid4())
        feild_add_qy['remark'] = '备注' + str(uuid.uuid4())
        res_data = Page企业档案.api_新增企业(self.session, feild_add_qy, self.header)
        self.qy_id = res_data.get('data').get('id')
        #新增企业员工(依赖企业)
        feild_add_yg = Param_企业员工.p_add_yg.get('业主')
        feild_add_yg['sword'] = self.encrypt_pwd
        feild_add_yg['confirmSword'] = self.encrypt_pwd
        feild_add_yg['nickName'] = '昵称' + str(uuid.uuid4())
        feild_add_yg['businessIds'] = [self.qy_id]
        feild_add_yg['scabbard'] = 'user' + str(uuid.uuid4()).split('-')[-1]
        feild_add_yg['mobile'] = create_phone()
        feild_add_yg['email'] = create_email()
        res_data = Page企业员工.api_新增企业员工(self.session,feild_add_yg,self.header)
        self.yg_id = res_data.get('data').get('id')
        #通过id查询企业员工，断言新增参数
        res_data = Page企业员工.api_通过id查询企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(feild_add_yg.get('nickName'),res_data.get('data').get('nickName'))
        self.assertEqual(str(feild_add_yg.get('businessIds')[0]),res_data.get('data').get('strBusinessIds'))
        self.assertEqual(feild_add_yg.get('mobile'),res_data.get('data').get('mobile'))
        self.assertEqual(feild_add_yg.get('email'),res_data.get('data').get('email'))
        #重置密码
        feild_reset_pwd = Param_企业员工.p_reset.get('01')
        feild_reset_pwd['id'] = self.yg_id
        new_pwd = rsa_encrypt(self.public_key, 'Webuild114')
        feild_reset_pwd['sword'] = new_pwd
        res_data = Page企业员工.api_企业员工重置密码(self.session,feild_reset_pwd,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #登录成功
        feild_login_yg = Param_企业员工.p_login_yz.get('01')
        feild_login_yg['scabbard'] = feild_add_yg.get('scabbard')
        feild_login_yg['sword'] = feild_reset_pwd.get('sword')
        res_data = PageAPP登录.api_业主登录(self.session, feild_login_yg, self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过id删除企业员工
        res_data = Page企业员工.api_删除企业员工(self.session,str(self.yg_id),self.header)
        self.assertEqual(res_data.get('ok'),True)

