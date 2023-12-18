import logging

import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page标准作业指导书(object):

    @classmethod
    def api_根据sopId获取标准作业指导书操作内容(cls, session: requests.Session, sopId: str,header:dict):
        api_name = 'api_根据sopId获取标准作业指导书操作内容'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+sopId
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_新增标准作业指导书及操作内容(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增标准作业指导书及操作内容'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_编辑标准作业指导书及操作内容(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_编辑标准作业指导书及操作内容'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_获取标准作业指导书分页列表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_获取标准作业指导书分页列表'
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
    def api_下载标准作业指导书模板(cls, session: requests.Session,header:dict):
        api_name = 'api_下载标准作业指导书模板'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method) #响应码不是200,主动抛出异常
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r

    @classmethod
    def api_导入标准作业指导书列表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_导入标准作业指导书列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_通过id删除标准作业指导书(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_通过id删除标准作业指导书'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.delete(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()
