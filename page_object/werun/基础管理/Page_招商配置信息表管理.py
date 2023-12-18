import requests
from requests_toolbelt import MultipartEncoder

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page招商配置信息表管理(object):


    @classmethod
    def api_下载招商配置模版(cls, session: requests.Session, header:dict):
        api_name = 'api_下载招商配置模版'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header) )
        return r

    @classmethod
    def api_上传导入招商配置(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_上传导入招商配置'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        m = MultipartEncoder(fields=feilds, boundary='----WebKitFormBoundarynuAGsBlvBWSGBhkU')
        header.update({'Content-Type': m.content_type})
        r = session.post(url, data = m,headers = header)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header),r.text,str(feilds))
        return r.json()

    @classmethod
    def api_新增招商配置信息表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增招商配置信息表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_修改招商配置信息表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_修改招商配置信息表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_招商配置信息集合查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_招商配置信息集合查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_招商配置信息分页查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_招商配置信息分页查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_招商配置信息通过id查询(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_招商配置信息通过id查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_招商配置信息通过id删除(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_招商配置信息通过id删除'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.delete(url, headers=header)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=None,request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()
