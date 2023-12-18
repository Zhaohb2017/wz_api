import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.专家知识库 import Param_企业故障标准手册
from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_项目管理, Param_设备类型
from common.M_Crypto import rsa_encrypt
from page_object.werun.专家知识库.Page_故障原因 import Page故障原因
from page_object.werun.专家知识库.Page_故障现象 import Page故障现象
from page_object.werun.专家知识库.Page_解决办法 import Page解决办法
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块


@ddt.ddt
class Case企业故障标准手册(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '企业故障标准手册'
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
        if hasattr(self,'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, str(self.p_id), self.header)
        if hasattr(self, 's_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session,str(self.s_id),self.header)
        if hasattr(self, 'fs_id'):
            Page设备类型表管理.api_设备类型通过id删除(self.session,str(self.fs_id),self.header)
        if hasattr(self, 'gzxx_id'):
            Page故障现象.api_通过id删除故障现象(self.session, str(self.gzxx_id), self.header)
        if hasattr(self, 'gzyy_id'):
            Page故障原因.api_通过id删除故障原因(self.session, str(self.gzyy_id), self.header)
        self.session.close()
        pass


    def test_故障原因_01(self):
        """
        单接口测试: 新增故障原因
        :return:
        """
        global add_res_data
        # 1.新增故障原因接口
        feild_add_gzxx = Param_企业故障标准手册.p_add_gzyy.get("一般")
        add_res_data = Page故障原因.api_新增故障原因(self.session, feild_add_gzxx, self.header)
        self.assertEqual( add_res_data.get("code"),200)

    def test_故障原因_02(self):
        """
        单接口: 通过id查询故障原因
        :return:
        """
        global gzyy_id
        gzyy_id =  add_res_data.get('data').get('id')
        query_res_data = Page故障原因.api_通过id查询故障原因(self.session, str(gzyy_id), self.header)
        self.assertEqual(query_res_data.get("code"), 200)


    def test_故障原因_03(self):
        """
        单接口: 通过id删除故障原因
        :return:
        """
        del_res_data = Page故障原因.api_通过id删除故障原因(self.session, str(gzyy_id), self.header)
        self.assertEqual(del_res_data.get("code"), 200)

    def test_故障原因_04(self):
        """
        单接口: 分页查询故障原因默认请求数据
        :return:
        """
        feilds = Param_企业故障标准手册.p_query_gzyy.get("默认查询")
        query_res_data = Page故障原因.api_分页查询故障原因(self.session, feilds, self.header)
        self.assertEqual(query_res_data.get("code"), 200)

    def test_故障现象_01(self):
        """
        单接口: 1.新增故障现象
        :return:
        """
        global gzxx_id
        feild_add_gzxx = Param_企业故障标准手册.p_add_gzxx.get('优先级1')
        res_data = Page故障现象.api_新增故障现象(self.session,feild_add_gzxx,self.header)
        self.assertEqual(res_data.get('code'),200)
        gzxx_id = res_data.get('data').get('id')

    def test_故障现象_02(self):
        """
        单接口: 2.修改故障现象
        :return:
        """

        feild_upd_gzxx = Param_企业故障标准手册.p_upd_gzxx.get('01')
        feild_upd_gzxx['id'] = gzxx_id
        res_data = Page故障现象.api_修改故障现象(self.session, feild_upd_gzxx, self.header)
        self.assertEqual(res_data.get('ok'), True)

    def test_故障现象_03(self):
        """
        单接口: 3.查询故障现象分页查询
        :return:
        """
        page_query_gzxx = Param_企业故障标准手册.p_query_gzxx.get('默认查询')
        res_data = Page故障现象.api_故障现象分页查询(self.session, page_query_gzxx, self.header)
        self.assertEqual(res_data.get('code'),200)

    def test_故障现象_04(self):
        """
        单接口: 4.通过id查询故障现象
        :return:
        """
        res_data = Page故障现象.api_通过id查询故障现象(self.session, str(gzxx_id), self.header)
        self.assertEqual(res_data.get('code'), 200)

    def test_故障现象_05(self):
        """
        单接口: 5.通过id删除故障现象
        :return:
        """
        # 5.通过id删除故障现象
        res_data = Page故障现象.api_通过id删除故障现象(self.session,str(gzxx_id),self.header)
        self.assertEqual(res_data.get('ok'),True)

    @ddt.data(*Param_企业故障标准手册.p_add_jjff.keys())
    def test_解决方法_增(self,key):
        """
        单接口：1.新增解决方法
        :return:
        """
        global jjff_id
        feild_add_jjff = Param_企业故障标准手册.p_add_jjff.get(key)
        res_data = Page解决办法.api_新增解决方法(self.session, feild_add_jjff, self.header)
        self.assertEqual(res_data.get('code'), 200)
        jjff_id = res_data.get('data').get('id')

    def test_解决方法_改(self):
        """
        单接口：2.修改解决方法
        :param key:
        :return:
        """
        # 2.修改解决方法
        upd_jjff = Param_企业故障标准手册.p_upd_jjff.get("01")
        upd_jjff["id"] = jjff_id
        res_data = Page解决办法.api_修改解决方法(self.session, upd_jjff, self.header)
        self.assertEqual(res_data.get('code'), 200)

    def test_解决方法_查01(self):
        """
        单接口:3.分页查询解决方法
        :return:
        """
        #3.分页查询解决方法
        query_jjff = Param_企业故障标准手册.p_query_jjff.get("01")
        res_data = Page解决办法.api_分页查询解决办法(self.session,query_jjff,self.header)
        self.assertEqual(res_data.get('code'),200)

    def test_解决方法_查02(self):
        """
        单接口:4.通过id 查询解决方法
        :return:
        """
        #4.通过id 查询解决方法
        res_data = Page解决办法.api_通过id查询解决方法(self.session,str(jjff_id),self.header)
        self.assertEqual(res_data.get('code'),200)

    def test_解决方法_删(self):
        """
        单接口: 5.通过id删除解决方法
        :return:
        """
        res_data = Page解决办法.api_通过id删除解决方法(self.session,str(jjff_id),self.header)
        self.assertEqual(res_data.get('code'),200)



    def test_解决方法_故障现象描述集合(self):
        """
        单接口: 1.故障现象描述集合
        :return:
        """
        upd_jjff = Param_企业故障标准手册.p_set_jjff.get("默认")
        res_data = Page解决办法.api_查询故障现象集合(self.session,upd_jjff,self.header)
        self.assertEqual(res_data.get('code'),200)








    # @ddt.data(*Param_企业故障标准手册.p_add_gzxx.keys())
    # def test_企业故障标准手册_01(self,key):
    #     """
    #     验证新增故障现象，通过id查询新增现象参数正确，通过id删除故障现象功能正常
    #     :return:
    #     """
    #     #新增项目，设置header的项目id
    #     feild_add = Param_项目管理.p_add.get('学校')
    #     feild_add['propertyName'] = "项目" + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId':self.p_id})
    #     # 新增同级
    #     feild_add = Param_设备类型.p_add.get('一级设备')
    #     feild_add['facCateName'] = '设备类型' + str(uuid.uuid4())
    #     feild_add['facCateCode'] = '类型编码' + str(uuid.uuid4())
    #     res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add, self.header)
    #     self.fs_id = res_data.get('data').get('id')
    #     # 新增下级
    #     feild_add_sub = Param_设备类型.p_add_sub.get('下级设备类型')
    #     feild_add_sub['facCateName'] = '设备类型' + str(uuid.uuid4())
    #     feild_add_sub['facCateCode'] = '类型编号' + str(uuid.uuid4())
    #     feild_add_sub['parentId'] = self.fs_id
    #     res_data = Page设备类型表管理.api_新增设备类型表(self.session, feild_add_sub, self.header)
    #     self.s_id = res_data.get('data').get('id')
    #     #新增故障现象(依赖项目)
    #     feild_add_gzxx = Param_企业故障标准手册.p_add_gzxx.get(key)
    #     feild_add_gzxx['manualName'] = '现象名称'+ str(uuid.uuid4())
    #     feild_add_gzxx['facCateId'] = self.s_id
    #     res_data = Page故障现象.api_新增故障现象(self.session,feild_add_gzxx,self.header)
    #     self.gzxx_id = res_data.get('data').get('id')
    #     #通过id查询故障现象，断言参数正常
    #     res_data = Page故障现象.api_通过id查询故障现象(self.session,str(self.gzxx_id),self.header)
    #     self.assertEqual(feild_add_gzxx.get('manualName'),res_data.get('data').get('manualName'))
    #     self.assertEqual(feild_add_gzxx.get('manualPriority'),res_data.get('data').get('manualPriority'))
    #     self.assertEqual(feild_add_gzxx.get('facCateId'),res_data.get('data').get('facCateId'))
    #     #通过id删除故障现象
    #     res_data = Page故障现象.api_通过id删除故障现象(self.session,str(self.gzxx_id),self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #通过id查询故障现象，验证删除成功
    #     res_data = Page故障现象.api_通过id查询故障现象(self.session,str(self.gzxx_id),self.header)
    #     self.assertEqual(res_data.get('data'),None)


if __name__ =="__main__":
    unittest.main()