import logging
import unittest
import uuid
import requests
from business.param_config.api_param.werun.基础管理 import Param_登录登出
from common.M_Crypto import rsa_encrypt
from page_object.werun.用户权限.Page_登录模块 import Page登录模块
from page_object.xinli.page_监测接口 import PageMonitorMonitor
from common.Encryption_AES import decrypt, md5_encode
from Configs import sign
from common.Common_Base import get_timestamp
from datetime import datetime


class ServiceCollection(unittest.TestCase):

    def setUp(self):
        # 获取requests.session
        self.session = requests.Session()
        # 获取公钥、加密登录
        res_data = Page登录模块.api_获取登录公钥(self.session, header={'traceId': str(uuid.uuid4())})
        self.public_key = res_data.get('data').get('RSA')
        # 密码加密后登陆
        feild = Param_登录登出.p_后台管理登陆.get('01').copy()
        secret_key = md5_encode(sign)
        user = decrypt(encoded_text=feild['scabbard'], key=secret_key)
        password = decrypt(encoded_text=feild['sword'], key=secret_key)
        self.encrypt_pwd = rsa_encrypt(self.public_key, password.decode('utf-8'))
        print(str(user))
        feild['sword'] = self.encrypt_pwd
        feild['scabbard'] = user.decode('utf-8')  # decode('utf-8') 字节数据转换成字符串
        print(feild)
        res_data = Page登录模块.api_后台管理登录(self.session, feild, {})
        print(res_data)
        self.header = {'traceId': str(uuid.uuid4()), 'Authorization': "Bearer " + res_data.get('data').get('token'),
                       "Propertyid": "436"}

    def tearDown(self):
        self.session.close()

    def test_alarm_page(self):
        """
        告警记录列表检查
        :return:
        """
        data = {"head": {"current": 1, "size": 10, "total": 10},
                "body": {"alarmLevel": "", "alarmType": "", "alarmStatus": ""}}
        res_data = PageMonitorMonitor.api_alarm_page(session=self.session, header=self.header, params=data)
        self.assertEqual(res_data.get("code"), 200)

    def test_facilities_page(self):
        """
        设备台账列表检查
        :return:
        """
        data = {"head": {"total": 0, "current": 1, "size": 10}, "body": {"parentIds": "0,547"}}
        res_data = PageMonitorMonitor.api_facilities_page(session=self.session, header=self.header, params=data)
        self.assertEqual(res_data.get("code"), 200)

    def test_passage_page(self):
        """
        智慧通行授权列表检查
        :return:
        """
        data = {"head": {"current": 1, "size": 10, "total": 1874},
                "body": {"city": None, "area": None, "userName": "", "userType": "", "cardNo": "", "companyId": ""}}
        res_data = PageMonitorMonitor.api_passage_page(session=self.session, header=self.header, params=data)
        self.assertEqual(res_data.get("code"), 200)

    def test_facility_operating_parameter(self):
        """
        设备运行参数检查: 设备名称-B1层电梯厅
        :return:
        """
        # 获取当前时间
        current_time = datetime.now().time()
        # 判断是否大于早上8点
        if current_time.hour >= 8:
            today = get_timestamp()
            midnight = get_timestamp(hour=23, minute=59, second=59, microsecond=59)
            data = {"deviceId": "ID10004", "attribute": "Temperature", "startTime": today, "endTime": midnight}
            historyInfo = PageMonitorMonitor.api_facility_history(session=self.session, header=self.header, params=data)
            self.assertNotEqual(len(historyInfo["data"]), 0, "设备: B1层电梯厅, 今天没有采集到IoT数据")

        else:
            logging.info("当前时间小于08:00,设备运行参数不进行校验")



if __name__ == "__main__":
    unittest.main()
