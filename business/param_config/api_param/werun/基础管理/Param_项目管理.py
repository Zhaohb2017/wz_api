
# 新增项目
p_add = {
    '写字楼':{"city":"0755","area":"440306","propertyArea":45646,"propertyPublicArea":45646,"propertyName":"项目写字楼","fullAddress":"沙三路与蚝乡路交叉口南80米","longitude":"113.796823","latitude":"22.739419","propertyType":"1","completionDate":1650729600000,"propertyParkTotal":"123","remark":"remark01001"},
    '商业综合体':{"city":"0839","area":"510822","propertyArea":321,"propertyPublicArea":321,"propertyName":"项目商业综合体","longitude":105.21189,"latitude":32.588622,"fullAddress":"四川省广元市青川县乔庄镇四沟里","propertyType":"2","completionDate":1650470400000,"propertyParkTotal":"121","remark":"remark0101"},
    '学校':{"city":"0451","area":"230103","propertyArea":123123,"propertyPublicArea":123123,"propertyName":"自动测试新增街道","fullAddress":"东大直街329号","longitude":"126.643242","latitude":"45.758867","propertyType":"3","completionDate":1650729600000,"propertyParkTotal":"1234","remark":"备注0010101"},
    '园区':{"city":"0751","area":"440204","propertyArea":123,"propertyPublicArea":123,"propertyName":"项目园区","longitude":113.608159,"latitude":24.808716,"fullAddress":"广东省韶关市浈江区东河街道文德路13号12栋","propertyType":"4","completionDate":1650729600000,"propertyParkTotal":"123","remark":"remark0110101111"},
    '医院':{"city":"0432","area":"220204","propertyArea":3213,"propertyPublicArea":3213,"propertyName":"项目医院","longitude":126.550007,"latitude":43.841297,"fullAddress":"吉林省吉林市船营区青岛街道和龙街12-6号乡企局小区","propertyType":"5","completionDate":1650729600000,"propertyParkTotal":"12312","remark":"remark010101"},
    '社区':{"city":"0594","area":"350322","propertyArea":321,"propertyPublicArea":321,"propertyName":"项目社区","longitude":118.703478,"latitude":25.375157,"fullAddress":"福建省莆田市仙游县鲤城街道清源东路仙游院子(建设中)","propertyType":"6","completionDate":1650729600000,"propertyParkTotal":"1122","remark":"remark01"},
}

#修改项目信息
p_upd = {
    '01':{"city":"440100","area":"1913","propertyType":"5","id":80,"propertyCode":None,"propertyName":"项目9d6bfb6b-5409-11ec-a786-fc017c01a764","propertyNameEn":None,"orgId":None,"propertyArea":202021,"propertyPublicArea":202021,"propertyParkTotal":"4322","companyCode":None,"country":None,"longitude":None,"latitude":None,"localAddress":None,"fullAddress":"天河街道003","functionalCode":None,"firstOnlineDate":None,"completionDate":1230103411200000,"circumferentialRadius":None,"logoPic":None,"mainPic":None,"layoutPic":None,"activeInd":1,"inactiveDate":None,"remark":None,"createdBy":None,"createdDate":1638516069832,"lastUpdatedBy":None,"lastUpdatedDate":1638516069833,"provinceName":None,"propertyTypeName":None,"buildingCount":None,"remarks":"天河街道003"}
}

# page查询项目
p_page = {
    '所在地区':{"head":{"total":2,"current":1,"size":10},"body":{"city":"0451","area":None,"location":["0451"]}},
    '所在地区And行政区':{"head":{"total":2,"current":1,"size":10},"body":{"city":"0451","area":"230103","location":["0451","230103"]}},
    # '项目类型':{"head":{"total":2,"current":1,"size":10},"body":{"city":None,"area":None,"location":[],"propertyType":"3"}},
    # '搜索关键字':{"head":{"total":0,"current":1,"size":10},"body":{"city":None,"area":None,"location":[],"propertyType":"","propertyName":"项目"}},
    # '项目类型And搜索关键字':{"head":{"total":0,"current":1,"size":10},"body":{"city":None,"area":None,"location":[],"propertyType":"3","propertyName":"项目"}},
    '所在地区And搜索关键字':{"head":{"total":0,"current":1,"size":10},"body":{"city":"0451","area":None,"location":["0451"],"propertyType":"","propertyName":"项目"}},
    '查询所有':{"head":{"total":1,"current":1,"size":10},"body":{"city":None,"area":None,"location":"","propertyType":"","propertyName":""}},
    "重置": {"head":{"total":0,"current":1,"size":10},"body":{"city":None,"area":None}}
}
