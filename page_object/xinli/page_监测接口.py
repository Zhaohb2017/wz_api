import logging

import requests
# from requests_toolbelt import MultipartEncoder
import json
from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class PageMonitorMonitor(object):
    """监测接口合集"""

    @classmethod
    def api_alarm_page(cls, session: requests.Session, header: dict, params: dict):
        """告警记录"""
        global r
        api_name = 'api告警记录列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.post(url, headers=header, json=params, timeout=20, verify=False)
            r.raise_for_status()
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name=api_name, api_address=url, api_header=str(header),
                                         api_response=r.text, api_param=json.dumps(params), request_method=r.request.method if r else None)
        return r.json() if r else None


    @classmethod
    def api_facilities_page(cls, session: requests.Session, header: dict, params: dict):
        """设备台账"""
        global r
        api_name = 'api_设备分页查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.post(url, headers=header, json=params, timeout=20, verify=False)
            r.raise_for_status()
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name=api_name, api_address=url, api_header=str(header),
                                         api_response=r.text, api_param=json.dumps(params), request_method=r.request.method if r else None)
        return r.json() if r else None

    @classmethod
    def api_passage_page(cls, session: requests.Session, header: dict, params: dict):
        """授权列表"""
        global r
        api_name = 'api_授权列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.post(url, headers=header, json=params, timeout=20, verify=False)
            r.raise_for_status()
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name=api_name, api_address=url, api_header=str(header),
                                         api_response=r.text, api_param=json.dumps(params), request_method=r.request.method if r else None)
        return r.json() if r else None

    @classmethod
    def api_facility_history(cls, session: requests.Session, header: dict, params: dict):
        """设备运行历史记录"""
        global r
        api_name = 'api_运行参数历史记录'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.post(url, headers=header, json=params, timeout=20, verify=False)
            r.raise_for_status()
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name=api_name, api_address=url, api_header=str(header),
                                         api_response=r.text, api_param=json.dumps(params),
                                         request_method=r.request.method if r else None)
        return r.json() if r else None


    @classmethod
    def api_consumecate_page(cls, session: requests.Session, header: dict, params={}):
        res_data = None
        method = None
        api_name = 'api_设备分页查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.post(url, headers=header, json=params, timeout=20, verify=False)
            r.raise_for_status()
            res_data = r.text
            method = r.request.method
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name=api_name, api_address=url, api_header=str(header),
                                         api_response=res_data,
                                         request_method=method, api_param=params)
        return r.json()

    @classmethod
    def api_energyConsumptionProfileByItemCode(cls, session: requests.Session, header: dict, params: dict):
        res_data = None
        method = None
        api_name = 'energyConsumptionProfileByItemCode'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.post(url, headers=header, json=params, timeout=20, verify=False)
            r.raise_for_status()
            res_data = r.text
            method = r.request.method
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name=api_name, api_address=url, api_header=str(header),
                                         api_response=res_data,
                                         request_method=method, api_param=params)
        return r.json()

    @classmethod
    def api_facconfig_page(cls, session: requests.Session, header: dict, params: dict):
        res_data = None
        method = None
        api_name = 'facconfig_page'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.post(url, headers=header, json=params, timeout=20, verify=False)
            r.raise_for_status()
            res_data = r.text
            method = r.request.method
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name=api_name, api_address=url, api_header=str(header),
                                         api_response=res_data,
                                         request_method=method, api_param=params)
        return r.json()

    @classmethod
    def api_history_list(cls, session: requests.Session, header: dict, params: dict):
        res_data = None
        method = None
        api_name = 'history_list'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.post(url, headers=header, json=params, timeout=20, verify=False)
            r.raise_for_status()
            res_data = r.text
            method = r.request.method
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name=api_name, api_address=url, api_header=str(header),
                                         api_response=res_data,
                                         request_method=method, api_param=params)
        return r.json()

    @classmethod
    def api_log_page(cls, session: requests.Session, header: dict, params={}):
        res_data = None
        method = None
        api_name = 'log_page'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = session.post(url, headers=header, json=params, timeout=20, verify=False)
            r.raise_for_status()
            res_data = r.text
            method = r.request.method
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name=api_name, api_address=url, api_header=str(header),
                                         api_response=res_data,
                                         request_method=method, api_param=params)
        return r.json()
