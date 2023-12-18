import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page登录模块(object):

    @classmethod
    def api_后台管理登录(cls, session: requests.Session, feilds: dict,header:dict):
        res_data = None
        method = None
        api_name = 'api_后台管理登录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.post(url, headers=header, json=feilds,timeout=20,verify=False)
            r.raise_for_status()
            res_data = r.text
            method=r.request.method
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name, url, str(header) ,res_data, str(feilds),request_method=method)
        return r.json()

    @classmethod
    def api_后台管理登出(cls, session: requests.Session,header:dict):
        r = None
        api_name = 'api_后台管理登出'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.get(url, headers=header, timeout=20,verify=False)
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name, url, str(header) ,r.text)
        return r.json()

    @classmethod
    def api_修改初始口令(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_修改初始口令'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_获取登录公钥(cls, session: requests.Session, header: dict):
        res_data = None
        method = None
        api_name = 'api_获取登录公钥'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.get(url, headers=header, timeout=20,verify=False)
            r.raise_for_status()
            res_data = r.text
            method = r.request.method
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name, url, str(header) ,res_data, request_method=method)
        return r.json()