import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page巡检任务管理(object):

    @classmethod
    def api_新增巡检任务(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_新增巡检任务'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_修改巡检任务(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_修改巡检任务'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_巡检任务根据状态统计任务数量(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_巡检任务根据状态统计任务数量'
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
    def api_执行巡检任务查询巡检机房(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_执行巡检任务查询巡检机房'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header,params = feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.json()

    @classmethod
    def api_执行巡检任务查询巡检机房列表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_执行巡检任务查询巡检机房列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header,params = feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.json()

    @classmethod
    def api_执行巡检任务完成巡检任务查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_执行巡检任务完成巡检任务查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header,params = feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.json()

    @classmethod
    def api_执行巡检任务完成巡检任务提交(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_执行巡检任务完成巡检任务提交'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_执行巡检任务提交巡检机房(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_执行巡检任务提交巡检机房'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_导出巡检任务表(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_导出巡检任务表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.get(url, headers=header,params = feilds)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            Common_Base.logging_api_error(err=e,api_name=api_name,api_address=url,api_header=str(header),api_response_code=str(r.status_code),
                                          api_param=str(feilds),request_method=r.request.method)
        Common_Base.logging_api_info(api_name, url, str(header), r.text,str(feilds))
        return r.text

    @classmethod
    def api_分页查询设备任务(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_分页查询设备任务'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_巡检任务集合查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_巡检任务集合查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_巡检任务分页查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_巡检任务分页查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_线上巡检数据概览(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_线上巡检数据概览'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_修改巡检人(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_修改巡检人'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.put(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_通过id查询巡检任务(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_通过id查询巡检任务'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.get(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()

    @classmethod
    def api_通过id删除巡检任务(cls, session: requests.Session, id: str,header:dict):
        api_name = 'api_通过id删除巡检任务'
        url = Api_Addr_WeRun.werun_apis.get(api_name)+id
        header.update(Browser_Param.headers.get('form').copy())
        r = session.delete(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()


    @classmethod
    def api_分页查询巡检任务(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_分页查询巡检任务'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
        return r.json()


    # @classmethod
    # def api_导出巡检任务表(cls, session: requests.Session, feilds: dict, header: dict):
    #     api_name = 'api_导出巡检任务表'
    #     url = Api_Addr_WeRun.werun_apis.get(api_name)
    #     header.update(Browser_Param.headers.get('json').copy())
    #     r = session.get(url, headers=header, params=feilds)
    #     r.raise_for_status()
    #     Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
    #     return r.json()


    @classmethod
    def api_获取所有建筑房间(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_获取所有建筑房间'
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
    def api_楼层的寻机房列表(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_根据楼栋或楼层id查询巡检机房列表'
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
    def api_巡检任务生成报告(cls, session: requests.Session, feilds: dict, header: dict):
        api_name = 'api_巡检任务生成报告'
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

