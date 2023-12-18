import requests
from requests_toolbelt import MultipartEncoder

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page项目花名册管理(object):

    @classmethod
    def api_新增项目花名册(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增项目花名册'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_下载花名册导入模版(cls, session: requests.Session,header:dict):
        api_name = 'api_下载花名册导入模版'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header))
        return r

    @classmethod
    def api_导出花名册(cls, session: requests.Session,header:dict):
        api_name = 'api_导出花名册'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header))
        return r

    @classmethod
    def api_导入项目花名册(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_导入项目花名册'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        m = MultipartEncoder(fields=feilds, boundary='----WebKitFormBoundarynuAGsBlvBWSGBhkU')
        header.update({'Content-Type': m.content_type})
        # proxies = {'http': 'http://localhost:8888', 'https':'http://localhost:8888'}
        # r = session.post(url, data = m,headers = header,proxies=proxies, verify=False)
        r = session.post(url, data = m,headers = header)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header),r.text,str(feilds))
        return r.json()

    @classmethod
    def api_修改项目花名册(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_修改项目花名册'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_项目花名册集合查询(cls, session: requests.Session,header:dict):
        api_name = 'api_项目花名册集合查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text)
        return r.json()

    @classmethod
    def api_项目花名册分页查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_项目花名册分页查询'
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
    def api_项目花名册通过id查询(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_项目花名册通过id查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_项目花名册通过id删除(cls, session: requests.Session, id: str, header: dict):
        api_name = 'api_项目花名册通过id删除'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.delete(url, headers=header)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()
