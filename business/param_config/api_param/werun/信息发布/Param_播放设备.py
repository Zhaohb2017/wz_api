


#新增
p_add={
    '使用中':{"facCateCode":"类型编号ed3855e1-bddc-476c-8129-3b3d3abe1e1c","spaceId":99,"showFacImg":"","facCategoryId":137,"facName":"fdsafecafe","facCode":"fafecafdafef","assetStatus":"1","facLinkCode":"fasdfeafda","facBimCode":"efdafd","serviceLife":"123","facImportance":"afefad","brandName":"adsf","manufacturer":"asfds","modelName":"sadf","oldFacCode":"fdae","productDate":1640707200000,"firstStartDate":1640707200000,"warrantyEndDate":1641484800000,"remark":"faefda","supplierName":"sfefda","contractNo":"fdsafds","supplierPerson":"sfsadf","supplierPhone":"18566666666","purchasePrice":"123123"},
    '闲置中':{"facCateCode":"类型编号ed3855e1-bddc-476c-8129-3b3d3abe1e1c","spaceId":99,"showFacImg":"","facCategoryId":137,"facName":"fdsafecafe","facCode":"fafecafdafef","assetStatus":"3","facLinkCode":"fasdfeafda","facBimCode":"efdafd","serviceLife":"123","facImportance":"afefad","brandName":"adsf","manufacturer":"asfds","modelName":"sadf","oldFacCode":"fdae","productDate":1640707200000,"firstStartDate":1640707200000,"warrantyEndDate":1641484800000,"remark":"faefda","supplierName":"sfefda","contractNo":"fdsafds","supplierPerson":"sfsadf","supplierPhone":"18566666666","purchasePrice":"123123"},
}

#分页查询
p_page={
    '设备名称':{"body":{"facCategoryId":148,"facName":"设备名称"},"head":{"current":1,"size":10,"total":1}},
    '设备位置':{"body":{"buildingId":143,"buildingFloorId":1556,"buildingFloorSpaceId":116,"facCategoryId":148,"facName":"","building":[143,1556,116]},"head":{"current":1,"size":10,"total":1}},
    '运行状态':{"body":{"facCategoryId":148,"facName":"","building":[],"facStatus":"1"},"head":{"current":1,"size":10,"total":1}},
    '重置':{"head":{"total":0,"current":1,"size":10},"body":{"facCategoryId":151}},
}

#修改
p_upd = {
    '使用中':{"facCateCode":"类型编号ed3855e1-bddc-476c-8129-3b3d3abe1e1c","spaceId":131,"facImg":None,"id":309,"facName":"设备名称f65c89f5-7341-4324-b51c-043d09df9165","facCode":"设备编码4b0a2f93-1f4f-4531-9a26-11b174fd8eb2","facBimCode":"efdafdffdcafecaeds","facCategoryId":165,"facLinkCode":"fasdfeafdaasdf","assetStatus":"3","firstStartDate":1641571200000,"facImportance":"fdsafe","serviceLife":"22","manufacturer":"fecadf","brandName":"sdfef","modelName":"dfacd","oldFacCode":"fdadafe","productDate":1640620800000,"warrantyEndDate":1643817600000,"depreciatedYears":None,"systemId":None,"facQrcode":None,"supplierName":"sfefdafdsafe","contractNo":"fdsafdsdaf","purchasePrice":"123124","supplierPerson":"sfsadfdaf","supplierPhone":"18566666665","remark":"faefdafdafe","delFlag":0,"createdBy":1,"createdDate":1640759340390,"lastUpdatedBy":1,"lastUpdatedDate":1640759370697,"propertyId":187,"tenantId":None,"revision":None,"facIp":None,"facPort":None,"facLoginName":None,"facLoginPwd":None,"facType":None,"videoUrl":None,"facStatus":"1","openType":None,"validateCode":None,"buildingFloorSpaceName":"room 9b85012f-6870-11ec-afde-fc017c01a764","buildingName":"楼栋9b759d73-6870-11ec-ae4b-fc017c01a764","floorName":"-3","facCateParentName":None,"facCateName":"设备类型fb6bf9e2-9425-41de-a467-ade6a2c6e1f5","alarmId":None,"workOrderNo":None,"isExist":None,"createdByName":"walt","lastUpdatedByName":"walt"},
}

#新增分组
p_add_group={
    '视频播放设备':{"tagType":"fac_ips","propertyId":5,"tagName":"视频播放设备"}
}
#通过id查询分组
p_search_group={
    '视频播放设备':{"head":{"current":1,"size":10,"total":0},"body":{"tagId":198,"assetStatus":"","tagType":"fac_ips"}}
}

#修改分组信息
p_upd_group = {
    '01':{"tagType":"fac_ips","propertyId":5,"tagName":"11311","id":198}
}

#打标签
p_tag = {
    '设备打标签':{"facIdList": [6724], "tagIdList": [15]}
}