
#转告警
p_alarm = {
    '安全告警':{"facId":862,"alarmType":"2","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称2ef69322-d56b-4ac3-b52e-8d862c0dd196黑名单告警","alarmLevel":"1","remark":"remarkremark","alarmSubType":"bl","alarmConfigId":42},
    '消防告警':{"facId":862,"alarmType":"3","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称2ef69322-d56b-4ac3-b52e-8d862c0dd196消防配置60e4abda061a","alarmLevel":"1","remark":"asdfsadfsaf","alarmSubType":"f","alarmConfigId":""},
    '紧急安全':{"facId":862,"alarmType":"2","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称2ef69322-d56b-4ac3-b52e-8d862c0dd196黑名单告警","alarmLevel":"1","remark":"remarkremark","alarmSubType":"bl","alarmConfigId":42},
    '严重消防':{"facId":862,"alarmType":"3","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称2ef69322-d56b-4ac3-b52e-8d862c0dd196消防配置60e4abda061a","alarmLevel":"2","remark":"asdfsadfsaf","alarmSubType":"f","alarmConfigId":""},
    '一般安全':{"facId":862,"alarmType":"2","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称2ef69322-d56b-4ac3-b52e-8d862c0dd196黑名单告警","alarmLevel":"3","remark":"remarkremark","alarmSubType":"bl","alarmConfigId":42},
    '轻微消防':{"facId":862,"alarmType":"3","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称2ef69322-d56b-4ac3-b52e-8d862c0dd196消防配置60e4abda061a","alarmLevel":"4","remark":"asdfsadfsaf","alarmSubType":"f","alarmConfigId":""},
    '告警名称':{"facId":862,"alarmType":"3","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称2ef69322-d56b-4ac3-b52e-8d862c0dd196消防配置60e4abda061a","alarmLevel":"4","remark":"asdfsadfsaf","alarmSubType":"f","alarmConfigId":""},
    '告警位置':{"facId":862,"alarmType":"3","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称2ef69322-d56b-4ac3-b52e-8d862c0dd196消防配置60e4abda061a","alarmLevel":"4","remark":"asdfsadfsaf","alarmSubType":"f","alarmConfigId":""},
    '跟进人姓名':{"facId":862,"alarmType":"3","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称2ef69322-d56b-4ac3-b52e-8d862c0dd196消防配置60e4abda061a","alarmLevel":"4","remark":"asdfsadfsaf","alarmSubType":"f","alarmConfigId":""},
    '跟进人电话':{"facId":862,"alarmType":"3","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称2ef69322-d56b-4ac3-b52e-8d862c0dd196消防配置60e4abda061a","alarmLevel":"4","remark":"asdfsadfsaf","alarmSubType":"f","alarmConfigId":""},
    '设备告警':{"facId":12612,"alarmType":"1","operatorMobile":"13888888888","currentOperator":"孙悟空","alarmName":"设备名称f2a264e9-bfc3-4d8c-842d-c687eb389759告警名称3931c181-87d4-4a8e-bbe5-be94351db0bd","alarmLevel":2,"remark":"autotest remark001","alarmSubType":"","alarmOperate":{"operateType":"1","operateMobil":"13888888888","operatorName":"孙悟空"}},

}
#分页查询
p_page_dcl = {
    # '设备告警':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":"","alarmType":"1","alarmStatus":"1"}},
    '安全告警':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":"","alarmType":"2","alarmStatus":"1"}},
    '消防告警':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":"","alarmType":"3","alarmStatus":"1"}},
    '紧急安全':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":1,"alarmType":"","alarmStatus":"1"}},
    '严重消防':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":2,"alarmType":"","alarmStatus":"1"}},
    '一般安全':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":3,"alarmType":"","alarmStatus":"1"}},
    '轻微消防':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":4,"alarmType":"","alarmStatus":"1"}},
    '告警名称':{"head":{"current":1,"size":10,"total":0},"body":{"alarmName":"设备名称","alarmLevel":"","alarmType":"","alarmStatus":"1"}},
    '告警位置':{"head":{"current":1,"size":10,"total":2},"body":{"alarmLocation":"楼栋","alarmLevel":"","alarmType":"","alarmStatus":"1"}},
    '跟进人姓名':{"head":{"current":1,"size":10,"total":2},"body":{"currentOperator":"孙悟空","alarmLevel":"","alarmType":"","alarmStatus":"1"}},
    '跟进人电话':{"head":{"current":1,"size":10,"total":0},"body":{"currentOperator":"13888888888","alarmLevel":"","alarmType":"","alarmStatus":"1"}},
}
#处理待处理告警
p_chuli = {
    '线下跟进':{"operatorName":"孙悟空","operateMobil":"13888888888","remark":"abcd123456","id":195,"operateType":1},
    '直接关闭':{"remark":"其它","alarmAttches":[],"operateType":3,"id":199},
    '变更跟进人':{"operatorName":"孙悟空","operateMobil":"13888888888","remark":"asdfafdsaf","alarmAttches":[],"id":201,"operateType":4},
    '消警':{"operateType":5,"remark":"我要消警","id":201},
}
#分页查询-处理中
p_page_clz = {
    '设备告警':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":"","alarmType":"1","alarmStatus":"2"}},
    '安全告警':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":"","alarmType":"2","alarmStatus":"2"}},
    '消防告警':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":"","alarmType":"3","alarmStatus":"2"}},
    '紧急安全':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":1,"alarmType":"","alarmStatus":"2"}},
    '严重消防':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":2,"alarmType":"","alarmStatus":"2"}},
    '一般安全':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":3,"alarmType":"","alarmStatus":"2"}},
    '轻微消防':{"head":{"current":1,"size":10,"total":0},"body":{"alarmLevel":4,"alarmType":"","alarmStatus":"2"}},
    '告警名称':{"head":{"current":1,"size":10,"total":0},"body":{"alarmName":"设备名称","alarmLevel":"","alarmType":"","alarmStatus":"2"}},
    '告警位置':{"head":{"current":1,"size":10,"total":2},"body":{"alarmLocation":"楼栋","alarmLevel":"","alarmType":"","alarmStatus":"2"}},
    '跟进人姓名':{"head":{"current":1,"size":10,"total":2},"body":{"currentOperator":"孙悟空","alarmLevel":"","alarmType":"","alarmStatus":"2"}},
    '跟进人电话':{"head":{"current":1,"size":10,"total":0},"body":{"currentOperator":"13888888888","alarmLevel":"","alarmType":"","alarmStatus":"2"}},
    '默认查询':{"head":{"current":1,"size":10,"total":60},"body":{"alarmName":"","alarmLocation":"","currentOperator":"","alarmLevel":"","alarmTypeList":"","alarmStatus":"1"}},
}