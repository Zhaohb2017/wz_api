import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page通行记录(object):

    @classmethod
    def api_分页查询通行记录(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_分页查询通行记录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_人行记录列表(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_人行记录列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_通行人行态势(cls, session: requests.Session, header: dict):
        api_name = 'api_通行人行态势'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_导出通行记录(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_导出通行记录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.get(url, headers=header, params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r
