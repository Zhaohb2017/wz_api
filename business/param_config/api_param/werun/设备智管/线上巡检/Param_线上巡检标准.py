

#新增
p_add = {
    '通用标准':{"facCateId":55,"remark":"fdsafsdfdas","specials":[],"normals":[{"attrCode":"ZNZMXT_ZMHL_KGZT","attrCondition":"eq","attrVal":10,"attrId":73,"inspectFlag":True},{"attrCode":"ZNZMXT_ZMHL_YXMS","attrCondition":"gt","attrVal":11,"attrId":74,"inspectFlag":False},{"attrCode":"FGZMXT_ZMHL_KGZT","attrCondition":"lt","attrVal":9,"attrId":75,"inspectFlag":True},{"attrCode":"FGZMXT_ZMHL_YXMS","attrCondition":"ge","attrVal":9,"attrId":76,"inspectFlag":False}]},
    '个性化标准':{"facCateId":55,"remark":"sdafdsafsdaf","specials":[{"facNames":"1#灯光","facCodes":"LIGHT001","facIds":"329","attrs":[{"attrVal":30,"attrId":74,"attrCondition":"lt"}]}],"normals":[{"attrCode":"ZNZMXT_ZMHL_KGZT","attrCondition":"le","attrVal":50,"attrId":73,"inspectFlag":True},{"attrCode":"ZNZMXT_ZMHL_YXMS","attrCondition":"eq","attrVal":300,"attrId":74,"inspectFlag":True},{"attrCode":"FGZMXT_ZMHL_KGZT","attrCondition":"it","attrVal":"50,60","attrId":75,"inspectFlag":True},{"attrCode":"FGZMXT_ZMHL_YXMS","attrCondition":"lt","attrVal":30,"attrId":76,"inspectFlag":True}]},
    '环境标准单条':{"spaceId":300,"remark":"remmmmmmmmm","checks":[{"checkContent":"asfdsafdsafsad"}]},
    '环境标准多条':{"spaceId":300,"remark":"fdsafdsafdsaf","checks":[{"checkContent":"fdsafdsgsdafsda"},{"checkContent":"hfdsgdfs"}]},
}

#分页查询
p_page = {
    '设备类型':{"head":{"current":1,"size":10},"body":{"total":1,"facCateId":55}},
    '启用状态':{"head":{"current":1,"size":10},"body":{"total":1,"facCateId":None,"activeState":1}},
    '禁用状态':{"head":{"current":1,"size":10},"body":{"total":2,"activeState":0}},
    '重置':{"head":{"current":1,"size":10},"body":{"total":0}},
    '环境空间类型':{"head":{"current":1,"size":10},"body":{"total":1,"spaceId":303}},
    '环境启用':{"head":{"current":1,"size":10},"body":{"total":1,"spaceId":None,"activeState":1}},
    '环境禁用':{"head":{"current":1,"size":10},"body":{"total":1,"spaceId":None,"activeState":0}},
    '环境重置':{"head":{"current":1,"size":10},"body":{"total":0}},
}
#启用禁用
p_on_off = {
    '启用':{"id":21,"activeState":1},
    '禁用':{"id":21,"activeState":0},
}
#编辑修改
p_upd = {
    '01':{"id":36,"facCateId":55,"remark":"fdsafsdf","specials":[{"id":11,"facStandardId":36,"facCodes":"LIGHT001","facIds":"329","remark":None,"createdBy":None,"createdDate":None,"lastUpdatedBy":None,"lastUpdatedDate":None,"propertyId":5,"facNames":"1#灯光","attrs":[{"id":9,"standardSpecialId":11,"attrCode":None,"attrId":218,"attrVal":88,"attrCondition":"ge","remark":None,"delFlag":0,"createdBy":None,"createdDate":None,"lastUpdatedBy":None,"lastUpdatedDate":None,"propertyId":5,"tenantId":None,"revision":None}]}],"normals":[{"attrCode":"ZNZMXT_ZMHL_KGZT","attrCondition":"gt","attrVal":50,"facStandardId":36,"attrId":216,"inspectFlag":True},{"attrCode":"ZNZMXT_ZMHL_YXMS","attrCondition":"lt","attrVal":51,"facStandardId":36,"attrId":217,"inspectFlag":True},{"attrCode":"FGZMXT_ZMHL_KGZT","attrCondition":"le","attrVal":52,"facStandardId":36,"attrId":218,"inspectFlag":True},{"attrCode":"FGZMXT_ZMHL_YXMS","attrCondition":"ge","attrVal":53,"facStandardId":36,"attrId":219,"inspectFlag":True}]},
    '环境':{"id":31,"spaceId":310,"remark":"fdsagdsafdsaf","checks":[{"id":60,"envId":31,"checkContent":"fdsafdsafdsafds","remark":None,"delFlag":0,"createdBy":None,"createdDate":None,"lastUpdatedBy":None,"lastUpdatedDate":None,"propertyId":1453,"tenantId":None,"revision":None}]},
}