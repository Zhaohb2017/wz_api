import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page能耗分析(object):

    @classmethod
    def api_用电能流图查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_用电能流图查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_查询能耗图表接口(cls, feilds: dict,header:dict):
        res_data = None
        method = None
        api_name = 'api_查询能耗图表接口'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        try:
            r = requests.post(url, headers=header, json=feilds, timeout=20)
            r.raise_for_status()
            res_data = r.text
            method = r.request.method
        except Exception as e:
            raise e
        finally:
            Common_Base.logging_api_info(api_name= api_name, api_address= url, api_header= str(header) ,
                                         api_response= res_data,  api_param= str(feilds),request_method=method)
        return r.json()



    @classmethod
    def api_用能统计查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_用能统计查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_单方能耗统计查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_单方能耗统计查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_能耗折碳排放趋势查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_能耗折碳排放趋势查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_能耗折标煤趋势查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_能耗折标煤趋势查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_分区用电占比查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_分区用电占比查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_分项用电占比查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_分项用电占比查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_分区用电趋势查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_分区用电趋势查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_查询能耗态势(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_查询能耗态势'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_分项用电趋势查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_分项用电趋势查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('form').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_分区用电排名查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_分区用电排名查询'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    pass