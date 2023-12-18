import requests
from requests_toolbelt import MultipartEncoder

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page附件管理(object):


    @classmethod
    def api_下载附件(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_下载附件'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r

    @classmethod
    def api_预览图片(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_预览图片'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_附件集合查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_附件集合查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_附件分页查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_附件分页查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()


    @classmethod
    def api_上传附件(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_上传附件'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        m = MultipartEncoder(fields=feilds, boundary='----WebKitFormBoundarynuAGsBlvBWSGBhkU')
        header.update({'Content-Type': m.content_type})
        r = session.post(url, data=m,headers = header)
        Common_Base.logging_api_info(api_name, url, str(header),r.text,str(feilds))
        return r.json()

    @classmethod
    def api_通过id查询附件(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_通过id查询附件'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_通过id删除附件(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_通过id删除附件'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.delete(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()
