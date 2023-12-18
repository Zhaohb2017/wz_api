import os
from common.Common_Base import getByte


#新增
p_add = {
    '严重':{"blackName":"asdfds","alarmLevel":"1","gender":1,"remark":"fdsafsdfef","faceUrl":"535780978782633984"},
    '紧急':{"blackName":"fdsafdsafsa","alarmLevel":"2","gender":1,"remark":"asdfsdafasfd","faceUrl":"546271944580792320"},
    '一般':{"blackName":"asdfasdfdsf","alarmLevel":"3","gender":2,"remark":"asdfsafsda","faceUrl":"546272108410306560"},
    '轻微':{"blackName":"aafdsafsda","alarmLevel":"4","gender":1,"remark":"fdasfdsaf","faceUrl":"546291346269274112"},
    '布控人员': {"blackName":"测试111","alarmLevel":2,"gender":1,"faceUrl":"690200334231928832"},
}
#分页查询黑名单
p_page = {
    '标签名称':{"head":{"current":1,"size":10,"total":6},"body":{"blackName":"asdfa"}},
    '告警等级':{"head":{"current":1,"size":10,"total":6},"body":{"alarmLevel":"1"}},
    '默认查询':{"head":{"current":1,"size":10,"total":0},"body":{}},
}
#上传黑名单图片
p_upload = {
    '01':{'file':('autotest.jpg', getByte('{}/we_run/test_data/auto_image/autotest.jpg'.format(os.getcwd()))),'classify':'alarm','bizPath':'member'},

}

#启用禁用黑名单
p_on_off = {
    '启用':{"id":118,"activeState":1},
    '禁用':{"id":118,"activeState":0},
}
#编辑修改安全告警配置
p_upd = {
    '01':{"id":118,"blackName":"asdfdfdsfsd","gender":1,"alarmLevel":"2","activeState":0,"remark":"fsdfsafsdf","delFlag":0,"createdBy":329,"createdDate":1644977419926,"lastUpdatedBy":329,"lastUpdatedDate":1644981036740,"propertyId":5,"tenantId":None,"revision":None,"createdByName":None,"faceUrl":"546272108410306560"},
}
#新增安全告警-其它告警
p_add_o = {
    '严重':{"eventName":"fasdfdsafd","alarmLevel":"1","configType":"1"},
    '紧急':{"eventName":"afdsafdsaf","alarmLevel":"2","configType":"1"},
    '一般':{"eventName":"afddsafsdfds","alarmLevel":"3","configType":"1"},
    '轻微':{"eventName":"fdsafgdfafds","alarmLevel":"4","configType":"1"},
}
#其它告警-启用禁用
p_on_off_o = {
    '启用':{"id":126,"activeState":1},
    '禁用':{"id":126,"activeState":2},
}
#编辑修改其它告警
p_upd_o = {
    '01':{"id":126,"eventName":"fdsafgdfafdsfdsd","alarmLevel":"2","activeState":2,"configType":"1","remark":None,"delFlag":0,"createdBy":329,"createdDate":1644982146388,"lastUpdatedBy":329,"lastUpdatedDate":1644983650790,"propertyId":5,"tenantId":None,"revision":None,"createdByName":None},
}
