import time

from lxml import etree

import requests

from business.param_config.api_param.werun.定时任务 import Param_定时任务
from page_object.werun.定时任务.Page_定时任务 import Page定时任务


class BizXxlJob(object):
    @classmethod
    def biz_执行定时任务(cls,session: requests.Session,module:str,exe_name:str):
        """
        biz_执行定时任务
        :param session: 会话句柄
        :param module: 模块
        :param exe_name: 执行任务名称（可模糊）
        :return:
        """
        # 登录
        res_data = Page定时任务.api_登录(session, Param_定时任务.p_login.get('登录'))
        # 通过jobinfo查询group_id
        res_data = Page定时任务.api_获取任务组HTML(session)
        # 通过xpath获取模块id
        data_html=etree.HTML(res_data).xpath("//*[@id='jobGroup']")
        options = data_html[0].xpath("option")
        job_group = ''
        for option in options:
            if module in option.text:
                job_group = option.attrib.get('value')
        # 通过group_id分页查询任务id
        feild_page = Param_定时任务.p_list.get('通过GROUPID查询列表')
        feild_page['jobGroup'] = job_group
        res_data = Page定时任务.api_通过GROUPID查询列表(session,feild_page)
        exe_list = res_data.get('data')
        exe_id = ''
        executorParam = ''
        for exe_item in exe_list:
            if exe_name in exe_item.get('jobDesc'):
                exe_id = str(exe_item.get('id'))
                executorParam = str(exe_item.get('executorParam'))
                break
        # 执行任务
        field_rw = Param_定时任务.p_trigger.get('其它任务')
        field_rw['id'] = exe_id
        field_rw['executorParam'] = executorParam
        res_data = Page定时任务.api_执行任务(session, field_rw)
        time.sleep(30)
        return res_data
