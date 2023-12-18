
#分页查询能耗告警
p_page = {
    '未确认':{"head":{"current":1,"size":10,"total":0},"body":{"alarmStatus":"0"}},
    '已确认':{"head":{"current":1,"size":10,"total":0},"body":{"alarmStatus":"1"}},
}
#能耗异常确认
p_clear = {
    '01':{"id":27,"alarmStatus":"1"},
}
#上报电表用量
p_upload_data = {
    '01':{"attrValue":"31","facLinkCode":"fasdfeafda"},
}