

#新增分项
p_add_fx = {
    '用电':{"partitionName":"","itemName":"分项名称123","energyType":"electricity","propertyId":"497","level":1},
    '用水':{"partitionName":"","itemName":"分项名称123","energyType":"water","propertyId":"497","level":1},
    '用气':{"partitionName":"","itemName":"分项名称123","energyType":"gas","propertyId":"497","level":1},
}

#分项分页查询
p_list_fx = {
    '用电':{'energyType':'electricity','propertyId':'497'},
    '用水':{'energyType':'water','propertyId':'497'},
    '用气':{'energyType':'gas','propertyId':'497'},
}
#修改分项名称
p_upd_fx = {
    '用电':{"partitionName":"","itemName":"测试123","energyType":"electricity","propertyId":"497","id":19,"level":1},
}
#新增指标
p_add_zb = {
    '新建分项':{"normName":"指标名称123","partitionId":33,"normUnit":"1","normAggregation":"4","facs":[{"id":296,"createdBy":4,"createdDate":1655090164451,"lastUpdatedBy":4,"lastUpdatedDate":1655090164451,"facId":15984,"facCode":"设备编码997a7877-9f45-4d63-8ee6-afdc7f001713","facName":"设备名称5d4b14a3-37d9-4a3c-b57e-4348bf66101a","facCateId":47087,"facCategoryName":"类型名称425b9687-5dfe-48ef-b196-ca228ca88ef6","attrCode":"DBPJ","delFlag":False,"propertyId":7886,"tenantId":None,"revision":None,"attrValue":0,"facDataType":0,"latestReadingTime":None,"strId":"296","bizName":"ENERGY_MEASUREMENT_FACILITIES_VO"}],"partitionName":"分项名称669bea2d-3506-48b2-b7c3-26fd00900bd8","itemId":33,"facIds":"15984","propertyId":"7886"},
}
#查询分项指标
p_search_zb = {
    'custom':{"itemId":33,"propertyId":"7886"},
}