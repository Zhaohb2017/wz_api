import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page自定义告警触发条件管理(object):

    @classmethod
    def api_新增自定义告警触发条件(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增自定义告警触发条件'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_修改自定义告警触发条件(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_修改自定义告警触发条件'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_自定义告警触发条件集合查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_自定义告警触发条件集合查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_自定义告警触发条件分页查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_自定义告警触发条件分页查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_自定义告警触发条件通过id查询(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_自定义告警触发条件通过id查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_自定义告警触发条件通过id删除(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_自定义告警触发条件通过id删除'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.delete(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()
