import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page工单表管理(object):

    @classmethod
    def api_新增工单表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增工单表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_修改工单表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_修改工单表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_下载物料使用信息报表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_下载物料使用信息报表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header, params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_获取工单设备维修分页列表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_获取工单设备维修分页列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_工单分页查询(cls, session: requests.Session, feilds: dict,header:dict):
        res_data = None
        method = None
        api_name = 'api_工单分页查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds, timeout=20)
        try:
            r = session.post(url, headers=header, json=feilds, timeout=20)
            r.raise_for_status()
            res_data=r.text
            method = r.request.method
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name= api_name, api_address= url, api_header= str(header), api_response= res_data,
                                         api_param= str(feilds),request_method=method)
        return r.json()

    @classmethod
    def api_获取工单分页列表总数目(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_获取工单分页列表总数目'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header, params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_获取今日更新工单状态数量(cls, session: requests.Session,header:dict):
        api_name = 'api_获取今日更新工单状态数量'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text)
        return r.json()

    @classmethod
    def api_根据排班计划id及排班时间获取派单人(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_根据排班计划id及排班时间获取派单人'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header, params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_打印工单信息(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_打印工单信息'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header, params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_查询姓名查询工单列表记录(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_查询姓名查询工单列表记录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header, params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_与我有关工单的信息数量(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_与我有关工单的信息数量'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header, params=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_获取工单的状态信息数量(cls, session: requests.Session,header:dict):
        api_name = 'api_获取工单的状态信息数量'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text)
        return r.json()

    @classmethod
    def api_工单通过id查询(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_工单通过id查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_工单数据概要(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_工单数据概要'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.get(url, headers=header,params = feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_工单通过id删除(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_工单通过id删除'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.delete(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()
