import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page定时任务(object):

    @classmethod
    def api_登录(cls, session: requests.Session, feilds: dict):
        api_name = 'api_登录'
        url = Api_Addr_WeRun.xxl_job.get(api_name)
        header=Browser_Param.headers.get('form').copy()
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_获取任务组HTML(cls, session: requests.Session):
        api_name = 'api_获取任务组HTML'
        url = Api_Addr_WeRun.xxl_job.get(api_name)
        header=Browser_Param.headers.get('form').copy()
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text)
        return r.text

    @classmethod
    def api_通过GROUPID查询列表(cls, session: requests.Session, feilds: dict):
        api_name = 'api_通过GROUPID查询列表'
        url = Api_Addr_WeRun.xxl_job.get(api_name)
        header=Browser_Param.headers.get('form').copy()
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_执行任务(cls, session: requests.Session, feilds: dict):
        api_name = 'api_执行任务'
        url = Api_Addr_WeRun.xxl_job.get(api_name)
        header=Browser_Param.headers.get('form').copy()
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_生成线上巡检任务(cls, session: requests.Session, feilds: dict):
        api_name = 'api_生成线上巡检任务'
        url = Api_Addr_WeRun.xxl_job.get(api_name)
        header=Browser_Param.headers.get('form').copy()
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_定时更新线上巡检任务状态(cls, session: requests.Session, feilds: dict):
        api_name = 'api_定时更新线上巡检任务状态'
        url = Api_Addr_WeRun.xxl_job.get(api_name)
        header=Browser_Param.headers.get('form').copy()
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_查询保养列表(cls, session: requests.Session, feilds: dict):
        api_name = 'api_查询保养列表'
        url = Api_Addr_WeRun.xxl_job.get(api_name)
        header=Browser_Param.headers.get('form').copy()
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_生成保养任务(cls, session: requests.Session, feilds: dict):
        api_name = 'api_生成保养任务'
        url = Api_Addr_WeRun.xxl_job.get(api_name)
        header=Browser_Param.headers.get('form').copy()
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_巡检定时任务列表(cls, session: requests.Session, feilds: dict):
        api_name = 'api_巡检定时任务列表'
        url = Api_Addr_WeRun.xxl_job.get(api_name)
        header=Browser_Param.headers.get('form').copy()
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_生成线下巡检任务(cls, session: requests.Session, feilds: dict):
        api_name = 'api_生成线下巡检任务'
        url = Api_Addr_WeRun.xxl_job.get(api_name)
        header=Browser_Param.headers.get('form').copy()
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_生成巡逻任务(cls, session: requests.Session, feilds: dict):
        api_name = 'api_生成巡逻任务'
        url = Api_Addr_WeRun.xxl_job.get(api_name)
        header=Browser_Param.headers.get('form').copy()
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_定时更新巡逻任务(cls, session: requests.Session, feilds: dict):
        api_name = 'api_定时更新巡逻任务'
        url = Api_Addr_WeRun.xxl_job.get(api_name)
        header=Browser_Param.headers.get('form').copy()
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()


