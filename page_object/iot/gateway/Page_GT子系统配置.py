import json

import requests
from requests_toolbelt import MultipartEncoder

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class PageGT子系统配置(object):

    @classmethod
    def api_导入IOT设备(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_导入IOT设备'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, json=feilds, headers=header,verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_更新点位数据(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_更新点位数据'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, json=feilds, headers=header,verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_分页查询设备(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_分页查询设备'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        m = MultipartEncoder(fields=feilds, boundary='----WebKitFormBoundarynuAGsBlvBWSGBhkU')
        header.update({'Content-Type': m.content_type})
        r = session.post(url, data=m, headers=header,verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r

    @classmethod
    def api_查询待导入IOT设备(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_查询待导入IOT设备'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, params=feilds, headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_添加监控点位(cls, session: requests.Session,params:dict, feilds: dict,header:dict):
        api_name = 'api_添加监控点位'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, json=feilds,params=params, headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_分页查询监控点位(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_分页查询监控点位'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, params=feilds, headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_重启子系统(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_重启子系统'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, json=feilds,headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_重启网关(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_重启网关'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, json=feilds,headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r

    @classmethod
    def api_新增网关子系统(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增网关子系统'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, json=feilds,headers=header,verify=False)
        Common_Base.logging_api_info(api_name, url,str(header),r.text,str(feilds))
        return r.json()

    @classmethod
    def api_分页查询网关子系统(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_分页查询网关子系统'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, params=feilds, headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_通过id删除监控点位(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_通过id删除监控点位'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, params=feilds, headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_通过id删除设备(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_通过id删除设备'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, params=feilds, headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_通过id删除网关子系统(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_通过id删除网关子系统'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, params=feilds, headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_通过id删除网关子系统2(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_通过id删除网关子系统2'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, json=feilds, headers=header, verify=False)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    # @classmethod
    # def api_上传附件(cls, session: requests.Session, feilds: dict, header: dict):
    #     api_name = 'api_上传附件'
    #     url = Api_Addr_WeRun.werun_apis.get(api_name)
    #     m = MultipartEncoder(fields=feilds, boundary='----WebKitFormBoundarynuAGsBlvBWSGBhkU')
    #     header.update({'Content-Type': m.content_type})
    #     r = session.post(url, data=m, headers=header)
    #     Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
    #     return r.json()