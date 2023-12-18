import copy
import unittest
import uuid

import ddt
import requests
import datetime
import time


from business.param_config.api_param.werun.信息发布 import Param_素材管理
from page_object.werun.信息发布.Page_素材管理 import Page素材管理
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.上传下载.Page_附件管理 import Page附件管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块

@ddt.ddt
class Case素材管理(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '素材管理'
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
        if hasattr(self, 'pic_id'):
            Page素材管理.api_通过id删除素材(self.session, str(self.spic_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass

    # def test_素材管理_01(self):
    #     """
    #     验证新增图片素材，通过id查询新增素材，删除素材功能正常
    #     :return:
    #     """
    #     # 新增项目
    #     feild_add_p = Param_项目管理.p_add.get('学校')
    #     feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': self.p_id})
    #     #上传图片
    #     feild_upload = Param_素材管理.p_upload.get('图片')
    #     res_data = Page附件管理.api_上传附件(self.session, feild_upload, self.header)
    #     fid = res_data.get('data').get('fid')
    #
    #     # 新增图片素材
    #     feild_add = Param_素材管理.p_add.get('图片')
    #     f_add = feild_add[0] #字典
    #     f_add ['materialName'] = self.case_name+str(uuid.uuid4())
    #     f_add['fileId'] = fid
    #     feild_add[0] = f_add
    #     Page素材管理.api_新增素材(self.session,feild_add,self.header)
    #
    #     # 通过集合查询，并断言素材fid
    #     now = datetime.datetime.now()
    #     strnow1 = now.strftime('%Y-%m-%d') + ' 00:00:00'
    #     strnow2 = now.strftime('%Y-%m-%d') + ' 23:59:59'
    #     a1 = datetime.datetime.strptime(strnow1, '%Y-%m-%d %H:%M:%S')
    #     a2 = datetime.datetime.strptime(strnow2, '%Y-%m-%d %H:%M:%S')
    #     t1 = int(time.mktime(a1.timetuple()) * 1000.0 + a1.microsecond / 1000.0)
    #     t2 = int(time.mktime(a2.timetuple()) * 1000.0 + a2.microsecond / 1000.0)
    #
    #     feild_search = copy.deepcopy(Param_素材管理.p_page.get('查询图片'))
    #     feild_search['body']['materialName'] = f_add ['materialName']
    #     feild_search['body']['createdDateStart'] = t1
    #     feild_search['body']['createdDateEnd'] = t2
    #     res_data = Page素材管理.api_素材集合查询(self.session,feild_search,self.header)
    #     records = res_data.get('data').get('records')
    #     self.assertIn(str(fid), str(records))
    #     self.spic_id = 0
    #     for d in records:
    #         if d.get('fileId') == fid:
    #             self.spic_id = d.get('id')
    #     # 删除素材
    #     res_data = Page素材管理.api_通过id删除素材(self.session, str(self.spic_id), self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     # 通过id查询预览素材，断言素材不存在
    #     res_data = Page素材管理.api_预览图片素材(self.session, str(self.spic_id), self.header)
    #     self.assertEqual(res_data.get('msg'), '素材不存在')

    def test_素材管理_02(self):
        """
        验证下载素材，断言素材内容正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})

        #上传图片
        feild_upload = Param_素材管理.p_upload.get('图片')
        res_data = Page素材管理.api_上传图片素材(self.session, feild_upload, self.header)
        fid = res_data.get('data').get('fid')

        # 新增图片素材
        feild_add = Param_素材管理.p_add.get('图片')
        f_add = feild_add[0] #字典
        f_add ['materialName'] = self.case_name+str(uuid.uuid4())
        f_add['fileId'] = fid
        feild_add[0] = f_add
        Page素材管理.api_新增素材(self.session,feild_add,self.header)

        # 通过集合查询，并断言素材fid
        now = datetime.datetime.now()
        strnow1 = now.strftime('%Y-%m-%d') + ' 00:00:00'
        strnow2 = now.strftime('%Y-%m-%d') + ' 23:59:59'
        a1 = datetime.datetime.strptime(strnow1, '%Y-%m-%d %H:%M:%S')
        a2 = datetime.datetime.strptime(strnow2, '%Y-%m-%d %H:%M:%S')
        t1 = int(time.mktime(a1.timetuple()) * 1000.0 + a1.microsecond / 1000.0)
        t2 = int(time.mktime(a2.timetuple()) * 1000.0 + a2.microsecond / 1000.0)

        feild_search = copy.deepcopy(Param_素材管理.p_page.get('查询图片'))
        feild_search['body']['materialName'] = f_add['materialName']
        feild_search['body']['createdDateStart'] = t1
        feild_search['body']['createdDateEnd'] = t2
        res_data = Page素材管理.api_素材集合查询(self.session, feild_search, self.header)
        records = res_data.get('data').get('records')
        self.assertIn(str(fid), str(records))
        self.spic_id = 0
        for d in records:
            if d.get('fileId') == fid:
                self.spic_id = d.get('id')

        #下载图片素材
        res_data = Page素材管理.api_下载素材(self.session,str(fid),self.header)
        self.assertEqual(res_data,200)

        # 删除素材
        res_data = Page素材管理.api_通过id删除素材(self.session, str(self.spic_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        # 通过id查询预览素材，断言素材不存在
        res_data = Page素材管理.api_预览图片素材(self.session, str(self.spic_id), self.header)
        self.assertEqual(res_data.get('msg'), '素材不存在')

    def test_素材管理_03(self):
        """
        验证新增音频素材，通过id查询新增素材，删除素材功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})
        #上传音频
        feild_upload = Param_素材管理.p_upload.get('音频')
        res_data = Page素材管理.api_上传音频素材(self.session, feild_upload, self.header)
        fid = res_data.get('data').get('fid')

        # 新增音频素材
        feild_add = Param_素材管理.p_add.get('音频')
        f_add = feild_add[0] #字典
        f_add ['materialName'] = self.case_name+str(uuid.uuid4())
        f_add['fileId'] = fid
        feild_add[0] = f_add
        Page素材管理.api_新增素材(self.session,feild_add,self.header)

        # 通过集合查询，并断言素材fid
        now = datetime.datetime.now()
        strnow1 = now.strftime('%Y-%m-%d') + ' 00:00:00'
        strnow2 = now.strftime('%Y-%m-%d') + ' 23:59:59'
        a1 = datetime.datetime.strptime(strnow1, '%Y-%m-%d %H:%M:%S')
        a2 = datetime.datetime.strptime(strnow2, '%Y-%m-%d %H:%M:%S')
        t1 = int(time.mktime(a1.timetuple()) * 1000.0 + a1.microsecond / 1000.0)
        t2 = int(time.mktime(a2.timetuple()) * 1000.0 + a2.microsecond / 1000.0)

        feild_search = copy.deepcopy(Param_素材管理.p_page.get('查询音频'))
        feild_search['body']['materialName'] = f_add ['materialName']
        feild_search['body']['createdDateStart'] = t1
        feild_search['body']['createdDateEnd'] = t2
        res_data = Page素材管理.api_素材集合查询(self.session,feild_search,self.header)
        records = res_data.get('data').get('records')
        self.assertIn(str(fid), str(records))
        self.spic_id = 0
        for d in records:
            if d.get('fileId') == fid:
                self.spic_id = d.get('id')
        # 删除素材
        res_data = Page素材管理.api_通过id删除素材(self.session, str(self.spic_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        # 通过id查询预览素材，断言素材不存在
        res_data = Page素材管理.api_预览图片素材(self.session, str(self.spic_id), self.header)
        self.assertEqual(res_data.get('msg'), '素材不存在')

    def test_素材管理_04(self):
        """
        验证新增视频素材，通过id查询新增素材，删除素材功能正常
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': self.p_id})
        #上传视频
        feild_upload = Param_素材管理.p_upload.get('视频')
        res_data = Page素材管理.api_上传视频素材(self.session, feild_upload, self.header)
        fid = res_data.get('data').get('fid')

        # 新增视频素材
        feild_add = Param_素材管理.p_add.get('视频')
        f_add = feild_add[0] #字典
        f_add ['materialName'] = self.case_name+str(uuid.uuid4())
        f_add['fileId'] = fid
        feild_add[0] = f_add
        Page素材管理.api_新增素材(self.session,feild_add,self.header)

        # 通过集合查询，并断言素材fid

        now = datetime.datetime.now()
        strnow1 = now.strftime('%Y-%m-%d') + ' 00:00:00'
        strnow2 = now.strftime('%Y-%m-%d') + ' 23:59:59'
        a1 = datetime.datetime.strptime(strnow1, '%Y-%m-%d %H:%M:%S')
        a2 = datetime.datetime.strptime(strnow2, '%Y-%m-%d %H:%M:%S')
        t1 = int(time.mktime(a1.timetuple()) * 1000.0 + a1.microsecond / 1000.0)
        t2 = int(time.mktime(a2.timetuple()) * 1000.0 + a2.microsecond / 1000.0)

        feild_search = copy.deepcopy(Param_素材管理.p_page.get('查询视频'))
        feild_search['body']['materialName'] = f_add ['materialName']
        feild_search['body']['createdDateStart'] = t1
        feild_search['body']['createdDateEnd'] = t2
        res_data = Page素材管理.api_素材集合查询(self.session,feild_search,self.header)
        records = res_data.get('data').get('records')
        self.assertIn(str(fid), str(records))
        self.spic_id = 0
        for d in records:
            if d.get('fileId') == fid:
                self.spic_id = d.get('id')
        # 删除素材
        res_data = Page素材管理.api_通过id删除素材(self.session, str(self.spic_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        # 通过id查询预览素材，断言素材不存在
        res_data = Page素材管理.api_预览图片素材(self.session, str(self.spic_id), self.header)
        self.assertEqual(res_data.get('msg'), '素材不存在')

