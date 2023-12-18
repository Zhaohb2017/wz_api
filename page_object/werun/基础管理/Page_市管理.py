import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page市管理(object):

    @classmethod
    def api_新增市区(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增市区'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_修改市区(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_修改市区'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_根据cityid获取城市信息(cls, session: requests.Session, cityid: str,header:dict):
        api_name = 'api_根据cityid获取城市信息'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+cityid
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_根据首字母查询城市(cls, session: requests.Session, firstChar: str,header:dict):
        api_name = 'api_根据首字母查询城市'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+firstChar
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_根据城市code查询城市(cls, session: requests.Session, cityValue: str,header:dict):
        api_name = 'api_根据城市code查询城市'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+cityValue
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_查询热门城市(cls, session: requests.Session,header:dict):
        api_name = 'api_查询热门城市'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_根据城市名称查询市列表(cls, session: requests.Session,cityName:str,header:dict):
        api_name = 'api_根据城市名称查询市列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+cityName
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()


    @classmethod
    def api_市区集合查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_市区集合查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_市区分页查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_市区分页查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()

    @classmethod
    def api_修改城市的调用次数(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_修改城市的调用次数'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_市区通过id查询(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_市区通过id查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_市区通过id删除(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_市区通过id删除'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.delete(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()
