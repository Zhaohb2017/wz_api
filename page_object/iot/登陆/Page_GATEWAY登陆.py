import json

import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class PageGATEWAY登陆(object):

    @classmethod
    def api_GATEWAY登录(cls, session: requests.Session, feilds: dict):
        api_name = 'api_GATEWAY登录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header = Browser_Param.headers.get('form').copy()
        r = session.post(url, json=feilds,headers = header,verify=False)
        Common_Base.logging_api_info(api_name, url,str(header),r.text,str(feilds))
        return r.json()

    @classmethod
    def api_获取TOKEN(cls, session: requests.Session,header:dict):
        api_name = 'api_获取TOKEN'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url,headers = header,verify=False)
        Common_Base.logging_api_info(api_name, url,str(header),r.text)
        return r
