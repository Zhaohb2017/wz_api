

#查询当前日期的巡检记录
p_record = {
    '01':{'excuteDate':'2022-01-01'},
}
#查询当前巡检记录详情
p_record_detail = {
    '01':{'excuteDate':'2022-01-01','pointId':'','scheduleId':''},
}
#编辑修改巡检人
p_upd = {
    '01':{'scheduleEqtLogIds':'','userNames':'','userIds':''}
}
#巡检记录状态变更
p_status = {
    '取消':{"id":643,"schEqtLogStatus":3,"handleName":"lichang1","handleId":1817,"remark":"auto cancel"},
    '开始':{"id":643,"schEqtLogStatus":4,"handleName":"lichang1","handleId":1817,"remark":"auto start"},
    '完成':{"id":643,"schEqtLogStatus":8,"handleName":"lichang1","handleId":1817,"remark":"auto finish"},
}
#使巡检记录可进行巡检作业
p_upd_pre = {
    '01':{"id":643,"schEqtLogStatus":2,"handleName":"lichang1","handleId":1817,"remark":"auto cancel"}
}