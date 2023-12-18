import os

#上传数据
p_upload_data = {
    '单条数据':[['微筑', '杭州市', '下城区', '孙悟空', '13888888888', '客服']],
    '多条数据':[['微筑', '杭州市', '下城区', '孙悟空', '13888888888', '客服'],['微筑', '杭州市', '下城区', '孙悟空', '13888888888', '客服']],
}
#分页查询
p_page = {
    '员工姓名':{"head":{"total":8,"current":1,"size":10},"body":{"userName":"花名"}},
    '手机号码':{"head":{"total":0,"current":1,"size":10},"body":{"userName":"18548561258"}},
    '重置':{"head":{"total":0,"current":1,"size":10},"body":{}},
}

# 上传

feild_upload_hmc = {
    "01":{"fileName": 'xmhmc1.xlsx', "file": ('xmhmc1.xlsx', open('{}/we_run/test_data/excel/xmhmc1.xlsx'.format(os.getcwd()), 'rb'),
                                                        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
}

xlsx = {
    "01": '{}/we_run/test_data/excel/xmhmc1.xlsx'.format(os.getcwd())
}