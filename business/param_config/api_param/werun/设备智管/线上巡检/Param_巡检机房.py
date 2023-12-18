

#新增
p_add = {
    '01':{"buildingId":673,"buildingFloorId":8226,"buildingFloorSpaceId":627,"remark":"123fdsa","cameras":None,"envStandards":[{"standardEnvCheckId":90,"standardEnvId":58}],"facs":[]},
    '巡检摄相头':{"buildingId":980,"buildingFloorId":12110,"buildingFloorSpaceId":911,"cameras":[{"id":None,"inspectRoomId":None,"inspectCameraId":833,"orderNum":1,"remark":None,"createdBy":None,"createdDate":None,"lastUpdatedBy":None,"lastUpdatedDate":None,"propertyId":None,"inspectCameraName":"设备名称16825253-709a-454b-a0fc-68fff4089ad6","cameraVideoUrl":None}],"envStandards":[{"standardEnvCheckId":159,"standardEnvId":124}],"facs":[{"inspectFacId":833,"inspectFacCateId":1436,"inspectFlag":True}]},
}

#分页查询
p_page = {
    '机房名称':{"head":{"current":1,"size":10},"body":{"total":7,"machineRoomName":"room"}},
    '状态启用':{"head":{"current":1,"size":10},"body":{"total":1,"machineRoomName":"","activeState":"1"}},
    '状态禁用':{"head":{"current":1,"size":10},"body":{"total":7,"activeState":"0"}},
    '重置':{"head":{"current":1,"size":10},"body":{"total":0}},
}

#启用禁用
p_on_off = {
    '启用':{"id":32,"activeState":1},
    '禁用':{"id":32,"activeState":0},
}

#编辑修改巡检机房
p_upd = {
    '01':{"id":673,"buildingId":673,"buildingFloorId":8226,"buildingFloorSpaceId":627,"remark":"123fdsa","cameras":None,"envStandards":[{"standardEnvCheckId":90,"standardEnvId":58}],"facs":[]},
}