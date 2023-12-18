import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.告警中心.告警配置 import Param_安全告警配置
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.上传下载.Page_附件管理 import Page附件管理
from page_object.werun.告警中心.Page_安防告警配置管理 import Page安防告警配置管理
from page_object.werun.告警中心.Page_黑名单布控管理 import Page黑名单布控管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case安全告警配置(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '安全告警配置'
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
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        if hasattr(self, 'aq_id'):
            Page黑名单布控管理.api_黑名单布控通过id删除(self.session, str(self.aq_id), self.header)
        if hasattr(self, 'aqpz_id'):
            Page安防告警配置管理.api_安防告警配置通过id删除(self.session, str(self.aqpz_id), self.header)
        self.session.close()
        pass

    @ddt.data(*Param_安全告警配置.p_add.keys())
    def test_安全告警配置_01(self,key):
        """
        验证新增黑名单布控，通过id查询新增布控人员，删除安全告警配置功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})
        #上传图片
        feild_upload = Param_安全告警配置.p_upload.get('01')
        res_data = Page附件管理.api_上传附件(self.session, feild_upload, self.header)
        fid = res_data.get('data').get('fid')
        # 新增安全告警配置
        feild_add_aqgj = Param_安全告警配置.p_add.get(key)
        feild_add_aqgj['blackName'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
        feild_add_aqgj['remark'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
        feild_add_aqgj['faceUrl'] = fid
        res_data = Page黑名单布控管理.api_新增黑名单布控(self.session,feild_add_aqgj,self.header)
        self.aq_id = res_data.get('data').get('id')
        # 通过id查询，并断言
        res_data = Page黑名单布控管理.api_黑名单布控通过id查询(self.session,str(self.aq_id),self.header)
        self.assertEqual(feild_add_aqgj.get('blackName'), res_data.get('data').get('blackName'))
        self.assertEqual(feild_add_aqgj.get('remark'), res_data.get('data').get('remark'))
        self.assertEqual(feild_add_aqgj.get('faceUrl'), res_data.get('data').get('faceUrl'))
        # 删除配置
        res_data = Page黑名单布控管理.api_黑名单布控通过id删除(self.session, str(self.aq_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过id查询，验证删除成功
        res_data = Page黑名单布控管理.api_黑名单布控通过id查询(self.session,str(self.aq_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    def test_安全告警配置_02(self):
        """
        验证分页查询黑名单布控功能正常（标签名称、告警等级、重置）
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})
        #上传图片
        feild_upload = Param_安全告警配置.p_upload.get('01')
        res_data = Page附件管理.api_上传附件(self.session, feild_upload, self.header)
        fid = res_data.get('data').get('fid')
        # 新增安全告警配置
        feild_add_aqgj = Param_安全告警配置.p_add.get('紧急')
        feild_add_aqgj['blackName'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
        feild_add_aqgj['remark'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
        feild_add_aqgj['faceUrl'] = fid
        res_data = Page黑名单布控管理.api_新增黑名单布控(self.session,feild_add_aqgj,self.header)
        self.aq_id = res_data.get('data').get('id')
        # 通过分页查询，并断言
        feild_page = Param_安全告警配置.p_page.get('标签名称')
        feild_page['body']['blackName'] = feild_add_aqgj.get('blackName')
        res_data = Page黑名单布控管理.api_黑名单布控分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_add_aqgj.get('blackName'),str(res_data))
        feild_page = Param_安全告警配置.p_page.get('告警等级')
        feild_page['body']['alarmLevel'] = feild_add_aqgj.get('alarmLevel')
        res_data = Page黑名单布控管理.api_黑名单布控分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_add_aqgj.get('blackName'),str(res_data))
        feild_page = Param_安全告警配置.p_page.get('重置')
        res_data = Page黑名单布控管理.api_黑名单布控分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_add_aqgj.get('blackName'),str(res_data))
        # 删除配置
        res_data = Page黑名单布控管理.api_黑名单布控通过id删除(self.session, str(self.aq_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过id查询，验证删除成功
        res_data = Page黑名单布控管理.api_黑名单布控通过id查询(self.session,str(self.aq_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    def test_安全告警配置_03(self):
        """
        验证黑名单布控名单启用、禁用功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})
        #上传图片
        feild_upload = Param_安全告警配置.p_upload.get('01')
        res_data = Page附件管理.api_上传附件(self.session, feild_upload, self.header)
        fid = res_data.get('data').get('fid')
        # 新增安全告警配置
        feild_add_aqgj = Param_安全告警配置.p_add.get('紧急')
        feild_add_aqgj['blackName'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
        feild_add_aqgj['remark'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
        feild_add_aqgj['faceUrl'] = fid
        res_data = Page黑名单布控管理.api_新增黑名单布控(self.session,feild_add_aqgj,self.header)
        self.aq_id = res_data.get('data').get('id')
        #禁用名单
        feild_off = Param_安全告警配置.p_on_off.get('禁用')
        feild_off['id'] = self.aq_id
        res_data = Page黑名单布控管理.api_黑名单布控启用禁用(self.session,feild_off,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询禁用状态
        res_data = Page黑名单布控管理.api_黑名单布控通过id查询(self.session, str(self.aq_id), self.header)
        self.assertEqual(0, res_data.get('data').get('activeState'))
        #启用名单
        feild_on = Param_安全告警配置.p_on_off.get('启用')
        feild_on['id'] = self.aq_id
        res_data = Page黑名单布控管理.api_黑名单布控启用禁用(self.session,feild_on,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询启用状态
        res_data = Page黑名单布控管理.api_黑名单布控通过id查询(self.session, str(self.aq_id), self.header)
        self.assertEqual(1, res_data.get('data').get('activeState'))
        # 删除配置
        res_data = Page黑名单布控管理.api_黑名单布控通过id删除(self.session, str(self.aq_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

    def test_安全告警配置_04(self):
        """
        验证编辑修改黑名单布控名单功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})
        #上传图片
        feild_upload = Param_安全告警配置.p_upload.get('01')
        res_data = Page附件管理.api_上传附件(self.session, feild_upload, self.header)
        fid = res_data.get('data').get('fid')
        # 新增安全告警配置
        feild_add_aqgj = Param_安全告警配置.p_add.get('紧急')
        feild_add_aqgj['blackName'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
        feild_add_aqgj['remark'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
        feild_add_aqgj['faceUrl'] = fid
        res_data = Page黑名单布控管理.api_新增黑名单布控(self.session,feild_add_aqgj,self.header)
        self.aq_id = res_data.get('data').get('id')
        #编辑修改安全告警配置
        feild_upd_aqgj = Param_安全告警配置.p_upd.get('01')
        feild_upd_aqgj['id'] = self.aq_id
        feild_upd_aqgj['blackName'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
        feild_upd_aqgj['remark'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
        feild_upd_aqgj['propertyId'] = self.p_id
        feild_upd_aqgj['faceUrl'] = fid
        res_data = Page黑名单布控管理.api_修改黑名单布控(self.session,feild_upd_aqgj,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询并断言
        res_data = Page黑名单布控管理.api_黑名单布控通过id查询(self.session, str(self.aq_id), self.header)
        self.assertEqual(feild_upd_aqgj.get('blackName'), res_data.get('data').get('blackName'))
        self.assertEqual(feild_upd_aqgj.get('remark'), res_data.get('data').get('remark'))
        self.assertEqual(feild_upd_aqgj.get('faceUrl'), res_data.get('data').get('faceUrl'))
        # 删除配置
        res_data = Page黑名单布控管理.api_黑名单布控通过id删除(self.session, str(self.aq_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

    @ddt.data(*Param_安全告警配置.p_add_o.keys())
    def test_安全告警配置_05(self,key):
        """
        验证新增安全告警其它布控，通过id查询新增其它布控断言比对正确，删除其它布控条目功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})
        # 新增安全告警配置(其它告警)
        feild_add_aqgj = Param_安全告警配置.p_add_o.get(key)
        feild_add_aqgj['eventName'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
        res_data = Page安防告警配置管理.api_新增安防告警配置(self.session,feild_add_aqgj,self.header)
        self.aqpz_id = res_data.get('data').get('id')
        # 通过id查询，并断言
        res_data = Page安防告警配置管理.api_安防告警配置通过id查询(self.session,str(self.aqpz_id),self.header)
        self.assertEqual(feild_add_aqgj.get('eventName'), res_data.get('data').get('eventName'))
        self.assertEqual(feild_add_aqgj.get('alarmLevel'), str(res_data.get('data').get('alarmLevel')))
        # 删除配置
        res_data = Page安防告警配置管理.api_安防告警配置通过id删除(self.session, str(self.aqpz_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过id查询，验证删除成功
        res_data = Page安防告警配置管理.api_安防告警配置通过id查询(self.session,str(self.aqpz_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    def test_安全告警配置_06(self):
        """
        验证安全告警其它布控启用禁用功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})
        # 新增安全告警配置(其它告警)
        feild_add_aqgj = Param_安全告警配置.p_add_o.get('一般')
        feild_add_aqgj['eventName'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
        res_data = Page安防告警配置管理.api_新增安防告警配置(self.session,feild_add_aqgj,self.header)
        self.aqpz_id = res_data.get('data').get('id')
        # 设置禁用
        feild_off = Param_安全告警配置.p_on_off_o.get('禁用')
        feild_off['id'] = self.aqpz_id
        res_data = Page安防告警配置管理.api_安防告警配置启用禁用(self.session,feild_off,self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询布控为禁用状态
        res_data = Page安防告警配置管理.api_安防告警配置通过id查询(self.session, str(self.aqpz_id), self.header)
        self.assertEqual(2, res_data.get('data').get('activeState'))
        # 设置启用
        feild_on = Param_安全告警配置.p_on_off_o.get('启用')
        feild_on['id'] = self.aqpz_id
        res_data = Page安防告警配置管理.api_安防告警配置启用禁用(self.session,feild_on,self.header)
        self.assertEqual(res_data.get('ok'),True)
        # 通过id查询布控为启用状态
        res_data = Page安防告警配置管理.api_安防告警配置通过id查询(self.session,str(self.aqpz_id),self.header)
        self.assertEqual(1, res_data.get('data').get('activeState'))
        # 删除配置
        res_data = Page安防告警配置管理.api_安防告警配置通过id删除(self.session, str(self.aqpz_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过id查询，验证删除成功
        res_data = Page安防告警配置管理.api_安防告警配置通过id查询(self.session,str(self.aqpz_id),self.header)
        self.assertEqual(res_data.get('data'),None)

    # def test_安全告警配置_07(self):
    #     """
    #     验证安全告警其它布控编辑修改功能正常
    #     :return:
    #     """
    #     # 新增项目
    #     feild_add_p = Param_项目管理.p_add.get('学校')
    #     feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': self.p_id})
    #     # 新增安全告警配置(其它告警)
    #     feild_add_aqgj = Param_安全告警配置.p_add_o.get('一般')
    #     feild_add_aqgj['eventName'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
    #     res_data = Page安防告警配置管理.api_新增安防告警配置(self.session,feild_add_aqgj,self.header)
    #     self.aqpz_id = res_data.get('data').get('id')
    #     # 编辑修改安全告警配置
    #     feild_upd = Param_安全告警配置.p_upd_o.get('01')
    #     feild_upd['id'] = self.aqpz_id
    #     feild_upd['eventName'] = self.case_name+str(uuid.uuid4()).split('-')[-1]
    #     res_data = Page安防告警配置管理.api_修改安防告警配置(self.session,feild_upd,self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     # 通过id查询安全告警配置并比对修改内容
    #     res_data = Page安防告警配置管理.api_安防告警配置通过id查询(self.session, str(self.aqpz_id), self.header)
    #     self.assertEqual(feild_upd.get('eventName'), res_data.get('data').get('eventName'))
    #     self.assertEqual(feild_upd.get('alarmLevel'), str(res_data.get('data').get('alarmLevel')))
    #     # 删除配置
    #     res_data = Page安防告警配置管理.api_安防告警配置通过id删除(self.session, str(self.aqpz_id), self.header)
    #     self.assertEqual(res_data.get('ok'), True)