import os


#新增
p_add={
    '使用中':{"facCateCode":"类型编号ed3855e1-bddc-476c-8129-3b3d3abe1e1c","spaceId":99,"showFacImg":"","facCategoryId":137,"facName":"fdsafecafe","facCode":"fafecafdafef","assetStatus":"1","facLinkCode":"fasdfeafda","facBimCode":"efdafd","serviceLife":"123","facImportance":"afefad","brandName":"adsf","manufacturer":"asfds","modelName":"sadf","oldFacCode":"fdae","productDate":1640707200000,"firstStartDate":1640707200000,"warrantyEndDate":1641484800000,"remark":"faefda","supplierName":"sfefda","contractNo":"fdsafds","supplierPerson":"sfsadf","supplierPhone":"18566666666","purchasePrice":"123123"},
    '闲置中':{"facCateCode":"类型编号ed3855e1-bddc-476c-8129-3b3d3abe1e1c","spaceId":99,"showFacImg":"","facCategoryId":137,"facName":"fdsafecafe","facCode":"fafecafdafef","assetStatus":"3","facLinkCode":"fasdfeafda","facBimCode":"efdafd","serviceLife":"123","facImportance":"afefad","brandName":"adsf","manufacturer":"asfds","modelName":"sadf","oldFacCode":"fdae","productDate":1640707200000,"firstStartDate":1640707200000,"warrantyEndDate":1641484800000,"remark":"faefda","supplierName":"sfefda","contractNo":"fdsafds","supplierPerson":"sfsadf","supplierPhone":"18566666666","purchasePrice":"123123"},
}

#分页查询
p_page={
    '设备名称':{"body":{"facCategoryId":148,"facName":"设备名称"},"head":{"current":1,"size":10,"total":1}},
    '设备位置':{"body":{"buildingId":143,"buildingFloorId":1556,"buildingFloorSpaceId":116,"facCategoryId":148,"facName":"","building":[143,1556,116]},"head":{"current":1,"size":10,"total":1}},
    '运行状态':{"body":{"facCategoryId":148,"facName":"","building":[],"facStatus":"2"},"head":{"current":1,"size":10,"total":1}},
    '资产状态':{"body":{"facCategoryId":148,"facName":"","building":[],"facStatus":"","assetStatus":"1"},"head":{"current":1,"size":10,"total":1}},
    '重置':{"head":{"total":0,"current":1,"size":10},"body":{"facCategoryId":151}},
    '默认查询': {"head":{"total":0,"current":1,"size":10},"body":{}},

}

#修改
p_upd = {
    '使用中':{"facCateCode":"类型编号4480bad4-6c00-421a-b68d-b5244cba6ce6","spaceId":16269,"facImg":None,"id":11718,"facName":"设备名称e9f5c5d0","facCode":"设备编码13050d99-cebf-","facBimCode":"efdafd1","facCategoryId":35885,"parentIds":"0,35884,","facLinkCode":"fasdfeafda1","facLinkPlatform":None,"assetStatus":3,"firstStartDate":1640707200000,"facImportance":"afefad1","serviceLife":"1231","manufacturer":"asfds1","brandName":"adsf1","modelName":"sadf1","oldFacCode":"fdae1","productDate":1640707200000,"warrantyEndDate":1641484800000,"depreciatedYears":None,"systemId":None,"systemCode":"F11","facQrcode":"{\"buildingName\":\"楼栋db48c778-d651-11ec-b0b7-fc017c01a764\",\"buildingFloorSpaceName\":\"room db558ea5-d651-11ec-af03-fc017c01a764\",\"buildingFloorSpaceId\":16268,\"facCateName\":\"设备类型ee47d2f7-93eb-424b-bf6a-bd9ae450d8f5\",\"facName\":\"设备名称e9f5c5d0-d1f4-4bcc-8ca4-4e525eccdb32\",\"qrCodeType\":\"facilities\",\"floorName\":\"-3\",\"id\":11718,\"propertyId\":40875,\"facCategoryId\":35885}","supplierName":"sfefda1","contractNo":"fdsafds1","purchasePrice":"123121","supplierPerson":"sfsadf1","supplierPhone":"18566666661","remark":"faefda1","delFlag":0,"createdBy":1817,"createdDate":1652840761138,"lastUpdatedBy":1817,"lastUpdatedDate":1652840761138,"propertyId":40875,"tenantId":None,"revision":None,"measureFlag":None,"facIp":None,"facPort":None,"facLoginName":None,"facLoginPwd":None,"facType":None,"videoUrl":None,"facStatus":"2","openType":None,"validateCode":None,"buildingFloorSpaceName":"room db558ea5-d651-11ec-af03-fc017c01a764","buildingName":"楼栋db48c778-d651-11ec-b0b7-fc017c01a764","floorName":"-3","facCateParentName":"设备类型74585d23-7256-460a-9028-44b315b49909","facCateName":"设备类型ee47d2f7-93eb-424b-bf6a-bd9ae450d8f5","alarmId":None,"workOrderNo":None,"isExist":None,"createdByName":"lichang1","lastUpdatedByName":"lichang1","tagName":None,"tagList":None,"tagNames":None,"controlVal":None},
}

feild_upload_hmc = {"01":{"fileName": 'xmhmc.xlsx',
                    "file": ('xmhmc.xlsx', open('{}/we_run/test_data/excel/xmhmc.xlsx'.format(os.getcwd()), 'rb'),
                             'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}}