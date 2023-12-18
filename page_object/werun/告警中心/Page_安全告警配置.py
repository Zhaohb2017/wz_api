#!/usr/bin/env python
# encoding: utf-8
import requests
from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base
from requests_toolbelt import MultipartEncoder

class Page安全告警配置(object):

    @classmethod
    def api_分页查询黑名单告警(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_分页查询安全告警配置'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_上传图片(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_上传图片素材'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        m = MultipartEncoder(fields=feilds, boundary='----WebKitFormBoundarynuAGsBlvBWSGBhkU')
        header.update({'Content-Type': m.content_type})
        r = session.post(url, data=m,headers = header)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header),r.text,str(feilds))
        return r.json()


    @classmethod
    def api_新增布控人员(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增黑名单布控'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()



    @classmethod
    def api_删除安全告警配置(cls, session: requests.Session, id: str, header: dict):
        api_name = 'api_删除安全告警配置'
        url = Api_Addr_WeRun.werun_apis.get(api_name) + id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.delete(url, headers=header)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=None,request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()



    @classmethod
    def api_布控通过id查询(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_黑名单布控通过id查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=None,request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_黑名单布控启用禁用(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_黑名单布控启用禁用'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()