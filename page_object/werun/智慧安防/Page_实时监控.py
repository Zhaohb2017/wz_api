#!/usr/bin/env python
# encoding: utf-8
import requests

from business.param_config.api_addr import Api_Addr_WeRun
from business.param_config.biz_param import Browser_Param
from common import Common_Base

class Page实时监控(object):
    @classmethod
    def api_实时监控列表(cls, session: requests.Session, header: dict):
        api_name = 'api_实时监控列表'
        url = Api_Addr_WeRun.werun_apis.get(api_name)
        header.update(Browser_Param.headers.get('json').copy())
        r = session.post(url, headers=header)
        Common_Base.logging_api_info(api_name, url, str(header), r.text)
        return r.json()