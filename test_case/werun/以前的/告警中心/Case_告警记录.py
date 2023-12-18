import time
import unittest
import uuid

import ddt
import requests

from business.foo_lib.modules_biz.werun.Biz_xxl_job import BizXxlJob
from business.foo_lib.modules_db.werun.Db_设备智管 import Db设备智管
from business.param_config.api_param.werun.告警中心 import Param_告警记录
from business.param_config.api_param.werun.告警中心.告警配置 import Param_消防告警配置, Param_安全告警配置
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_楼栋信息, Param_空间类型, Param_空间信息, \
    Param_设备类型
from business.param_config.api_param.werun.设备智管 import Param_设备台账
from business.param_config.api_param.werun.设备智管.线上巡检 import Param_巡检计划
from business.param_config.api_param.werun.设备智管.线上巡检 import Param_线上巡检标准, Param_巡检机房, Param_巡检任务
from business.param_config.api_param.werun.设备智管.线上巡检.Param_巡检计划 import p_xmhmc
from common.Common_Base import write_excel_xmhmc
from common.M_Crypto import rsa_encrypt
from page_object.werun.上传下载.Page_附件管理 import Page附件管理
from page_object.werun.告警中心.Page_告警记录管理 import Page告警记录管理
from page_object.werun.告警中心.Page_安防告警配置管理 import Page安防告警配置管理
from page_object.werun.告警中心.Page_黑名单布控管理 import Page黑名单布控管理
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目花名册管理 import Page项目花名册管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.线上巡检.Page_巡检任务管理 import Page巡检任务管理
from page_object.werun.线上巡检.Page_巡检机房管理 import Page巡检机房管理
from page_object.werun.线上巡检.Page_巡检计划管理 import Page巡检计划管理
from page_object.werun.线上巡检.Page_环境巡检标准管理 import Page环境巡检标准管理


@ddt.ddt
class Case告警记录(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.session_xxl = requests.Session()
        self.case_name = '告警记录'
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
        if hasattr(self,'gjjl_id'):
            Page告警记录管理.api_告警记录通过id删除(self.session,str(self.gjjl_id),self.header)
        if hasattr(self, 'rw_id'):
            Page巡检任务管理.api_通过id删除巡检任务(self.session, str(self.rw_id), self.header)
        if hasattr(self, 'aq_id'):
            Page黑名单布控管理.api_黑名单布控通过id删除(self.session, str(self.aq_id), self.header)
        if hasattr(self, 'xf_id'):
            Page安防告警配置管理.api_安防告警配置通过id删除(self.session, str(self.xf_id), self.header)
        if hasattr(self, 'tz_id'):
            Page设备表管理.api_设备通过id删除(self.session, str(self.tz_id), self.header)
        if hasattr(self, 'sub_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.sub_id), self.header)
        if hasattr(self, 's_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session, str(self.s_id), self.header)
        if hasattr(self, 'jh_id'):
            Page巡检计划管理.api_通过id删除巡检计划(self.session, str(self.jh_id), self.header)
        if hasattr(self,'jf_id'):
            Page巡检机房管理.api_通过id删除巡检机房(self.session,str(self.jf_id),self.header)
        if hasattr(self, 'sbxj_id'):
            Page环境巡检标准管理.api_通过id删除环境巡检标准(self.session, str(self.sbxj_id), self.header)
        if hasattr(self, 'hmc_u_id'):
            Page项目花名册管理.api_项目花名册通过id删除(self.session, str(self.hmc_u_id), self.header)
        if hasattr(self, 'hmc_u_id1'):
            Page项目花名册管理.api_项目花名册通过id删除(self.session, str(self.hmc_u_id1), self.header)
        if hasattr(self, 'room_id'):
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(self.session, str(self.room_id), self.header)
        if hasattr(self, 'space_type_id'):
            Page空间类型表管理.api_空间类型通过id删除(self.session, str(self.space_type_id), self.header)
        if hasattr(self, 'f_id'):
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(self.session, str(self.f_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass
    #
    # @ddt.data(*Param_告警记录.p_page_dcl.keys())
    # def test_告警记录_01(self,key):
    #     """
    #     验证通过线上巡检转告警，分页查询告警展示信息正确
    #     :return:
    #     """
    #     #通过线上巡检，转告警
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
    #     self.floor_id = res_data.get('data').get('list')[0].get('id')
    #     # 新增空间类型
    #     feild_add_space_type = Param_空间类型.p_add.get('同级')
    #     feild_add_space_type['spaceCode'] = "room" + str(uuid.uuid1())
    #     res_data = Page空间类型表管理.api_新增空间类型表(self.session, feild_add_space_type, self.header)
    #     self.space_type_id = res_data.get('data').get('id')
    #     # 新增空间
    #     feild_add_space = Param_空间信息.p_add.get('空间类型2')
    #     feild_add_space['propertyId'] = self.p_id
    #     feild_add_space['buildingId'] = self.f_id
    #     feild_add_space['buildingFloorId'] = self.floor_id
    #     feild_add_space['buildingFloorSpaceName'] = "room " + str(uuid.uuid1())
    #     feild_add_space['spaceId'] = self.space_type_id
    #     res_data = Page楼层房间信息表管理.api_新增楼层房间信息表(self.session, feild_add_space, self.header)
    #     self.room_id = res_data.get('data').get('id')
    #     # 新增环境巡检标准（依赖空间类型）
    #     feild_add_sbxj = Param_线上巡检标准.p_add.get('环境标准单条')
    #     feild_add_sbxj['spaceId'] = self.space_type_id
    #     feild_add_sbxj['remark'] = 'remark' + str(uuid.uuid4())
    #     feild_add_sbxj['checks'][0]['checkContent'] = '检查内容' + str(uuid.uuid4())
    #     res_data = Page环境巡检标准管理.api_新增环境巡检标准(self.session, feild_add_sbxj, self.header)
    #     self.sbxj_id = res_data.get('data').get('id')
    #     # 通过id查询标准，断言新增数据
    #     res_data = Page环境巡检标准管理.api_通过id查询环境巡检标准(self.session, str(self.sbxj_id), self.header)
    #     content_id = res_data.get('data').get('checks')[0].get('id')
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
    #     # 新增设备
    #     feild_add_tz = Param_设备台账.p_add.get('使用中')
    #     feild_add_tz['spaceId'] = self.room_id
    #     feild_add_tz['facCategoryId'] = self.sub_id
    #     feild_add_tz['facCateCode'] = feild_add_sub.get('facCateCode')
    #     feild_add_tz['facName'] = '设备名称' + str(uuid.uuid4())
    #     feild_add_tz['facCode'] = '设备编码' + str(uuid.uuid4())
    #     res_data = Page设备表管理.api_新增设备表(self.session, feild_add_tz, self.header)
    #     self.tz_id = res_data.get('data').get('id')
    #     # 新增巡检机房(依赖房间、环境巡检标准)
    #     feild_add = Param_巡检机房.p_add.get('巡检摄相头')
    #     feild_add['buildingId'] = self.f_id
    #     feild_add['buildingFloorId'] = self.floor_id
    #     feild_add['buildingFloorSpaceId'] = self.room_id
    #     feild_add['remark'] = 'remark' + str(uuid.uuid4())
    #     feild_add['envStandards'][0]['standardEnvId'] = self.sbxj_id
    #     feild_add['envStandards'][0]['standardEnvCheckId'] = content_id
    #     feild_add['cameras'][0]['inspectCameraId'] = self.tz_id
    #     feild_add['cameras'][0]['inspectCameraName'] = feild_add_tz.get('facName')
    #     feild_add['facs'][0]['inspectFacId'] = self.tz_id
    #     feild_add['facs'][0]['inspectFacCateId'] = self.sub_id
    #     res_data = Page巡检机房管理.api_新增巡检机房(self.session, feild_add, self.header)
    #     self.jf_id = res_data.get('data').get('id')
    #     # 上传Excel项目花名册人员
    #     # 将项目名称写入excel文件
    #     xmhmc = p_xmhmc.copy()
    #     xmhmc[0] = feild_add_p.get('propertyName')
    #     xmhmc[1] = '哈尔滨市'
    #     xmhmc[2] = '南岗区'
    #     write_excel_xmhmc('./test_data/excel/xmhmc.xlsx', xmhmc)
    #     # 上传
    #     feild_upload_hmc = {"file": ('xmhmc.xlsx', open('./test_data/excel/xmhmc.xlsx', 'rb'), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
    #     res_data = Page项目花名册管理.api_导入项目花名册(self.session, feild_upload_hmc, self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     # 获取名称列表，拿到花名册人员参数id
    #     res_data = Page项目花名册管理.api_项目花名册集合查询(self.session, self.header)
    #     self.hmc_u_id = res_data.get('data')[0].get('id')
    #     # 新增巡检计划（依赖机房、用户）
    #     start_time = int(round(time.time() * 1000))
    #     feild_add_xjjh = Param_巡检计划.p_add.get('任务测试')
    #     feild_add_xjjh['rooms'][0]['inspectRoomId'] = self.jf_id
    #     feild_add_xjjh['inspectUser'] = self.hmc_u_id
    #     feild_add_xjjh['planStart'] = start_time
    #     feild_add_xjjh['planEnd'] = start_time + 86400000 * 5
    #     feild_add_xjjh['inspectPlanName'] = '计划名称' + str(uuid.uuid4())
    #     res_data = Page巡检计划管理.api_新增巡检计划(self.session, feild_add_xjjh, self.header)
    #     self.jh_id = res_data.get('data').get('id')
    #     # 新建消防告警配置
    #     feild_add_xfgj = Param_消防告警配置.p_add.get('紧急')
    #     feild_add_xfgj['eventName'] = '消防配置' + str(uuid.uuid4()).split('-')[-1]
    #     res_data = Page安防告警配置管理.api_新增安防告警配置(self.session, feild_add_xfgj, self.header)
    #     self.xf_id = res_data.get('data').get('id')
    #     # 新建安全告警配置
    #     # 上传图片
    #     feild_upload = Param_安全告警配置.p_upload.get('01')
    #     res_data = Page附件管理.api_上传附件(self.session, feild_upload, self.header)
    #     fid = res_data.get('data').get('fid')
    #     # 新增安全告警配置
    #     feild_add_aqgj = Param_安全告警配置.p_add.get('严重')
    #     feild_add_aqgj['blackName'] = '黑名称' + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_aqgj['remark'] = '备注' + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_aqgj['faceUrl'] = fid
    #     res_data = Page黑名单布控管理.api_新增黑名单布控(self.session, feild_add_aqgj, self.header)
    #     self.aq_id = res_data.get('data').get('id')
    #     # 执行生成线上巡检任务
    #     BizXxlJob.biz_执行定时任务(self.session_xxl, '线上巡检', '生成线上巡检任务')
    #     # 变更数据库开始时间为前一天开始
    #     Db设备智管.db_变更线上巡检任务开始时间(feild_add_xjjh.get('inspectPlanName'), start_time - 86400000)
    #     # 执行定时更新线上巡检任务状态
    #     BizXxlJob.biz_执行定时任务(self.session_xxl, '线上巡检', '定时更新线上巡检任务状态')
    #     # 通过名称page查询任务的id  task/page
    #     feild_page_rw = Param_巡检任务.p_page.get('任务名称')
    #     res_data = Page巡检任务管理.api_巡检任务分页查询(self.session, feild_page_rw, self.header)
    #     self.rw_id = res_data.get('data').get('records')[0].get('id')
    #     # 通过任务id查询任务房间列表  task/doTaskRoomList?id=1236
    #     feild_room_list = {'id': str(self.rw_id)}
    #     res_data = Page巡检任务管理.api_执行巡检任务查询巡检机房列表(self.session, feild_room_list, self.header)
    #     task_room_id = res_data.get('data')[0].get('id')
    #     # 通过房间列表查询房间的内容（获取参数）doTaskRoom?inspectTaskId=1236&taskRoomId=3029
    #     feild_room_task = {'inspectTaskId': str(self.rw_id),
    #                        'taskRoomId': str(task_room_id)}  # inspectTaskId=1642&taskRoomId=3986
    #     res_data = Page巡检任务管理.api_执行巡检任务查询巡检机房(self.session, feild_room_task, self.header)
    #     env_id = res_data.get('data').get('envs')[0].get('id')
    #     fac_id = res_data.get('data').get('facs')[0].get('id')
    #     #转消防告警
    #     feild_xf_alarm = Param_告警记录.p_alarm.get(key)
    #     feild_xf_alarm['facId'] = self.tz_id
    #     if '消防' in key:
    #         feild_xf_alarm['alarmConfigId'] = self.xf_id
    #     elif '安全' in key:
    #         feild_xf_alarm['alarmConfigId'] = self.aq_id
    #     res_data = Page告警记录管理.api_新增告警记录(self.session, feild_xf_alarm, self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     #分页查询告警展示信息并断言
    #     feild_page = Param_告警记录.p_page_dcl.get(key)
    #     res_data = Page告警记录管理.api_告警记录分页查询(self.session,feild_page,self.header)
    #     self.assertIn(feild_xf_alarm.get('alarmName'),str(res_data))
    #
    # def test_告警记录_02(self):
    #     """
    #     验证告警待处理，验证告警记录处理后状态正确（线下跟进）
    #     :return:
    #     """
    #     #通过线上巡检，转告警
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
    #     self.floor_id = res_data.get('data').get('list')[0].get('id')
    #     # 新增空间类型
    #     feild_add_space_type = Param_空间类型.p_add.get('同级')
    #     feild_add_space_type['spaceCode'] = "room" + str(uuid.uuid1())
    #     res_data = Page空间类型表管理.api_新增空间类型表(self.session, feild_add_space_type, self.header)
    #     self.space_type_id = res_data.get('data').get('id')
    #     # 新增空间
    #     feild_add_space = Param_空间信息.p_add.get('空间类型2')
    #     feild_add_space['propertyId'] = self.p_id
    #     feild_add_space['buildingId'] = self.f_id
    #     feild_add_space['buildingFloorId'] = self.floor_id
    #     feild_add_space['buildingFloorSpaceName'] = "room " + str(uuid.uuid1())
    #     feild_add_space['spaceId'] = self.space_type_id
    #     res_data = Page楼层房间信息表管理.api_新增楼层房间信息表(self.session, feild_add_space, self.header)
    #     self.room_id = res_data.get('data').get('id')
    #     # 新增环境巡检标准（依赖空间类型）
    #     feild_add_sbxj = Param_线上巡检标准.p_add.get('环境标准单条')
    #     feild_add_sbxj['spaceId'] = self.space_type_id
    #     feild_add_sbxj['remark'] = 'remark' + str(uuid.uuid4())
    #     feild_add_sbxj['checks'][0]['checkContent'] = '检查内容' + str(uuid.uuid4())
    #     res_data = Page环境巡检标准管理.api_新增环境巡检标准(self.session, feild_add_sbxj, self.header)
    #     self.sbxj_id = res_data.get('data').get('id')
    #     # 通过id查询标准，断言新增数据
    #     res_data = Page环境巡检标准管理.api_通过id查询环境巡检标准(self.session, str(self.sbxj_id), self.header)
    #     content_id = res_data.get('data').get('checks')[0].get('id')
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
    #     # 新增设备
    #     feild_add_tz = Param_设备台账.p_add.get('使用中')
    #     feild_add_tz['spaceId'] = self.room_id
    #     feild_add_tz['facCategoryId'] = self.sub_id
    #     feild_add_tz['facCateCode'] = feild_add_sub.get('facCateCode')
    #     feild_add_tz['facName'] = '设备名称' + str(uuid.uuid4())
    #     feild_add_tz['facCode'] = '设备编码' + str(uuid.uuid4())
    #     res_data = Page设备表管理.api_新增设备表(self.session, feild_add_tz, self.header)
    #     self.tz_id = res_data.get('data').get('id')
    #     # 新增巡检机房(依赖房间、环境巡检标准)
    #     feild_add = Param_巡检机房.p_add.get('巡检摄相头')
    #     feild_add['buildingId'] = self.f_id
    #     feild_add['buildingFloorId'] = self.floor_id
    #     feild_add['buildingFloorSpaceId'] = self.room_id
    #     feild_add['remark'] = 'remark' + str(uuid.uuid4())
    #     feild_add['envStandards'][0]['standardEnvId'] = self.sbxj_id
    #     feild_add['envStandards'][0]['standardEnvCheckId'] = content_id
    #     feild_add['cameras'][0]['inspectCameraId'] = self.tz_id
    #     feild_add['cameras'][0]['inspectCameraName'] = feild_add_tz.get('facName')
    #     feild_add['facs'][0]['inspectFacId'] = self.tz_id
    #     feild_add['facs'][0]['inspectFacCateId'] = self.sub_id
    #     res_data = Page巡检机房管理.api_新增巡检机房(self.session, feild_add, self.header)
    #     self.jf_id = res_data.get('data').get('id')
    #     # 上传Excel项目花名册人员
    #     # 将项目名称写入excel文件
    #     xmhmc = p_xmhmc.copy()
    #     xmhmc[0] = feild_add_p.get('propertyName')
    #     xmhmc[1] = 'Haerbin'
    #     xmhmc[2] = 'Nangang District'
    #     write_excel_xmhmc('./test_data/excel/xmhmc.xlsx', xmhmc)
    #     # 上传
    #     feild_upload_hmc = {"fileName": 'xmhmc.xlsx', "file": (
    #     'xmhmc.xlsx', open('./test_data/excel/xmhmc.xlsx', 'rb'), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
    #     res_data = Page项目花名册管理.api_导入项目花名册(self.session, feild_upload_hmc, self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     # 获取名称列表，拿到花名册人员参数id
    #     res_data = Page项目花名册管理.api_项目花名册集合查询(self.session, self.header)
    #     self.hmc_u_id = res_data.get('data')[0].get('id')
    #     # 新增巡检计划（依赖机房、用户）
    #     start_time = int(round(time.time() * 1000))
    #     feild_add_xjjh = Param_巡检计划.p_add.get('任务测试')
    #     feild_add_xjjh['rooms'][0]['inspectRoomId'] = self.jf_id
    #     feild_add_xjjh['inspectUser'] = self.hmc_u_id
    #     feild_add_xjjh['planStart'] = start_time
    #     feild_add_xjjh['planEnd'] = start_time + 86400000 * 5
    #     feild_add_xjjh['inspectPlanName'] = '计划名称' + str(uuid.uuid4())
    #     res_data = Page巡检计划管理.api_新增巡检计划(self.session, feild_add_xjjh, self.header)
    #     self.jh_id = res_data.get('data').get('id')
    #     # 新建消防告警配置
    #     feild_add_xfgj = Param_消防告警配置.p_add.get('紧急')
    #     feild_add_xfgj['eventName'] = '消防配置' + str(uuid.uuid4()).split('-')[-1]
    #     res_data = Page安防告警配置管理.api_新增安防告警配置(self.session, feild_add_xfgj, self.header)
    #     self.xf_id = res_data.get('data').get('id')
    #     # 新建安全告警配置
    #     # 上传图片
    #     feild_upload = Param_安全告警配置.p_upload.get('01')
    #     res_data = Page附件管理.api_上传附件(self.session, feild_upload, self.header)
    #     fid = res_data.get('data').get('fid')
    #     # 新增安全告警配置
    #     feild_add_aqgj = Param_安全告警配置.p_add.get('严重')
    #     feild_add_aqgj['blackName'] = '黑名称' + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_aqgj['remark'] = '备注' + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_aqgj['faceUrl'] = fid
    #     res_data = Page黑名单布控管理.api_新增黑名单布控(self.session, feild_add_aqgj, self.header)
    #     self.aq_id = res_data.get('data').get('id')
    #     # 执行生成线上巡检任务
    #     BizXxlJob.biz_执行定时任务(self.session_xxl, '线上巡检', '生成线上巡检任务')
    #     # 变更数据库开始时间为前一天开始
    #     Db设备智管.db_变更线上巡检任务开始时间(feild_add_xjjh.get('inspectPlanName'), start_time - 86400000)
    #     # 执行定时更新线上巡检任务状态
    #     BizXxlJob.biz_执行定时任务(self.session_xxl, '线上巡检', '定时更新线上巡检任务状态')
    #     # 通过名称page查询任务的id  task/page
    #     feild_page_rw = Param_巡检任务.p_page.get('任务名称')
    #     res_data = Page巡检任务管理.api_巡检任务分页查询(self.session, feild_page_rw, self.header)
    #     self.rw_id = res_data.get('data').get('records')[0].get('id')
    #     # 通过任务id查询任务房间列表  task/doTaskRoomList?id=1236
    #     feild_room_list = {'id': str(self.rw_id)}
    #     res_data = Page巡检任务管理.api_执行巡检任务查询巡检机房列表(self.session, feild_room_list, self.header)
    #     task_room_id = res_data.get('data')[0].get('id')
    #     # 通过房间列表查询房间的内容（获取参数）doTaskRoom?inspectTaskId=1236&taskRoomId=3029
    #     feild_room_task = {'inspectTaskId': str(self.rw_id),
    #                        'taskRoomId': str(task_room_id)}  # inspectTaskId=1642&taskRoomId=3986
    #     res_data = Page巡检任务管理.api_执行巡检任务查询巡检机房(self.session, feild_room_task, self.header)
    #     env_id = res_data.get('data').get('envs')[0].get('id')
    #     fac_id = res_data.get('data').get('facs')[0].get('id')
    #     #转告警
    #     feild_xf_alarm = Param_告警记录.p_alarm.get('安全告警')
    #     feild_xf_alarm['facId'] = self.tz_id
    #     feild_xf_alarm['alarmConfigId'] = self.aq_id
    #     res_data = Page告警记录管理.api_新增告警记录(self.session, feild_xf_alarm, self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     self.gjjl_id = res_data.get('data').get('id')
    #     #处理为线下跟进
    #     feild_chuli = Param_告警记录.p_chuli.get('线下跟进')
    #     feild_chuli['id'] = self.gjjl_id
    #     feild_chuli['remark'] = '备注'+str(uuid.uuid4())
    #     res_data = Page告警记录管理.api_处理告警(self.session,feild_chuli,self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #分页查询处理中告警展示信息并断言
    #     feild_page = Param_告警记录.p_page_clz.get('告警名称')
    #     res_data = Page告警记录管理.api_告警记录分页查询(self.session,feild_page,self.header)
    #     self.assertIn(feild_xf_alarm.get('alarmName'),str(res_data))
    #
    # def test_告警记录_03(self):
    #     """
    #     验证告警待处理，验证告警记录处理后状态正确（直接关闭）
    #     :return:
    #     """
    #     #通过线上巡检，转告警
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
    #     self.floor_id = res_data.get('data').get('list')[0].get('id')
    #     # 新增空间类型
    #     feild_add_space_type = Param_空间类型.p_add.get('同级')
    #     feild_add_space_type['spaceCode'] = "room" + str(uuid.uuid1())
    #     res_data = Page空间类型表管理.api_新增空间类型表(self.session, feild_add_space_type, self.header)
    #     self.space_type_id = res_data.get('data').get('id')
    #     # 新增空间
    #     feild_add_space = Param_空间信息.p_add.get('空间类型2')
    #     feild_add_space['propertyId'] = self.p_id
    #     feild_add_space['buildingId'] = self.f_id
    #     feild_add_space['buildingFloorId'] = self.floor_id
    #     feild_add_space['buildingFloorSpaceName'] = "room " + str(uuid.uuid1())
    #     feild_add_space['spaceId'] = self.space_type_id
    #     res_data = Page楼层房间信息表管理.api_新增楼层房间信息表(self.session, feild_add_space, self.header)
    #     self.room_id = res_data.get('data').get('id')
    #     # 新增环境巡检标准（依赖空间类型）
    #     feild_add_sbxj = Param_线上巡检标准.p_add.get('环境标准单条')
    #     feild_add_sbxj['spaceId'] = self.space_type_id
    #     feild_add_sbxj['remark'] = 'remark' + str(uuid.uuid4())
    #     feild_add_sbxj['checks'][0]['checkContent'] = '检查内容' + str(uuid.uuid4())
    #     res_data = Page环境巡检标准管理.api_新增环境巡检标准(self.session, feild_add_sbxj, self.header)
    #     self.sbxj_id = res_data.get('data').get('id')
    #     # 通过id查询标准，断言新增数据
    #     res_data = Page环境巡检标准管理.api_通过id查询环境巡检标准(self.session, str(self.sbxj_id), self.header)
    #     content_id = res_data.get('data').get('checks')[0].get('id')
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
    #     # 新增设备
    #     feild_add_tz = Param_设备台账.p_add.get('使用中')
    #     feild_add_tz['spaceId'] = self.room_id
    #     feild_add_tz['facCategoryId'] = self.sub_id
    #     feild_add_tz['facCateCode'] = feild_add_sub.get('facCateCode')
    #     feild_add_tz['facName'] = '设备名称' + str(uuid.uuid4())
    #     feild_add_tz['facCode'] = '设备编码' + str(uuid.uuid4())
    #     res_data = Page设备表管理.api_新增设备表(self.session, feild_add_tz, self.header)
    #     self.tz_id = res_data.get('data').get('id')
    #     # 新增巡检机房(依赖房间、环境巡检标准)
    #     feild_add = Param_巡检机房.p_add.get('巡检摄相头')
    #     feild_add['buildingId'] = self.f_id
    #     feild_add['buildingFloorId'] = self.floor_id
    #     feild_add['buildingFloorSpaceId'] = self.room_id
    #     feild_add['remark'] = 'remark' + str(uuid.uuid4())
    #     feild_add['envStandards'][0]['standardEnvId'] = self.sbxj_id
    #     feild_add['envStandards'][0]['standardEnvCheckId'] = content_id
    #     feild_add['cameras'][0]['inspectCameraId'] = self.tz_id
    #     feild_add['cameras'][0]['inspectCameraName'] = feild_add_tz.get('facName')
    #     feild_add['facs'][0]['inspectFacId'] = self.tz_id
    #     feild_add['facs'][0]['inspectFacCateId'] = self.sub_id
    #     res_data = Page巡检机房管理.api_新增巡检机房(self.session, feild_add, self.header)
    #     self.jf_id = res_data.get('data').get('id')
    #     # 上传Excel项目花名册人员
    #     # 将项目名称写入excel文件
    #     xmhmc = p_xmhmc.copy()
    #     xmhmc[0] = feild_add_p.get('propertyName')
    #     xmhmc[1] = 'haerbin'
    #     xmhmc[2] = 'Nangang District'
    #     write_excel_xmhmc('./test_data/excel/xmhmc.xlsx', xmhmc)
    #     # 上传
    #     feild_upload_hmc = {"fileName": 'xmhmc.xlsx', "file": (
    #     'xmhmc.xlsx', open('./test_data/excel/xmhmc.xlsx', 'rb'), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
    #     res_data = Page项目花名册管理.api_导入项目花名册(self.session, feild_upload_hmc, self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     # 获取名称列表，拿到花名册人员参数id
    #     res_data = Page项目花名册管理.api_项目花名册集合查询(self.session, self.header)
    #     self.hmc_u_id = res_data.get('data')[0].get('id')
    #     # 新增巡检计划（依赖机房、用户）
    #     start_time = int(round(time.time() * 1000))
    #     feild_add_xjjh = Param_巡检计划.p_add.get('任务测试')
    #     feild_add_xjjh['rooms'][0]['inspectRoomId'] = self.jf_id
    #     feild_add_xjjh['inspectUser'] = self.hmc_u_id
    #     feild_add_xjjh['planStart'] = start_time
    #     feild_add_xjjh['planEnd'] = start_time + 86400000 * 5
    #     feild_add_xjjh['inspectPlanName'] = '计划名称' + str(uuid.uuid4())
    #     res_data = Page巡检计划管理.api_新增巡检计划(self.session, feild_add_xjjh, self.header)
    #     self.jh_id = res_data.get('data').get('id')
    #     # 新建消防告警配置
    #     feild_add_xfgj = Param_消防告警配置.p_add.get('紧急')
    #     feild_add_xfgj['eventName'] = '消防配置' + str(uuid.uuid4()).split('-')[-1]
    #     res_data = Page安防告警配置管理.api_新增安防告警配置(self.session, feild_add_xfgj, self.header)
    #     self.xf_id = res_data.get('data').get('id')
    #     # 新建安全告警配置
    #     # 上传图片
    #     feild_upload = Param_安全告警配置.p_upload.get('01')
    #     res_data = Page附件管理.api_上传附件(self.session, feild_upload, self.header)
    #     fid = res_data.get('data').get('fid')
    #     # 新增安全告警配置
    #     feild_add_aqgj = Param_安全告警配置.p_add.get('严重')
    #     feild_add_aqgj['blackName'] = '黑名称' + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_aqgj['remark'] = '备注' + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_aqgj['faceUrl'] = fid
    #     res_data = Page黑名单布控管理.api_新增黑名单布控(self.session, feild_add_aqgj, self.header)
    #     self.aq_id = res_data.get('data').get('id')
    #     # 执行生成线上巡检任务
    #     BizXxlJob.biz_执行定时任务(self.session_xxl, '线上巡检', '生成线上巡检任务')
    #     # 变更数据库开始时间为前一天开始
    #     Db设备智管.db_变更线上巡检任务开始时间(feild_add_xjjh.get('inspectPlanName'), start_time - 86400000)
    #     # 执行定时更新线上巡检任务状态
    #     BizXxlJob.biz_执行定时任务(self.session_xxl, '线上巡检', '定时更新线上巡检任务状态')
    #     # 通过名称page查询任务的id  task/page
    #     feild_page_rw = Param_巡检任务.p_page.get('任务名称')
    #     res_data = Page巡检任务管理.api_巡检任务分页查询(self.session, feild_page_rw, self.header)
    #     self.rw_id = res_data.get('data').get('records')[0].get('id')
    #     # 通过任务id查询任务房间列表  task/doTaskRoomList?id=1236
    #     feild_room_list = {'id': str(self.rw_id)}
    #     res_data = Page巡检任务管理.api_执行巡检任务查询巡检机房列表(self.session, feild_room_list, self.header)
    #     task_room_id = res_data.get('data')[0].get('id')
    #     # 通过房间列表查询房间的内容（获取参数）doTaskRoom?inspectTaskId=1236&taskRoomId=3029
    #     feild_room_task = {'inspectTaskId': str(self.rw_id),
    #                        'taskRoomId': str(task_room_id)}  # inspectTaskId=1642&taskRoomId=3986
    #     res_data = Page巡检任务管理.api_执行巡检任务查询巡检机房(self.session, feild_room_task, self.header)
    #     env_id = res_data.get('data').get('envs')[0].get('id')
    #     fac_id = res_data.get('data').get('facs')[0].get('id')
    #     #转告警
    #     feild_xf_alarm = Param_告警记录.p_alarm.get('安全告警')
    #     feild_xf_alarm['facId'] = self.tz_id
    #     feild_xf_alarm['alarmConfigId'] = self.aq_id
    #     res_data = Page告警记录管理.api_新增告警记录(self.session, feild_xf_alarm, self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     self.gjjl_id = res_data.get('data').get('id')
    #     #处理为直接关闭
    #     feild_chuli = Param_告警记录.p_chuli.get('直接关闭')
    #     feild_chuli['id'] = self.gjjl_id
    #     feild_chuli['remark'] = '备注'+str(uuid.uuid4())
    #     res_data = Page告警记录管理.api_处理告警(self.session,feild_chuli,self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #通过id查询，状态为已完成
    #     res_data = Page告警记录管理.api_告警记录通过id查询(self.session,str(self.gjjl_id),self.header)
    #     self.assertEqual('3',str(res_data.get('data').get('alarmStatus')))
    #
    # def test_告警记录_04(self):
    #     """
    #     验证告警处理，处理中标签，验证告警记录处理后状态正确（更改跟进人、消警）
    #     :return:
    #     """
    #     #通过线上巡检，转告警
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
    #     self.floor_id = res_data.get('data').get('list')[0].get('id')
    #     # 新增空间类型
    #     feild_add_space_type = Param_空间类型.p_add.get('同级')
    #     feild_add_space_type['spaceCode'] = "room" + str(uuid.uuid1())
    #     res_data = Page空间类型表管理.api_新增空间类型表(self.session, feild_add_space_type, self.header)
    #     self.space_type_id = res_data.get('data').get('id')
    #     # 新增空间
    #     feild_add_space = Param_空间信息.p_add.get('空间类型2')
    #     feild_add_space['propertyId'] = self.p_id
    #     feild_add_space['buildingId'] = self.f_id
    #     feild_add_space['buildingFloorId'] = self.floor_id
    #     feild_add_space['buildingFloorSpaceName'] = "room " + str(uuid.uuid1())
    #     feild_add_space['spaceId'] = self.space_type_id
    #     res_data = Page楼层房间信息表管理.api_新增楼层房间信息表(self.session, feild_add_space, self.header)
    #     self.room_id = res_data.get('data').get('id')
    #     # 新增环境巡检标准（依赖空间类型）
    #     feild_add_sbxj = Param_线上巡检标准.p_add.get('环境标准单条')
    #     feild_add_sbxj['spaceId'] = self.space_type_id
    #     feild_add_sbxj['remark'] = 'remark' + str(uuid.uuid4())
    #     feild_add_sbxj['checks'][0]['checkContent'] = '检查内容' + str(uuid.uuid4())
    #     res_data = Page环境巡检标准管理.api_新增环境巡检标准(self.session, feild_add_sbxj, self.header)
    #     self.sbxj_id = res_data.get('data').get('id')
    #     # 通过id查询标准，断言新增数据
    #     res_data = Page环境巡检标准管理.api_通过id查询环境巡检标准(self.session, str(self.sbxj_id), self.header)
    #     content_id = res_data.get('data').get('checks')[0].get('id')
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
    #     # 新增设备
    #     feild_add_tz = Param_设备台账.p_add.get('使用中')
    #     feild_add_tz['spaceId'] = self.room_id
    #     feild_add_tz['facCategoryId'] = self.sub_id
    #     feild_add_tz['facCateCode'] = feild_add_sub.get('facCateCode')
    #     feild_add_tz['facName'] = '设备名称' + str(uuid.uuid4())
    #     feild_add_tz['facCode'] = '设备编码' + str(uuid.uuid4())
    #     res_data = Page设备表管理.api_新增设备表(self.session, feild_add_tz, self.header)
    #     self.tz_id = res_data.get('data').get('id')
    #     # 新增巡检机房(依赖房间、环境巡检标准)
    #     feild_add = Param_巡检机房.p_add.get('巡检摄相头')
    #     feild_add['buildingId'] = self.f_id
    #     feild_add['buildingFloorId'] = self.floor_id
    #     feild_add['buildingFloorSpaceId'] = self.room_id
    #     feild_add['remark'] = 'remark' + str(uuid.uuid4())
    #     feild_add['envStandards'][0]['standardEnvId'] = self.sbxj_id
    #     feild_add['envStandards'][0]['standardEnvCheckId'] = content_id
    #     feild_add['cameras'][0]['inspectCameraId'] = self.tz_id
    #     feild_add['cameras'][0]['inspectCameraName'] = feild_add_tz.get('facName')
    #     feild_add['facs'][0]['inspectFacId'] = self.tz_id
    #     feild_add['facs'][0]['inspectFacCateId'] = self.sub_id
    #     res_data = Page巡检机房管理.api_新增巡检机房(self.session, feild_add, self.header)
    #     self.jf_id = res_data.get('data').get('id')
    #     # 上传Excel项目花名册人员
    #     # 将项目名称写入excel文件
    #     xmhmc = p_xmhmc.copy()
    #     xmhmc[0] = feild_add_p.get('propertyName')
    #     xmhmc[1] = 'haerbin'
    #     xmhmc[2] = 'Nangang District'
    #     write_excel_xmhmc('./test_data/excel/xmhmc.xlsx', xmhmc)
    #     # 上传
    #     feild_upload_hmc = {"fileName": 'xmhmc.xlsx', "file": (
    #     'xmhmc.xlsx', open('./test_data/excel/xmhmc.xlsx', 'rb'), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
    #     res_data = Page项目花名册管理.api_导入项目花名册(self.session, feild_upload_hmc, self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     # 获取名称列表，拿到花名册人员参数id
    #     res_data = Page项目花名册管理.api_项目花名册集合查询(self.session, self.header)
    #     self.hmc_u_id = res_data.get('data')[0].get('id')
    #     # 新增巡检计划（依赖机房、用户）
    #     start_time = int(round(time.time() * 1000))
    #     feild_add_xjjh = Param_巡检计划.p_add.get('任务测试')
    #     feild_add_xjjh['rooms'][0]['inspectRoomId'] = self.jf_id
    #     feild_add_xjjh['inspectUser'] = self.hmc_u_id
    #     feild_add_xjjh['planStart'] = start_time
    #     feild_add_xjjh['planEnd'] = start_time + 86400000 * 5
    #     feild_add_xjjh['inspectPlanName'] = '计划名称' + str(uuid.uuid4())
    #     res_data = Page巡检计划管理.api_新增巡检计划(self.session, feild_add_xjjh, self.header)
    #     self.jh_id = res_data.get('data').get('id')
    #     # 新建消防告警配置
    #     feild_add_xfgj = Param_消防告警配置.p_add.get('紧急')
    #     feild_add_xfgj['eventName'] = '消防配置' + str(uuid.uuid4()).split('-')[-1]
    #     res_data = Page安防告警配置管理.api_新增安防告警配置(self.session, feild_add_xfgj, self.header)
    #     self.xf_id = res_data.get('data').get('id')
    #     # 新建安全告警配置
    #     # 上传图片
    #     feild_upload = Param_安全告警配置.p_upload.get('01')
    #     res_data = Page附件管理.api_上传附件(self.session, feild_upload, self.header)
    #     fid = res_data.get('data').get('fid')
    #     # 新增安全告警配置
    #     feild_add_aqgj = Param_安全告警配置.p_add.get('严重')
    #     feild_add_aqgj['blackName'] = '黑名称' + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_aqgj['remark'] = '备注' + str(uuid.uuid4()).split('-')[-1]
    #     feild_add_aqgj['faceUrl'] = fid
    #     res_data = Page黑名单布控管理.api_新增黑名单布控(self.session, feild_add_aqgj, self.header)
    #     self.aq_id = res_data.get('data').get('id')
    #     # 执行生成线上巡检任务
    #     BizXxlJob.biz_执行定时任务(self.session_xxl, '线上巡检', '生成线上巡检任务')
    #     # 变更数据库开始时间为前一天开始
    #     Db设备智管.db_变更线上巡检任务开始时间(feild_add_xjjh.get('inspectPlanName'), start_time - 86400000)
    #     # 执行定时更新线上巡检任务状态
    #     BizXxlJob.biz_执行定时任务(self.session_xxl, '线上巡检', '定时更新线上巡检任务状态')
    #     # 通过名称page查询任务的id  task/page
    #     feild_page_rw = Param_巡检任务.p_page.get('任务名称')
    #     res_data = Page巡检任务管理.api_巡检任务分页查询(self.session, feild_page_rw, self.header)
    #     self.rw_id = res_data.get('data').get('records')[0].get('id')
    #     # 通过任务id查询任务房间列表  task/doTaskRoomList?id=1236
    #     feild_room_list = {'id': str(self.rw_id)}
    #     res_data = Page巡检任务管理.api_执行巡检任务查询巡检机房列表(self.session, feild_room_list, self.header)
    #     task_room_id = res_data.get('data')[0].get('id')
    #     # 通过房间列表查询房间的内容（获取参数）doTaskRoom?inspectTaskId=1236&taskRoomId=3029
    #     feild_room_task = {'inspectTaskId': str(self.rw_id),
    #                        'taskRoomId': str(task_room_id)}  # inspectTaskId=1642&taskRoomId=3986
    #     res_data = Page巡检任务管理.api_执行巡检任务查询巡检机房(self.session, feild_room_task, self.header)
    #     env_id = res_data.get('data').get('envs')[0].get('id')
    #     fac_id = res_data.get('data').get('facs')[0].get('id')
    #     #转告警
    #     feild_xf_alarm = Param_告警记录.p_alarm.get('安全告警')
    #     feild_xf_alarm['facId'] = self.tz_id
    #     feild_xf_alarm['alarmConfigId'] = self.aq_id
    #     res_data = Page告警记录管理.api_新增告警记录(self.session, feild_xf_alarm, self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     self.gjjl_id = res_data.get('data').get('id')
    #     #处理为线下跟进
    #     feild_chuli = Param_告警记录.p_chuli.get('线下跟进')
    #     feild_chuli['id'] = self.gjjl_id
    #     feild_chuli['remark'] = '备注'+str(uuid.uuid4())
    #     res_data = Page告警记录管理.api_处理告警(self.session,feild_chuli,self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #变更跟进人
    #     feild_gjr = Param_告警记录.p_chuli.get('变更跟进人')
    #     feild_gjr['id'] = self.gjjl_id
    #     res_data = Page告警记录管理.api_处理告警(self.session,feild_gjr,self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     # 处理为消警
    #     feild_chuli = Param_告警记录.p_chuli.get('消警')
    #     feild_chuli['id'] = self.gjjl_id
    #     feild_chuli['remark'] = '备注' + str(uuid.uuid4())
    #     res_data = Page告警记录管理.api_处理告警(self.session, feild_chuli, self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     # 通过id查询，状态为已完成
    #     res_data = Page告警记录管理.api_告警记录通过id查询(self.session, str(self.gjjl_id), self.header)
    #     self.assertEqual('3',str(res_data.get('data').get('alarmStatus')))