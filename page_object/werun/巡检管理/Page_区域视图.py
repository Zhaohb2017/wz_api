import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page线下巡检区域视图(object):

    @classmethod
    def api_巡检区域视图_基础信息概览(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_巡检区域视图_基础信息概览'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header, params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_巡检区域视图_巡检任务分析(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_巡检区域视图_巡检任务分析'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header, params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_巡检区域视图_完成率Top5项目(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_巡检区域视图_完成率Top5项目'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header, params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()
