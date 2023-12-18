import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page能耗分项管理(object):



    @classmethod
    def api_新增能耗分项(cls, session: requests.Session, feilds: dict, header:dict):
        api_name = 'api_新增能耗分项'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_新增能耗分项指标(cls, session: requests.Session, feilds: dict, header:dict):
        api_name = 'api_新增能耗分项指标'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_通过id查询分项指标(cls, session: requests.Session, feilds: dict, header:dict):
        api_name = 'api_通过id查询分项指标'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_编辑修改能耗分项(cls, session: requests.Session, feilds: dict, header:dict):
        api_name = 'api_编辑修改能耗分项'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_通过id删除能耗分项(cls, session: requests.Session, id: str, header:dict):
        api_name = 'api_通过id删除能耗分项'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('json').copy())
        r = session.delete(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text)
        return r.json()

    @classmethod
    def api_通过id删除分项指标(cls, session: requests.Session, id: str, header:dict):
        api_name = 'api_通过id删除分项指标'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('json').copy())
        r = session.delete(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text)
        return r.json()

    @classmethod
    def api_能耗分项列表查询(cls, session: requests.Session, feilds: dict, header:dict):
        api_name = 'api_能耗分项列表查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

