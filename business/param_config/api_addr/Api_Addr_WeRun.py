import Configs

xxl_job = {
    'api_登录':f'{Configs.env_c.get("werun_xxl_job_host")}/xxl-job-admin/login', #userName=admin&password=123456&ifRemember=on

    'api_获取任务组HTML':f'{Configs.env_c.get("werun_xxl_job_host")}/xxl-job-admin/jobinfo',
    'api_通过GROUPID查询列表':f'{Configs.env_c.get("werun_xxl_job_host")}/xxl-job-admin/jobinfo/pageList',
    'api_执行任务':f'{Configs.env_c.get("werun_xxl_job_host")}/xxl-job-admin/jobinfo/trigger',
    #线上巡检
    'api_生成线上巡检任务':f'{Configs.env_c.get("werun_xxl_job_host")}/xxl-job-admin/jobinfo/trigger',
    'api_定时更新线上巡检任务状态':f'{Configs.env_c.get("werun_xxl_job_host")}/xxl-job-admin/jobinfo/trigger',
    #保养
    'api_查询保养列表':f'{Configs.env_c.get("werun_xxl_job_host")}/xxl-job-admin/jobinfo/pageList',
    'api_生成保养任务':f'{Configs.env_c.get("werun_xxl_job_host")}/xxl-job-admin/jobinfo/trigger',
    #线下巡检
    'api_巡检定时任务列表': f'{Configs.env_c.get("werun_xxl_job_host")}/xxl-job-admin/jobinfo/pageList',
    'api_生成线下巡检任务': f'{Configs.env_c.get("werun_xxl_job_host")}/xxl-job-admin/jobinfo/trigger',
    #视频巡逻
    'api_生成巡逻任务':f'{Configs.env_c.get("werun_xxl_job_host")}/xxl-job-admin/jobinfo/trigger',
    'api_定时更新巡逻任务':f'{Configs.env_c.get("werun_xxl_job_host")}/xxl-job-admin/jobinfo/trigger',

}

werun_apis={
    #首页
    'api_查询能耗图表接口': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/energyCounting/itemColum',

    #告警中心-----------------------------------------------------------------
    # 告警中心-告警操作记录管理
    'api_新增告警操作记录': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/operatelog',
    'api_修改告警操作记录': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/operatelog',
    'api_告警操作记录集合查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/operatelog/list',
    'api_告警操作记录分页查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/operatelog/page',
    'api_告警操作记录通过id查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/operatelog/',
    'api_告警操作记录通过id删除': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/operatelog/',
    'api_告警数据概览': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/alarmOverview',
    'api_告警数据统计': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/countAlarmGroupByLevel',

    # 告警中心-告警记录管理
    'api_新增告警记录': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record',
    'api_修改告警记录': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record',
    'api_告警处理进度': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/alarmHandleProgress',
    'api_处理告警': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/alarmOperate',
    'api_统计各类型告警数量': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/alarmStatistics',
    'api_安防告警今日本月未处理统计': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/countDayMonthSecurityAlarm',
    'api_安防告警黑名单违停消防统计': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/countDetailSecurityAlarm',
    'api_设备态势': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/countFacilityAlarm',
    'api_安防态势': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/countSecurityAlarm',
    'api_根据设备facId查询进行中的告警': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/getByFacId',
    'api_智管告警趋势': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/getFacAlarmTrend',
    'api_安防告警趋势': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/getSecurityAlarmTrend',
    'api_告警记录集合查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/list',
    'api_告警记录分页查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/page',
    'api_今日安全告警': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/todaySecurityAlarm',
    'api_告警记录通过id查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/',
    'api_告警记录通过id删除': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/',

    # 告警中心-告警附件管理
    'api_新增告警附件': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/attch',
    'api_修改告警附件': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/attch',
    'api_告警附件集合查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/attch/list',
    'api_告警附件分页查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/attch/page',
    'api_告警附件通过id查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/attch/',
    'api_告警附件通过id删除': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/attch/',

    # 告警中心-告警安防配置管理
    'api_新增安防告警配置': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/securityconfig',
    'api_修改安防告警配置': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/securityconfig',
    'api_安防告警配置集合查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/securityconfig/list',
    'api_安防告警配置分页查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/securityconfig/page',
    'api_安防告警配置启用禁用': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/securityconfig/updateActiveState',
    'api_安防告警配置通过id查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/securityconfig/',
    'api_安防告警配置通过id删除': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/securityconfig/',

    # 告警中心-系统告警类型条件管理
    'api_新增系统告警类型条件': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerparamsys',
    'api_修改系统告警类型条件': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerparamsys',
    'api_系统告警类型条件集合查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerparamsys/list',
    'api_系统告警类型条件分页查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerparamsys/page',
    'api_系统告警类型条件通过id查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerparamsys/',
    'api_系统告警类型条件通过id删除': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerparamsys/',

    # 告警中心-自定义告警触发条件管理
    'api_新增自定义告警触发条件': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerparamcustom',
    'api_修改自定义告警触发条件': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerparamcustom',
    'api_自定义告警触发条件集合查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerparamcustom/list',
    'api_自定义告警触发条件分页查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerparamcustom/page',
    'api_自定义告警触发条件通过id查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerparamcustom/',
    'api_自定义告警触发条件通过id删除': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerparamcustom/',

    # 告警中心-触发条件管理
    'api_新增触发条件': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerinfo',
    'api_修改触发条件': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerinfo',
    'api_触发条件集合查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerinfo/list',
    'api_触发条件分页查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerinfo/page',
    'api_触发条件通过id查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerinfo/',
    'api_触发条件通过id删除': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerinfo/',

    # 告警中心-触发条件设备关联表管理
    'api_新增触发条件设备关联表': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerfac',
    'api_修改触发条件设备关联表': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerfac',
    'api_触发条件设备关联表集合查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerfac/list',
    'api_触发条件设备关联表分页查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerfac/page',
    'api_触发条件设备关联表通过id查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerfac/',
    'api_触发条件设备关联表通过id删除': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/triggerfac/',

    # 告警中心-设备告警配置管理
    'api_新增设备告警配置': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/facconfig',
    'api_修改设备告警配置': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/facconfig',
    'api_获取设备告警配置列表': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/facconfig/getFacConfigList',
    'api_设备告警配置集合查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/facconfig/list',
    'api_设备告警配置分页查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/facconfig/page',
    'api_设备告警配置启用禁用': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/facconfig/updateActiveState',
    'api_设备告警配置通过id查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/facconfig/',
    'api_设备告警配置通过id删除': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/facconfig/',

    # 告警中心-黑名单布控管理
    'api_新增黑名单布控': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/blacklist',
    'api_修改黑名单布控': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/blacklist',
    'api_黑名单布控集合查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/blacklist/list',
    'api_黑名单布控分页查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/blacklist/page',
    'api_黑名单布控启用禁用': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/blacklist/updateActiveState',
    'api_黑名单布控通过id查询': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/blacklist/',
    'api_黑名单布控通过id删除': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/blacklist/',
    #告警中心-应急预案
    'api_新增应急预案': f'{Configs.env_c.get("werun_pc_host")}/contingency/plan/defense',
    'api_修改应急预案': f'{Configs.env_c.get("werun_pc_host")}/contingency/plan/defense',
    'api_分页查询应急预案': f'{Configs.env_c.get("werun_pc_host")}/contingency/plan/defense/page',
    'api_应急预案启用禁用': f'{Configs.env_c.get("werun_pc_host")}/contingency/plan/defense/OffOrOn',
    'api_通过id查询应急预案': f'{Configs.env_c.get("werun_pc_host")}/contingency/plan/defense/',
    'api_删除应急预案': f'{Configs.env_c.get("werun_pc_host")}/contingency/plan/defense/',

    #基础管理--------------------------------------------------------
    # 基础管理-区县表管理
    'api_新增区县表': f'{Configs.env_c.get("werun_pc_host")}/assets/area',
    'api_修改区县表': f'{Configs.env_c.get("werun_pc_host")}/assets/area',
    'api_区县表集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/area/list',
    'api_区县表分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/area/page',
    'api_区县表通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/area/',
    'api_区县表通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/area/',

    # 基础管理-区域或楼栋的楼层信息表管理
    'api_新增楼层信息表': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingfloor',
    'api_修改楼层信息表': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingfloor',
    'api_楼层信息集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingfloor/list',
    'api_楼层信息分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingfloor/page',
    'api_楼层信息通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingfloor/',
    'api_楼层信息通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingfloor/',

    # 基础管理-区域或楼栋表管理
    'api_新增区域或楼栋表': f'{Configs.env_c.get("werun_pc_host")}/assets/building/addBuilding',
    'api_修改区域或楼栋表': f'{Configs.env_c.get("werun_pc_host")}/assets/building/update',
    'api_楼栋信息分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/building/findBuildingPageList',
    'api_查询楼层树形菜单': f'{Configs.env_c.get("werun_pc_host")}/assets/building/getBuildingFloorTree',
    'api_查询区域楼栋下拉列表': f'{Configs.env_c.get("werun_pc_host")}/assets/building/getBuildingOptions',
    'api_区域或楼栋通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/building/',
    'api_区域或楼栋通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/building/',
    'api_获取所有建筑房间': f'{Configs.env_c.get("werun_pc_host")}/assets/building/getAllBuildingFloor',

    # 基础管理-图表api接口配置表管理
    'api_新增图表api接口配置表': f'{Configs.env_c.get("werun_pc_host")}/assets/chartorderapi',
    'api_修改图表api接口配置表': f'{Configs.env_c.get("werun_pc_host")}/assets/chartorderapi',
    'api_图表api接口配置集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/chartorderapi/list',
    'api_图表api接口配置分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/chartorderapi/page',
    'api_图表api接口配置通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/chartorderapi/',
    'api_图表api接口配置通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/chartorderapi/',

    # 基础管理-图表配置表管理
    'api_新增图表配置表': f'{Configs.env_c.get("werun_pc_host")}/assets/chartorder',
    'api_查询图表配置': f'{Configs.env_c.get("werun_pc_host")}/assets/chartorder/getChartOrder',
    'api_图表配置分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/chartorder/page',
    'api_更新图表配置': f'{Configs.env_c.get("werun_pc_host")}/assets/chartorder/updateChartOrder',
    'api_图表配置通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/chartorder/',
    'api_图表配置通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/chartorder/',

    # 基础管理-图表api接口配置表管理
    'api_新增字典表': f'{Configs.env_c.get("werun_pc_host")}/assets/dict',
    'api_修改字典表': f'{Configs.env_c.get("werun_pc_host")}/assets/dict',
    'api_字典集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/dict/list',
    'api_字典分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/dict/page',
    'api_字典通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/dict/',
    'api_字典通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/dict/',

    # 基础管理-市管理
    'api_新增市区': f'{Configs.env_c.get("werun_pc_host")}/assets/city',
    'api_修改市区': f'{Configs.env_c.get("werun_pc_host")}/assets/city',
    'api_根据cityid获取城市信息': f'{Configs.env_c.get("werun_pc_host")}/assets/city/getByCityId/',
    'api_根据首字母查询城市': f'{Configs.env_c.get("werun_pc_host")}/assets/city/getCityByFirstChar',
    'api_根据城市code查询城市': f'{Configs.env_c.get("werun_pc_host")}/assets/city/getCityInfoByCityValue/',
    'api_查询热门城市': f'{Configs.env_c.get("werun_pc_host")}/assets/city/getHotCity',
    'api_根据城市名称查询市列表': f'{Configs.env_c.get("werun_pc_host")}/assets/city/getListByCityName',
    'api_市区集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/city/list',
    'api_市区分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/city/page',
    'api_修改城市的调用次数': f'{Configs.env_c.get("werun_pc_host")}/assets/city/updateUseNum/',
    'api_市区通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/city/',
    'api_市区通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/city/',

    # 基础管理-招商配置信息表管理
    'api_新增招商配置信息表': f'{Configs.env_c.get("werun_pc_host")}/assets/merchants',
    'api_下载招商配置模版': f'{Configs.env_c.get("werun_pc_host")}/assets/merchants/downloadTemplate',
    'api_上传导入招商配置': f'{Configs.env_c.get("werun_pc_host")}/assets/merchants/import',
    'api_修改招商配置信息表': f'{Configs.env_c.get("werun_pc_host")}/assets/merchants',
    'api_招商配置信息集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/merchants/list',
    'api_招商配置信息分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/merchants/page',
    'api_招商配置信息通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/merchants/',
    'api_招商配置信息通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/merchants/',

    # 基础管理-楼层房间信息表管理
    'api_新增楼层房间信息表': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingFloorSpace',
    'api_修改楼层房间信息表': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingFloorSpace',
    'api_楼层房间信息集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingFloorSpace/list',
    'api_楼层房间信息分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingFloorSpace/findListPage',
    'api_楼层房间信息通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingFloorSpace/',
    'api_楼层房间信息通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingFloorSpace/',
    'api_楼层空间信息': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingFloorSpace/spaceTenseRoom',
    'api_楼层房间统计': f'{Configs.env_c.get("werun_pc_host")}/assets/buildingFloorSpace/countExceptionRoom',



    # 基础管理-监控配置表管理
    'api_新增监控配置表': f'{Configs.env_c.get("werun_pc_host")}/assets/cameraorder',
    'api_修改监控配置表': f'{Configs.env_c.get("werun_pc_host")}/assets/cameraorder',
    'api_监控配置集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/cameraorder/list',
    'api_监控配置分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/cameraorder/page',
    'api_监控更新摄像头配置': f'{Configs.env_c.get("werun_pc_host")}/assets/cameraorder/update',
    'api_监控配置通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/cameraorder/',
    'api_监控配置通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/cameraorder/',
    'api_监控设备分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/cameraorder/pageCamera',

    # 基础管理-省管理
    'api_新增省区': f'{Configs.env_c.get("werun_pc_host")}/assets/province',
    'api_修改省区': f'{Configs.env_c.get("werun_pc_host")}/assets/province',
    'api_省区集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/province/list',
    'api_省区分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/province/page',
    'api_省区通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/province/',
    'api_省区通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/province/',

    # 基础管理-空间类型表管理
    'api_新增空间类型表': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace',
    'api_修改空间类型表': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace',
    'api_空间类型树形态': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace/findTreeList',
    'api_空间类型分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace/page',
    'api_空间类型通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace/',
    'api_空间类型通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace/',


    # 基础管理-设备属性表管理
    'api_新增设备属性表': f'{Configs.env_c.get("werun_pc_host")}/assets/attribute',
    'api_修改设备属性表': f'{Configs.env_c.get("werun_pc_host")}/assets/attribute',
    'api_获取实际设备值分页列表': f'{Configs.env_c.get("werun_pc_host")}/assets/attribute/facAttrValueListPage',
    'api_设备属性集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/attribute/list',
    'api_设备属性分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/attribute/page',
    'api_设备属性查询历史参数': f'{Configs.env_c.get("werun_pc_host")}/assets/attribute/queryHistory',
    'api_设备属性通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/attribute/',
    'api_设备属性通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/attribute/',

    # 基础管理-设备摄像头关联关系管理
    'api_新增设备摄相头关联关系': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace',
    'api_修改设备摄相头关联关系': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace',
    'api_获取单个设备关联的摄像头': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace',
    'api_设备摄相头关联关系集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace/findTreeList',
    'api_设备摄相头关联关系分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace/page',
    'api_设备摄相头关联关系通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace/',
    'api_设备摄相头关联关系通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace/',

    # 基础管理-设备操作日志管理
    'api_新增设备操作日志': f'{Configs.env_c.get("werun_pc_host")}/assets/operatelog',
    'api_修改设备操作日志': f'{Configs.env_c.get("werun_pc_host")}/assets/operatelog',
    'api_设备操作日志集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/operatelog/list',
    'api_设备操作日志分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/spcspace/page',
    'api_设备操作日志通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/operatelog/',
    'api_设备操作日志通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/operatelog/',

    # 基础管理-设备类型表管理
    'api_新增设备类型表': f'{Configs.env_c.get("werun_pc_host")}/assets/category',
    'api_修改设备类型表': f'{Configs.env_c.get("werun_pc_host")}/assets/category',
    'api_根据parentId查询设备类型': f'{Configs.env_c.get("werun_pc_host")}/assets/category/getFacCategoryByParentId',
    'api_设备类型集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/category/list',
    'api_设备类型分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/category/page',
    'api_设备类型树列表查询': f'{Configs.env_c.get("werun_pc_host")}/assets/category/treeList',
    'api_设备类型通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/category/',
    'api_设备类型通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/category/',

    # 基础管理-设备表管理
    'api_新增设备表': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities',
    'api_修改设备表': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities',
    'api_查询摄相头分页列表': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/findCameraList',
    'api_根据facBimCode查询设备': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/getByBimId',
    'api_根据facCode查询设备': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/getByFacCode/',
    'api_根据facLinkCode查询设备': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/getByFacLinkCode',
    'api_根据状态统计设备数据': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/countByStatus',
    'api_设备集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/list',
    'api_设备分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/page',
    'api_设备通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/',
    'api_设备通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/',
    'api_查询设备态势': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/facCountBySystem',
    'api_运行参数历史记录': f'{Configs.env_c.get("werun_pc_host")}/iot_data_persistence/history/list',


    #设备智管-设备台账
    'api_设备模板下载': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/downloadTemplate',
    'api_设备模板导入': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/import',
    'api_授权列表': f'{Configs.env_c.get("werun_pc_host")}/passage/passageauthrecord/page',


    #设备智管 - 设备远程控制
    'api_设备远程控制page': f'{Configs.env_c.get("werun_pc_host")}/assets/facilitiescontrol/page',
    'api_设备远程控制左侧标签': f'{Configs.env_c.get("werun_pc_host")}/assets/tag/getAllTags',
    'api_设备远程控制新增标签': f'{Configs.env_c.get("werun_pc_host")}/assets/tag',
    'api_设备远程控制删除标签': f'{Configs.env_c.get("werun_pc_host")}/assets/tag/',

    'api_设备远程控制打标签': f'{Configs.env_c.get("werun_pc_host")}assets/facilitiestag/addList',





    # 基础管理-项目人员编制表管理
    'api_新增项目人员编制表': f'{Configs.env_c.get("werun_pc_host")}/assets/staffnumber/add',
    'api_根据id查询项目人员编制': f'{Configs.env_c.get("werun_pc_host")}/assets/staffnumber/findPropertyStaff',
    'api_项目人员编制分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/staffnumber/page',
    'api_修改项目人员编制表': f'{Configs.env_c.get("werun_pc_host")}/assets/staffnumber/update',
    'api_项目人员编制通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/staffnumber/',
    'api_项目人员编制通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/staffnumber/',

    # 基础管理-项目花名册管理
    'api_新增项目花名册': f'{Configs.env_c.get("werun_pc_host")}/assets/staff',
    'api_导入项目花名册': f'{Configs.env_c.get("werun_pc_host")}/assets/staff/import',
    'api_修改项目花名册': f'{Configs.env_c.get("werun_pc_host")}/assets/staff',
    'api_下载花名册导入模版': f'{Configs.env_c.get("werun_pc_host")}/assets/staff/downloadTemplate',
    'api_导出花名册': f'{Configs.env_c.get("werun_pc_host")}/assets/staff/export',
    'api_项目花名册集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/staff/list',
    'api_项目花名册分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/staff/getStaffListPage',
    'api_项目花名册通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/staff/',
    'api_项目花名册通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/staff/',

    # 基础管理-项目信息
    'api_新增项目表': f'{Configs.env_c.get("werun_pc_host")}/assets/property',
    'api_修改项目表': f'{Configs.env_c.get("werun_pc_host")}/assets/property',
    'api_查询所有项目': f'{Configs.env_c.get("werun_pc_host")}/assets/property/getAll',
    'api_通过城市字典查询项目': f'{Configs.env_c.get("werun_pc_host")}/assets/property/getPropertyByCitys',
    'api_通过组织结构PropertIds查询项目集合': f'{Configs.env_c.get("werun_pc_host")}/assets/property/getPropertyListByIds',
    'api_查询项目下拉列表': f'{Configs.env_c.get("werun_pc_host")}/assets/property/getPropertyOptions',
    'api_项目集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/property/list',
    'api_项目分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/property/page',
    'api_获取项目视图': f'{Configs.env_c.get("werun_pc_host")}/assets/property/propertyView',
    'api_项目通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/property/',
    'api_项目通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/property/',


    # 用户权限-----------------------------------------------------------------------------------------
    # 用户权限-app端登陆模块
    'api_app方登录': f'{Configs.env_c.get("werun_pc_host")}/user/v1/app/appLogin',
    'api_通过name获取用户': f'{Configs.env_c.get("werun_pc_host")}/user/v1/app/getAppUserByName',

    # 用户权限-用户表管理
    'api_创建用户': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/create',
    'api_用户通过id删除': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/delUser/',
    'api_用户离职': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/departure',
    'api_用户分页查询': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/findUserInfoPageList',
    'api_通过用户名查询登录信息': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/getUserByUserName',
    'api_查询派单人信息列表': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/getUserDispathList',
    'api_获取用户信息': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/getUserInfo',
    'api_查询接单人信息列表': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/getUserReceiveOrderList',
    'api_查询巡检负责人信息列表': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/getUserScheduleLeaderList',
    'api_用户通过id查询': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/getUserbyUserId',
    'api_用户集合查询': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/list',
    'api_用户重置密码': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/resetSword',
    'api_用户编辑账号': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/saveUser',
    'api_用户启用禁用': f'{Configs.env_c.get("werun_pc_host")}/user/v1/user/userOffOrOn',

    # 用户权限-用户角色关联表管理
    'api_新增用户角色关联表': f'{Configs.env_c.get("werun_pc_host")}/user/userrole',
    'api_修改用户角色关联表': f'{Configs.env_c.get("werun_pc_host")}/user/userrole',
    'api_用户角色关联集合查询': f'{Configs.env_c.get("werun_pc_host")}/user/userrole/list',
    'api_用户角色关联分页查询': f'{Configs.env_c.get("werun_pc_host")}/user/userrole/page',
    'api_用户角色关联通过id查询': f'{Configs.env_c.get("werun_pc_host")}/user/userrole/',
    'api_用户角色关联通过id删除': f'{Configs.env_c.get("werun_pc_host")}/user/userrole/',

    # 用户权限-后台登陆模块
    'api_后台管理登录': f'{Configs.env_c.get("werun_pc_host")}/user/v1/login',
    'api_后台管理登出': f'{Configs.env_c.get("werun_pc_host")}/auth/oauth/logout',
    'api_获取登录公钥': f'{Configs.env_c.get("werun_pc_host")}/user/v1/getPublic',
    'api_修改初始口令': f'{Configs.env_c.get("werun_pc_host")}/user/v1/updatePwd',

    # 用户权限-组织架构与用户的关联表管理
    'api_新增组织架构与用户的关联': f'{Configs.env_c.get("werun_pc_host")}/user/userorg',
    'api_修改组织架构与用户的关联': f'{Configs.env_c.get("werun_pc_host")}/user/userorg',
    'api_组织架构与用户的关联集合查询': f'{Configs.env_c.get("werun_pc_host")}/user/userorg/list',
    'api_组织架构与用户的关联分页查询': f'{Configs.env_c.get("werun_pc_host")}/user/userorg/page',
    'api_组织架构与用户的关联通过id查询': f'{Configs.env_c.get("werun_pc_host")}/user/userorg/',
    'api_组织架构与用户的关联通过id删除': f'{Configs.env_c.get("werun_pc_host")}/user/userorg/',

    # 用户权限-组织架构表管理
    'api_新增组织架构': f'{Configs.env_c.get("werun_pc_host")}/user/v1/org/add',
    'api_组织架构通过id删除': f'{Configs.env_c.get("werun_pc_host")}/user/v1/org/deleteOrg/',
    'api_查询上一级组织架构下所有的成员列表': f'{Configs.env_c.get("werun_pc_host")}/user/v1/org/findOrgChildrenUserList',
    'api_通过IdOrgCode查询组织架构': f'{Configs.env_c.get("werun_pc_host")}/user/v1/org/getOrg',
    'api_组织架构集合查询': f'{Configs.env_c.get("werun_pc_host")}/user/v1/org/list',
    'api_获取组织架构的树形结构': f'{Configs.env_c.get("werun_pc_host")}/user/v1/org/orgStructure',
    'api_组织架构分页查询': f'{Configs.env_c.get("werun_pc_host")}/user/v1/org/page',
    'api_修改组织架构': f'{Configs.env_c.get("werun_pc_host")}/user/v1/org/update',

    # 用户权限-组织项目关联表管理
    'api_新增组织项目关联': f'{Configs.env_c.get("werun_pc_host")}/user/orgproperty',
    'api_修改组织项目关联': f'{Configs.env_c.get("werun_pc_host")}/user/orgproperty',
    'api_组织项目关联集合查询': f'{Configs.env_c.get("werun_pc_host")}/user/orgproperty/list',
    'api_组织项目关联分页查询': f'{Configs.env_c.get("werun_pc_host")}/user/orgproperty/page',
    'api_组织项目关联通过id查询': f'{Configs.env_c.get("werun_pc_host")}/user/orgproperty/',
    'api_组织项目关联通过id删除': f'{Configs.env_c.get("werun_pc_host")}/user/orgproperty/',
    'api_用户关联所有项目': f'{Configs.env_c.get("werun_pc_host")}/user/orgproperty/getOrgPropertyByUid',

    # 用户权限-菜单表管理
    'api_新增菜单': f'{Configs.env_c.get("werun_pc_host")}/user/menu',
    'api_修改菜单': f'{Configs.env_c.get("werun_pc_host")}/user/menu',
    'api_菜单集合查询': f'{Configs.env_c.get("werun_pc_host")}/user/menu/list',
    'api_菜单分页查询': f'{Configs.env_c.get("werun_pc_host")}/user/menu/page',
    'api_菜单通过id查询': f'{Configs.env_c.get("werun_pc_host")}/user/menu/',
    'api_菜单通过id删除': f'{Configs.env_c.get("werun_pc_host")}/user/menu/',

    # 用户权限-角色权限关联表管理
    'api_新增角色权限关联': f'{Configs.env_c.get("werun_pc_host")}/user/rolemenu',
    'api_修改角色权限关联': f'{Configs.env_c.get("werun_pc_host")}/user/rolemenu',
    'api_资源树形结构': f'{Configs.env_c.get("werun_pc_host")}/user/rolemenu/getResourceTree',
    'api_获取角色的资源id和所有资源数结构': f'{Configs.env_c.get("werun_pc_host")}/user/rolemenu/getRoleMenu',
    'api_角色权限关联集合查询': f'{Configs.env_c.get("werun_pc_host")}/user/rolemenu/list',
    'api_角色权限关联分页查询': f'{Configs.env_c.get("werun_pc_host")}/user/rolemenu/page',
    'api_角色权限关联通过id查询': f'{Configs.env_c.get("werun_pc_host")}/user/rolemenu/',
    'api_角色权限关联通过id删除': f'{Configs.env_c.get("werun_pc_host")}/user/rolemenu/',

    # 用户权限-角色表管理
    'api_新增角色': f'{Configs.env_c.get("werun_pc_host")}/user/v1/role/createRole',
    'api_修改角色': f'{Configs.env_c.get("werun_pc_host")}/user/v1/role/updateRole',
    'api_角色集合查询': f'{Configs.env_c.get("werun_pc_host")}/user/v1/role/list',
    'api_角色分页查询': f'{Configs.env_c.get("werun_pc_host")}/user/v1/role/getRolePageList',
    'api_角色通过id查询': f'{Configs.env_c.get("werun_pc_host")}/user/v1/role/',
    'api_角色通过id删除': f'{Configs.env_c.get("werun_pc_host")}/user/v1/role/',


    # 客户档案-企业档案
    'api_新增商户': f'{Configs.env_c.get("werun_pc_host")}/customer/business/files',
    'api_修改商户': f'{Configs.env_c.get("werun_pc_host")}/customer/business/files',
    'api_导入企业': f'{Configs.env_c.get("werun_pc_host")}/customer/business/files/import',
    'api_分页查询企业': f'{Configs.env_c.get("werun_pc_host")}/customer/business/files/page',
    'api_通过id查询企业': f'{Configs.env_c.get("werun_pc_host")}/customer/business/files/',
    'api_删除企业': f'{Configs.env_c.get("werun_pc_host")}/customer/business/files/',
    'api_企业档案模板': f'{Configs.env_c.get("werun_pc_host")}/customer/business/files/down',

    # 客户档案-企业员工
    'api_新增企业员工': f'{Configs.env_c.get("werun_pc_host")}/customer/business/user',
    'api_修改企业员工': f'{Configs.env_c.get("werun_pc_host")}/customer/business/user',
    'api_企业员工重置密码': f'{Configs.env_c.get("werun_pc_host")}/customer/business/user/resetSword',
    'api_企业员工启用禁用': f'{Configs.env_c.get("werun_pc_host")}/customer/business/user/OffOrOn',
    'api_分页查询企业员工': f'{Configs.env_c.get("werun_pc_host")}/customer/business/user/page',
    'api_通过id查询企业员工': f'{Configs.env_c.get("werun_pc_host")}/customer/business/user/',
    'api_删除企业员工': f'{Configs.env_c.get("werun_pc_host")}/customer/business/user/',
    'api_批量导入员工模板': f'{Configs.env_c.get("werun_pc_host")}/customer/business/user/down',


    #能耗
    'api_新增计量对象': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyMeasurementFacilities',
    'api_通过id移除计量设备': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyMeasurementFacilities/bachDelete',
    'api_计量对象分页查询': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyMeasurementFacilities/page',
    'api_计量设备批量移除': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyMeasurementFacilities/bachDelete',

    'api_新增统计分组': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyStatisticsGroup',
    'api_通过id查询分组': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyNorm/page',
    'api_通过名称查询分组': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyStatisticsGroup/list',
    'api_编辑分组': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyStatisticsGroup',
    'api_通过id删除分组': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyStatisticsGroup/',
    #能耗-能耗分区管理
    'api_查询能耗分区列表': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/partition/treeList',
    'api_新增能耗分区': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/partition',
    'api_修改能耗分区': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/partition',
    'api_通过id删除能耗分区': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/partition/',
    'api_新增能耗指标': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/partitionnorm',
    'api_通过id删除指标': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/partitionnorm/',
    'api_通过id查询指标': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/partitionnorm/getByPartition',
    #能耗-能耗分项管理
    'api_新增能耗分项': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/item',
    'api_编辑修改能耗分项': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/item',
    'api_能耗分项列表查询': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/item/treeList',
    'api_通过id删除能耗分项': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/item/',
    'api_新增能耗分项指标': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/itemnorm',
    'api_通过id查询分项指标': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/itemnorm/getByPartition',
    'api_通过id删除分项指标': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/itemnorm/',
    #能耗-用量定额管理
    'api_分页查询定额列表': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyConfigPlan/page',
    'api_指标配置用量定额': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyConfigPlan',
    'api_用量定额配置重置': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyConfigPlan/reset/',
    #能耗-能耗告警
    'api_分页查询能耗告警': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyAlarmRecord/page',
    'api_APP上报电表用量': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energymanualup/addEenergyManualUp',
    'api_能耗异常确认': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/energyAlarmRecord',
    #能耗-能耗统计
    'api_查询能耗统计图表': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/stat',
    #能耗-环境监测
    'api_查看环境监测数据': f'{Configs.env_c.get("werun_pc_host")}/iot_data_persistence/shadow',
    #能耗-能耗分析
    'api_用电能流图查询': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/itemFlow',
    'api_用能统计查询': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/line',
    'api_单方能耗统计查询': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/unitEnergyState',
    'api_能耗折碳排放趋势查询': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/energyToCarbon',
    'api_能耗折标煤趋势查询': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/energyToCoal',
    'api_分区用电占比查询': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/partitionColum',
    'api_分项用电占比查询': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/itemColum',
    'api_分区用电趋势查询': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/partitionTrend',
    'api_分项用电趋势查询': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/itemTrend',
    'api_分区用电排名查询': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/partitionEnergy',
    'api_查询能耗态势': f'{Configs.env_c.get("werun_pc_host")}/werun_energy_consumption/charts/energyTrend',


    #信息发布
    'api_新增素材': f'{Configs.env_c.get("werun_pc_host")}/ips/material/addBatch',
    'api_预览图片素材': f'{Configs.env_c.get("werun_pc_host")}/ips/material/',
    'api_素材集合查询': f'{Configs.env_c.get("werun_pc_host")}/ips/material/page',
    'api_下载素材': f'{Configs.env_c.get("werun_pc_host")}/wz_file/ossfile/imgPreview/',
    'api_通过id删除素材': f'{Configs.env_c.get("werun_pc_host")}/ips/material/',
    'api_通过id查询素材': f'{Configs.env_c.get("werun_pc_host")}/ips/material/',
    'api_上传图片素材': f'{Configs.env_c.get("werun_pc_host")}/wz_file/ossfile/upload',
    'api_上传音频素材': f'{Configs.env_c.get("werun_pc_host")}/wz_file/ossfile/upload',
    'api_上传视频素材': f'{Configs.env_c.get("werun_pc_host")}/wz_file/ossfile/upload',

    # 播放设备
    'api_新增播放设备': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities',
    'api_新增播放分组标签': f'{Configs.env_c.get("werun_pc_host")}/assets/tag',
    'api_修改播放分组标签': f'{Configs.env_c.get("werun_pc_host")}/assets/tag',
    'api_修改播放设备': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities',
    'api_查询播放设备分页列表': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/findCameraList',
    'api_根据facCode查询播放设备': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/getByFacCode/',
    'api_根据状态统计播放设备数据': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/getFacCountByStatus',
    'api_播放设备集合查询': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/list',
    'api_播放设备分页查询': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/page',
    'api_播放设备通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/',
    'api_播放分组标签通过id查询': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/pageWithTag',
    'api_播放设备通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/facilities/',
    'api_播放分组标签通过id删除': f'{Configs.env_c.get("werun_pc_host")}/assets/tag/',
    'api_播放设备打标签': f'{Configs.env_c.get("werun_pc_host")}/assets/facilitiestag/addList',
    'api_播放设备移除标签': f'{Configs.env_c.get("werun_pc_host")}/assets/facilitiestag/deleteList',

    #招商项目监测接口
    'api告警记录列表': f'{Configs.env_c.get("werun_pc_host")}/werun_alarm/record/page',




    #iot 登录页
    'api_IOT登录': f'{Configs.env_c.get("iot_host")}/CMAX/Default/Index',
    'api_IOT获取用户信息': f'{Configs.env_c.get("iot_host")}/CMAX/Core/UserInfo',
    #iot 子系统管理
    'api_IOT新增子系统': f'{Configs.env_c.get("iot_host")}/CMAX/SubSystem/Add',
    'api_IOT切换项目': f'{Configs.env_c.get("iot_host")}/CMAX/Core/ChangeProject',
    'api_IOT切换FRAME': f'{Configs.env_c.get("iot_host")}/CMAX/Home/Index_MainFrameTab',
    'api_IOT获取语言': f'{Configs.env_c.get("iot_host")}/CMAX/Core/GetLanguage',
    'api_IOT子系统分页查询': f'{Configs.env_c.get("iot_host")}/CMAX/api/API_SubSystem/GetList',
    'api_通过Code删除子系统': f'{Configs.env_c.get("iot_host")}/CMAX/SubSystem/SubSystem/Delete',
    #iot 模板管理
    'api_添加模板': f'{Configs.env_c.get("iot_host")}/CMAX/Templet/Add',
    'api_添加设备服务': f'{Configs.env_c.get("iot_host")}/CMAX/Templet/AddService',
    'api_添加设备属性': f'{Configs.env_c.get("iot_host")}/CMAX/Templet/AddProperty',
    'api_分页查询模板': f'{Configs.env_c.get("iot_host")}/CMAX/api/API_Device/AllTempletList',
    'api_分页查询设备服务': f'{Configs.env_c.get("iot_host")}/CMAX/api/API_Device/GetTempletServiceInfoList',
    'api_分页查询设备属性': f'{Configs.env_c.get("iot_host")}/CMAX/api/API_Device/GetTempletPropertyList',
    'api_通过id删除设备属性': f'{Configs.env_c.get("iot_host")}/CMAX/Device/Templet/DeleteProperty',
    'api_通过id删除设备服务': f'{Configs.env_c.get("iot_host")}/CMAX/Device/Templet/DeleteService',
    'api_通过id删除设备模板': f'{Configs.env_c.get("iot_host")}/CMAX/Device/Templet/Delete',
    #iot 产品管理
    'api_新增产品': f'{Configs.env_c.get("iot_host")}/CMAX/Product/Add',
    'api_分页查询产品': f'{Configs.env_c.get("iot_host")}/CMAX/api/API_Product/GetList',
    'api_通过id删除产品': f'{Configs.env_c.get("iot_host")}/CMAX/Product/Product/Delete',
    #iot 设备管理
    'api_新增注册设备': f'{Configs.env_c.get("iot_host")}/CMAX/Device/Add',
    'api_通过id删除注册设备': f'{Configs.env_c.get("iot_host")}/CMAX/Device/Device/Delete',
    'api_分页查询注册设备': f'{Configs.env_c.get("iot_host")}/CMAX/api/API_Device/AllSensorList',


    #iot gateway
    'api_GATEWAY登录': f'{Configs.env_c.get("iot_gateway_host")}/API_User/Login',
    'api_新增网关子系统': f'{Configs.env_c.get("iot_gateway_host")}/API_SubSystem/Add',
    'api_分页查询网关子系统': f'{Configs.env_c.get("iot_gateway_host")}/API_SubSystem/List',
    'api_查询待导入IOT设备': f'{Configs.env_c.get("iot_gateway_host")}/API_Device/Import',
    'api_分页查询设备': f'{Configs.env_c.get("iot_gateway_host")}/API_Device/List',
    'api_导入IOT设备': f'{Configs.env_c.get("iot_gateway_host")}/API_Device/Add',
    'api_添加监控点位': f'{Configs.env_c.get("iot_gateway_host")}/API_Device/AddTags',
    'api_更新点位数据': f'{Configs.env_c.get("iot_gateway_host")}/API_Tag/Edit',
    'api_分页查询监控点位': f'{Configs.env_c.get("iot_gateway_host")}/API_Tag/List',
    'api_重启子系统': f'{Configs.env_c.get("iot_gateway_host")}/API_G/reloadsubsystem',
    'api_重启网关': f'{Configs.env_c.get("iot_gateway_host")}/API_Gateway/RestartGateway',
    'api_通过id删除监控点位': f'{Configs.env_c.get("iot_gateway_host")}/API_Tag/Delete',
    'api_通过id删除设备': f'{Configs.env_c.get("iot_gateway_host")}/API_Device/Delete',
    'api_通过id删除网关子系统': f'{Configs.env_c.get("iot_gateway_host")}/API_SubSystem/Delete',
    'api_通过id删除网关子系统2': f'{Configs.env_c.get("iot_gateway_host2")}/gateway/manage/removesubsystem',
    'api_获取TOKEN': f'{Configs.env_c.get("iot_gateway_host")}/API_Gateway/getToken',


    #项目日志
    'api_项目日志分页查询': f'{Configs.env_c.get("werun_pc_host")}/wz_log/syslog/page',



}