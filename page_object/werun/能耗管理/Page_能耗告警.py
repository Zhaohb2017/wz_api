import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page能耗告警(object):

    @classmethod
    def api_分页查询能耗告警(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_分页查询能耗告警'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_能耗异常确认(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_能耗异常确认'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_APP上报电表用量(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_APP上报电表用量'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    pass
    # @classmethod
    # def api_新增巡逻任务与巡逻区域关联(cls, session: requests.Session, feilds: dict,header:dict):
    #     api_name = 'api_新增巡逻任务与巡逻区域关联'
    #     url = Api_Addr_WeRun.werun_apis.get(api_name)
    #     header.update(Browser_Param.headers.get('json').copy())
    #     r = session.post(url, headers=header, json=feilds)
    #     Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
    #     return r.json()
    #
    # @classmethod
    # def api_修改巡逻任务与巡逻区域关联(cls, session: requests.Session, feilds: dict,header:dict):
    #     api_name = 'api_修改巡逻任务与巡逻区域关联'
    #     url = Api_Addr_WeRun.werun_apis.get(api_name)
    #     header.update(Browser_Param.headers.get('json').copy())
    #     r = session.put(url, headers=header, json=feilds)
    #     Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
    #     return r.json()
    #
    # @classmethod
    # def api_巡逻任务与巡逻区域集合查询(cls, session: requests.Session, feilds: dict,header:dict):
    #     api_name = 'api_巡逻任务与巡逻区域集合查询'
    #     url = Api_Addr_WeRun.werun_apis.get(api_name)
    #     header.update(Browser_Param.headers.get('json').copy())
    #     r = session.post(url, headers=header, json=feilds)
    #     Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
    #     return r.json()
    #
    # @classmethod
    # def api_巡逻任务巡逻区域详情检查项(cls, session: requests.Session, feilds: dict,header:dict):
    #     api_name = 'api_巡逻任务巡逻区域详情检查项'
    #     url = Api_Addr_WeRun.werun_apis.get(api_name)
    #     header.update(Browser_Param.headers.get('form').copy())
    #     r = session.get(url, headers=header, params=feilds)
    #     Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
    #     return r.json()
    #
    # @classmethod
    # def api_查询巡逻任务的巡逻区域的异常检查项列表(cls, session: requests.Session, feilds: dict,header:dict):
    #     api_name = 'api_查询巡逻任务的巡逻区域的异常检查项列表'
    #     url = Api_Addr_WeRun.werun_apis.get(api_name)
    #     header.update(Browser_Param.headers.get('form').copy())
    #     r = session.get(url, headers=header, params=feilds)
    #     Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
    #     return r.json()
    #
    # @classmethod
    # def api_巡逻任务与巡逻区域分页查询(cls, session: requests.Session, feilds: dict,header:dict):
    #     api_name = 'api_巡逻任务与巡逻区域分页查询'
    #     url = Api_Addr_WeRun.werun_apis.get(api_name)
    #     header.update(Browser_Param.headers.get('json').copy())
    #     r = session.post(url, headers=header, json=feilds)
    #     Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
    #     return r.json()
    #

    #
    # @classmethod
    # def api_巡逻任务与巡逻区域通过id查询(cls, session: requests.Session, id: str,header:dict):
    #     api_name = 'api_巡逻任务与巡逻区域通过id查询'
    #     url = Api_Addr_WeRun.werun_apis.get(api_name)+id
    #     header.update(Browser_Param.headers.get('form').copy())
    #     r = session.get(url, headers=header)
    #     Common_Base.logging_api_info(api_name, url, str(header), r.text)
    #     return r.json()
    #
    # @classmethod
    # def api_巡逻任务与巡逻区域通过id删除(cls, session: requests.Session, id: str,header:dict):
    #     api_name = 'api_巡逻任务与巡逻区域通过id删除'
    #     url = Api_Addr_WeRun.werun_apis.get(api_name)+id
    #     header.update(Browser_Param.headers.get('form').copy())
    #     r = session.delete(url, headers=header)
    #     Common_Base.logging_api_info(api_name, url, str(header), r.text)
    #     return r.json()
