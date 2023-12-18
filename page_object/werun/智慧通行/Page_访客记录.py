import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page访客记录(object):

    @classmethod
    def api_分页查询访客记录(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_分页查询访客记录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_邀请访客(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_邀请访客'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_通过id查询访客记录(cls, session: requests.Session, id: str, header: dict):
        api_name = 'api_通过id查询访客记录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('json').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_导出访客记录(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_导出访客记录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r
