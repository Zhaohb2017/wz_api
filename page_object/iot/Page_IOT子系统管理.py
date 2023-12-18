import json

import requests
from requests_toolbelt import MultipartEncoder

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class PageIOT子系统管理(object):

    @classmethod
    def api_IOT新增子系统(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_IOT新增子系统'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        m = MultipartEncoder(fields=feilds, boundary='----WebKitFormBoundarynuAGsBlvBWSGBhkU')
        header.update({'Content-Type': m.content_type})
        r = session.post(url, data=m, headers=header,verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r

    @classmethod
    def api_IOT子系统分页查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_IOT子系统分页查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.get(url, headers=header,verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_通过Code删除子系统(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_通过Code删除子系统'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, params=feilds, headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r

    @classmethod
    def api_IOT切换项目(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_IOT切换项目'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, json=feilds, headers=header,verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_IOT切换FRAME(cls, session: requests.Session):
        api_name = 'api_IOT切换FRAME'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header=Browser_Param.headers.get('json').copy()
        r = session.get(url,verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r

    @classmethod
    def api_IOT获取语言(cls, session: requests.Session):
        api_name = 'api_IOT获取语言'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        heade=Browser_Param.headers.get('json').copy()
        r = session.get(url,verify=False)
        Common_Base.logging_api_info(api_name, url, r.text,)
        return r

    # @classmethod
    # def api_上传附件(cls, session: requests.Session, feilds: dict, header: dict):
    #     api_name = 'api_上传附件'
    #     url = Api_Addr_WeRun.werun_apis.get(api_name)
    #     m = MultipartEncoder(fields=feilds, boundary='----WebKitFormBoundarynuAGsBlvBWSGBhkU')
    #     header.update({'Content-Type': m.content_type})
    #     r = session.post(url, data=m, headers=header)
    #     Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
    #     return r.json()