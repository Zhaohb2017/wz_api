import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page保养区域视图(object):


    @classmethod
    def api_区域视图_基础信息概览(cls, session: requests.Session,header:dict):
        api_name = 'api_区域视图_基础信息概览'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_区域视图_保养任务分析(cls, session: requests.Session,header:dict):
        api_name = 'api_区域视图_保养任务分析'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_区域视图_完成率Top5项目(cls, session: requests.Session,header:dict):
        api_name = 'api_区域视图_完成率Top5项目'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()


