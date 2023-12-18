import os

#项目花名册
p_xmhmc = ['微筑', '杭州市', '下城区', '孙悟空', '13888888888', '客服', '2021/1/1 16:20:37', '2021/12/10 16:20:37']
p_xmhmc_list = [['微筑', '杭州市', '下城区', '孙悟空', '13888888888', '客服', '2021/1/1 16:20:37', '2021/12/10 16:20:37'],['微筑', '杭州市', '下城区', '孙悟饭', '13888888888', '客服', '2021/1/1 16:20:37', '2021/12/10 16:20:37']]

#新增
p_add = {
    '自动巡检':{"planStart":1642953600000,"planEnd":1646063999000,"nums":[{"execStartTime":"08:00","execEndTime":"08:01","execOrder":0}],"repeatRate":"","rooms":[{"inspectRoomId":67,"remark":"remark4dd03f1a-5da5-4e4a-8627-bf86c9b14e6f","orderNum":0}],"inspectUser":74,"inspectPlanName":"dlsajfldksjasaf","repeatRateType":"day","inspectWay":"0"},
    '手动巡检':{"planStart":1642953600000,"planEnd":1646841599000,"nums":[{"execStartTime":"08:00","execEndTime":"08:02","execOrder":0}],"repeatRate":"6","rooms":[{"inspectRoomId":67,"remark":"remark4dd03f1a-5da5-4e4a-8627-bf86c9b14e6f","orderNum":0}],"inspectPlanName":"fdsafdsafds","inspectUser":74,"inspectWay":"1","repeatRateType":"week"},
    '任务测试':{"planStart":1642953600000,"planEnd":1646841599000,"nums":[{"execStartTime":"08:00","execEndTime":"08:02","execOrder":0}],"repeatRate":"","rooms":[{"inspectRoomId":67,"remark":"remark4dd03f1a-5da5-4e4a-8627-bf86c9b14e6f","orderNum":0}],"inspectPlanName":"fdsafdsafds","inspectUser":74,"inspectWay":"1","repeatRateType":"day"},
}

#上传项目花名册人员
p_upload_hmc = {
    '01':{"fileName": 'xmhmc.xlsx',"file": ('xmhmc.xls',open('{}/we_run/test_data/excel/xmhmc.xlsx'.format(os.getcwd()), 'rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
}

#分页查询巡检计划
p_page = {
    '计划名称':{"head":{"current":1,"size":10},"body":{"total":1,"activeStatus":"","inspectPlanName":"计划名称"}},
    '巡检人员':{"head":{"current":1,"size":10},"body":{"total":1,"activeStatus":"","inspectUserName":"孙悟空"}},
    '启用状态':{"head":{"current":1,"size":10},"body":{"total":1,"activeStatus":1}},
    '禁用状态':{"head":{"current":1,"size":10},"body":{"total":1,"activeState":0}},
    '重置':{"head":{"current":1,"size":10},"body":{"total":0}},
}
#启用禁用
p_on_off = {
    '启用':{"id":55,"activeState":1},
    '禁用':{"id":55,"activeState":0},
}

p_upd = {
    '01':{"planStart":1642953600000,"planEnd":1646063999000,"nums":[{"execStartTime":"08:00","execEndTime":"09:50","execOrder":0}],"repeatRate":"2,3","rooms":[{"inspectRoomId":152,"remark":"remarkf28e8310-d076-4273-be1a-0e3faabc1b76","orderNum":0,"id":139,"inspectPlanId":139}],"id":139,"inspectPlanName":"计划名称ba187e3e-096c-4b9a-84f8-307c1cb43da7","activeState":0,"inspectUser":198,"schedulingPlanId":None,"userType":None,"repeatRateType":"week","inspectWay":"1","remark":None,"createdBy":4,"createdDate":1653879345337,"lastUpdatedBy":4,"lastUpdatedDate":1653879345381,"propertyId":2019},
}
