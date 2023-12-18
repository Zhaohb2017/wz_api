import unittest
import uuid
import ddt
import requests
from business.param_config.api_param.werun.基础管理 import Param_登录登出
from common.M_Crypto import rsa_encrypt
import datetime
import time
from page_object.werun.工单管理.Page_工单表管理 import Page工单表管理
from page_object.werun.用户权限.Page_用户表管理 import Page用户表管理
from page_object.werun.用户权限.Page_登录模块 import Page登录模块



@ddt.ddt
class Case工单记录(unittest.TestCase):
    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        self.case_name = '工单记录'
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(session=self.session,header={'traceId': str(uuid.uuid4())})
        self.public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        self.encrypt_pwd = rsa_encrypt(self.public_key, feild.get('sword'))
        feild['sword'] = self.encrypt_pwd
        res_data = Page登录模块.api_后台管理登录(session=self.session, feilds=feild, header={'traceId': str(uuid.uuid4())})
        self.uuid_str = str(uuid.uuid4())
        self.header = {'traceId': self.uuid_str, 'Authorization': "Bearer " + res_data.get('data').get('token')}
        res_data = Page用户表管理.api_获取用户信息(self.session,self.header)
        self.user_info = res_data.get('data')


    def tearDown(self):
        self.session.close()



    def test_工单记录_查询所有_01(self):
        """
        查询所有->校验是否全部有数据
        :return:
        """
        feild_page_gd = {"head": {"current": 1, "size": 10}, "body": {"totalCount": 2059, "startDate": "", "endDate": ""}}
        res_data = Page工单表管理.api_工单分页查询(self.session,feild_page_gd,self.header)
        self.assertGreater(len(res_data.get('data').get('records')), 0,"默认条件, 查询工单页面无数据返回!")

    def test_工单记录_查询当天_01(self):
        """
        查询当天->只看接口是否正常
        :return:
        """
        # 获取当前时间
        now = datetime.datetime.now()
        # 获取当天 0 点整的时间戳
        today_start = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
        today_start_timestamp = int(time.mktime(today_start.timetuple()) * 1000)
        # 获取当天 23 点 59 分 59 秒 59 毫秒的时间戳
        today_end = datetime.datetime(now.year, now.month, now.day, 23, 59, 59, 999999)
        today_end_timestamp = int(time.mktime(today_end.timetuple()) * 1000 + today_end.microsecond / 1000)
        feild_page_gd = {"head":{"current":1,"size":10},"body":{"totalCount":2059,"startDate":today_start_timestamp,"endDate":today_end_timestamp}}
        res_data = Page工单表管理.api_工单分页查询(self.session,feild_page_gd,self.header)
        self.assertEqual(res_data.get('code'),200,"工单记录,查询当天数据,请求失败!")



