

#新增
p_add={
    '同级':{"orgName":"同级组织1231","remark":"remarkremark","dataRangeType":1,"level":"总公司","propertyIdList":[],"parentId":0,"propertyIds":"","propertyVoList":[],"citys":"","province":"140000","city":"0358","leaderUserIds":"","leaderUserNames":""},
    '下级':{"orgName":"下级组织01","remark":"remarkremark","dataRangeType":1,"level":"0","propertyIdList":[],"parentId":7945,"propertyIds":"","propertyVoList":[],"citys":"","province":"140000","city":"0354","leaderUserIds":"","leaderUserNames":""},
}
#新增下级
p_add_sub = {
    '区域公司':{"orgName":"asdf","remark":"asdfefasd","dataRangeType":1,"level":"0","propertyIdList":[],"parentId":73,"propertyIds":"","province":"210000","city":"210300","citys":"","leaderUserIds":"","leaderUserNames":""},
    '城市公司':{"orgName":"fdsafefda","remark":"faewfda","dataRangeType":1,"level":"1","propertyIdList":[],"parentId":44,"propertyIds":"","province":"310000","city":"310100","citys":"","leaderUserIds":"","leaderUserNames":""},
    '项目':{"orgName":"faefdsaf","remark":"feasdc","dataRangeType":1,"level":"2","propertyIdList":[],"parentId":44,"propertyIds":"","province":"120000","city":"120100","citys":"","leaderUserIds":"","leaderUserNames":""},
    '部门':{"orgName":"facafe","remark":"afecafe","dataRangeType":1,"level":"3","propertyIdList":[],"parentId":44,"propertyIds":"","province":"230000","city":"230300","citys":"","leaderUserIds":"","leaderUserNames":""},
}
#修改
p_upd = {
    '同级':{"id":41,"companyCode":None,"orgCode":"6c25f3ce52aa4865980830858c8c3c66","orgName":"sdafasdf","parentIds":None,"sort":None,"establishedTime":None,"leaderUserNames":"","dataRangeType":1,"remark":"asdfasdfasdfdf","delFlag":0,"createdBy":1,"createdDate":1640159290423,"lastUpdatedBy":1,"lastUpdatedDate":1640159290423,"propertyId":5,"tenantId":None,"revision":None,"parentName":None,"cityName":"天津","provinceName":"天津市","responsePropertyName":None,"propertyVoList":None,"propertyIds":"","propertyIdList":[],"level":"总公司","parentId":0,"province":"130000","city":"130200","citys":"","leaderUserIds":""},
    '下级':{"id":49,"companyCode":None,"orgCode":"83f535b665a34fca97be31353ff9df7e","orgName":"asdfsdafsdsdf","parentIds":None,"sort":None,"establishedTime":None,"leaderUserNames":"","dataRangeType":1,"remark":"feafddasd","delFlag":0,"createdBy":1,"createdDate":1640160982899,"lastUpdatedBy":1,"lastUpdatedDate":1640160982899,"propertyId":5,"tenantId":None,"revision":None,"parentName":"sdafasdf","cityName":"赤峰市","provinceName":"内蒙古自治区","responsePropertyName":None,"propertyVoList":None,"propertyIds":"","propertyIdList":[],"level":"3","parentId":41,"province":"150000","city":"150400","citys":"","leaderUserIds":""},
}
#变更组织机构，使用用户负责项目
p_upd_org = {
    '01':{"id":7949,"companyCode":None,"orgCode":"d9c3467942f44580bebe0fa7926b815e","orgName":"orgName 908cbcb2-e6df-451e-be2a-de56d65f0877","parentIds":None,"sort":None,"establishedTime":None,"leaderUserNames":"nickNamea7cc57e6-f3e1-4e9b-b8b2-62a771d2c564","dataRangeType":3,"remark":"remarkremark01","delFlag":0,"createdBy":1817,"createdDate":1651127176117,"lastUpdatedBy":1817,"lastUpdatedDate":1651127176117,"propertyId":31717,"tenantId":None,"revision":None,"parentName":None,"cityName":"Lvliang","provinceName":"Shanxi","responsePropertyName":None,"level":"总公司","propertyIdList":[],"parentId":0,"propertyIds":"31717","propertyVoList":[{"propertyId":31717,"cityName":"Haerbin","propertyName":"项目19411ce1-c6bc-11ec-8625-fc017c01a764","orgId":None,"beResponsibleFor":True}],"citys":"","province":"140000","city":"0358","leaderUserIds":"4817"},
}