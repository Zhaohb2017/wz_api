

#新增
p_add = {
    '一日一班':{"schedulingName":"测试班次","records":[{"scheduingName":"ss","schStartTime":"00:00","schEndTime":"00:20","schTime":[]}]},
    '一日两班':{"schedulingName":"asdfsdf","records":[{"scheduingName":"sdfasdf","schStartTime":"01:10","schEndTime":"05:40"},{"scheduingName":"faefdafd","schStartTime":"10:10","schEndTime":"21:00"}]},
}

p_upd={
    '一日两班':{"schedulingName":"asdfsafd","records":[{"schStartTime":"00:10","schEndTime":"02:00","scheduingName":"asdfefdaf"},{"scheduingName":"fefadsfdas","schStartTime":"00:30","schEndTime":"03:50"}],"id":31},
}
#分页查询
p_page={
    '名称':{"body":{"schedulingName":"BanCi"},"head":{"current":1,"size":10,"total":8},"current":1},
    '重置':{"body":{},"head":{"current":1,"size":10,"total":0}},
    "默认查询": {"body":{},"head":{"current":1,"size":10,"total":2}},
}