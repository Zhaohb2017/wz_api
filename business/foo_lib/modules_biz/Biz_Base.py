import requests

from business.foo_lib.modules_db.werun.Db_设备智管 import Db设备智管
from page_object.werun.上传下载.Page_附件管理 import Page附件管理
from page_object.werun.专家知识库.Page_故障原因 import Page故障原因
from page_object.werun.专家知识库.Page_故障现象 import Page故障现象
from page_object.werun.专家知识库.Page_标准作业指导书 import Page标准作业指导书
from page_object.werun.专家知识库.Page_解决办法 import Page解决办法
from page_object.werun.专家知识库.Page_资料库 import Page资料库
from page_object.werun.保养管理.Page_维保标准表管理 import Page维保标准表管理
from page_object.werun.保养管理.Page_维保计划表管理 import Page维保计划表管理
from page_object.werun.信息发布.Page_素材管理 import Page素材管理
from page_object.werun.信息发布.Page_节目管理 import Page节目管理
from page_object.werun.告警中心.Page_告警记录管理 import Page告警记录管理
from page_object.werun.告警中心.Page_安防告警配置管理 import Page安防告警配置管理
from page_object.werun.告警中心.Page_应急预案 import Page应急预案
from page_object.werun.告警中心.Page_设备告警配置管理 import Page设备告警配置管理
from page_object.werun.告警中心.Page_黑名单布控管理 import Page黑名单布控管理
from page_object.werun.基础管理.Page_企业员工 import Page企业员工
from page_object.werun.基础管理.Page_企业档案 import Page企业档案
from page_object.werun.基础管理.Page_区域或楼栋表管理 import Page区域或楼栋表管理
from page_object.werun.基础管理.Page_楼层房间信息表管理 import Page楼层房间信息表管理
from page_object.werun.基础管理.Page_空间类型表管理 import Page空间类型表管理
from page_object.werun.基础管理.Page_设备类型表管理 import Page设备类型表管理
from page_object.werun.基础管理.Page_设备表管理 import Page设备表管理
from page_object.werun.基础管理.Page_项目花名册管理 import Page项目花名册管理
from page_object.werun.基础管理.Page_项目表管理 import Page项目表管理
from page_object.werun.巡检管理.Page_巡检标准表管理 import Page巡检标准表管理
from page_object.werun.巡检管理.Page_巡检点表管理 import Page巡检点表管理
from page_object.werun.巡检管理.Page_巡检计划表管理 import Page巡检计划表管理
from page_object.werun.库存管理.Page_物料分类管理 import Page物料分类管理
from page_object.werun.排班管理.Page_排班计划管理 import Page排班计划管理
from page_object.werun.排班管理.Page_班次管理 import Page班次管理
from page_object.werun.能耗管理.Page_能耗统计管理 import Page能耗统计管理
from page_object.werun.智慧通行.Page_企业通行规则 import Page企业通行规则
from page_object.werun.智慧通行.Page_停车场管理 import Page停车场管理
from page_object.werun.智慧通行.Page_授权列表 import Page授权列表
from page_object.werun.智慧通行.Page_车场授权管理 import Page车辆授权管理
from page_object.werun.智慧通行.Page_通行设备 import Page通行设备
from page_object.werun.模式联动规则配置.Page_联动模式管理 import Page联动模式管理
from page_object.werun.模式联动规则配置.Page_运行模式管理 import Page运行模式管理
from page_object.werun.用户权限.Page_用户表管理 import Page用户表管理
from page_object.werun.用户权限.Page_组织架构表管理 import Page组织架构表管理
from page_object.werun.用户权限.Page_角色表管理 import Page角色表管理
from page_object.werun.线上巡检.Page_巡检任务管理 import Page巡检任务管理
from page_object.werun.线上巡检.Page_巡检机房管理 import Page巡检机房管理
from page_object.werun.线上巡检.Page_巡检计划管理 import Page巡检计划管理
from page_object.werun.线上巡检.Page_环境巡检标准管理 import Page环境巡检标准管理
from page_object.werun.视频巡逻.Page_巡逻区域配置表管理 import Page巡逻区域配置表管理
from page_object.werun.视频巡逻.Page_巡逻检查项配置表管理 import Page巡逻检查项配置表管理
from page_object.werun.视频巡逻.Page_巡逻计划表管理 import Page巡逻计划表管理


def clear_data(session:requests.Session,header:dict,**ids):
    """
    tearDown清理自动化产生的数据
    :param header:
    :param session: 会话
    :param ids:
    :return:
    """
    id_keys = ids.keys()
    for key in id_keys:
        if key == 'plan_id':
            Page巡检计划表管理.api_巡检计划通过id删除(session, str(ids[key]), header)
        if key == 'xjp_id':
            Page巡检点表管理.api_巡检点通过id删除(session, str(ids[key]), header)
        if key == 'yxms_id':
            Page运行模式管理.api_运行模式通过id删除(session, str(ids[key]), header)
        if key == 'ldms_id':
            Page联动模式管理.api_联动模式通过id删除(session, str(ids[key]), header)
        if key == 'bp_id':
            Page维保计划表管理.api_计划表通过id删除(session, str(ids[key]), header)
        if key == 'xmzl_id':
            Page资料库.api_删除项目资料(session, str(ids[key]), header)
        if key == 'zlk_id':
            Page资料库.api_删除资料库(session, str(ids[key]), header)
        if key == 'zds_id':
            Page标准作业指导书.api_通过id删除标准作业指导书(session, str(ids[key]), header)
        if key == 'jjff_id':
            Page解决办法.api_通过id删除解决方法(session, str(ids[key]), header)
        if key == 'gzyy_id':
            Page故障原因.api_通过id删除故障原因(session, str(ids[key]), header)
        if key == 'gzxx_id':
            Page故障现象.api_通过id删除故障现象(session, str(ids[key]), header)
        if key == 'by_id':
            Page维保标准表管理.api_维保标准通过id删除(session, str(ids[key]), header)
        if key == 'x_id':
            Page巡检标准表管理.api_巡检标准通过id删除(session, str(ids[key]), header)
        if key =='wf_id':
            Page物料分类管理.api_通过id删除物料分类(session, str(ids[key]), header)
        if key =='sqlb_id':
            Page授权列表.api_通过id删除授权(session, str(ids[key]), header)
        if key =='pic_id':
            Page附件管理.api_通过id删除附件(session,str(ids[key]),header)
        if key == 'cldj_id':
            Page停车场管理.api_通过id删除车辆登记(session, str(ids[key]), header)
        if key =='clsq_id':
            Page车辆授权管理.api_通过id删除车辆授权(session, str(ids[key]), header)
        if key == 'tcc_id':
            Page停车场管理.api_通过id删除停车场(session, str(ids[key]), header)
        if key =='bq_id':
            Page通行设备.api_通行设备删除标签(session, str(ids[key]), header)
        if key == 'txgz_id':
            Page企业通行规则.api_删除企业通行规则(session, str(ids[key]), header)
        if key == 'feild_add_g_id':
            Page能耗统计管理.api_通过id删除分组(session, str(ids[key]), header)
        if key == 'yg_id':
            Page企业员工.api_删除企业员工(session, str(ids[key]), header)
        if key == 'qy_id':
            Page企业档案.api_删除企业(session, str(ids[key]), header)
        if key =='b_plan_id':
            Page排班计划管理.api_通过id删除班次计划(session,str(ids[key]),header)
        if key == 'b_id':
            Page班次管理.api_通过id删除班次(session, str(ids[key]), header)
        if key == 'yjya_id':
            Page应急预案.api_删除应急预案(session, str(ids[key]), header)
        if key == 'sbgj_id':
            Page设备告警配置管理.api_设备告警配置通过id删除(session, str(ids[key]), header)
        if key == 'jh_id':
            Page巡检计划管理.api_通过id删除巡检计划(session, str(ids[key]), header)
        if key =='jf_id':
            Page巡检机房管理.api_通过id删除巡检机房(session,str(ids[key]),header)
        if key == 'sbxj_id':
            Page环境巡检标准管理.api_通过id删除环境巡检标准(session, str(ids[key]), header)
        if key == 'xf_id' or key == 'aqpz_id':
            Page安防告警配置管理.api_安防告警配置通过id删除(session, str(ids[key]), header)
        if key == 'aq_id':
            Page黑名单布控管理.api_黑名单布控通过id删除(session, str(ids[key]), header)
        if key =='gjjl_id':
            Page告警记录管理.api_告警记录通过id删除(session,str(ids[key]),header)
        if key == 'rw_id':
            Page巡检任务管理.api_通过id删除巡检任务(session, str(ids[key]), header)
        if key == 'pro_id':
            Page节目管理.api_通过id删除节目(session, str(ids[key]), header)
        if key == 'spic_id':
            Page素材管理.api_通过id删除素材(session, str(ids[key]), header)
        if key == 'hmc_u_id' or key == 'hmc_u_id1':
            Page项目花名册管理.api_项目花名册通过id删除(session, str(ids[key]), header)
        if key == 'xljh_id':
            Page巡逻计划表管理.api_巡逻计划通过id删除(session, str(ids[key]), header)
        if key == 'xlqy_id':
            Page巡逻区域配置表管理.api_巡逻区域配置通过id删除(session, str(ids[key]), header)
        if key == 'xlbz_id':
            Page巡逻检查项配置表管理.api_巡逻检查项配置通过id删除(session, str(ids[key]), header)
        if key == 'tz_id':
            Page设备表管理.api_设备通过id删除(session, str(ids[key]), header)
        if key == 'sub_id' or key == 's_id' or key == 'fs_id' or key == 's_id2':
            Page设备类型表管理.api_设备类型通过id删除(session, str(ids[key]), header)
        if key == 'u_id':
            Page用户表管理.api_用户通过id删除(session, str(ids[key]), header)
        if key == 'j_id':
            Page角色表管理.api_角色通过id删除(session, str(ids[key]), header)
        if key == 'z_id' or key == 'z_id_sub':
            Page组织架构表管理.api_组织架构通过id删除(session, str(ids[key]), header)
        if key == 'room_id' or key == 'room_id2':
            Page楼层房间信息表管理.api_楼层房间信息通过id删除(session, str(ids[key]), header)
        if key == 'space_type_id' or key == 'space_type_id_sub':
            Page空间类型表管理.api_空间类型通过id删除(session, str(ids[key]), header)
        if key == 'f_id':
            Page区域或楼栋表管理.api_区域或楼栋通过id删除(session, str(ids[key]), header)
        if key == 'p_id':
            Page项目表管理.api_项目通过id删除(session, ids[key], header)
        if key == 'sub_id':
            Db设备智管.db_删除设备执行动作(str(ids[key]))
        if key == 's_id':
            Db设备智管.db_删除设备执行动作(str(ids[key]))