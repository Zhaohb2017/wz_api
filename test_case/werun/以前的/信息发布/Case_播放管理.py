import copy
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.信息发布 import Param_素材管理, Param_节目管理, Param_播放管理, Param_播放设备
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_设备类型, Param_楼栋信息, Param_空间信息
from common.M_Crypto import rsa_encrypt
from page_object.werun.信息发布 import Page_节目管理, Page_播放管理
from page_object.werun.信息发布.Page_播放设备 import Page播放设备
from page_object.werun.信息发布.Page_素材管理 import Page素材管理
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块



@ddt.ddt
class Case播放管理(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '播放管理'
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
        if hasattr(self, 'tz_id'):
            Page播放设备.api_播放设备通过id删除(self.session, str(self.tz_id), self.header)
        if hasattr(self, 's_id'):
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

    def test_播放管理_01(self):
        """
        验证新增播放，通过id查询新增规则参数正确，通过id删除规则功能正常
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
        # 新增播放设备
        feild_add_tz = Param_播放设备.p_add.get('使用中')
        feild_add_tz['spaceId'] = self.room_id
        feild_add_tz['facCategoryId'] = self.s_id
        feild_add_tz['facCateCode'] = feild_add.get('facCateCode')
        feild_add_tz['facName'] = self.case_name + str(uuid.uuid4())
        feild_add_tz['facCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page播放设备.api_新增播放设备(self.session, feild_add_tz, self.header)
        self.tz_id = res_data.get('data').get('id')

        # 上传图片
        feild_upload = Param_素材管理.p_upload.get('图片')
        res_data = Page素材管理.api_上传图片素材(self.session, feild_upload, self.header)
        fid = res_data.get('data').get('fid')

        # 新增图片素材
        feild_add = Param_素材管理.p_add.get('图片')
        f_add = feild_add[0]  # 字典
        f_add['materialName'] = self.case_name + str(uuid.uuid4())
        f_add['fileId'] = fid
        feild_add[0] = f_add
        Page素材管理.api_新增素材(self.session, feild_add, self.header)

        # 通过集合查询，并断言素材fid
        feild_search = copy.deepcopy(Param_素材管理.p_page.get('查询图片'))
        feild_search['body']['materialName'] = f_add['materialName']
        res_data = Page素材管理.api_素材集合查询(self.session, feild_search, self.header)
        records = res_data.get('data').get('records')
        self.assertIn(str(fid), str(records))
        pic_id = 0
        for d in records:
            if d.get('fileId') == fid:
                pic_id = d.get('id')

        # 新增节目
        feild_add_program = copy.deepcopy(Param_节目管理.p_add_program.get('图片'))
        feild_add_m = feild_add_program.get('materials')
        f_m = feild_add_m[0]
        f_m['materialId'] = pic_id
        feild_add_m[0] = f_m
        feild_add_program['programName'] = self.case_name + str(uuid.uuid4())
        res_data = Page_节目管理.Page节目管理.api_新增节目(self.session, feild_add_program, self.header)
        pro_id = res_data.get('data').get('id')

        #新增一个播放规则
        feild_add_rule = copy.deepcopy(Param_播放管理.p_add_rule.get('图片节目规则-不重复'))
        feild_add_rule['planName'] = '图片节目规则-不重复'+str(uuid.uuid4()) #1
        f_r_p_t = feild_add_rule.get('programs') #获取节目元组
        f_r_p_d = f_r_p_t [0]  #获取节目字典
        f_r_p_d['programId'] = pro_id
        f_r_p_m = f_r_p_d.get('materials') #获取素材元组
        f_r_p_m_d = f_r_p_m[0]  # 获取素材字典
        f_r_p_m_d['materialId'] = pic_id
        f_r_p_m_d['materialProgramId'] = pro_id
        f_r_p_m[0] = f_r_p_m_d
        f_r_p_d['materials'] = f_r_p_m #2

        f_r_p_t[0] =  f_r_p_d
        feild_add_rule['programs'] = f_r_p_t #2

        f_r_p_device = feild_add_rule.get('facs')  # 获取播放设备元组
        f_r_p_device_d = f_r_p_device[0]  # 获取播放设备字典
        f_r_p_device_d['facId'] = self.tz_id
        f_r_p_device[0] = f_r_p_device_d
        feild_add_rule['facs'] = f_r_p_device  # 3

        res_data = Page_播放管理.Page播放管理.api_新增播放规则(self.session,feild_add_rule,self.header)
        self.assertEqual(res_data.get('ok'), True)
        r = res_data.get('data').get('nums')
        rule_id = r[0].get('planId')

        #通过id查询规则，并断言规则信息是否正确
        res_data = Page_播放管理.Page播放管理.api_通过id查询播放规则(self.session,str(rule_id),self.header)
        self.assertEqual(res_data.get('ok'),True)

        #删除一个播放规则
        res_data = Page_播放管理.Page播放管理.api_通过id删除播放规则(self.session,str(rule_id),self.header)
        self.assertEqual(res_data.get('ok'), True)

        # 删除节目
        res_data = Page_节目管理.Page节目管理.api_通过id删除节目(self.session, str(pro_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

        # 通过id查询节目，断言节目是否删除成功
        res_data = Page_节目管理.Page节目管理.api_通过id查询节目(self.session, str(pro_id), self.header)
        self.assertEqual(res_data.get('data'), None)

        # 删除素材
        res_data = Page素材管理.api_通过id删除素材(self.session, str(pic_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

        # 通过id查询预览素材，断言素材不存在
        res_data = Page素材管理.api_预览图片素材(self.session, str(pic_id), self.header)
        self.assertEqual(res_data.get('msg'), '素材不存在')
        pass

