

#新增设备告警配置
p_add = {
    '自定义具体设备':{"configType":"2","eventName":"告警事件名称","alarmLevel":"2","toWorkOrder":0,"remark":"asbcdfsaf123123","triggerInfoList":[{"triggerCondition":"1","facCategoryId":4171,"triggerType":"1","triggerParamCustomList":[{"facParam":"ZNZMXT_ZMHL_AUTOTEST","operator":"eq","thresholdStart":"45","triggerTime":"1"}],"facIdList":[{"id":1734}],"facCamList":[{"facilities":{"id":1734},"camList":[]}]}]},
    '自定义设备类型':{"configType":"2","eventName":"autoauto","alarmLevel":"1","toWorkOrder":0,"remark":"abcd1234 remark","triggerInfoList":[{"triggerCondition":"1","facCategoryId":4158,"triggerType":"2","triggerParamCustomList":[{"facParam":"ZNZMXT_ZMHL_AUTOTEST","operator":"eq","thresholdStart":"10","triggerTime":"1"}],"facIdList":[],"facCamList":[]}]},
    '自定义设备类型摄相头':{"configType":"2","eventName":"aabcdfds","alarmLevel":"3","toWorkOrder":0,"remark":"123asdf","triggerInfoList":[{"triggerCondition":"1","facCategoryId":4758,"triggerType":"1","triggerParamCustomList":[{"facParam":"ZNZMXT_ZMHL_AUTOTEST","operator":"gt","thresholdStart":"15","triggerTime":"2","triggerTimeInterval":15,"timeUnit":"1"}],"facIdList":[{"id":1964}],"facCamList":[{"facilities":{"id":1964},"camList":[{"id":1964}]}]}]},
    '系统具体设备':{"configType":"1","eventName":"abcabcasd","alarmLevel":"2","toWorkOrder":0,"remark":"a1234adf","triggerInfoList":[{"triggerCondition":"1","facCategoryId":4374,"triggerType":"1","triggerParamSysList":[{"alarmTriggerParam":"ZNZMXT_ZMHL_AUTOTEST"}],"facIdList":[{"id":1818}],"facCamList":[{"facilities":{"id":1818},"camList":[]}]}]},
    '系统设备类型':{"configType":"1","eventName":"abcabcab","alarmLevel":"4","toWorkOrder":1,"remark":"abdcabac","triggerInfoList":[{"triggerCondition":"1","facCategoryId":4371,"triggerType":"2","triggerParamSysList":[{"alarmTriggerParam":"ZNZMXT_ZMHL_AUTOTEST"}],"facIdList":[],"facCamList":[]}]},
}
#分页查询告警配置
p_page = {
    '设备系统':{"head":{"current":1,"size":10,"total":18},"body":{"facCategoryId":54}},
    '设备名称':{"head":{"current":1,"size":10,"total":19},"body":{"facName":"设备名称"}},
    '事件名称':{"head":{"current":1,"size":10,"total":18},"body":{"eventName":"告警名称"}},
    '重置':{"head":{"current":1,"size":10,"total":0},"body":{}},
    '默认查询':{"head":{"current":1,"size":10,"total":18},"body":{}},

}
#启用禁用设备告警配置
p_on_off = {
    '启用':{"id":2926,"activeState":1},
    '禁用':{"id":2926,"activeState":0},
}

p_upd = {
    '01':{"configType":"2","id":2934,"eventName":"告警名称abcd","alarmLevel":"4","toWorkOrder":1,"activeState":0,"remark":"备注asdfasfdsaf","delFlag":0,"createdBy":1520,"createdDate":1645525088556,"lastUpdatedBy":1520,"lastUpdatedDate":1645525096930,"propertyId":6897,"tenantId":None,"revision":None,"facCount":None,"facCateName":None,"facCateParentName":None,"createdByName":None,"triggerInfoList":[{"id":111,"triggerCondition":"1","facCategoryId":4383,"triggerType":"1","triggerParamCustomList":[{"id":102,"alarmFacConfigId":2934,"alarmTriggerInfoId":111,"facParam":"ZNZMXT_ZMHL_AUTOTEST","operator":"eq","thresholdStart":"13","thresholdEnd":None,"triggerTime":"1","triggerTimeInterval":None,"timeUnit":None,"remark":None,"delFlag":0,"createdBy":None,"createdDate":None,"lastUpdatedBy":None,"lastUpdatedDate":None,"propertyId":None,"tenantId":None,"revision":None}],"facIdList":[{"id":1826}],"facCamList":[{"facilities":{"id":1826},"camList":[]}]}]},
}