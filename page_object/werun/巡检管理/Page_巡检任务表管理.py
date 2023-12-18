import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page巡检任务表管理(object):


    @classmethod
    def api_修改巡检任务记录信息表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_修改巡检任务记录信息表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_导出巡检记录(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_导出巡检记录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header,params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.json()

    @classmethod
    def api_查询巡检任务执行记录列表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_查询巡检任务执行记录列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header,params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.json()

    @classmethod
    def api_获取今日巡检任务状态数量(cls, session: requests.Session,header:dict):
        api_name = 'api_获取今日巡检任务状态数量'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_查询打印巡检记录(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_查询打印巡检记录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header,params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.json()

    @classmethod
    def api_巡检记录导出列表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_巡检记录导出列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_编辑查询选中的巡检任务记录(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_编辑查询选中的巡检任务记录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header,params=feilds)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.json()

    @classmethod
    def api_打印巡检计划及巡检点(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_打印巡检计划及巡检点'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header,params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.json()

    @classmethod
    def api_查询巡检任务执行记录详情(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_查询巡检任务执行记录详情'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header,params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.json()

    @classmethod
    def api_查询巡检任务执行记录分页列表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_查询巡检任务执行记录分页列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_获取打印巡检记录(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_获取打印巡检记录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header,params=feilds)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.json()

    @classmethod
    def api_批量更新查询选中的巡检任务记录(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_批量更新查询选中的巡检任务记录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header,params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.json()

    @classmethod
    def api_巡检任务通过id查询(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_巡检任务通过id查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_线下巡检任务概览(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_线下巡检任务概览'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.get(url, headers=header,params = feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_巡检任务通过id删除(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_巡检任务通过id删除'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.delete(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()
