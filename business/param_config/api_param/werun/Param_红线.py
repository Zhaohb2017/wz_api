
#新增企业
p_add_qy = {
    '01':{"spaceId":269,"businessName":"sdffesadf","contactInformation":"18564545651","contactPerson":"asfsdf","enterTime":1642435200000,"remark":"123123123"},
}

#分页查询企业
p_page_qy = {
    '01':{"head":{"current":1,"size":10},"body":{"totalCount":0,"total":3,"businessName":"sdf"}},
}

#新增企业员工
p_add_qyyg = {
    '01':{"sword":"MYS8WLyVbe2DnR0v4s/T7oPuwB3wLFHTmVosrqWfWN/fDbzaMuS1VOnzf4pzUeLIOBAUQYQ7QxwTt2gRPMi+qV04vfcQpgXZLRfqPepzk1rs6LGDH5Z3RLQjnTg64Aa01pgYhmnpYEpL2otLuxGDCGy+MvfmticENpTExDLBf77fTFEzAhUO98RrnaHvRpE3r//XxYdEFFStbA3STGVIfaKv2/ECWK6zwFXGtLWFv25FRER8Q9WwcCHQFfdw99u0nYulP8kfb6fkQUS4u3up0aAABn5X0Wy7udyTZez1uBx3/Ophx2CMJybzcbxwrZCDAgxrfbhvRrF/euKoFVnB7w==","confirmSword":"BvDMGiQHDt9VQVfn+h7bBbW29uvhvBr+DkEFL7RBFH8W7fQM2TppMMOD1L6TOvR4EAa4Alg45hQ/dBRDrnTyd9+xg1B14m/2Yf3xrSYRM26SAZcs0PGMppvR+UvgN5wtuRJjVtBGT4HObDNVKnjv1LvmsGqkoCsDh69oTLMQFcSu1V2OOvmhbGH5e0ubDC4dfYKzeP1X2ljU0lV1/vBuoM1z1PsEmR6+wMfvDhf3M2+y11vr/zY66wmQfsv6H7zUvOW5c0661Iv8i5V6nftdsBW1Dy8LdEBSU4JAbhMVKNNgmJUtDOe+b0NzMuUNAswZgrl5A2WWJjLXAwAGx/9CDQ==","nickName":"dsafsdf","businessId":1,"scabbard":"root","mobile":"18564565456","email":"asdfasdfasdf@qq.com"},
}
#分页查询企业员工
p_page_qyyg = {
    '01':{"head":{"current":1,"size":10},"body":{"totalCount":0,"total":3,"nickName":"dsa"}},
}

#分页查询告警记录
p_page_gjjl = {
    '01':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":"","alarmType":"","alarmStatus":"1"}},
}

#安全告警配置新增
p_add_aqgj = {
    '01':{"blackName":"asdfds","alarmLevel":"1","gender":1,"remark":"fdsafsdfef","faceUrl":"535780978782633984"},
}

#分页查询安全告警配置
p_page_aqgj = {
    '01':{"head":{"current":1,"size":10,"total":5},"body":{"blackName":"asd"}},
}

#消防告警配置新增
p_add_xfgj = {
    '01':{"eventName":"fdsafdsfefda","alarmLevel":"1","configType":"2"},
}

#分页查询消防告警配置
p_page_xfgj = {
    '01':{"body":{"configType":"2"},"head":{"current":1,"size":10,"total":5}},
}

#设备告警配置新增
p_add_sbgj = {
    '01':{"configType":"2","eventName":"dsafsdffgdsaf","alarmLevel":"1","toWorkOrder":0,"remark":"fdsafsdgas","triggerInfoList":[{"triggerCondition":"1","facCategoryId":55,"triggerType":"1","triggerParamCustomList":[{"facParam":"ZNZMXT_ZMHL_KGZT","operator":"eq","thresholdStart":"50","triggerTime":"1"}],"facIdList":[{"id":329}],"facCamList":[{"facilities":{"id":329},"camList":[]}]}]},
}

#分页查询设备告警配置
p_page_sbgj = {
    '01':{"head":{"current":1,"size":10,"total":8},"body":{"facName":"","eventName":"dsa"}},
}

#应急预案新增
p_add_yjya = {
    '一级预案':{"name":"预案名称111","number":"编号111","level":1,"planStart":1644940800000,"planEnd":1645977600000,"content":"内容内容001"},
    '二级预案':{"name":"预案名称002","number":"预案编号002","level":2,"planStart":1645027200000,"planEnd":1645545600000,"content":"内容内容0023222"},
    '三级预案':{"name":"预案名称33","number":"预案编号33","level":3,"planStart":1645545600000,"planEnd":1646841600000,"content":"内容33333"},
}

#分页查询应急预案
p_page_yjya = {
    '01':{"head":{"current":1,"size":10,"total":21},"body":{"name":"afs"}},
}

#查询运行模式列表
p_list_yxms = {
    '01':{"idList":[1,2,5,8,9,10,11,12,13,14,15,16,17,18,19,20],"effectiveDateStart":1640966400000,"effectiveDateEnd":1643644799000},
}

#运行模式新增
p_add_yxms = {
    '01':{"effectiveDateStart":1642435200000,"effectiveDateEnd":1643817600000,"repeatDate":"","operationInfoList":[{"facId":"","operationFacType":"2","operationTime":"14:38","facCategoryId":6,"facOperationActionList":[{"actionName":"currentTemperature","actionValue":"13"}],"deviceParamsOptions":[{"label":"温度","value":"currentTemperature"},{"label":"水泵温度","value":"pumpTemperature"},{"label":"水管压力","value":"pipePressure"},{"label":"控制模式","value":"modeControl"},{"label":"报警状态","value":"alarmState"},{"label":"运行状态","value":"runningState"}]}],"modeName":"fdsafdsafdsaf","repeatRate":"daily","color":"#939393","remark":"fdsafsdf"},
}

#分页查询运行模式
p_page_yxms = {
    '01':{"head":{"current":2,"size":10},"body":{"head":{"total":0,"current":1,"size":10},"body":{"modeName":"fdsafd"}}},
}

#新增联动配置
p_add_ldpz = {
    '01':{"effectiveDateStart":1642435200000,"effectiveDateEnd":1643558400000,"repeatTimeStart":"15:05","repeatTimeEnd":"16:06","repeatDate":"","linkageInfoList":[{"facCategoryId":52,"deviceParamsOptions":[{"label":"手自动状态","value":"GPS_SB_SZD"},{"label":"启停状态","value":"GPS_SB_QT"},{"label":"故障状态","value":"GPS_SB_GZ"}],"linkageFacType":"2","linkageThresholdList":[{"facParam":"GPS_SB_SZD","operator":"eq","thresholdStart":"50","triggerType":"1"}],"linkageInfoFacList":None}],"linkageActionInfoList":[{"facCategoryId":6,"deviceParamsOptions":[{"label":"温度","value":"currentTemperature"},{"label":"水泵温度","value":"pumpTemperature"},{"label":"水管压力","value":"pipePressure"},{"label":"控制模式","value":"modeControl"},{"label":"报警状态","value":"alarmState"},{"label":"运行状态","value":"runningState"}],"operationFacType":"2","linkageActionList":[{"actionName":"pumpTemperature","actionValue":"30"}],"linkageActionInfoFacList":None}],"modeName":"dsafsafefdsafds","repeatRate":"daily","triggerCondition":"1","remark":"fdsafsdfsda"},
}

#分页查询联动配置
p_page_ldpz = {
    '01':{"head":{"current":2,"size":10},"body":{"head":{"total":0,"current":1,"size":10},"body":{"modeName":"dsaf"}}},
}

#修改工单配置
p_upd_gdpz = {
    '01':{"id":1,"timelinessRate":"50","arriveAddrTime":"2","finishedAfterVisitTime":"2","timeLimit":"2","dispatchConfig":1,"jspId":63},
}

#新增标准作业指导书
p_add_bzzyzds = {
    '01':{"sopVo":{"sopName":"fdsaffds","facCateId":55,"sopVersion":"1"},"sopContentVos":[{"sopContentName":"fdsafsdafsd","sopOperationContent":"<p>fsdafsdafsdafsd</p>"}]},
}

#分页查询标准作业指导书
p_page_bzzyzds = {
    '01':{"body":{"sopName":"fds"},"head":{"current":1,"size":10,"total":1}},
}

#新增故障现象
p_add_gzxx = {
    '01':{"manualName":"fdsafdsafdsfs","manualPriority":1,"facCateId":55,"manualType":2},
}

#分页查询故障现象
p_page_gzxx = {
    '01':{"body":{},"head":{"current":1,"size":10,"total":4}},
}

#新增故障原因
p_add_gzyy = {
    '01':{"manualId":16,"manualContentDescribe":"fdsafsda","manualContentSeverity":1,"manualType":2},
}

#分页查询故障原因
p_page_gzyy = {
    '01':{"body":{},"head":{"current":1,"size":10,"total":4}},
}

#新增解决方法
p_add_jjff = {
    '01':{"manualContentResolventHours":2,"manualId":16,"manualContentId":11,"manualContentResolventName":"fdsafdsafsdaf","manualType":2},
}

#分页查询解决方法
p_page_jjff = {
    '01':{"body":{},"head":{"current":1,"size":10,"total":1}},
}

#新增资料库
p_add_zlk = {
    '01':{"folderId":9,"filePath":"535870139959083008","fileFormat":"jpg","fileOriginalName":"autotest","fileSize":630,"fileName":"fdsafsda","fileVersion":"fdsafsdaf","remark":"asfsdafsadf"},
}

#分页查询资料库
p_page_zlk = {
    '01':{"body":{"folderId":9,"folderIds":"0,","fileName":"fdsa"},"head":{"current":1,"size":10,"total":0},"page":1,"rows":10,"pages":2,"total":12},
}

#新增企业保养手册
p_add_qybysc = {
    '01':{"maintenanceStandardVo":{"maintenanceStandardName":"fdafsdaf","facCateId":69,"cycle":"6","maintenanceStandardType":1},"maintenanceStandardContentVoList":[{"maintenanceStandardContentName":"fdsafsdaf","maintenanceStandardContentDescription":"sdfsadfsa","appPhotograph":1}]},
}

#分页查询企业保养手册
p_page_qybysc = {
    '01':{"body":{"maintenanceStandardType":1,"maintenanceStandardName":"fdafs"},"head":{"current":1,"size":10,"total":5}},
}

#新增巡检机房
p_add_xjjf = {
    '01':{"buildingId":6,"buildingFloorId":18,"buildingFloorSpaceId":269,"remark":"dfdsafdsafdsa","cameras":None,"envStandards":[{"standardEnvCheckId":32,"standardEnvId":13}],"facs":[{"inspectFacId":408,"inspectFacCateId":361,"inspectFlag":True},{"inspectFacId":537,"inspectFacCateId":80,"inspectFlag":True}]},
}

#分页查询巡检机房
p_page_xjjf = {
    '01':{"head":{"current":1,"size":10},"body":{"total":4,"machineRoomName":"1027"}},
}

#新增巡检计划
p_add_xjjh = {
    '01':{"planStart":1642521600000,"planEnd":1643471999000,"nums":[{"execStartTime":"08:00","execEndTime":"08:00","execOrder":0}],"repeatRate":"","rooms":[{"inspectRoomId":24,"remark":None,"orderNum":0}],"inspectPlanName":"fdsafdsafefdsa","inspectUser":15,"repeatRateType":"day","inspectWay":"0"},
}

#分页查询巡检计划
p_page_xjjh = {
    '01':{"head":{"current":1,"size":10},"body":{"total":1,"inspectPlanName":"fdsa"}},
}

#分页查询巡检任务
p_page_xjrw = {
    '01':{"head":{"current":1,"size":10},"body":{"range":[],"taskStatus":2},"taskStatus":2},
}

#新增巡逻标准
p_add_xlbz = {
    '01':{"propertyId":None,"patrolItemName":"fdsadsfsafds","remark":"fdsafsafdsa","standards":[{"itemStandard":"fdsafsdafsafe"}]},
}

#分页查询巡逻标准
p_page_xlbz = {
    '01':{"head":{"current":1,"size":10},"body":{"patrolItemName":"fdsa"}},
}

#新增巡逻区域
p_add_xlqy = {
    '01':{"propertyId":None,"cameras":[{"cameraId":261,"orderNum":1}],"checks":[{"patrolItemId":1,"itemStandardId":2},{"patrolItemId":1,"itemStandardId":13}],"patrolRangeName":"fdsafsdafdsaf","remark":"fdsafsadf"},
}

#分页查询巡逻区域
p_page_xlqy = {
    '01':{"head":{"current":1,"size":10},"body":{"patrolRangeName":"fdsa"}},
}

#新增巡逻区域
p_add_xljh = {
    '01':{"patrolPlanName":"fdsafdsafdsa","patrolUser":15,"repeatRateType":"day","planStart":1642435200000,"planEnd":1643904000000,"repeatRate":"","nums":[{"execStartTime":"00:00","execEndTime":"00:05"}],"ranges":[{"patrolRangeId":16}],"propertyId":None},
}

#分页查询巡逻区域
p_page_xljh = {
    '01':{"head":{"current":1,"size":10},"body":{"patrolPlanName":"fdsa"}},
}

#分页查询巡逻区域
p_page_xlrw = {
    '01':{"head":{"current":1,"size":10},"body":{"taskStatus":2}},
}

#实时监控配置
p_upd_ssjk = {
    '01':[{"cameraId":261,"sort":1}],
}

#新增授权列表
p_add_sqlb = {
    '01':{"propertyId":"5","userType":1,"mobile":"12334456567","authStartDate":"","authEndDate":"","remark":"123123","faceUrl":"","cardList":[],"authType":1,"userId":330,"neverExpires":1,"userName":"lxy","buildingId":6,"facIdList":[],"tagList":[{"facTagId":3,"facTagName":"4A门禁"}]},
}

#分页查询授权列表
p_page_sqlb = {
    '01':{"head":{"current":1,"size":10,"total":8},"body":{"city":None,"area":None,"userName":"lxy"}},
}

#分页查询通行记录
p_page_txjl = {
    '01':{"head":{"current":1,"size":10,"total":0},"body":{}},
}

#分页查询访客记录
p_page_fkjl = {
    '01':{"head":{"current":1,"size":10,"total":0},"body":{}},
}

#新增企业通行规则
p_add_qytxgz = {
    '01':{"passageRuleVo":{"passageType":1,"propertyId":5,"authType":2,"businessId":1,"buildingId":7,"supplierPerson":"李四","mobil":"15175521235","authStartDate":1642521600000,"authEndDate":1643558400000,"remark":"dsafsdafsda"},"facIdList":[537,422,408],"tagList":[]},
}

#分页查询授权列表
p_page_qytxgz = {
    '01':{"head":{"current":1,"size":10,"total":4},"body":{"startDate":"","endDate":"","businessId":1}},
}

#新增访客通行规则
p_add_fktxgz = {
    '01':{"passageRuleVo":{"passageType":2,"propertyId":5,"authType":1,"accessRange":1,"remark":None,"id":31},"facIdList":[],"tagList":[{"facTagId":3,"facTagName":"4A门禁"},{"facTagId":6,"facTagName":"4C门禁"},{"facTagId":9,"facTagName":"4D"}]},
}

#查询访客通行规则
p_get_fktxgz = {
    '01':{'propertyId':'5'},
}

