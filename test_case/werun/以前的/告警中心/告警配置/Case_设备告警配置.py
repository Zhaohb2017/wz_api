import unittest
import uuid

import ddt
import requests

from business.foo_lib.modules_db.werun.Db_设备智管 import Db设备智管
from business.param_config.api_param.werun.告警中心.告警配置 import Param_设备告警配置
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_设备类型, Param_空间信息, Param_楼栋信息
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from common.M_Crypto import rsa_encrypt
from page_object.werun.告警中心.Page_设备告警配置管理 import Page设备告警配置管理
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case设备告警配置(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '设备告警配置'
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
        if hasattr(self, 'sbgj_id'):
            Page设备告警配置管理.api_设备告警配置通过id删除(self.session, str(self.sbgj_id), self.header)
        if hasattr(self, 'tz_id'):
            Page设备表管理.api_设备通过id删除(self.session, str(self.tz_id), self.header)
        if hasattr(self, 's_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.s_id), self.header)
        if hasattr(self, 'sub_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.sub_id), self.header)
        if hasattr(self, 'room_id'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session, str(self.room_id), self.header)
        if hasattr(self, 'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        Db设备智管.db_删除设备执行动作(str(self.sub_id))
        Db设备智管.db_删除设备执行动作(str(self.s_id))
        self.session.close()
        pass

    def test_设备告警配置_01(self):
        """
        验证新增设备告警配置，通过id查询设备告警配置并断言，通过id删除设备告警配置功能正常(自定义设备类型)
        :return:
        """
        # 新增项目，设置header的项目id
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级
        feild_add = Param_设备类型.p_add.get('一级设备')
        feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
        self.s_id = res_data.get('data').get('id')
        # 新增下级
        feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
        feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['parentId'] = self.s_id
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
        self.sub_id = res_data.get('data').get('id')
        #sql添加执行动作
        Db设备智管.db_插入设备执行动作(self.p_id,feild_add_sub.get('facCateCode'),self.sub_id)
        #新增设备告警配置(依赖设备类型、执行动作)
        feild_add_sbgj = Param_设备告警配置.p_add.get('自定义设备类型')
        feild_add_sbgj['eventName'] = '告警名称'+str(uuid.uuid4())
        feild_add_sbgj['remark'] = '备注'+str(uuid.uuid4())
        feild_add_sbgj['triggerInfoList'][0]['facCategoryId'] = self.sub_id
        res_data = Page设备告警配置管理.api_新增设备告警配置(self.session,feild_add_sbgj,self.header)
        self.sbgj_id = res_data.get('data').get('id')
        #通过id查询设备告警配置，断言比对
        res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
        self.assertEqual(feild_add_sbgj.get('eventName'),res_data.get('data').get('eventName'))
        self.assertEqual(feild_add_sbgj.get('remark'),res_data.get('data').get('remark'))
        #通过id删除设备告警配置
        res_data = Page设备告警配置管理.api_设备告警配置通过id删除(self.session,str(self.sbgj_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询设备告警配置，验证删除成功
        res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    def test_设备告警配置_02(self):
        """
        验证新增设备告警配置，通过id查询设备告警配置并断言，通过id删除设备告警配置功能正常(自定义具体设备)
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级
        feild_add = Param_设备类型.p_add.get('一级设备')
        feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
        self.s_id = res_data.get('data').get('id')
        # 新增下级
        feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
        feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['parentId'] = self.s_id
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
        self.sub_id = res_data.get('data').get('id')
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
        # 新增设备台账
        feild_add_tz = Param_设备台账.p_add.get("使用中")
        feild_add_tz['spaceId'] = self.room_id
        feild_add_tz['facCategoryId'] = self.sub_id
        feild_add_tz['facName'] = '设备名称' + str(uuid.uuid4())
        feild_add_tz['facCode'] = '设备编码' + str(uuid.uuid4())
        feild_add_tz['facCateCode'] = feild_add.get('facCateCode')
        res_data = Page设备表管理.api_新增设备表(self.session, feild_add_tz, self.header)
        self.tz_id = res_data.get('data').get('id')
        #sql添加执行动作
        Db设备智管.db_插入设备执行动作(self.p_id,feild_add_sub.get('facCateCode'),self.sub_id)
        #新增设备告警配置(依赖具体设备、执行动作)
        feild_add_sbgj = Param_设备告警配置.p_add.get('自定义具体设备')
        feild_add_sbgj['eventName'] = '告警名称'+str(uuid.uuid4())
        feild_add_sbgj['remark'] = '备注'+str(uuid.uuid4())
        feild_add_sbgj['triggerInfoList'][0]['facIdList'][0]['id'] = self.tz_id
        feild_add_sbgj['triggerInfoList'][0]['facCamList'][0]['facilities']['id'] = self.tz_id
        feild_add_sbgj['triggerInfoList'][0]['facCategoryId'] = self.sub_id
        res_data = Page设备告警配置管理.api_新增设备告警配置(self.session,feild_add_sbgj,self.header)
        self.sbgj_id = res_data.get('data').get('id')
        #通过id查询设备告警配置，断言比对
        res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
        self.assertEqual(feild_add_sbgj.get('eventName'),res_data.get('data').get('eventName'))
        self.assertEqual(feild_add_sbgj.get('remark'),res_data.get('data').get('remark'))
        # self.assertEqual(feild_add_sbgj['triggerInfoList'][0].get('facIdList')[0].get('id'),res_data.get('data')['triggerInfoList'][0].get('facIdList')[0].get('id'))
        self.assertEqual(feild_add_sbgj['triggerInfoList'][0].get('facCamList')[0].get('facilities').get('id'),res_data.get('data')['triggerInfoList'][0].get('facCamList')[0].get('facilities').get('id'))
        self.assertEqual(feild_add_sbgj.get('triggerInfoList')[0].get('facCategoryId'),res_data.get('data').get('triggerInfoList')[0].get('facCategoryId'))
        #通过id删除设备告警配置
        res_data = Page设备告警配置管理.api_设备告警配置通过id删除(self.session,str(self.sbgj_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询设备告警配置，验证删除成功
        res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    def test_设备告警配置_02_1(self):
        """
        验证新增设备告警配置，通过id查询设备告警配置并断言，通过id删除设备告警配置功能正常(自定义具体设备，含摄相头)
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级
        feild_add = Param_设备类型.p_add.get('一级设备')
        feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
        self.s_id = res_data.get('data').get('id')
        # 新增下级
        feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
        feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['parentId'] = self.s_id
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
        self.sub_id = res_data.get('data').get('id')
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
        # 新增设备台账
        feild_add_tz = Param_设备台账.p_add.get("使用中")
        feild_add_tz['spaceId'] = self.room_id
        feild_add_tz['facCategoryId'] = self.sub_id
        feild_add_tz['facName'] = '设备名称' + str(uuid.uuid4())
        feild_add_tz['facCode'] = '设备编码' + str(uuid.uuid4())
        feild_add_tz['facCateCode'] = feild_add_sub.get('facCateCode')
        res_data = Page设备表管理.api_新增设备表(self.session, feild_add_tz, self.header)
        self.tz_id = res_data.get('data').get('id')
        #sql添加执行动作
        Db设备智管.db_插入设备执行动作(self.p_id,feild_add_sub.get('facCateCode'),self.sub_id)
        #新增设备告警配置(依赖具体设备、执行动作)
        feild_add_sbgj = Param_设备告警配置.p_add.get('自定义设备类型摄相头')
        feild_add_sbgj['eventName'] = '告警名称'+str(uuid.uuid4())
        feild_add_sbgj['remark'] = '备注'+str(uuid.uuid4())
        feild_add_sbgj['triggerInfoList'][0]['facIdList'][0]['id'] = self.tz_id
        feild_add_sbgj['triggerInfoList'][0]['facCamList'][0]['facilities']['id'] = self.tz_id
        feild_add_sbgj['triggerInfoList'][0]['facCamList'][0]['camList'][0]['id'] = self.tz_id
        feild_add_sbgj['triggerInfoList'][0]['facCategoryId'] = self.sub_id
        res_data = Page设备告警配置管理.api_新增设备告警配置(self.session,feild_add_sbgj,self.header)
        self.sbgj_id = res_data.get('data').get('id')
        #通过id查询设备告警配置，断言比对
        res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
        self.assertEqual(feild_add_sbgj.get('eventName'),res_data.get('data').get('eventName'))
        self.assertEqual(feild_add_sbgj.get('remark'),res_data.get('data').get('remark'))
        self.assertEqual(feild_add_sbgj['triggerInfoList'][0].get('facIdList')[0].get('id'),res_data.get('data')['triggerInfoList'][0].get('facIdList')[0].get('id'))
        self.assertEqual(feild_add_sbgj['triggerInfoList'][0].get('facCamList')[0].get('facilities').get('id'),res_data.get('data')['triggerInfoList'][0].get('facCamList')[0].get('facilities').get('id'))
        self.assertEqual(feild_add_sbgj['triggerInfoList'][0].get('facCamList')[0].get('camList')[0].get('id'),res_data.get('data')['triggerInfoList'][0].get('facCamList')[0].get('camList')[0].get('id'))
        self.assertEqual(feild_add_sbgj.get('triggerInfoList')[0].get('facCategoryId'),res_data.get('data').get('triggerInfoList')[0].get('facCategoryId'))
        #通过id删除设备告警配置
        res_data = Page设备告警配置管理.api_设备告警配置通过id删除(self.session,str(self.sbgj_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询设备告警配置，验证删除成功
        res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    # def test_设备告警配置_03(self):
    #     """
    #     验证新增设备告警配置，通过id查询设备告警配置并断言，通过id删除设备告警配置功能正常(系统设备类型)
    #     :return:
    #     """
    #     # 新增项目，设置header的项目id
    #     feild_add = Param_项目管理.p_add.get('学校')
    #     feild_add['propertyName'] = "项目" + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': str(self.p_id)})
    #     # 新增同级
    #     feild_add = Param_设备类型.p_add.get('一级设备')
    #     feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
    #     feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
    #     res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
    #     self.s_id = res_data.get('data').get('id')
    #     # 新增下级
    #     feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
    #     feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
    #     feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
    #     feild_add_sub['parentId'] = self.s_id
    #     res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
    #     self.sub_id = res_data.get('data').get('id')
    #     #sql添加执行动作
    #     Db设备智管.db_插入设备执行动作(self.p_id,feild_add_sub.get('facCateCode'),self.sub_id)
    #     #新增设备告警配置(依赖设备类型、执行动作)
    #     feild_add_sbgj = Param_设备告警配置.p_add.get('系统设备类型')
    #     feild_add_sbgj['eventName'] = '告警名称'+str(uuid.uuid4())
    #     feild_add_sbgj['remark'] = '备注'+str(uuid.uuid4())
    #     feild_add_sbgj['triggerInfoList'][0]['facCategoryId'] = self.sub_id
    #     res_data = Page设备告警配置管理.api_新增设备告警配置(self.session,feild_add_sbgj,self.header)
    #     self.sbgj_id = res_data.get('data').get('id')
    #     #通过id查询设备告警配置，断言比对
    #     res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
    #     self.assertEqual(feild_add_sbgj.get('eventName'),res_data.get('data').get('eventName'))
    #     self.assertEqual(feild_add_sbgj.get('remark'),res_data.get('data').get('remark'))
    #     self.assertIn(feild_add_sbgj.get('triggerInfoList')[0].get('triggerParamSysList')[0].get('alarmTriggerParam'),str(res_data))
    #     #通过id删除设备告警配置
    #     res_data = Page设备告警配置管理.api_设备告警配置通过id删除(self.session,str(self.sbgj_id),self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #通过id查询设备告警配置，验证删除成功
    #     res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
    #     self.assertEqual(res_data.get('data'),None)
    #
    # def test_设备告警配置_04(self):
    #     """
    #     验证新增设备告警配置，通过id查询设备告警配置并断言，通过id删除设备告警配置功能正常(系统具体设备)
    #     :return:
    #     """
    #     # 新增项目
    #     feild_add_p = Param_项目管理.p_add.get('学校')
    #     feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': str(self.p_id)})
    #     # 新增同级
    #     feild_add = Param_设备类型.p_add.get('一级设备')
    #     feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
    #     feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
    #     res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
    #     self.s_id = res_data.get('data').get('id')
    #     # 新增下级
    #     feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
    #     feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
    #     feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
    #     feild_add_sub['parentId'] = self.s_id
    #     res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
    #     self.sub_id = res_data.get('data').get('id')
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
    #     # 新增设备台账
    #     feild_add_tz = Param_设备台账.p_add.get("使用中")
    #     feild_add_tz['spaceId'] = self.room_id
    #     feild_add_tz['facCategoryId'] = self.sub_id
    #     feild_add_tz['facName'] = '设备名称' + str(uuid.uuid4())
    #     feild_add_tz['facCode'] = '设备编码' + str(uuid.uuid4())
    #     feild_add_tz['facCateCode'] = feild_add.get('facCateCode')
    #     res_data = Page设备表管理.api_新增设备表(self.session, feild_add_tz, self.header)
    #     self.tz_id = res_data.get('data').get('id')
    #     #sql添加执行动作
    #     Db设备智管.db_插入设备执行动作(self.p_id,feild_add_sub.get('facCateCode'),self.sub_id)
    #     #新增设备告警配置(依赖具体设备、执行动作)
    #     feild_add_sbgj = Param_设备告警配置.p_add.get('系统具体设备')
    #     feild_add_sbgj['eventName'] = '告警名称'+str(uuid.uuid4())
    #     feild_add_sbgj['remark'] = '备注'+str(uuid.uuid4())
    #     feild_add_sbgj['triggerInfoList'][0]['facIdList'][0]['id'] = self.tz_id
    #     feild_add_sbgj['triggerInfoList'][0]['facCamList'][0]['facilities']['id'] = self.tz_id
    #     feild_add_sbgj['triggerInfoList'][0]['facCategoryId'] = self.sub_id
    #     res_data = Page设备告警配置管理.api_新增设备告警配置(self.session,feild_add_sbgj,self.header)
    #     self.sbgj_id = res_data.get('data').get('id')
    #     #通过id查询设备告警配置，断言比对
    #     res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
    #     self.assertEqual(feild_add_sbgj.get('eventName'),res_data.get('data').get('eventName'))
    #     self.assertEqual(feild_add_sbgj.get('remark'),res_data.get('data').get('remark'))
    #     # self.assertEqual(feild_add_sbgj['triggerInfoList'][0].get('facIdList')[0].get('id'),res_data.get('data')['triggerInfoList'][0].get('facIdList')[0].get('id'))
    #     self.assertEqual(feild_add_sbgj['triggerInfoList'][0].get('facCamList')[0].get('facilities').get('id'),res_data.get('data')['triggerInfoList'][0].get('facCamList')[0].get('facilities').get('id'))
    #     self.assertEqual(feild_add_sbgj.get('triggerInfoList')[0].get('facCategoryId'),res_data.get('data').get('triggerInfoList')[0].get('facCategoryId'))
    #     #通过id删除设备告警配置
    #     res_data = Page设备告警配置管理.api_设备告警配置通过id删除(self.session,str(self.sbgj_id),self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #通过id查询设备告警配置，验证删除成功
    #     res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
    #     self.assertEqual(res_data.get('data'),None)

    def test_设备告警配置_05(self):
        """
        验证分页查询设备告警配置功能(设备系统、设备名称、事件名称、重置)
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级
        feild_add = Param_设备类型.p_add.get('一级设备')
        feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
        self.s_id = res_data.get('data').get('id')
        # 新增下级
        feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
        feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['parentId'] = self.s_id
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
        self.sub_id = res_data.get('data').get('id')
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
        # 新增设备台账
        feild_add_tz = Param_设备台账.p_add.get("使用中")
        feild_add_tz['spaceId'] = self.room_id
        feild_add_tz['facCategoryId'] = self.sub_id
        feild_add_tz['facName'] = '设备名称' + str(uuid.uuid4())
        feild_add_tz['facCode'] = '设备编码' + str(uuid.uuid4())
        feild_add_tz['facCateCode'] = feild_add.get('facCateCode')
        res_data = Page设备表管理.api_新增设备表(self.session, feild_add_tz, self.header)
        self.tz_id = res_data.get('data').get('id')
        # sql添加执行动作
        Db设备智管.db_插入设备执行动作(self.p_id, feild_add_sub.get('facCateCode'),self.sub_id)
        # 新增设备告警配置(依赖具体设备、执行动作)
        feild_add_sbgj = Param_设备告警配置.p_add.get('自定义具体设备')
        feild_add_sbgj['eventName'] = '告警名称' + str(uuid.uuid4())
        feild_add_sbgj['remark'] = '备注' + str(uuid.uuid4())
        feild_add_sbgj['triggerInfoList'][0]['facIdList'][0]['id'] = self.tz_id
        feild_add_sbgj['triggerInfoList'][0]['facCamList'][0]['facilities']['id'] = self.tz_id
        feild_add_sbgj['triggerInfoList'][0]['facCategoryId'] = self.sub_id
        res_data = Page设备告警配置管理.api_新增设备告警配置(self.session, feild_add_sbgj, self.header)
        self.sbgj_id = res_data.get('data').get('id')
        # 通过分页查询设备告警配置，断言比对(设备系统)
        feild_page = Param_设备告警配置.p_page.get('设备系统')
        feild_page['body']['facCategoryId'] = self.sub_id
        res_data = Page设备告警配置管理.api_设备告警配置分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_add_sbgj.get('eventName'),str(res_data))
        #设备名称
        feild_page = Param_设备告警配置.p_page.get('设备名称')
        res_data = Page设备告警配置管理.api_设备告警配置分页查询(self.session, feild_page, self.header)
        self.assertIn(feild_add_sbgj.get('eventName'), str(res_data))
        #事件名称
        feild_page = Param_设备告警配置.p_page.get('事件名称')
        res_data = Page设备告警配置管理.api_设备告警配置分页查询(self.session, feild_page, self.header)
        self.assertIn(feild_add_sbgj.get('eventName'), str(res_data))
        # 重置
        feild_page = Param_设备告警配置.p_page.get('重置')
        res_data = Page设备告警配置管理.api_设备告警配置分页查询(self.session, feild_page, self.header)
        self.assertNotEqual(res_data.get('data').get('records'),[])
        self.assertNotEqual(res_data.get('data').get('records'),None)
        # 通过id删除设备告警配置
        res_data = Page设备告警配置管理.api_设备告警配置通过id删除(self.session, str(self.sbgj_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        # 通过id查询设备告警配置，验证删除成功
        res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session, str(self.sbgj_id), self.header)
        self.assertEqual(res_data.get('data'), None)

    def test_设备告警配置_06(self):
        """
        验证设备告警配置功能启用禁用功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级
        feild_add = Param_设备类型.p_add.get('一级设备')
        feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
        self.s_id = res_data.get('data').get('id')
        # 新增下级
        feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
        feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
        feild_add_sub['parentId'] = self.s_id
        res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
        self.sub_id = res_data.get('data').get('id')
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
        # 新增设备台账
        feild_add_tz = Param_设备台账.p_add.get("使用中")
        feild_add_tz['spaceId'] = self.room_id
        feild_add_tz['facCategoryId'] = self.sub_id
        feild_add_tz['facName'] = '设备名称' + str(uuid.uuid4())
        feild_add_tz['facCode'] = '设备编码' + str(uuid.uuid4())
        feild_add_tz['facCateCode'] = feild_add.get('facCateCode')
        res_data = Page设备表管理.api_新增设备表(self.session, feild_add_tz, self.header)
        self.tz_id = res_data.get('data').get('id')
        # sql添加执行动作
        Db设备智管.db_插入设备执行动作(self.p_id, feild_add_sub.get('facCateCode'),self.sub_id)
        # 新增设备告警配置(依赖具体设备、执行动作)
        feild_add_sbgj = Param_设备告警配置.p_add.get('自定义具体设备')
        feild_add_sbgj['eventName'] = '告警名称' + str(uuid.uuid4())
        feild_add_sbgj['remark'] = '备注' + str(uuid.uuid4())
        feild_add_sbgj['triggerInfoList'][0]['facIdList'][0]['id'] = self.tz_id
        feild_add_sbgj['triggerInfoList'][0]['facCamList'][0]['facilities']['id'] = self.tz_id
        feild_add_sbgj['triggerInfoList'][0]['facCategoryId'] = self.sub_id
        res_data = Page设备告警配置管理.api_新增设备告警配置(self.session, feild_add_sbgj, self.header)
        self.sbgj_id = res_data.get('data').get('id')
        #禁用设备告警配置
        feild_off = Param_设备告警配置.p_on_off.get('禁用')
        feild_off['id'] = self.sbgj_id
        res_data = Page设备告警配置管理.api_设备告警配置启用禁用(self.session,feild_off,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询配置，断言状态
        res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
        self.assertEqual(res_data.get('data').get('activeState'),0)
        #启用设备告警配置
        feild_on = Param_设备告警配置.p_on_off.get('启用')
        feild_on['id'] = self.sbgj_id
        res_data = Page设备告警配置管理.api_设备告警配置启用禁用(self.session,feild_on,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询配置，断言状态
        res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session, str(self.sbgj_id), self.header)
        self.assertEqual(res_data.get('data').get('activeState'), 1)
        # 通过id删除设备告警配置
        res_data = Page设备告警配置管理.api_设备告警配置通过id删除(self.session, str(self.sbgj_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        # 通过id查询设备告警配置，验证删除成功
        res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session, str(self.sbgj_id), self.header)
        self.assertEqual(res_data.get('data'), None)

    # def test_设备告警配置_07(self):
    #     """
    #     验证设备告警配置编辑修改功能正常
    #     :return:
    #     """
    #     # 新增项目
    #     feild_add_p = Param_项目管理.p_add.get('学校')
    #     feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': str(self.p_id)})
    #     # 新增同级
    #     feild_add = Param_设备类型.p_add.get('一级设备')
    #     feild_add['facCateName'] = self.case_name + str(uuid.uuid4())
    #     feild_add['facCateCode'] = self.case_name + str(uuid.uuid4())
    #     res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
    #     self.s_id = res_data.get('data').get('id')
    #     # 新增下级
    #     feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
    #     feild_add_sub['facCateName'] = self.case_name + str(uuid.uuid4())
    #     feild_add_sub['facCateCode'] = self.case_name + str(uuid.uuid4())
    #     feild_add_sub['parentId'] = self.s_id
    #     res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
    #     self.sub_id = res_data.get('data').get('id')
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
    #     # 新增设备台账
    #     feild_add_tz = Param_设备台账.p_add.get("使用中")
    #     feild_add_tz['spaceId'] = self.room_id
    #     feild_add_tz['facCategoryId'] = self.sub_id
    #     feild_add_tz['facName'] = '设备名称' + str(uuid.uuid4())
    #     feild_add_tz['facCode'] = '设备编码' + str(uuid.uuid4())
    #     feild_add_tz['facCateCode'] = feild_add.get('facCateCode')
    #     res_data = Page设备表管理.api_新增设备表(self.session, feild_add_tz, self.header)
    #     self.tz_id = res_data.get('data').get('id')
    #     #sql添加执行动作
    #     Db设备智管.db_插入设备执行动作(self.p_id,feild_add_sub.get('facCateCode'),self.sub_id)
    #     #新增设备告警配置(依赖具体设备、执行动作)
    #     feild_add_sbgj = Param_设备告警配置.p_add.get('自定义具体设备')
    #     feild_add_sbgj['eventName'] = '告警名称'+str(uuid.uuid4())
    #     feild_add_sbgj['remark'] = '备注'+str(uuid.uuid4())
    #     feild_add_sbgj['triggerInfoList'][0]['facIdList'][0]['id'] = self.tz_id
    #     feild_add_sbgj['triggerInfoList'][0]['facCamList'][0]['facilities']['id'] = self.tz_id
    #     feild_add_sbgj['triggerInfoList'][0]['facCategoryId'] = self.sub_id
    #     res_data = Page设备告警配置管理.api_新增设备告警配置(self.session,feild_add_sbgj,self.header)
    #     self.sbgj_id = res_data.get('data').get('id')
    #     #通过id查询
    #     res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session, str(self.sbgj_id), self.header)
    #     triggerInfoList_id = res_data.get('data')['triggerInfoList'][0]['id']
    #     triggerParamCustomList_id = res_data.get('data')['triggerInfoList'][0]['triggerParamCustomList'][0]['id']
    #     alarmFacConfig_id = res_data.get('data')['triggerInfoList'][0]['triggerParamCustomList'][0]['alarmFacConfigId']
    #     #编辑修改设备告警配置
    #     feild_upd = Param_设备告警配置.p_upd.get('01')
    #     feild_upd['id'] = self.sbgj_id
    #     feild_upd['eventName'] = '告警名称' + str(uuid.uuid4())
    #     feild_upd['propertyId'] = self.p_id
    #     feild_upd['triggerInfoList'][0]['id'] = triggerInfoList_id
    #     feild_upd['triggerInfoList'][0]['triggerParamCustomList'][0]['alarmTriggerInfoId'] = triggerInfoList_id
    #     feild_upd['triggerInfoList'][0]['triggerParamCustomList'][0]['id'] = triggerParamCustomList_id
    #     feild_upd['triggerInfoList'][0]['triggerParamCustomList'][0]['alarmFacConfigId'] = alarmFacConfig_id
    #     feild_upd['remark'] = '备注' + str(uuid.uuid4())
    #     feild_upd['triggerInfoList'][0]['facIdList'][0]['id'] = self.tz_id
    #     feild_upd['triggerInfoList'][0]['facCamList'][0]['facilities']['id'] = self.tz_id
    #     feild_upd['triggerInfoList'][0]['facCategoryId'] = self.sub_id
    #     res_data = Page设备告警配置管理.api_修改设备告警配置(self.session,feild_upd,self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #通过id查询设备告警配置，断言比对
    #     res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
    #     self.assertEqual(feild_upd.get('eventName'),res_data.get('data').get('eventName'))
    #     self.assertEqual(feild_upd.get('remark'),res_data.get('data').get('remark'))
    #     # self.assertEqual(feild_add_sbgj['triggerInfoList'][0].get('facIdList')[0].get('id'),res_data.get('data')['triggerInfoList'][0].get('facIdList')[0].get('id'))
    #     self.assertEqual(feild_upd['triggerInfoList'][0].get('facCamList')[0].get('facilities').get('id'),res_data.get('data')['triggerInfoList'][0].get('facCamList')[0].get('facilities').get('id'))
    #     self.assertEqual(feild_upd.get('triggerInfoList')[0].get('facCategoryId'),res_data.get('data').get('triggerInfoList')[0].get('facCategoryId'))
    #     #通过id删除设备告警配置
    #     res_data = Page设备告警配置管理.api_设备告警配置通过id删除(self.session,str(self.sbgj_id),self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #通过id查询设备告警配置，验证删除成功
    #     res_data = Page设备告警配置管理.api_设备告警配置通过id查询(self.session,str(self.sbgj_id),self.header)
    #     self.assertEqual(res_data.get('data'),None)