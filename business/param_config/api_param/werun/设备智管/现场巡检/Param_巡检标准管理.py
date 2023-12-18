import os

#新增设备巡检标准
p_add = {
    '仪表类':{"scheduleBenchmarkVo":{"benchmarkType":2,"facCateId":121},"scheduleBenchmarkRecordVoList":[{"benchmarkName":"fdsafefdasfdsf","benchmarkType":1,"showAlarm":1,"needPic":1,"benchmarkOperator":3,"benchmarkUnit":"A","facCateTypeName":"电流表","facCateType":"1","maxVal":35}]},
    '非仪表类':{"scheduleBenchmarkVo":{"benchmarkType":2,"facCateId":121},"scheduleBenchmarkRecordVoList":[{"benchmarkName":"fdsafeafdac","benchmarkType":2,"benchmarkResult":1,"needPic":1}]},
    '结果类型为合格':{"scheduleBenchmarkVo":{"benchmarkType":2,"facCateId":121},"scheduleBenchmarkRecordVoList":[{"benchmarkName":"fdsafeaf","benchmarkType":2,"benchmarkResult":2,"needPic":1}]},
    '不需要拍照':{"scheduleBenchmarkVo":{"benchmarkType":2,"facCateId":121},"scheduleBenchmarkRecordVoList":[{"benchmarkName":"fasfefdssa","benchmarkType":2,"benchmarkResult":1,"needPic":0}]},
    '两条巡检内容':{"scheduleBenchmarkVo":{"benchmarkType":2,"facCateId":121},"scheduleBenchmarkRecordVoList":[{"benchmarkName":"dfasdfeafda","benchmarkType":1,"showAlarm":1,"needPic":0,"benchmarkOperator":1,"benchmarkUnit":"kwh","facCateTypeName":"电度表","facCateType":"2","minVal":123,"maxVal":124},{"benchmarkName":"fdasfea","benchmarkType":2,"benchmarkResult":2,"needPic":0}]},
}

#新增位置巡检标准
p_add_st = {
    '仪表类':{"scheduleBenchmarkVo":{"benchmarkType":2,"spaceId":129},"scheduleBenchmarkRecordVoList":[{"benchmarkName":"dsafefdas","benchmarkType":1,"showAlarm":1,"needPic":1,"benchmarkOperator":2,"benchmarkUnit":"A","facCateTypeName":"电流表","facCateType":"1","minVal":35}]},
    '非仪表类':{"scheduleBenchmarkVo":{"benchmarkType":2,"spaceId":129},"scheduleBenchmarkRecordVoList":[{"benchmarkName":"fdsafefda","benchmarkType":2,"benchmarkResult":1,"needPic":1}]},
    '结果类型为合格':{"scheduleBenchmarkVo":{"benchmarkType":2,"spaceId":129},"scheduleBenchmarkRecordVoList":[{"benchmarkName":"dfsafefa","benchmarkType":2,"benchmarkResult":2,"needPic":1}]},
    '不需要拍照':{"scheduleBenchmarkVo":{"benchmarkType":2,"spaceId":129},"scheduleBenchmarkRecordVoList":[{"benchmarkName":"asdfawef","benchmarkType":2,"benchmarkResult":1,"needPic":0}]},
    '两条巡检内容':{"scheduleBenchmarkVo":{"benchmarkType":2,"spaceId":129},"scheduleBenchmarkRecordVoList":[{"benchmarkName":"dsafefdsa","benchmarkType":1,"showAlarm":1,"needPic":1,"benchmarkOperator":1,"benchmarkUnit":"A","facCateTypeName":"电流表","facCateType":"1","minVal":15,"maxVal":30},{"benchmarkName":"fdsafefea","benchmarkType":2,"benchmarkResult":2,"needPic":1}]},
}

#编辑修改
p_upd = {
    '01':{"scheduleBenchmarkVo":{"benchmarkType":2,"id":72,"spaceId":129},"scheduleBenchmarkRecordVoList":[{"id":100,"scheduleBenchmarkId":72,"benchmarkName":"feadfafefd","benchmarkType":2,"facCateType":None,"facCateTypeName":None,"minVal":None,"maxVal":None,"benchmarkOperator":None,"benchmarkUnit":None,"benchmarkResult":2,"showAlarm":None,"needPic":1,"createdBy":None,"createdDate":None,"lastUpdatedBy":None,"lastUpdatedDate":None,"propertyId":None,"remark":None,"delFlag":0}]},
}

# 上传
feild_upload_hmc = {
    "01":{"fileName": 'xmhmc.xlsx',
                    "file": ('xmhmc.xlsx', open('{}/we_run/test_data/excel/xmhmc.xlsx'.format(os.getcwd()), 'rb'),
                             'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
}