

p_add = {
    '周期_日':{"carAuthorizationName":"车辆授权类型01","parkingLotId":63,"carRegisterNum":0,"authorizationCycle":1,"carRegisterLimit":1,"authorizationCycleUnit":1},
    '周期_月':{"carAuthorizationName":"车辆授权类型02","parkingLotId":63,"carRegisterNum":0,"authorizationCycle":2,"carRegisterLimit":2,"authorizationCycleUnit":2},
    '周期_年':{"carAuthorizationName":"车辆授权类型03","parkingLotId":63,"carRegisterNum":0,"authorizationCycle":3,"carRegisterLimit":3,"authorizationCycleUnit":3},
}

p_page = {
    '重置':{"head":{"total":1,"current":1,"size":10},"body":{}},
    '停车场':{"head":{"total":1,"current":1,"size":10},"body":{"parkingLotId":70}},
    '启用状态':{"head":{"total":0,"current":1,"size":10},"body":{"activeState":1}},
    '禁用状态':{"head":{"total":0,"current":1,"size":10},"body":{"activeState":0}},
    '授权类型':{"head":{"total":1,"current":1,"size":10},"body":{"carAuthorizationName":"授权类型"}},
}
#启用禁用功能正常
p_on_off = {
    '启用':{"id":41,"activeState":1},
    '禁用':{"id":41,"activeState":0},
}
#编辑修改车辆授权
p_upd = {
    '01':{"carAuthorizationName":"授权类型c2081bf0","parkingLotId":75,"carRegisterNum":0,"authorizationCycle":5,"carRegisterLimit":5,"authorizationCycleUnit":3,"id":45,"createdBy":1817,"createdDate":1650610682813,"lastUpdatedBy":1817,"lastUpdatedDate":1650610682813,"remark":None,"activeState":1,"delFlag":0,"propertyId":28278,"parkingName":"停车场名称c5649fad-dfd2-4cea-b967-1b2b264ad485","strId":"null","bizName":"CAR_AUTHORIZATION_VO"},
}