import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page物料出入库记录(object):

    @classmethod
    def api_出入库记录历史下载(cls, session: requests.Session,header:dict):
        api_name = 'api_出入库记录历史下载'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.get(url,headers=header)
        Common_Base.logging_api_info(api_name, url, str(header) ,str(r.status_code))
        return r.status_code

    @classmethod
    def api_分页查询出入库记录历史(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_分页查询出入库记录历史'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()

    @classmethod
    def api_查询简单的物料出入库记录集合(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_查询简单的物料出入库记录集合'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header, json=feilds)
        Common_Base.logging_api_info(api_name, url, str(header) ,r.text, str(feilds),request_method=r.request.method)
        return r.json()