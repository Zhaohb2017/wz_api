import copy
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.信息发布 import Param_播放设备
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_设备类型, Param_项目管理, Param_空间信息, Param_楼栋信息
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from common.M_Crypto import rsa_encrypt
from page_object.werun.信息发布 import Page_播放设备
from page_object.werun.信息发布.Page_播放设备 import Page播放设备
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case播放设备(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '播放设备'
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
        if hasattr(self,'tz_id'):
            Page播放设备.api_播放设备通过id删除(self.session, str(self.tz_id), self.header)
        if hasattr(self, 's_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.s_id), self.header)
        if hasattr(self, 'sub_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.s_id), self.header)
        if hasattr(self, 'fs_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.fs_id), self.header)
        if hasattr(self, 's_id2'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.s_id2), self.header)
        if hasattr(self, 'room_id'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session, str(self.room_id), self.header)
        if hasattr(self, 'room_id2'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session, str(self.room_id2), self.header)
        if hasattr(self, 'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass

    def test_播放设备_01(self):
        """
        验证新增播放设备功能，通过id查询播放设备参数正确，通过id删除播放设备功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级
        feild_add = Param_设备类型.p_add.get('一级设备')
        feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
        self.fs_id = res_data.get('data').get('id')
        # 新增下级
        feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
        feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['parentId'] = self.fs_id
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
        self.s_id = res_data.get('data').get('id')
        # 新增区域楼栋
        feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
        feild_add_ld['propertyId'] = int(self.p_id)
        feild_add_ld['buildingName'] = self.case_name + str(uuid.uuid1())
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
        #新增播放设备
        feild_add_tz = Param_播放设备.p_add.get('使用中')
        feild_add_tz['spaceId'] = self.room_id
        feild_add_tz['facCategoryId'] = self.s_id
        feild_add_tz['facCateCode'] = feild_add.get('facCateCode')
        feild_add_tz['facName'] = self.case_name+str(uuid.uuid4())
        feild_add_tz['facCode'] = self.case_name+str(uuid.uuid4())
        res_data = Page播放设备.api_新增播放设备(self.session,feild_add_tz,self.header)
        self.tz_id = res_data.get('data').get('id')
        #通过id查询新增设备参数正确
        res_data = Page播放设备.api_播放设备通过id查询(self.session,str(self.tz_id),self.header)
        self.assertEqual(feild_add_tz.get('facName'),res_data.get('data').get('facName'))
        self.assertEqual(feild_add_tz.get('facCode'),res_data.get('data').get('facCode'))
        self.assertEqual(feild_add_tz.get('facCategoryId'),res_data.get('data').get('facCategoryId'))
        self.assertEqual(feild_add_tz.get('assetStatus'),res_data.get('data').get('assetStatus'))
        self.assertEqual(feild_add_tz.get('facLinkCode'),res_data.get('data').get('facLinkCode'))
        self.assertEqual(feild_add_tz.get('facBimCode'),res_data.get('data').get('facBimCode'))
        self.assertEqual(str(feild_add_tz.get('serviceLife')),str(res_data.get('data').get('serviceLife')))
        self.assertEqual(feild_add_tz.get('facImportance'),res_data.get('data').get('facImportance'))
        self.assertEqual(feild_add_tz.get('brandName'),res_data.get('data').get('brandName'))
        self.assertEqual(feild_add_tz.get('manufacturer'),res_data.get('data').get('manufacturer'))
        self.assertEqual(feild_add_tz.get('modelName'),res_data.get('data').get('modelName'))
        self.assertEqual(feild_add_tz.get('oldFacCode'),res_data.get('data').get('oldFacCode'))
        self.assertEqual(feild_add_tz.get('remark'),res_data.get('data').get('remark'))
        self.assertEqual(feild_add_tz.get('supplierName'),res_data.get('data').get('supplierName'))
        self.assertEqual(feild_add_tz.get('contractNo'),res_data.get('data').get('contractNo'))
        self.assertEqual(feild_add_tz.get('supplierPerson'),res_data.get('data').get('supplierPerson'))
        self.assertEqual(feild_add_tz.get('supplierPhone'),res_data.get('data').get('supplierPhone'))
        self.assertIn(str(feild_add_tz.get('purchasePrice')),str(res_data.get('data').get('purchasePrice')))
        #通过id删除播放
        res_data = Page播放设备.api_播放设备通过id删除(self.session,str(self.tz_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询台账，断言台账已删除
        res_data = Page播放设备.api_播放设备通过id查询(self.session, str(self.tz_id), self.header)
        self.assertEqual(res_data.get('data'), None)
        pass

    def test_播放设备_02(self):
        """
        验证播放设备分页查询功能，断言查询到的内容正确
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级
        feild_add = Param_设备类型.p_add.get('一级设备')
        feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
        self.fs_id = res_data.get('data').get('id')
        # 新增下级
        feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
        feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['parentId'] = self.fs_id
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
        self.s_id = res_data.get('data').get('id')
        # 新增区域楼栋
        feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
        feild_add_ld['propertyId'] = int(self.p_id)
        feild_add_ld['buildingName'] = self.case_name + str(uuid.uuid1())
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
        #新增播放设备
        feild_add_tz = Param_播放设备.p_add.get("使用中")
        feild_add_tz['spaceId'] = self.room_id
        feild_add_tz['facCategoryId'] = self.s_id
        feild_add_tz['facCateCode'] = feild_add.get('facCateCode')
        feild_add_tz['facName'] = self.case_name+str(uuid.uuid4())
        feild_add_tz['facCode'] = self.case_name+str(uuid.uuid4())
        res_data = Page播放设备.api_新增播放设备(self.session,feild_add_tz,self.header)
        self.tz_id = res_data.get('data').get('id')
        #分页查询新增设备参数正确
        feild_page = Param_播放设备.p_page.get('设备位置')
        feild_page['body']['facCategoryId'] = feild_add_tz.get('facCategoryId')
        feild_page['body']['buildingId'] = self.f_id
        feild_page['body']['buildingFloorId'] = floor_id
        feild_page['body']['buildingFloorSpaceId'] = self.room_id
        feild_page['body']['building'] = [self.f_id,floor_id,self.room_id]
        res_data = Page播放设备.api_播放设备分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_add_tz.get('facName'),str(res_data.get('data')))
        pass

    def test_播放设备_03(self):
        """
        验证_播放设备编辑修改功能，通过id查询更新后的_播放设备参数正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级
        feild_add_lx_p = Param_设备类型.p_add.get('一级设备')
        feild_add_lx_p['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add_lx_p['facCateCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_lx_p, self.header)
        self.fs_id = res_data.get('data').get('id')
        #新增设备类型
        feild_add_lx_s1 = Param_设备类型.p_add_sub.get('下级设备类型').copy()
        feild_add_lx_s1['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add_lx_s1['facCateCode'] = self.case_name + str(uuid.uuid4())
        feild_add_lx_s1['parentId'] = self.fs_id
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_lx_s1, self.header)
        self.s_id = res_data.get('data').get('id')

        feild_add_lx_s2 = Param_设备类型.p_add_sub.get('下级设备类型').copy()
        feild_add_lx_s2['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add_lx_s2['facCateCode'] = self.case_name + str(uuid.uuid4())
        feild_add_lx_s2['parentId'] = self.fs_id
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_lx_s2, self.header)
        self.s_id2 = res_data.get('data').get('id')
        # 新增区域楼栋
        feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
        feild_add_ld['propertyId'] = int(self.p_id)
        feild_add_ld['buildingName'] = self.case_name + str(uuid.uuid1())
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

        feild_add_space = Param_空间信息.p_add.get('空间类型1')
        feild_add_space['propertyId'] = self.p_id
        feild_add_space['buildingId'] = self.f_id
        feild_add_space['buildingFloorId'] = floor_id
        feild_add_space['buildingFloorSpaceName'] = "room " + str(uuid.uuid1())
        res_data = Page楼层房间信息表管理.api_新增楼层房间信息表(self.session, feild_add_space, self.header)
        self.room_id2 = res_data.get('data').get('id')
        #新增_播放设备
        feild_add_tz = Param_播放设备.p_add.get('使用中')
        feild_add_tz['spaceId'] = self.room_id
        feild_add_tz['facCategoryId'] = self.s_id
        feild_add_tz['facCateCode'] = feild_add_lx_s1.get('facCateCode')
        feild_add_tz['facName'] = self.case_name+str(uuid.uuid4())
        feild_add_tz['facCode'] = self.case_name+str(uuid.uuid4())
        res_data = Page播放设备.api_新增播放设备(self.session,feild_add_tz,self.header)
        self.tz_id = res_data.get('data').get('id')
        #修改播放设备
        feild_upd = Param_设备台账.p_upd.get('使用中')
        feild_upd['facCateCode'] = feild_add_lx_s2['facCateCode']
        feild_upd['spaceId'] = self.room_id2
        feild_upd['id'] = self.tz_id
        feild_upd['facName'] = self.case_name + str(uuid.uuid4())
        feild_upd['facCode'] = self.case_name + str(uuid.uuid4())
        feild_upd['facCategoryId'] = self.s_id2
        feild_upd['parentIds'] = f"0,{str(self.s_id)},"
        feild_upd['propertyId'] = self.p_id
        feild_upd['buildingFloorSpaceName'] = feild_add_space['buildingFloorSpaceName']
        feild_upd['buildingName'] = feild_add_ld['buildingName']
        feild_upd['facCateParentName'] = feild_add_lx_p['facCateName']
        feild_upd['facCateName'] = feild_add_lx_s2['facCateName']
        Page播放设备.api_修改播放设备(self.session,feild_upd,self.header)
        #通过id查询播放设备参数正确
        res_data = Page播放设备.api_播放设备通过id查询(self.session,str(self.tz_id),self.header)
        self.assertEqual(feild_upd.get('facName'),res_data.get('data').get('facName'))
        self.assertEqual(feild_upd.get('facCode'),res_data.get('data').get('facCode'))
        self.assertEqual(feild_upd.get('facCategoryId'),res_data.get('data').get('facCategoryId'))
        self.assertEqual(str(feild_upd.get('assetStatus')),res_data.get('data').get('assetStatus'))
        self.assertEqual(feild_upd.get('facLinkCode'),res_data.get('data').get('facLinkCode'))
        self.assertEqual(feild_upd.get('facBimCode'),res_data.get('data').get('facBimCode'))
        self.assertEqual(str(feild_upd.get('serviceLife')),str(res_data.get('data').get('serviceLife')))
        self.assertEqual(feild_upd.get('facImportance'),res_data.get('data').get('facImportance'))
        self.assertEqual(feild_upd.get('brandName'),res_data.get('data').get('brandName'))
        self.assertEqual(feild_upd.get('manufacturer'),res_data.get('data').get('manufacturer'))
        self.assertEqual(feild_upd.get('modelName'),res_data.get('data').get('modelName'))
        self.assertEqual(feild_upd.get('oldFacCode'),res_data.get('data').get('oldFacCode'))
        self.assertEqual(feild_upd.get('remark'),res_data.get('data').get('remark'))
        self.assertEqual(feild_upd.get('supplierName'),res_data.get('data').get('supplierName'))
        self.assertEqual(feild_upd.get('contractNo'),res_data.get('data').get('contractNo'))
        self.assertEqual(feild_upd.get('supplierPerson'),res_data.get('data').get('supplierPerson'))
        self.assertEqual(feild_upd.get('supplierPhone'),res_data.get('data').get('supplierPhone'))
        self.assertIn(str(feild_upd.get('purchasePrice')),str(res_data.get('data').get('purchasePrice')))
        pass

    # def test_播放设备_04(self):
    #     """
    #     验证新增分组标签功能，通过id查询新增的播放设备参数正常
    #     :return:
    #     """
    #     # 新增项目
    #     feild_add_p = Param_项目管理.p_add.get('学校')
    #     feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
    #     self.p_id_int = res_data.get('data').get('id')
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': str(self.p_id)})
    #
    #     # 新增分组
    #     feild_add_group = copy.deepcopy(Param_播放设备.p_add_group.get('视频播放设备'))
    #     feild_add_group['tagName'] = self.case_name + str(uuid.uuid4())
    #     feild_add_group['propertyId'] = self.p_id_int
    #     res_data = Page_播放设备.Page播放设备.api_新增播放分组标签(self.session, feild_add_group, self.header)
    #     feild_add_g_id = res_data.get('data').get('id')
    #
    #     # 通过id查询分组
    #     feild_search_group = copy.deepcopy(Param_播放设备.p_search_group.get('视频播放设备'))
    #     feild_search_group['body']['tagId'] = feild_add_g_id
    #     res_data = Page_播放设备.Page播放设备.api_播放分组标签通过id查询(self.session, feild_search_group, self.header)
    #     self.assertEqual(res_data.get('code'), 200)
    #
    #     # 通过id删除分组
    #     res_data = Page_播放设备.Page播放设备.api_播放分组标签通过id删除(self.session, str(feild_add_g_id), self.header)
    #     self.assertEqual(res_data.get('code'), 200)

    def test_播放设备_05(self):
        """
        验证编辑分组标签功能，通过id查询更新后的播放设备参数正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.p_id_int = res_data.get('data').get('id')
        self.header.update({'propertyId': str(self.p_id)})

        # 新增分组
        feild_add_group = copy.deepcopy(Param_播放设备.p_add_group.get('视频播放设备'))
        feild_add_group['tagName'] = self.case_name + str(uuid.uuid4())
        feild_add_group['propertyId'] = self.p_id_int
        res_data = Page_播放设备.Page播放设备.api_新增播放分组标签(self.session, feild_add_group, self.header)
        feild_add_g_id = res_data.get('data').get('id')

        #修改分组名称
        feild_upd = Param_播放设备.p_upd_group.get('01')
        feild_upd['propertyId'] =  self.p_id_int
        feild_upd['tagName'] = self.case_name + str(uuid.uuid4())
        feild_upd['id'] = feild_add_g_id
        Page_播放设备.Page播放设备.api_修改播放分组标签(self.session,feild_upd,self.header)

        # 通过id查询分组
        feild_search_group = copy.deepcopy(Param_播放设备.p_search_group.get('视频播放设备'))
        feild_search_group['body']['tagId'] = feild_add_g_id
        res_data = Page_播放设备.Page播放设备.api_播放分组标签通过id查询(self.session, feild_search_group, self.header)
        self.assertEqual(res_data.get('code'), 200)

        # 通过id删除分组
        res_data = Page_播放设备.Page播放设备.api_播放分组标签通过id删除(self.session, str(feild_add_g_id), self.header)
        self.assertEqual(res_data.get('code'), 200)


    # def test_播放设备_06(self):
    #     """
    #     验证打标签功能，通过id查询该设备是否已经被打赏标签
    #     :return:
    #     """
    #     # 新增项目
    #     feild_add_p = Param_项目管理.p_add.get('学校')
    #     feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': str(self.p_id)})
    #     # 新增同级
    #     feild_add = Param_设备类型.p_add.get('一级设备')
    #     feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
    #     feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
    #     res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
    #     self.fs_id = res_data.get('data').get('id')
    #     # 新增下级
    #     feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
    #     feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
    #     feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
    #     feild_add_sub['parentId'] = self.fs_id
    #     res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
    #     self.s_id = res_data.get('data').get('id')
    #     # 新增区域楼栋
    #     feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
    #     feild_add_ld['propertyId'] = int(self.p_id)
    #     feild_add_ld['buildingName'] = self.case_name + str(uuid.uuid1())
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
    #     # 新增播放设备
    #     feild_add_tz = Param_播放设备.p_add.get('使用中')
    #     feild_add_tz['spaceId'] = self.room_id
    #     feild_add_tz['facCategoryId'] = self.s_id
    #     feild_add_tz['facCateCode'] = feild_add.get('facCateCode')
    #     feild_add_tz['facName'] = self.case_name + str(uuid.uuid4())
    #     feild_add_tz['facCode'] = self.case_name + str(uuid.uuid4())
    #     res_data = Page播放设备.api_新增播放设备(self.session, feild_add_tz, self.header)
    #     self.tz_id = res_data.get('data').get('id')
    #
    #     # 新增分组
    #     feild_add_group = copy.deepcopy(Param_播放设备.p_add_group.get('视频播放设备'))
    #     feild_add_group['tagName'] = self.case_name + str(uuid.uuid4())
    #     feild_add_group['propertyId'] = self.p_id
    #
    #     res_data = Page_播放设备.Page播放设备.api_新增播放分组标签(self.session, feild_add_group, self.header)
    #     feild_add_g_id = res_data.get('data').get('id')
    #
    #     #给设备打标签
    #     feild_tag = Param_播放设备.p_tag.get('设备打标签')
    #     feild_tag['facIdList'] = [self.tz_id]
    #     feild_tag['tagIdList'] = [feild_add_g_id]
    #     Page_播放设备.Page播放设备.api_播放设备打标签(self.session, feild_tag, self.header)
    #
    #     # 通过id查询分组,断言设备是否在分组内
    #     feild_search_group = copy.deepcopy(Param_播放设备.p_search_group.get('视频播放设备'))
    #     feild_search_group['body']['tagId'] = feild_add_g_id
    #     res_data = Page_播放设备.Page播放设备.api_播放分组标签通过id查询(self.session, feild_search_group, self.header)
    #     self.assertIn(str(self.tz_id),str(res_data.get('data').get('records')))
    #
    #     # 通过id删除分组
    #     res_data = Page_播放设备.Page播放设备.api_播放分组标签通过id删除(self.session, str(feild_add_g_id), self.header)
    #     self.assertEqual(res_data.get('code'), 200)
    #
    #     pass


    def test_播放设备_07(self):
        """
        验证移除标签功能，通过id查询该设备是否已经被移除标签
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级
        feild_add = Param_设备类型.p_add.get('一级设备')
        feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
        self.fs_id = res_data.get('data').get('id')
        # 新增下级
        feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
        feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['parentId'] = self.fs_id
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
        self.s_id = res_data.get('data').get('id')
        # 新增区域楼栋
        feild_add_ld = Param_楼栋信息.p_add.get('公共区域')
        feild_add_ld['propertyId'] = int(self.p_id)
        feild_add_ld['buildingName'] = self.case_name + str(uuid.uuid1())
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
        # 新增播放设备
        feild_add_tz = Param_播放设备.p_add.get('使用中')
        feild_add_tz['spaceId'] = self.room_id
        feild_add_tz['facCategoryId'] = self.s_id
        feild_add_tz['facCateCode'] = feild_add.get('facCateCode')
        feild_add_tz['facName'] = self.case_name + str(uuid.uuid4())
        feild_add_tz['facCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page播放设备.api_新增播放设备(self.session, feild_add_tz, self.header)
        self.tz_id = res_data.get('data').get('id')

        # 新增分组
        feild_add_group = copy.deepcopy(Param_播放设备.p_add_group.get('视频播放设备'))
        feild_add_group['tagName'] = self.case_name + str(uuid.uuid4())
        feild_add_group['propertyId'] = self.p_id

        res_data = Page_播放设备.Page播放设备.api_新增播放分组标签(self.session, feild_add_group, self.header)
        feild_add_g_id = res_data.get('data').get('id')

        # 给设备打标签
        feild_tag = Param_播放设备.p_tag.get('设备打标签')
        feild_tag['facIdList'] = [self.tz_id]
        feild_tag['tagIdList'] = [feild_add_g_id]
        Page_播放设备.Page播放设备.api_播放设备打标签(self.session, feild_tag, self.header)


        # 通过id查询分组,断言设备是否在分组内
        feild_search_group = copy.deepcopy(Param_播放设备.p_search_group.get('视频播放设备'))
        feild_search_group['body']['tagId'] = feild_add_g_id
        res_data = Page_播放设备.Page播放设备.api_播放分组标签通过id查询(self.session, feild_search_group, self.header)
        self.assertIn(str(self.tz_id), str(res_data.get('data').get('records')))

        Page_播放设备.Page播放设备.api_播放设备移除标签(self.session, feild_tag, self.header)

        # 通过id查询分组,断言设备是否在分组内
        feild_search_group = copy.deepcopy(Param_播放设备.p_search_group.get('视频播放设备'))
        feild_search_group['body']['tagId'] = feild_add_g_id
        res_data = Page_播放设备.Page播放设备.api_播放分组标签通过id查询(self.session, feild_search_group, self.header)
        self.assertNotIn(str(self.tz_id), str(res_data.get('data').get('records')))

        # 通过id删除分组
        res_data = Page_播放设备.Page播放设备.api_播放分组标签通过id删除(self.session, str(feild_add_g_id), self.header)
        self.assertEqual(res_data.get('code'), 200)
        pass