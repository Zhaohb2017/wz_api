#!/usr/bin/env python
# encoding: utf-8
import requests
from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base


class Page项目日志(object):

    @classmethod
    def api_项目日志分页查询(cls, session: requests.Session, feilds: dict,header:dict):
        api_name = 'api_项目日志分页查询'
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

