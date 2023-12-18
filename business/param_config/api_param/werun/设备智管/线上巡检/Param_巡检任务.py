

#分页查询
p_page = {
    '任务名称':{"head":{"current":1,"size":10},"body":{"range":[],"taskStatus":2,"inspectTaskName":"计划名称"},"taskStatus":2},
    '负责人':{"head":{"current":1,"size":10},"body":{"range":[],"taskStatus":2,"execUserName":"悟空","inspectTaskName":""},"taskStatus":2},
    '自动巡检':{"head":{"current":1,"size":10},"body":{"range":[],"taskStatus":2,"execUserName":"","inspectTaskName":"","inspectWay":"0"},"taskStatus":2},
    '人工巡检':{"head":{"current":1,"size":10},"body":{"range":[],"taskStatus":2,"execUserName":"","inspectTaskName":"","inspectWay":"1"},"taskStatus":2},
    '全部':{"head":{"current":1,"size":10},"body":{"range":[],"taskStatus":None},"taskStatus":None},
    '重置':{"head":{"current":1,"size":10},"body":{},"taskStatus":2},
}
#执行房间确认
p_done_task_room = {
    '01':{"id":4436,"inspectTaskId":1841,"remark":None,"envs":[{"id":7766,"taskRoomId":4436,"taskEnvId":127,"taskEnvCheckName":"检查内容bf4046d2-6370-4f3a-ab58-c66b5cede138","taskEnvResult":1,"envCheckTime":None,"envCheckUser":None,"remark":None,"delFlag":0,"createdBy":None,"createdDate":1643274440562,"lastUpdatedBy":None,"lastUpdatedDate":None,"propertyId":2282,"tenantId":None,"revision":None}],"facs":[{"id":27489,"taskRoomId":4436,"facCateCode":None,"facCateId":1442,"facId":836,"facCode":None,"taskFacResult":1,"facInspectTime":None,"facInspectUser":None,"remark":None,"delFlag":0,"createdBy":None,"createdDate":1643274440564,"lastUpdatedBy":None,"lastUpdatedDate":None,"propertyId":2282,"facCateName":"设备类型dc02182c-7525-4ddf-a234-e647fc37570a","facName":"设备名称bdecda36-be68-4ef7-973f-b9b4c3b3e8e7","attrs":None}]},
}
#执行任务结果
p_done_task = {
    '01':{'inspectTaskId':'1891','taskRoomId':'4549'},
}
#确认巡检完成
p_done = {
    '01':{"completeSignUser":"孙悟空","id":"1891"},
}
#转告警
p_alarm = {
    '安全':{"facId":862,"alarmType":"2","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称2ef69322-d56b-4ac3-b52e-8d862c0dd196黑名单告警","alarmLevel":"1","remark":"remarkremark","alarmSubType":"bl","alarmConfigId":42},
    '消防':{"facId":862,"alarmType":"3","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称2ef69322-d56b-4ac3-b52e-8d862c0dd196消防配置60e4abda061a","alarmLevel":"1","remark":"asdfsadfsaf","alarmSubType":"f","alarmConfigId":""},
    '设备':{"facId":2103,"alarmType":"1","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称e4525f4b-cf0f-4e39-a69d-a2d3705f9571告警名称59083469-8056-4786-af06-85d46b9ea229","alarmLevel":"2","remark":"abcfreafsadfsadf","alarmSubType":"","alarmOperate":{"operateType":"1","operateMobil":"13888888888","operatorName":"孙悟空"}},
}
#任务转派
p_rwzp={
    '01':{"id":2274,"execUserId":103},
}