import json

import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class PageIOT登陆(object):

    @classmethod
    def api_IOT登录(cls, session: requests.Session, feilds: dict):
        api_name = 'api_IOT登录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header = Browser_Param.headers.get('form').copy()
        r = session.post(url, json=feilds,headers = header,verify=False)
        # r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url,str(header))
        return r

    @classmethod
    def api_IOT获取用户信息(cls, session: requests.Session):
        api_name = 'api_IOT获取用户信息'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        r = session.get(url,verify=False)
        Common_Base.logging_api_info(api_name, url, r.text)
        return r.text.split('"Authorization":"')[1].split('","')[0]