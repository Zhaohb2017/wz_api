

#列表查询
p_list = {
    '用电':{'parentId':'','energyType':'electricity'},
    '用水':{'parentId':'','energyType':'water'},
    '用气':{'parentId':'','energyType':'gas'},
}
#新增分区
p_add_fq = {
    '01':{"partitionName":"fdfwsd","itemName":"","energyType":"electricity","propertyId":"497","level":1},
}
#修改分区
p_upd_fq = {
    '01':{"partitionName":"sdaef","itemName":"","energyType":"electricity","propertyId":"497","id":15,"level":1},
}

p_add_zb = {
    '楼栋':{"normName":"指标名称123","partitionId":3194,"normUnit":"1","normAggregation":"1","facs":[{"id":237,"createdBy":4,"createdDate":1654742945090,"lastUpdatedBy":4,"lastUpdatedDate":1654742945090,"facId":15403,"facCode":"设备编码9a930088-ea7b-4e14-97af-0e4d1b2d1657","facName":"设备名称b8e5c5c4-53f2-4a51-b8d8-22015732bcf6","facCateId":45542,"facCategoryName":"类型名称b1ce4ee5-496a-401f-bf64-6847894f60f7","attrCode":"DBPJ","delFlag":False,"propertyId":6340,"tenantId":None,"revision":None,"attrValue":0,"facDataType":0,"latestReadingTime":None,"strId":"237","bizName":"ENERGY_MEASUREMENT_FACILITIES_VO"}],"partitionName":"楼栋b951da5c-e79e-11ec-921c-fe017c01a763","facIds":"15403","partitionType":"building","propertyId":"6340"},
    '楼层':{"normName":"指标名称-楼层","partitionId":41496,"normUnit":"1","normAggregation":"2","facs":[{"id":250,"createdBy":4,"createdDate":1654753744062,"lastUpdatedBy":4,"lastUpdatedDate":1654753744062,"facId":15418,"facCode":"设备编码dc270acd-2820-4106-85b1-743ee3b953fb","facName":"设备名称b44b4ab2-4d3a-40e2-90cc-0dde69b757ab","facCateId":45568,"facCategoryName":"类型名称e95b03eb-eb7b-4eeb-a042-855898750122","attrCode":"DBPJ","delFlag":False,"propertyId":6353,"tenantId":None,"revision":None,"attrValue":0,"facDataType":0,"latestReadingTime":None,"strId":"250","bizName":"ENERGY_MEASUREMENT_FACILITIES_VO"}],"partitionName":"-3","facIds":"15418","partitionType":"floor","propertyId":"6353"},
    '新建分区':{"normName":"指标名称-分区","partitionId":21,"normUnit":"1","normAggregation":"3","facs":[{"id":255,"createdBy":4,"createdDate":1654756529668,"lastUpdatedBy":4,"lastUpdatedDate":1654756529668,"facId":15424,"facCode":"设备编码607c1c9c-1ef6-46e2-81ca-4e9f68bf7eb3","facName":"设备名称700ab709-2c4f-41ff-beb0-bab7bed973ce","facCateId":45580,"facCategoryName":"类型名称3f7a0885-6e0f-4a1e-a502-d9e67640c9aa","attrCode":"DBPJ","delFlag":False,"propertyId":6359,"tenantId":None,"revision":None,"attrValue":0,"facDataType":0,"latestReadingTime":None,"strId":"255","bizName":"ENERGY_MEASUREMENT_FACILITIES_VO"}],"partitionName":"分区名称70f46055-1dbb-47cd-ba4a-7161ba35012d","facIds":"15424","partitionType":"custom","propertyId":"6359"},
    '房间分区':{"normName":"指标名称-房间","partitionId":6331,"normUnit":"1","normAggregation":"1","facs":[{"id":595,"createdBy":4,"createdDate":1655975860816,"lastUpdatedBy":4,"lastUpdatedDate":1655975860816,"facId":18146,"facCode":"设备编码410446a7-0b29-4b41-99e3-d37e9ae3ca58","facName":"设备名称d36ea037-08f5-4dde-9b46-76e4ee9ce4db","facCateId":52784,"facCategoryName":"类型名称07f03a57-0fa3-4624-9642-28a7f6fa7c99","attrCode":"DBPJ","delFlag":False,"propertyId":13582,"tenantId":None,"revision":None,"attrValue":0,"facDataType":0,"latestReadingTime":None,"strId":"595","bizName":"ENERGY_MEASUREMENT_FACILITIES_VO"}],"partitionName":"room 548dad6c-f2d5-11ec-9e5f-fc017c01a764","facIds":"18146","partitionType":"room","propertyId":"13582"},
}

p_search_zb = {
    'custom':{"partitionId":18,"propertyId":"497","partitionType":"custom"},
    'building':{"partitionId":18,"propertyId":"497","partitionType":"building"},
    'floor':{"partitionId":41522,"propertyId":"6355","partitionType":"floor"},
}