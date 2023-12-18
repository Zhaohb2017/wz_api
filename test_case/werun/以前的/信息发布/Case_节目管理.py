import copy
import time
import unittest
import uuid

import ddt
import requests
import datetime


from business.param_config.api_param.werun.信息发布 import Param_素材管理, Param_节目管理
from page_object.werun.信息发布 import Page_节目管理
from page_object.werun.信息发布.Page_素材管理 import Page素材管理
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块

@ddt.ddt
class Case节目管理(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '节目管理'
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
        self.session.close()
        pass

    def test_节目管理_01(self):
        """
        验证新增图片节目，通过id查询新增节目，删除节目功能正常
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
        feild_search = copy.deepcopy(Param_素材管理.p_page.get('查询图片'))
        feild_search['body']['materialName'] = f_add ['materialName']
        res_data = Page素材管理.api_素材集合查询(self.session,feild_search,self.header)
        records = res_data.get('data').get('records')
        self.assertIn(str(fid), str(records))
        pic_id = 0
        for d in records:
            if d.get('fileId') == fid:
                pic_id = d.get('id')

        #新增节目
        feild_add_program = copy.deepcopy(Param_节目管理.p_add_program.get('图片'))
        feild_add_m = feild_add_program.get('materials')
        f_m = feild_add_m[0]
        f_m['materialId'] = pic_id
        feild_add_m[0] = f_m
        feild_add_program['programName'] = self.case_name +str(uuid.uuid4())
        res_data = Page_节目管理.Page节目管理.api_新增节目(self.session,feild_add_program,self.header)
        self.pro_id = res_data.get('data').get('id')

        # 通过id查询节目，断言节目是否新增成功
        res_data = Page_节目管理.Page节目管理.api_通过id查询节目(self.session,str(self.pro_id),self.header)
        self.assertEqual(res_data.get('data').get('programName'),feild_add_program['programName'])
        self.assertEqual(res_data.get('data').get('resolution'),feild_add_program.get('resolution'))
        self.assertEqual(res_data.get('data').get('playInterval'), feild_add_program.get('playInterval'))
        self.assertEqual(res_data.get('data').get('remark'), feild_add_program.get('remark'))
        self.assertIn(str(pic_id),str(res_data.get('data').get('materials')))

        #删除节目
        res_data = Page_节目管理.Page节目管理.api_通过id删除节目(self.session,str(self.pro_id),self.header)
        self.assertEqual(res_data.get('ok'), True)

        # 通过id查询节目，断言节目是否删除成功
        res_data = Page_节目管理.Page节目管理.api_通过id查询节目(self.session,str(self.pro_id),self.header)
        self.assertEqual(res_data.get('data'),None)

        # 删除素材
        res_data = Page素材管理.api_通过id删除素材(self.session, str(pic_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

        # 通过id查询预览素材，断言素材不存在
        res_data = Page素材管理.api_预览图片素材(self.session, str(pic_id), self.header)
        self.assertEqual(res_data.get('msg'), '素材不存在')

    # def test_节目管理_02(self):
    #     """
    #     验证新增音频节目，通过id查询新增节目，删除节目功能正常
    #     :return:
    #     """
    #     # 新增项目
    #     feild_add_p = Param_项目管理.p_add.get('学校')
    #     feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': self.p_id})
    #     #上传音频
    #     feild_upload = {'file':('autotest.mp3', open('test_data/auto_audio/autotest.mp3','rb'),'text/plain'),'classify':'publish','bizPath':'audio'}
    #     res_data = Page素材管理.api_上传音频素材(self.session, feild_upload, self.header)
    #     fid = res_data.get('data').get('fid')
    #
    #     # 新增音频素材
    #     feild_add = Param_素材管理.p_add.get('音频')
    #     f_add = feild_add[0] #字典
    #     f_add ['materialName'] = self.case_name+str(uuid.uuid4())
    #     f_add['fileId'] = fid
    #     feild_add[0] = f_add
    #     Page素材管理.api_新增素材(self.session,feild_add,self.header)
    #
    #     # 通过集合查询，并断言素材fid
    #     feild_search = copy.deepcopy(Param_素材管理.p_page.get('查询音频'))
    #     feild_search['body']['materialName'] = f_add ['materialName']
    #     res_data = Page素材管理.api_素材集合查询(self.session,feild_search,self.header)
    #     records = res_data.get('data').get('records')
    #     self.assertIn(str(fid), str(records))
    #     pic_id = 0
    #     for d in records:
    #         if d.get('fileId') == fid:
    #             pic_id = d.get('id')
    #
    #     # 新增节目
    #     feild_add_program = copy.deepcopy(Param_节目管理.p_add_program.get('音频'))
    #     feild_add_m = feild_add_program.get('materials')
    #     f_m = feild_add_m[0]
    #     f_m['materialId'] = pic_id
    #     feild_add_m[0] = f_m
    #     feild_add_program['programName'] = self.case_name + str(uuid.uuid4())
    #     res_data = Page_节目管理.Page节目管理.api_新增节目(self.session, feild_add_program, self.header)
    #     self.pro_id = res_data.get('data').get('id')
    #
    #     # 通过id查询节目，断言节目是否新增成功
    #     res_data = Page_节目管理.Page节目管理.api_通过id查询节目(self.session, str(self.pro_id), self.header)
    #     self.assertEqual(res_data.get('data').get('programName'), feild_add_program['programName'])
    #     self.assertEqual(res_data.get('data').get('resolution'), feild_add_program.get('resolution'))
    #     self.assertEqual(res_data.get('data').get('playInterval'), feild_add_program.get('playInterval'))
    #     self.assertEqual(res_data.get('data').get('remark'), feild_add_program.get('remark'))
    #     self.assertIn(str(pic_id), str(res_data.get('data').get('materials')))
    #
    #     # 删除节目
    #     res_data = Page_节目管理.Page节目管理.api_通过id删除节目(self.session, str(self.pro_id), self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #
    #     # 通过id查询节目，断言节目是否删除成功
    #     res_data = Page_节目管理.Page节目管理.api_通过id查询节目(self.session, str(self.pro_id), self.header)
    #     self.assertEqual(res_data.get('data'), None)
    #
    #     # 删除素材
    #     res_data = Page素材管理.api_通过id删除素材(self.session, str(pic_id), self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     # 通过id查询预览素材，断言素材不存在
    #     res_data = Page素材管理.api_预览图片素材(self.session, str(pic_id), self.header)
    #     self.assertEqual(res_data.get('msg'), '素材不存在')
    #
    # def test_节目管理_03(self):
    #     """
    #     验证新增视频节目，通过id查询新增节目，删除节目功能正常
    #     :return:
    #     """
    #     # 新增项目
    #     feild_add_p = Param_项目管理.p_add.get('学校')
    #     feild_add_p['propertyName'] = self.case_name + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': self.p_id})
    #     #上传视频
    #     feild_upload = {'file':('autotest.mp4', open('test_data/auto_video/autotest.mp4','rb'),'text/plain'),'classify':'publish','bizPath':'video'}
    #     res_data = Page素材管理.api_上传视频素材(self.session, feild_upload, self.header)
    #     fid = res_data.get('data').get('fid')
    #
    #     # 新增视频素材
    #     feild_add = Param_素材管理.p_add.get('视频')
    #     f_add = feild_add[0] #字典
    #     f_add ['materialName'] = self.case_name+str(uuid.uuid4())
    #     f_add['fileId'] = fid
    #     feild_add[0] = f_add
    #     Page素材管理.api_新增素材(self.session,feild_add,self.header)
    #
    #     # 通过集合查询，并断言素材fid
    #     feild_search = copy.deepcopy(Param_素材管理.p_page.get('查询视频'))
    #     feild_search['body']['materialName'] = f_add ['materialName']
    #     res_data = Page素材管理.api_素材集合查询(self.session,feild_search,self.header)
    #     records = res_data.get('data').get('records')
    #     self.assertIn(str(fid), str(records))
    #     pic_id = 0
    #     for d in records:
    #         if d.get('fileId') == fid:
    #             pic_id = d.get('id')
    #
    #     # 新增节目
    #     feild_add_program = copy.deepcopy(Param_节目管理.p_add_program.get('视频'))
    #     feild_add_m = feild_add_program.get('materials')
    #     f_m = feild_add_m[0]
    #     f_m['materialId'] = pic_id
    #     feild_add_m[0] = f_m
    #     feild_add_program['programName'] = self.case_name + str(uuid.uuid4())
    #     res_data = Page_节目管理.Page节目管理.api_新增节目(self.session, feild_add_program, self.header)
    #     self.pro_id = res_data.get('data').get('id')
    #
    #     # 通过id查询节目，断言节目是否新增成功
    #     res_data = Page_节目管理.Page节目管理.api_通过id查询节目(self.session, str(self.pro_id), self.header)
    #     self.assertEqual(res_data.get('data').get('programName'), feild_add_program['programName'])
    #     self.assertEqual(res_data.get('data').get('resolution'), feild_add_program.get('resolution'))
    #     self.assertEqual(res_data.get('data').get('playInterval'), feild_add_program.get('playInterval'))
    #     self.assertEqual(res_data.get('data').get('remark'), feild_add_program.get('remark'))
    #     self.assertIn(str(pic_id), str(res_data.get('data').get('materials')))
    #
    #     # 删除节目
    #     res_data = Page_节目管理.Page节目管理.api_通过id删除节目(self.session, str(self.pro_id), self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #
    #     # 通过id查询节目，断言节目是否删除成功
    #     res_data = Page_节目管理.Page节目管理.api_通过id查询节目(self.session, str(self.pro_id), self.header)
    #     self.assertEqual(res_data.get('data'), None)
    #
    #     # 删除素材
    #     res_data = Page素材管理.api_通过id删除素材(self.session, str(pic_id), self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     # 通过id查询预览素材，断言素材不存在
    #     res_data = Page素材管理.api_预览图片素材(self.session, str(pic_id), self.header)
    #     self.assertEqual(res_data.get('msg'), '素材不存在')

    def test_节目管理_04(self):
        """
        验证编辑节目，通过id查询编辑后的节目，信息修改功能正常
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
        pic_fid = res_data.get('data').get('fid')

        # 新增图片素材
        feild_add_pic = Param_素材管理.p_add.get('图片')
        f_add_pic = feild_add_pic[0] #字典
        f_add_pic ['materialName'] = self.case_name+str(uuid.uuid4())
        f_add_pic['fileId'] = pic_fid
        feild_add_pic[0] = f_add_pic
        Page素材管理.api_新增素材(self.session,feild_add_pic,self.header)

        # 通过集合查询，并断言素材fid
        feild_search_pic = copy.deepcopy(Param_素材管理.p_page.get('查询图片'))
        feild_search_pic['body']['materialName'] = f_add_pic['materialName']
        res_data = Page素材管理.api_素材集合查询(self.session,feild_search_pic,self.header)
        records = res_data.get('data').get('records')
        self.assertIn(str(pic_fid), str(records))
        pic_id = 0
        for d in records:
            if d.get('fileId') == pic_fid:
                pic_id = d.get('id')

        #上传音频
        feild_upload = {'file':('autotest.mp3', open('test_data/auto_audio/autotest.mp3','rb'),'text/plain'),'classify':'publish','bizPath':'audio'}
        res_data = Page素材管理.api_上传音频素材(self.session, feild_upload, self.header)
        audio_fid = res_data.get('data').get('fid')

        # 新增音频素材
        feild_add_audio= Param_素材管理.p_add.get('音频')
        f_add_audio = feild_add_audio[0] #字典
        f_add_audio ['materialName'] = self.case_name+str(uuid.uuid4())
        f_add_audio['fileId'] = audio_fid
        feild_add_audio[0] = f_add_audio
        Page素材管理.api_新增素材(self.session,feild_add_audio,self.header)

        # 通过集合查询，并断言素材fid
        feild_search_audio = copy.deepcopy(Param_素材管理.p_page.get('查询音频'))
        feild_search_audio['body']['materialName'] = f_add_audio ['materialName']
        res_data = Page素材管理.api_素材集合查询(self.session,feild_search_audio,self.header)
        records = res_data.get('data').get('records')
        self.assertIn(str(audio_fid), str(records))
        audio_id = 0
        for d in records:
            if d.get('fileId') == audio_fid:
                audio_id = d.get('id')
        #新增节目
        feild_add_program = copy.deepcopy(Param_节目管理.p_add_program.get('图片'))
        feild_add_m = feild_add_program.get('materials')
        f_m = feild_add_m[0]
        f_m['materialId'] = pic_id
        feild_add_m[0] = f_m
        feild_add_program['programName'] = self.case_name +str(uuid.uuid4())
        res_data = Page_节目管理.Page节目管理.api_新增节目(self.session,feild_add_program,self.header)
        self.pro_id = res_data.get('data').get('id')

        #修改节目{"materials":[{"materialId":33}],"programName":"新增节目","resolution":"1366*768","playInterval":"1","remark":"1","id":19}
        feild_upd_program = copy.deepcopy(Param_节目管理.p_upd_program.get('01'))
        feild_upd_m = feild_upd_program.get('materials')
        f_m = feild_upd_m[0]
        f_m['materialId'] = audio_id
        feild_upd_m[0] = f_m
        feild_upd_program['programName'] = "图片节目改音频节目" +str(uuid.uuid4())
        feild_upd_program['resolution'] = "3840*2160"
        feild_upd_program['playInterval'] = '2'
        feild_upd_program['remark'] = "图片节目改音频节目"
        feild_upd_program['id'] = self.pro_id
        res_data = Page_节目管理.Page节目管理.api_修改节目(self.session,feild_upd_program  , self.header)

        # 通过id查询节目，断言节目是否编辑成功
        res_data = Page_节目管理.Page节目管理.api_通过id查询节目(self.session,str(self.pro_id),self.header)
        self.assertEqual(res_data.get('data').get('programName'),feild_upd_program['programName'])
        self.assertEqual(res_data.get('data').get('resolution'),feild_upd_program.get('resolution'))
        self.assertEqual(res_data.get('data').get('playInterval'), feild_upd_program.get('playInterval'))
        self.assertEqual(res_data.get('data').get('remark'), feild_upd_program.get('remark'))
        self.assertIn(str(audio_id),str(res_data.get('data').get('materials')))

        #删除节目
        res_data = Page_节目管理.Page节目管理.api_通过id删除节目(self.session,str(self.pro_id),self.header)
        self.assertEqual(res_data.get('ok'), True)

        # 通过id查询节目，断言节目是否删除成功
        res_data = Page_节目管理.Page节目管理.api_通过id查询节目(self.session,str(self.pro_id),self.header)
        self.assertEqual(res_data.get('data'),None)

        # 删除图片素材
        res_data = Page素材管理.api_通过id删除素材(self.session, str(pic_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

        # 删除音频素材
        res_data = Page素材管理.api_通过id删除素材(self.session, str(audio_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

        # 通过id查询预览素材，断言素材不存在
        res_data = Page素材管理.api_预览图片素材(self.session, str(pic_id), self.header)
        self.assertEqual(res_data.get('msg'), '素材不存在')


    def test_节目管理_05(self):
        """
        验证节目集合查询功能，断言查询到的内容正确
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
        feild_search = copy.deepcopy(Param_素材管理.p_page.get('查询图片'))
        feild_search['body']['materialName'] = f_add ['materialName']
        res_data = Page素材管理.api_素材集合查询(self.session,feild_search,self.header)
        records = res_data.get('data').get('records')
        self.assertIn(str(fid), str(records))
        pic_id = 0
        for d in records:
            if d.get('fileId') == fid:
                pic_id = d.get('id')

        #新增节目
        feild_add_program = copy.deepcopy(Param_节目管理.p_add_program.get('图片'))
        feild_add_m = feild_add_program.get('materials')
        f_m = feild_add_m[0]
        f_m['materialId'] = pic_id
        feild_add_m[0] = f_m
        feild_add_program['programName'] = self.case_name +str(uuid.uuid4())
        res_data = Page_节目管理.Page节目管理.api_新增节目(self.session,feild_add_program,self.header)
        self.pro_id = res_data.get('data').get('id')

        #获取时间戳
        now = datetime.datetime.now()
        strnow1 = now.strftime('%Y-%m-%d') + ' 00:00:00'
        strnow2 = now.strftime('%Y-%m-%d') + ' 23:59:59'
        a1 = datetime.datetime.strptime(strnow1, '%Y-%m-%d %H:%M:%S')
        a2 = datetime.datetime.strptime(strnow2, '%Y-%m-%d %H:%M:%S')
        t1 = int(time.mktime(a1.timetuple()) * 1000.0 + a1.microsecond / 1000.0)
        t2 = int(time.mktime(a2.timetuple()) * 1000.0 + a2.microsecond / 1000.0)

        # 通过集合查询节目，断言节目是否新增成功
        feild_search = copy.deepcopy(Param_节目管理.p_page.get('集合查询'))
        feild_search['body']['programName'] = feild_add_program['programName']
        feild_search['body']['createdDateStart'] = t1
        feild_search['body']['createdDateEnd'] = t2
        res_data = Page_节目管理.Page节目管理.api_节目集合查询(self.session,feild_search,self.header)
        records = res_data.get('data').get('records')
        search_r = 0
        for r in records:
            if r.get('id') == self.pro_id:
                search_r = r
                pass
        self.assertEqual(feild_add_program['programName'], str(search_r.get('programName')))

        #删除节目
        res_data = Page_节目管理.Page节目管理.api_通过id删除节目(self.session,str(self.pro_id),self.header)
        self.assertEqual(res_data.get('ok'), True)

        # 通过id查询节目，断言节目是否删除成功
        res_data = Page_节目管理.Page节目管理.api_通过id查询节目(self.session,str(self.pro_id),self.header)
        self.assertEqual(res_data.get('data'),None)

        # 删除素材
        res_data = Page素材管理.api_通过id删除素材(self.session, str(pic_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

        # 通过id查询预览素材，断言素材不存在
        res_data = Page素材管理.api_预览图片素材(self.session, str(pic_id), self.header)
        self.assertEqual(res_data.get('msg'), '素材不存在')