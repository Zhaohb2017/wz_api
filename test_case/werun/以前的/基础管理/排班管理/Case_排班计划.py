import datetime
import unittest
import uuid

import ddt
import requests

from business.param_config.api_param.werun.基础管理 import Param_登录登出, Param_角色权限, Param_组织机构, Param_用户管理, Param_项目管理
from business.param_config.api_param.werun.基础管理.排班管理 import Param_班次管理, Param_排班计划
from common.Common_Base import create_phone, create_email
from common.M_Crypto import rsa_encrypt
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.排班管理.Page_排班计划管理 import Page排班计划管理
from page_object.werun.排班管理.Page_班次管理 import Page班次管理
from page_object.werun.用户权限.Page_用户表管理 import Page用户表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.werun.用户权限.Page_组织架构表管理 import Page组织架构表管理
from page_object.werun.用户权限.Page_角色表管理 import Page角色表管理


@ddt.ddt
class Case排班计划(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
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
        if hasattr(self,'b_plan_id'):
            Page排班计划管理.api_通过id删除班次计划(self.session,str(self.b_plan_id),self.header)
        if hasattr(self, 'b_id'):
            Page班次管理.api_通过id删除班次(self.session, str(self.b_id), self.header)
        if hasattr(self, 'u_id'):
            Page用户表管理.api_用户通过id删除(self.session, str(self.u_id), self.header)
        if hasattr(self, 'z_id'):
            Page组织架构表管理.api_组织架构通过id删除(self.session, str(self.z_id), self.header)
        if hasattr(self, 'j_id'):
            Page角色表管理.api_角色通过id删除(self.session, str(self.j_id), self.header)
        if hasattr(self, 'p_id'):
            Page项目表管理.api_项目通过id删除(self.session, self.p_id, self.header)
        self.session.close()
        pass


    def test_排班计划_01(self):
        """
        验证新增排班计划，查询排班计划新增参数正确，通过id删除排班计划正常(一人)
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级组织机构，获取id
        feild_add_z = Param_组织机构.p_add.get('同级')
        feild_add_z['orgName'] = "orgName " + self.uuid_str
        res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
        self.z_id = res_data.get('data').get('id')
        # 新增角色，获取id
        feild_add_j = Param_角色权限.p_add.get('01').copy()
        feild_add_j['name'] = "jiaose" + self.uuid_str
        res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
        self.j_id = res_data.get('data').get('id')
        #新增用户
        feild_add_u = Param_用户管理.p_add.get('客服').copy()
        feild_add_u['orgIds'] = [self.z_id]
        feild_add_u['roleIds'] = [self.j_id]
        feild_add_u['scabbard'] = "user" + str(uuid.uuid4())
        feild_add_u['sword'] = self.encrypt_pwd
        feild_add_u['confirmSword'] = self.encrypt_pwd
        feild_add_u['mobile'] = create_phone()
        feild_add_u['email'] = create_email()
        res_data = Page用户表管理.api_创建用户(self.session, feild_add_u, self.header)
        self.u_id = res_data.get('data').get('id')
        #新增班次
        feild_add_banci = Param_班次管理.p_add.get('一日两班').copy()
        feild_add_banci['schedulingName'] = 'BanCi' + str(uuid.uuid1())
        feild_add_banci['records'][0]['scheduingName'] = 'BanCiSub' + str(uuid.uuid1())
        feild_add_banci['records'][1]['scheduingName'] = 'BanCiSub' + str(uuid.uuid4())
        res_data = Page班次管理.api_新增或更新班次以及时间安排(self.session, feild_add_banci, self.header)
        self.b_id = res_data.get('data')
        #通过id查询班次，获取内部班次id
        res_data = Page班次管理.api_通过班次id查询班次时间安排(self.session, str(self.b_id), self.header)
        jsr_id1 = res_data.get('data')[0].get('id')
        jsr_id2 = res_data.get('data')[1].get('id')
        #新增排班计划
        feild_add_plan = Param_排班计划.p_add.get('一人').copy()
        feild_add_plan['orgId'] = self.z_id
        feild_add_plan['jsId'] = self.b_id
        feild_add_plan['planName'] = "排班计划"+str(uuid.uuid1())
        for item in feild_add_plan.get('list'):
            if item['jsrId'] == 127:
                item['jsrId'] = jsr_id1
            elif item['jsrId'] == 128:
                item['jsrId'] = jsr_id2
            item['userId'] = self.u_id
        res_data = Page排班计划管理.api_添加或更新班次及明细信息(self.session,feild_add_plan,self.header)
        self.b_plan_id = res_data.get('data')
        #查询排班计划，断言新增的参数正确
        feild_search = Param_排班计划.p_search.get('一人')
        feild_search['jspId'] = self.b_plan_id
        res_data = Page排班计划管理.api_排班计划明细查询(self.session,feild_search,self.header)
        self.assertEqual(feild_add_plan.get('planName'),res_data.get('data').get('jobSchedulingPlan').get('planName'))
        self.assertEqual(feild_add_plan.get('orgId'),res_data.get('data').get('jobSchedulingPlan').get('orgId'))
        self.assertEqual(feild_add_plan.get('jsId'),res_data.get('data').get('jobSchedulingPlan').get('jsId'))
        self.assertEqual(feild_add_plan.get('list')[0].get('jsrId'),res_data.get('data').get('jobSchedulingPlanRecordList').get(str(self.u_id))[0].get('jsrId'))
        #通过id删除排班计划
        res_data =Page排班计划管理.api_通过id删除班次计划(self.session,str(self.b_plan_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #查询排班计划，断言删除成功
        feild_search = Param_排班计划.p_search.get('一人')
        feild_search['jspId'] = self.b_plan_id
        res_data = Page排班计划管理.api_排班计划明细查询(self.session, feild_search, self.header)
        self.assertEqual(res_data.get('data'),None)
        pass

    # def test_排班计划_02(self):
    #     """
    #     验证新增排班计划，查询排班计划新增参数正确，通过id删除排班计划正常(两人)
    #     :return:
    #     """
    #     # 新增项目
    #     feild_add_p = Param_项目管理.p_add.get('学校')
    #     feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
    #     res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
    #     self.p_id = str(res_data.get('data').get('id'))
    #     self.header.update({'propertyId': str(self.p_id)})
    #     # 新增同级组织机构，获取id
    #     feild_add_z = Param_组织机构.p_add.get('同级')
    #     feild_add_z['orgName'] = "orgName " + self.uuid_str
    #     res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
    #     self.z_id = res_data.get('data').get('id')
    #     # 新增角色，获取id
    #     feild_add_j = Param_角色权限.p_add.get('01').copy()
    #     feild_add_j['name'] = "jiaose" + self.uuid_str
    #     res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
    #     self.j_id = res_data.get('data').get('id')
    #     #新增用户
    #     feild_add_u = Param_用户管理.p_add.get('客服').copy()
    #     feild_add_u['orgIds'] = [self.z_id]
    #     feild_add_u['roleIds'] = [self.j_id]
    #     feild_add_u['scabbard'] = "user" + str(uuid.uuid4())
    #     feild_add_u['sword'] = self.encrypt_pwd
    #     feild_add_u['confirmSword'] = self.encrypt_pwd
    #     feild_add_u['mobile'] = create_phone()
    #     feild_add_u['email'] = create_email()
    #     res_data = Page用户表管理.api_创建用户(self.session, feild_add_u, self.header)
    #     self.u_id = res_data.get('data').get('id')
    #
    #     feild_add_u = Param_用户管理.p_add.get('客服').copy()
    #     feild_add_u['orgIds'] = [self.z_id]
    #     feild_add_u['roleIds'] = [self.j_id]
    #     feild_add_u['scabbard'] = "user" + str(uuid.uuid4())
    #     feild_add_u['sword'] = self.encrypt_pwd
    #     feild_add_u['confirmSword'] = self.encrypt_pwd
    #     feild_add_u['mobile'] = create_phone()
    #     feild_add_u['email'] = create_email()
    #     res_data = Page用户表管理.api_创建用户(self.session, feild_add_u, self.header)
    #     self.u_id1 = res_data.get('data').get('id')
    #     #新增班次
    #     feild_add_banci = Param_班次管理.p_add.get('一日两班').copy()
    #     feild_add_banci['schedulingName'] = 'BanCi' + str(uuid.uuid1())
    #     feild_add_banci['records'][0]['scheduingName'] = 'BanCiSub' + str(uuid.uuid1())
    #     feild_add_banci['records'][1]['scheduingName'] = 'BanCiSub' + str(uuid.uuid4())
    #     res_data = Page班次管理.api_新增或更新班次以及时间安排(self.session, feild_add_banci, self.header)
    #     self.b_id = res_data.get('data')
    #     #通过id查询班次，获取内部班次id
    #     res_data = Page班次管理.api_通过班次id查询班次时间安排(self.session, str(self.b_id), self.header)
    #     jsr_id1 = res_data.get('data')[0].get('id')
    #     jsr_id2 = res_data.get('data')[1].get('id')
    #     #新增排班计划
    #     feild_add_plan = Param_排班计划.p_add.get('两人').copy()
    #     feild_add_plan['orgId'] = self.z_id
    #     feild_add_plan['jsId'] = self.b_id
    #     feild_add_plan['planName'] = "排班计划"+str(uuid.uuid1())
    #     for item in feild_add_plan.get('list'):
    #         if item['jsrId'] == 141:
    #             item['jsrId'] = jsr_id1
    #         elif item['jsrId'] == 142:
    #             item['jsrId'] = jsr_id2
    #         if item['userId'] == 109:
    #             item['userId'] = self.u_id
    #         elif item['userId'] == 110:
    #             item['userId'] = self.u_id1
    #     res_data = Page排班计划管理.api_添加或更新班次及明细信息(self.session,feild_add_plan,self.header)
    #     self.b_plan_id = res_data.get('data')
    #     #查询排班计划，断言新增的参数正确
    #     feild_search = Param_排班计划.p_search.get('两人')
    #     feild_search['jspId'] = self.b_plan_id
    #     res_data = Page排班计划管理.api_排班计划明细查询(self.session,feild_search,self.header)
    #     self.assertEqual(feild_add_plan.get('planName'),res_data.get('data').get('jobSchedulingPlan').get('planName'))
    #     self.assertEqual(feild_add_plan.get('orgId'),res_data.get('data').get('jobSchedulingPlan').get('orgId'))
    #     self.assertEqual(feild_add_plan.get('jsId'),res_data.get('data').get('jobSchedulingPlan').get('jsId'))
    #     self.assertEqual(feild_add_plan.get('list')[0].get('jsrId'),res_data.get('data').get('jobSchedulingPlanRecordList').get(str(self.u_id))[0].get('jsrId'))
    #     self.assertEqual(feild_add_plan.get('list')[31].get('jsrId'),res_data.get('data').get('jobSchedulingPlanRecordList').get(str(self.u_id1))[0].get('jsrId'))
    #     #通过id删除排班计划
    #     res_data =Page排班计划管理.api_通过id删除班次计划(self.session,str(self.b_plan_id),self.header)
    #     self.assertEqual(res_data.get('ok'),True)
    #     #查询排班计划，断言删除成功
    #     feild_search = Param_排班计划.p_search.get('两人')
    #     feild_search['jspId'] = self.b_plan_id
    #     res_data = Page排班计划管理.api_排班计划明细查询(self.session, feild_search, self.header)
    #     self.assertEqual(res_data.get('data'),None)
    #     # 删除用户
    #     res_data = Page用户表管理.api_用户通过id删除(self.session, str(self.u_id1), self.header)
    #     self.assertEqual(res_data.get('ok'), True)
    #     pass

    def test_排班计划_03(self):
        """
        验证分页查询功能，断言查询内容正确（通过计划名称）
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级组织机构，获取id
        feild_add_z = Param_组织机构.p_add.get('同级')
        feild_add_z['orgName'] = "orgName " + self.uuid_str
        res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
        self.z_id = res_data.get('data').get('id')
        # 新增角色，获取id
        feild_add_j = Param_角色权限.p_add.get('01').copy()
        feild_add_j['name'] = "jiaose" + self.uuid_str
        res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
        self.j_id = res_data.get('data').get('id')
        #新增用户
        feild_add_u = Param_用户管理.p_add.get('客服').copy()
        feild_add_u['orgIds'] = [self.z_id]
        feild_add_u['roleIds'] = [self.j_id]
        feild_add_u['scabbard'] = "user" + str(uuid.uuid4())
        feild_add_u['sword'] = self.encrypt_pwd
        feild_add_u['confirmSword'] = self.encrypt_pwd
        feild_add_u['mobile'] = create_phone()
        feild_add_u['email'] = create_email()
        res_data = Page用户表管理.api_创建用户(self.session, feild_add_u, self.header)
        self.u_id = res_data.get('data').get('id')
        #新增班次
        feild_add_banci = Param_班次管理.p_add.get('一日两班').copy()
        feild_add_banci['schedulingName'] = 'BanCi' + str(uuid.uuid1())
        feild_add_banci['records'][0]['scheduingName'] = 'BanCiSub' + str(uuid.uuid1())
        feild_add_banci['records'][1]['scheduingName'] = 'BanCiSub' + str(uuid.uuid4())
        res_data = Page班次管理.api_新增或更新班次以及时间安排(self.session, feild_add_banci, self.header)
        self.b_id = res_data.get('data')
        #通过id查询班次，获取内部班次id
        res_data = Page班次管理.api_通过班次id查询班次时间安排(self.session, str(self.b_id), self.header)
        jsr_id1 = res_data.get('data')[0].get('id')
        jsr_id2 = res_data.get('data')[1].get('id')
        #新增排班计划
        feild_add_plan = Param_排班计划.p_add.get('一人').copy()
        feild_add_plan['orgId'] = self.z_id
        feild_add_plan['jsId'] = self.b_id
        feild_add_plan['planName'] = "排班计划"+str(uuid.uuid1())
        for item in feild_add_plan.get('list'):
            if item['jsrId'] == 127:
                item['jsrId'] = jsr_id1
            elif item['jsrId'] == 128:
                item['jsrId'] = jsr_id2
            item['userId'] = self.u_id
        res_data = Page排班计划管理.api_添加或更新班次及明细信息(self.session,feild_add_plan,self.header)
        self.b_plan_id = res_data.get('data')
        #分页查询排班计划，断言新增的参数正确
        feild_page = Param_排班计划.p_page.get('计划名称').copy()
        feild_page['body']['planName'] = feild_add_plan.get('planName')
        res_data = Page排班计划管理.api_排班计划分页查询(self.session,feild_page,self.header)
        self.assertIn(feild_add_plan.get('planName'),str(res_data.get('data')))
        self.assertIn(str(feild_add_plan.get('orgId')),str(res_data.get('data')))
        self.assertIn(str(feild_add_plan.get('jsId')),str(res_data.get('data')))
        #通过id删除排班计划
        res_data =Page排班计划管理.api_通过id删除班次计划(self.session,str(self.b_plan_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        pass

    def test_排班计划_04(self):
        """
        验证分页查询功能，断言查询内容正确（重置默认）
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级组织机构，获取id
        feild_add_z = Param_组织机构.p_add.get('同级')
        feild_add_z['orgName'] = "orgName " + self.uuid_str
        res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
        self.z_id = res_data.get('data').get('id')
        # 新增角色，获取id
        feild_add_j = Param_角色权限.p_add.get('01').copy()
        feild_add_j['name'] = "jiaose" + self.uuid_str
        res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
        self.j_id = res_data.get('data').get('id')
        #新增用户
        feild_add_u = Param_用户管理.p_add.get('客服').copy()
        feild_add_u['orgIds'] = [self.z_id]
        feild_add_u['roleIds'] = [self.j_id]
        feild_add_u['scabbard'] = "user" + str(uuid.uuid4())
        feild_add_u['sword'] = self.encrypt_pwd
        feild_add_u['confirmSword'] = self.encrypt_pwd
        feild_add_u['mobile'] = create_phone()
        feild_add_u['email'] = create_email()
        res_data = Page用户表管理.api_创建用户(self.session, feild_add_u, self.header)
        self.u_id = res_data.get('data').get('id')
        #新增班次
        feild_add_banci = Param_班次管理.p_add.get('一日两班').copy()
        feild_add_banci['schedulingName'] = 'BanCi' + str(uuid.uuid1())
        feild_add_banci['records'][0]['scheduingName'] = 'BanCiSub' + str(uuid.uuid1())
        feild_add_banci['records'][1]['scheduingName'] = 'BanCiSub' + str(uuid.uuid4())
        res_data = Page班次管理.api_新增或更新班次以及时间安排(self.session, feild_add_banci, self.header)
        self.b_id = res_data.get('data')
        #通过id查询班次，获取内部班次id
        res_data = Page班次管理.api_通过班次id查询班次时间安排(self.session, str(self.b_id), self.header)
        jsr_id1 = res_data.get('data')[0].get('id')
        jsr_id2 = res_data.get('data')[1].get('id')
        #新增排班计划
        feild_add_plan = Param_排班计划.p_add.get('一人').copy()
        feild_add_plan['orgId'] = self.z_id
        feild_add_plan['jsId'] = self.b_id
        feild_add_plan['planName'] = "排班计划"+str(uuid.uuid1())
        for item in feild_add_plan.get('list'):
            if item['jsrId'] == 127:
                item['jsrId'] = jsr_id1
            elif item['jsrId'] == 128:
                item['jsrId'] = jsr_id2
            item['userId'] = self.u_id
        res_data = Page排班计划管理.api_添加或更新班次及明细信息(self.session,feild_add_plan,self.header)
        self.b_plan_id = res_data.get('data')
        #分页查询排班计划，断言新增的参数正确
        feild_page = Param_排班计划.p_page.get('重置').copy()
        res_data = Page排班计划管理.api_排班计划分页查询(self.session,feild_page,self.header)
        self.assertNotEqual(res_data.get('data').get('records'),[])
        #通过id删除排班计划
        res_data =Page排班计划管理.api_通过id删除班次计划(self.session,str(self.b_plan_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        pass

    def test_排班计划_05(self):
        """
        验证编辑修改排班计划功能正常，验证查询排班计划修改参数正确
        :return:
        """
        # 新增项目
        feild_add_p = Param_项目管理.p_add.get('学校')
        feild_add_p['propertyName'] = "项目" + str(uuid.uuid1())
        res_data = Page项目表管理.api_新增项目表(self.session, feild_add_p, self.header)
        self.p_id = str(res_data.get('data').get('id'))
        self.header.update({'propertyId': str(self.p_id)})
        # 新增同级组织机构，获取id
        feild_add_z = Param_组织机构.p_add.get('同级')
        feild_add_z['orgName'] = "orgName " + self.uuid_str
        res_data = Page组织架构表管理.api_新增组织架构(self.session, feild_add_z, self.header)
        self.z_id = res_data.get('data').get('id')
        # 新增角色，获取id
        feild_add_j = Param_角色权限.p_add.get('01').copy()
        feild_add_j['name'] = "jiaose" + self.uuid_str
        res_data = Page角色表管理.api_新增角色(self.session, feild_add_j, self.header)
        self.j_id = res_data.get('data').get('id')
        #新增用户
        feild_add_u = Param_用户管理.p_add.get('客服').copy()
        feild_add_u['orgIds'] = [self.z_id]
        feild_add_u['roleIds'] = [self.j_id]
        feild_add_u['scabbard'] = "user" + str(uuid.uuid4())
        feild_add_u['sword'] = self.encrypt_pwd
        feild_add_u['confirmSword'] = self.encrypt_pwd
        feild_add_u['mobile'] = create_phone()
        feild_add_u['email'] = create_email()
        res_data = Page用户表管理.api_创建用户(self.session, feild_add_u, self.header)
        self.u_id = res_data.get('data').get('id')
        #新增班次
        feild_add_banci = Param_班次管理.p_add.get('一日两班').copy()
        feild_add_banci['schedulingName'] = 'BanCi' + str(uuid.uuid1())
        feild_add_banci['records'][0]['scheduingName'] = 'BanCiSub' + str(uuid.uuid1())
        feild_add_banci['records'][1]['scheduingName'] = 'BanCiSub' + str(uuid.uuid4())
        res_data = Page班次管理.api_新增或更新班次以及时间安排(self.session, feild_add_banci, self.header)
        self.b_id = res_data.get('data')
        #通过id查询班次，获取内部班次id
        res_data = Page班次管理.api_通过班次id查询班次时间安排(self.session, str(self.b_id), self.header)
        jsr_id1 = res_data.get('data')[0].get('id')
        jsr_id2 = res_data.get('data')[1].get('id')
        #新增排班计划
        feild_add_plan = Param_排班计划.p_add.get('一人').copy()
        current_date = str(datetime.date.today()).split('-')
        if int(current_date[1]) == 2:
            feild_add_plan.get('list').pop()
            feild_add_plan.get('list').pop()
            feild_add_plan.get('list').pop()
        elif int(current_date[1]) in [4,6,9,11]:
            feild_add_plan.get('list').pop()
        feild_add_plan['year'] = int(current_date[0])
        feild_add_plan['month'] = int(current_date[1])
        feild_add_plan['orgId'] = self.z_id
        feild_add_plan['jsId'] = self.b_id
        feild_add_plan['planName'] = "排班计划"+str(uuid.uuid1())
        for item in feild_add_plan.get('list'):
            if item['jsrId'] == 127:
                item['jsrId'] = jsr_id1
            elif item['jsrId'] == 128:
                item['jsrId'] = jsr_id2
            item['userId'] = self.u_id
        res_data = Page排班计划管理.api_添加或更新班次及明细信息(self.session,feild_add_plan,self.header)
        self.b_plan_id = res_data.get('data')
        #查询排班计划，并将id赋值
        feild_search = Param_排班计划.p_search.get('一人')
        feild_search['jspId'] = self.b_plan_id
        res_data = Page排班计划管理.api_排班计划明细查询(self.session, feild_search, self.header)
        plan_list_ids = res_data.get('data').get('jobSchedulingPlanRecordList').get(str(self.u_id))
        #修改排班计划
        feild_upd = Param_排班计划.p_upd.get('大月')
        if int(current_date[1]) == 2:
            feild_upd.get('list').pop()
            feild_upd.get('list').pop()
            feild_upd.get('list').pop()
        elif int(current_date[1]) in [4, 6, 9, 11]:
            feild_upd.get('list').pop()
        feild_upd['id'] = self.b_plan_id
        feild_upd['year'] = int(current_date[0])
        feild_upd['month'] = int(current_date[1])
        feild_upd['orgId'] = self.z_id
        feild_upd['jsId'] = self.b_id
        feild_upd['planName'] = feild_add_plan.get('planName')
        plan_list = feild_upd.get('list')
        for item in range(len(plan_list)):
            if plan_list[item]['jsrId'] == 157:
                plan_list[item]['jsrId'] = jsr_id1
            elif plan_list[item]['jsrId'] == 158:
                plan_list[item]['jsrId'] = jsr_id2
            plan_list[item]['userId'] = self.u_id
            plan_list[item]['id'] = plan_list_ids[item].get('id')
        res_data = Page排班计划管理.api_添加或更新班次及明细信息(self.session,feild_upd,self.header)
        #查询排班计划，断言修改的参数正确
        feild_search = Param_排班计划.p_search.get('一人')
        feild_search['jspId'] = self.b_plan_id
        feild_search['year'] = int(current_date[0])
        feild_search['month'] = int(current_date[1])
        res_data = Page排班计划管理.api_排班计划明细查询(self.session,feild_search,self.header)
        self.assertEqual(feild_upd.get('list')[0].get('jsrId'),res_data.get('data').get('jobSchedulingPlanRecordList').get(str(self.u_id))[0].get('jsrId'))
        self.assertEqual(feild_upd.get('list')[1].get('jsrId'),res_data.get('data').get('jobSchedulingPlanRecordList').get(str(self.u_id))[1].get('jsrId'))
        self.assertEqual(feild_upd.get('list')[2].get('jsrId'),res_data.get('data').get('jobSchedulingPlanRecordList').get(str(self.u_id))[2].get('jsrId'))
        #通过id删除排班计划
        res_data =Page排班计划管理.api_通过id删除班次计划(self.session,str(self.b_plan_id),self.header)
        self.assertEqual(res_data.get('ok'),True)
        #查询排班计划，断言删除成功
        feild_search = Param_排班计划.p_search.get('一人')
        feild_search['jspId'] = self.b_plan_id
        res_data = Page排班计划管理.api_排班计划明细查询(self.session, feild_search, self.header)
        self.assertEqual(res_data.get('data'),None)
        pass