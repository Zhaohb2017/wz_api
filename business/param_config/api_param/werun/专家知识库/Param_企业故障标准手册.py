

#新增指导书
p_add_gzxx = {
    '优先级1':{"manualName":"自动化脚本","manualPriority":1,"facCateId":68083,"manualType":2},
    '优先级2':{"manualName":"fdsafdsaf","manualPriority":1,"facCateId":388,"manualType":2},
    '优先级3':{"manualName":"fdsafdsaf","manualPriority":1,"facCateId":388,"manualType":2},
    '优先级4':{"manualName":"fdsafdsaf","manualPriority":1,"facCateId":388,"manualType":2},
}
#编辑修改故障现象
p_upd_gzxx = {
    '01':{"id":48,"manualType":2,"manualCode":"e31bcffb3a6740ce99f553c421a11317","manualName":"自动化脚本","manualVersion":None,"manualCycle":None,"manualFrequency":None,"manualHours":None,"manualPriority":3,"remark":None,"facCateId":75},
}

#分页查询故障原因
p_query_gzyy= {
    "默认查询": {"body":{},"head":{"current":1,"size":10}}
}

#分页查询故障现象
p_query_gzxx = {
"默认查询": {"body":{},"head":{"current":1,"size":20,"total":5}}
}
#分页查询解决方法
p_query_jjff = {
"01":{"body":{},"head":{"current":1,"size":10}}
}


#新增故障原因
p_add_gzyy = {
    '较轻':{"manualId":48,"manualContentDescribe":"asdfsdfasdf","manualContentSeverity":1,"manualType":2},
    '一般':{"manualId":54,"manualContentDescribe":"我是自动化脚本执行","manualContentSeverity":2,"manualType":2},
    '严重':{"manualId":54,"manualContentDescribe":"adsfsafdsaf","manualContentSeverity":3,"manualType":2},
}
#编辑修改故障原因
p_upd_gzyy = {
    '01':{"id":49,"manualId":54,"manualType":2,"manualContentCode":"4e1ccc9838f2489eadce79702c696a01","manualContentName":None,"manualContentDescribe":"asdfsdafsda","manualContentSeverity":3,"manualContentCycle":None,"manualContentFrequency":None,"manualContentHours":None,"remark":None},
}
#新增解决方法
p_add_jjff = {
    '带工时':{"manualContentResolventHours":12,"manualId":54,"manualContentId":19,"manualContentResolventName":"这是脚本制造带工时","manualType":2},
    '不带工时':{"manualId":48,"manualContentId":20,"manualContentResolventName":"这是脚本制造不带工时","manualType":2},
}
#编辑修改解决方法
p_upd_jjff = {
    '01':{"id":14,"manualId":19,"manualContentId":20,"manualContentResolventCode":"c2f24f967dd844729d70eab53879ad06","manualContentResolventName":"更换开关asdf","manualContentResolventHours":2,"remark":None,"manualType":2},
}

p_set_jjff = {
"默认":{"manualType":2}
}