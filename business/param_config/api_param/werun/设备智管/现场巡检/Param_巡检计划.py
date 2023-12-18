

#新增
p_add = {
    '排班计划':{"scheduleName":"dsafefads","scheduleTime":"2","schPointIdList":[10],"termOfValidityStart":1735660800000,"termOfValidityEnd":1738252800000,"scheduleCycle":1,"dispatchType":1,"facCateId":54,"jspId":15,"scheduleAdvanceTime":3,"personInChargeUserId":None,"scheduleContent":"","scheduleExcuteMwTime":"00:25"},
    '指定负责人':{"scheduleName":"faedsac","scheduleTime":"12","schPointIdList":[11],"termOfValidityStart":1735660800000,"termOfValidityEnd":1738252800000,"scheduleCycle":2,"dispatchType":2,"facCateId":54,"jspId":None,"scheduleAdvanceTime":3,"scheduleExcuteHmTime":"00:20","personInChargeUserId":1,"scheduleContent":"fdsafefda","personInChargeUserName":"walt","scheduleExcuteMwTime":"4"},
    '执行任务计划':{"scheduleName":"线下巡检计划","scheduleTime":"1.5","schPointIdList":[1858],"termOfValidityStart":1651852800000,"termOfValidityEnd":1652976000000,"scheduleCycle":1,"dispatchType":2,"facCateId":30870,"jspId":None,"scheduleAdvanceTime":1,"personInChargeUserId":1817,"scheduleContent":"工作内容remark","personInChargeUserName":"lichang1","scheduleExcuteMwTime":"05:00"},
    '两个巡检点':{"scheduleName":"sd","scheduleTime":"2","schPointIdList":[17,11],"termOfValidityStart":1735660800000,"termOfValidityEnd":1738252800000,"scheduleCycle":3,"dispatchType":1,"facCateId":77,"jspId":15,"scheduleAdvanceTime":3,"scheduleExcuteHmTime":"04:05","personInChargeUserId":None,"scheduleContent":"","scheduleExcuteMwTime":"5"},
}

#修改
p_upd = {
    '01':{"scheduleName":"巡检计划487fe658-2bba-4014-b0a0-6b6b60e66076asfdsf","scheduleTime":"12","schPointIdList":[536],"termOfValidityStart":1735660800000,"termOfValidityEnd":1738252800000,"scheduleCycle":2,"dispatchType":2,"facCateId":9077,"jspId":None,"scheduleAdvanceTime":3,"scheduleExcuteHmTime":"00:20","personInChargeUserId":2569,"scheduleContent":"remark123123","id":95,"scheduleExcuteMwTime":"4"},
}

#分页查询
p_page = {
    '巡检类型':{"head":{"current":1,"size":10},"body":{"startDate":"","endDate":"","facCateId":54,"totalCount":0,"total":0}},
    '巡检时间':{"head":{"current":1,"size":10},"body":{"startDate":1735660800000,"endDate":1738252800000,"totalCount":0,"total":0}},
    '巡检名称':{"head":{"current":1,"size":10},"body":{"startDate":"","endDate":"","totalCount":0,"total":1,"scheduleName":"巡检计划"}},
    '负责人':{"head":{"current":1,"size":10},"body":{"startDate":"","endDate":"","totalCount":0,"total":1,"scheduleName":"","personInChargeUserId":287}},
    '当前状态':{"head":{"current":1,"size":10},"body":{"startDate":"","endDate":"","totalCount":0,"total":1,"scheduleName":"","statusStr":"2"}},
    '巡检类型And巡检名称':{"head":{"current":1,"size":10},"body":{"startDate":"","endDate":"","facCateId":277,"totalCount":0,"total":1,"scheduleName":"巡检计划"}},
    '重置':{"head":{"current":1,"size":10},"body":{"startDate":"","endDate":"","totalCount":0}},
}

#启用禁用
p_open_close = {
    '启用':{"id":28,"scheduleStatus":1},
    '禁用':{"id":28,"scheduleStatus":2},
}