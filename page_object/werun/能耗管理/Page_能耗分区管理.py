import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page能耗分区管理(object):

    @classmethod
    def api_查询能耗分区列表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_查询能耗分区列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_新增能耗指标(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增能耗指标'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_通过id查询指标(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_通过id查询指标'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_新增能耗分区(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增能耗分区'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_修改能耗分区(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_修改能耗分区'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_通过id删除能耗分区(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_通过id删除能耗分区'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('json').copy())
        r = session.delete(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text)
        return r.json()

    @classmethod
    def api_通过id删除指标(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_通过id删除指标'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('json').copy())
        r = session.delete(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text)
        return r.json()

