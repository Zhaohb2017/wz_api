

#新增
p_add = {
    '每天执行':{"patrolUser":1382,"patrolPlanName":"计划名称123","patrol_frequency":"day","planStart":1647964800000,"planEnd":1651248000000,"repeatRate":"","nums":[{"execStartTime":"00:00","execEndTime":"04:55"}],"ranges":[{"patrolRangeId":126}],"propertyId":None},
    '每周执行':{"patrolPlanName":"计划名称321","patrolUser":1382,"patrol_frequency":"week","planStart":1647964800000,"planEnd":1651248000000,"repeatRate":"5,7","nums":[{"execStartTime":"00:05","execEndTime":"03:25"}],"ranges":[{"patrolRangeId":126}],"propertyId":None},
    '每月执行':{"patrolPlanName":"计划名称65423","patrolUser":1382,"patrol_frequency":"month","planStart":1647964800000,"planEnd":1651248000000,"repeatRate":"12","nums":[{"execStartTime":"00:00","execEndTime":"04:00"}],"ranges":[{"patrolRangeId":126}],"propertyId":None},
}

#分页查询
p_page = {
    '名称':{"head":{"current":1,"size":10},"body":{"patrolPlanName":"巡逻计划"}},
    '启用':{"head":{"current":1,"size":10},"body":{"activeState":1}},
    '禁用':{"head":{"current":1,"size":10},"body":{"activeState":0}},
    '重置':{"head":{"current":1,"size":10},"body":{}},
}
#启用禁用
p_on_off = {
    '启用':{"id":15,"activeState":1},
    '禁用':{"id":132,"activeState":0},
}
#更新
p_upd = {
    '01':{"id":135,"patrolPlanName":"巡逻计划83a3601a-8a2","activeState":0,"patrolUser":1508,"schedulingPlanId":None,"userType":None,"repeatRateType":None,"repeatWeek":None,"repeatMoth":None,"remark":None,"createdBy":1817,"createdDate":1648275324158,"lastUpdatedBy":1817,"lastUpdatedDate":1648275324158,"propertyId":None,"rateNums":None,"patrol_frequency":"day","planStart":1648483200000,"planEnd":1648569600000,"repeatRate":"0","nums":[{"execStartTime":"00:10","execEndTime":"04:35"}],"ranges":[{"patrolRangeId":167}]},
}