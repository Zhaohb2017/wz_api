import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class PageAPP登录(object):

    @classmethod
    def api_业主登录(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_业主登录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()
