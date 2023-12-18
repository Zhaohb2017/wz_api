import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page巡检计划表管理(object):

    @classmethod
    def api_新增巡检计划表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增巡检计划表'
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
    def api_修改巡检计划表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_修改巡检计划表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_检查巡检计划名称是否存在(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_检查巡检计划名称是否存在'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header,params = feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.json()

    @classmethod
    def api_查询巡检计划下拉框(cls, session: requests.Session,header:dict):
        api_name = 'api_查询巡检计划下拉框'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_查询定时任务列表(cls, session: requests.Session, feilds: dict,header:dict):
        res_data = None
        method = None
        api_name = 'api_查询定时任务列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.post(url, headers=header, json=feilds, timeout=20)
            r.raise_for_status()
            res_data = r.text
            method = r.request.method
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name= api_name,api_address=  url, api_header=  str(header) ,
                                         api_response= res_data, api_param= str(feilds),request_method=method)
        return r.json()

    @classmethod
    def api_修改巡检计划状态(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_修改巡检计划状态'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method)
            raise Exception(e)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_巡检计划通过id查询(cls, session: requests.Session, id: str,header:dict):
        res_data = None
        method = None
        api_name = 'api_巡检计划通过id查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        try:
            r = session.get(url, headers=header, timeout=20)
            r.raise_for_status()
            res_data = r.text
            method = r.request.method
        except Exception as e:
            raise  e
        finally:
            Common_Base.logging_api_info(api_name= api_name, api_address= url,  api_header=  str(header),
                                         api_response= res_data,request_method=method)
        return r.json()

    @classmethod
    def api_巡检计划通过id删除(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_巡检计划通过id删除'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.delete(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()
