
#应急预案新增
p_add = {
    '一级预案': {"name": "预案名称111", "number": "编号111", "level": 1, "planStart": 1644940800000, "planEnd": 1645977600000,"content": "内容内容001"},
    '二级预案': {"name": "预案名称002", "number": "预案编号002", "level": 2, "planStart": 1645027200000, "planEnd": 1645545600000,"content": "内容内容0023222"},
    '三级预案': {"name": "预案名称33", "number": "预案编号33", "level": 3, "planStart": 1645545600000, "planEnd": 1646841600000,"content": "内容33333"},
}
#应急预案分页查询
p_page = {
    '预案等级':{"head":{"current":1,"size":10,"total":5},"body":{"level":1}},
    '预案名称':{"head":{"current":1,"size":10,"total":5},"body":{"name":"预案名称"}},
    '启用状态':{"head":{"current":1,"size":10,"total":5},"body":{"status":1}},
    '禁用状态':{"head":{"current":1,"size":10,"total":1},"body":{"status":0}},
}
#应急预案启用禁用
p_on_off = {
    '启用':{"id":62,"status":1},
    '禁用':{"id":28,"status":0},
}
#编辑修改应急预案
p_upd = {
    '01':{"id":66,"number":"预案编号002123123","name":"预案名称00212312","level":3,"planStart":1645545600000,"planEnd":1646150400000,"status":0,"content":"内容内容002322212312","createdBy":329,"createdDate":1644993850779,"lastUpdatedBy":329,"lastUpdatedDate":1644993850780,"delFlag":0,"propertyId":5,"propertyName":None,"tenantId":None,"revision":None,"createdName":None},
}