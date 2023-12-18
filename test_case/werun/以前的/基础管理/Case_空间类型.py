import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_空间类型, Param_登录登出, Param_项目管理
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case空间类型(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '空间类型'
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session)
        self.public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        self.encrypt_pwd = rsa_encrypt(self.public_key, feild.get('sword'))
        feild['sword'] = self.encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(self.session, feild, {})
        self.header = {'traceId': str(uuid.uuid4()), 'Authorization': "Bearer " + res_data.get('data').get('token')}
        pass

    def tearDown(self):
        if hasattr(self, 'space_type_id'):
            Page空间类型表管理.api_空间类型通过id删除(self.session, str(self.space_type_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.session.close()
        pass


    def test_空间类型_01(self):
        """
        验证新增同级空间类型、通过Id查询空间类型并断言新增信息正确、通过id删除空间类型
        :return:
        """
        #新增项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = res_data.get('data').get('id')
        #新增同级空间类型
        feild_add = Param_空间类型.p_add.get("同级")
        feild_add['spaceName'] = "空间"+str(uuid.uuid1())
        feild_add['spaceCode'] = "code"+str(uuid.uuid1())
        self.header.update({'propertyId':str(self.p_id)})
        res_data = Page空间类型表管理.api_新增空间类型表(self.session,feild_add,self.header)
        self.space_type_id = res_data.get('data').get('id')
        #通过id查询空间类型并断言新增的信息
        res_data = Page空间类型表管理.api_空间类型通过id查询(self.session,str(self.space_type_id),self.header)
        self.assertEqual(feild_add.get('spaceName'),res_data.get('data').get('spaceName'))
        self.assertEqual(feild_add.get('spaceCode'),res_data.get('data').get('spaceCode'))
        #通过id删除新增空间类型
        res_data = Page空间类型表管理.api_空间类型通过id删除(self.session,str(self.space_type_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #通过id查询，断言数据已删除
        res_data = Page空间类型表管理.api_空间类型通过id查询(self.session, str(self.space_type_id), self.header)
        self.assertEqual(res_data.get('data'), None)
        #删除新增项目
        res_data = Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

    def test_空间类型_02(self):
        """
        验证新增下级空间类型、通过Id查询下级空间类型并断言新增信息正确、通过id删除下级空间类型
        :return:
        """
        #新建项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = res_data.get('data').get('id')
        #新建同级空间类型，header加个项目id
        feild_add = Param_空间类型.p_add.get("同级")
        feild_add['spaceName'] = "空间" + str(uuid.uuid1())
        feild_add['spaceCode'] = "code" + str(uuid.uuid1())
        self.header.update({'propertyId': str(self.p_id)})
        res_data = Page空间类型表管理.api_新增空间类型表(self.session,feild_add,self.header)
        self.space_type_id = res_data.get('data').get('id')
        #新建下级空间类型
        feild_add_sub = Param_空间类型.p_add.get('下级')
        feild_add_sub['spaceName'] = "空间" + str(uuid.uuid1())
        feild_add_sub['spaceCode'] = "code" + str(uuid.uuid1())
        feild_add_sub['parentId'] = self.space_type_id
        res_data = Page空间类型表管理.api_新增空间类型表(self.session, feild_add_sub, self.header)
        self.space_type_id_sub = res_data.get('data').get('id')
        #通过id查询下级空间类型并断言新增信息正确
        res_data = Page空间类型表管理.api_空间类型通过id查询(self.session, str(self.space_type_id_sub), self.header)
        self.assertEqual(feild_add_sub.get('spaceName'), res_data.get('data').get('spaceName'))
        self.assertEqual(feild_add_sub.get('spaceCode'), res_data.get('data').get('spaceCode'))
        self.assertEqual(feild_add_sub.get('parentId'), res_data.get('data').get('parentId'))
        #通过id删除下级空间类型
        res_data = Page空间类型表管理.api_空间类型通过id删除(self.session, str(self.space_type_id_sub), self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过id查询
        res_data = Page空间类型表管理.api_空间类型通过id查询(self.session, str(self.space_type_id_sub), self.header)
        self.assertEqual(res_data.get('data'),None)
        #通过id删除同级空间类型
        res_data = Page空间类型表管理.api_空间类型通过id删除(self.session, str(self.space_type_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过id删除项目
        res_data = Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

    def test_空间类型_03(self):
        """
        验证同级空间类型编辑修改功能、通过Id查询修改后的空间类型并断言修改信息正确
        :return:
        """
        #新建项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = res_data.get('data').get('id')
        #新建同级空间类型，header加个项目id
        feild_add = Param_空间类型.p_add.get("同级")
        feild_add['spaceName'] = "空间" + str(uuid.uuid1())
        feild_add['spaceCode'] = "code" + str(uuid.uuid1())
        self.header.update({'propertyId': str(self.p_id)})
        res_data = Page空间类型表管理.api_新增空间类型表(self.session, feild_add, self.header)
        self.space_type_id = res_data.get('data').get('id')
        #修改同级空间类型
        feild_upd = Param_空间类型.p_upd.get('同级')
        feild_upd['spaceName'] = "空间" + str(uuid.uuid1())
        feild_upd['spaceCode'] = "code" + str(uuid.uuid1())
        feild_upd['id'] = self.space_type_id
        Page空间类型表管理.api_修改空间类型表(self.session, feild_upd, self.header)
        #通过id查询空间类型，并断言修改后内容变更
        res_data = Page空间类型表管理.api_空间类型通过id查询(self.session, str(self.space_type_id), self.header)
        self.assertEqual(feild_upd.get('spaceName'), res_data.get('data').get('spaceName'))
        self.assertEqual(feild_upd.get('spaceCode'), res_data.get('data').get('spaceCode'))
        #通过id删除同级空间类型
        res_data = Page空间类型表管理.api_空间类型通过id删除(self.session, str(self.space_type_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过id删除项目
        res_data = Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.assertEqual(res_data.get('ok'), True)

    def test_空间类型_04(self):
        """
        验证下级空间类型编辑修改功能、通过Id查询修改后的空间类型并断言修改信息正确
        :return:
        """
        #新增项目
        feild_add = Param_项目管理.p_add.get('学校')
        feild_add['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
        self.p_id = res_data.get('data').get('id')
        #新增同级空间类型，header加个项目id
        feild_add = Param_空间类型.p_add.get("同级")
        feild_add['spaceName'] = "空间" + str(uuid.uuid1())
        feild_add['spaceCode'] = "code" + str(uuid.uuid1())
        self.header.update({'propertyId': str(self.p_id)})
        res_data = Page空间类型表管理.api_新增空间类型表(self.session, feild_add, self.header)
        self.space_type_id = res_data.get('data').get('id')
        #新增下级空间类型
        feild_add_sub = Param_空间类型.p_add.get('下级')
        feild_add_sub['spaceName'] = "空间" + str(uuid.uuid1())
        feild_add_sub['spaceCode'] = "code" + str(uuid.uuid1())
        feild_add_sub['parentId'] = self.space_type_id
        res_data = Page空间类型表管理.api_新增空间类型表(self.session, feild_add_sub, self.header)
        self.space_type_id_sub = res_data.get('data').get('id')
        #修改下级空间类型
        feild_upd = Param_空间类型.p_upd.get('下级')
        feild_upd['spaceName'] = "空间" + str(uuid.uuid1())
        feild_upd['spaceCode'] = "code" + str(uuid.uuid1())
        feild_upd['parentId'] = self.space_type_id
        feild_upd['id'] = self.space_type_id_sub
        Page空间类型表管理.api_修改空间类型表(self.session, feild_upd, self.header)
        #通过id查询空间类型，断言新增的信息
        res_data = Page空间类型表管理.api_空间类型通过id查询(self.session, str(self.space_type_id_sub), self.header)
        self.assertEqual(feild_upd.get('spaceName'), res_data.get('data').get('spaceName'))
        self.assertEqual(feild_upd.get('spaceCode'), res_data.get('data').get('spaceCode'))
        self.assertEqual(str(feild_upd.get('parentId')), str(res_data.get('data').get('parentId')))
        #删除同级空间类型
        res_data = Page空间类型表管理.api_空间类型通过id删除(self.session, str(self.space_type_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        #通过id查询下级空间类型,断言新增的下级已删除
        res_data = Page空间类型表管理.api_空间类型通过id查询(self.session, str(self.space_type_id_sub), self.header)
        self.assertEqual(res_data.get('data'),None)
        #通过id删除项目
        res_data = Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        self.assertEqual(res_data.get('ok'), True)
        pass

    # def test_空间类型_05(self):
    #     """
    #     验证空间类型导入功能，断言查询与导入的空间类型参数一致
    #     :return:
    #     """
    #     #新增项目,获取项目id
    #     #重写excel里面项目id
    #     #导入空间类型（有返回id则获取id）
    #     #查询空间类型并断言
    #     #通过id删除空间类型
    #     #通过id删除项目
    #     pass
    #
    # def test_空间类型_06(self):
    #     """
    #     验证空间类型下载导入模版功能,断言返回正常
    #     :return:
    #     """
    #     #下载导入模版
    #     #断言ok
    #     pass

