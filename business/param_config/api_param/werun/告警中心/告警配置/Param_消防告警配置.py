
#新增消防告警配置
p_add = {
    '紧急':{"eventName":"fdsafdsaf","alarmLevel":"1","configType":"2"},
    '严重':{"eventName":"fdsafdssds","alarmLevel":"2","configType":"2"},
    '一般':{"eventName":"fdsasdfeddd","alarmLevel":"3","configType":"2"},
    '轻微':{"eventName":"dfedafc","alarmLevel":"4","configType":"2"},
    '新增消防告警':{"eventName":"烟感告警","alarmLevel":1,"toWorkOrder":0,"remark":"","flag":"1","notificationIdList":[{"configType":3,"businessType":1,"notificationMethod":"0","personSource":"1","jobShedulingPlanIds":"469"}],"followIdList":[{"configType":3,"businessType":2,"personSource":"1","jobShedulingPlanIds":"469"}],"configType":"2"},
}
#分页查询
p_page = {
    '01':{"body":{"configType":"2"},"head":{"current":1,"size":10,"total":5}},
}
#消防告警配置启用-禁用
p_on_off = {
    '启用':{"id":126,"activeState":1},
    '禁用':{"id":126,"activeState":2},
}
#消防告警配置编辑修改
p_upd = {
    '01':{"id":143,"eventName":"dfedafcasdfsdf","alarmLevel":"3","activeState":2,"configType":"2","remark":None,"delFlag":0,"createdBy":329,"createdDate":1644990593458,"lastUpdatedBy":329,"lastUpdatedDate":1644991787110,"propertyId":5,"tenantId":None,"revision":None,"createdByName":None},
}

