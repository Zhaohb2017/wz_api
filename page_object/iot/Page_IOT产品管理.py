import requests
from requests_toolbelt import MultipartEncoder

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class PageIOT产品管理(object):

    @classmethod
    def api_新增产品(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增产品'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        m = MultipartEncoder(fields=feilds, boundary='----WebKitFormBoundarynuAGsBlvBWSGBhkU')
        header.update({'Content-Type': m.content_type})
        r = session.post(url, data=m, headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r

    @classmethod
    def api_分页查询产品(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_分页查询产品'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.get(url, params=feilds,verify=False)
        Common_Base.logging_api_info(api_name, url,str(header),r.text,str(feilds))
        return r.json()

    @classmethod
    def api_通过id删除产品(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_通过id删除产品'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, params=feilds, headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r