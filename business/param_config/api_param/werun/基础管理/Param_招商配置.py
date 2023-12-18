import os

p_upload_data = {
    '一条数据':[['公司名称','项目名称','城市','区县','楼栋名称','房间名称','2000','123456','1234567','信息技术','1']],
    '多条数据':[['公司名称','项目名称','城市','区县','楼栋名称','房间名称','2000','123456','1234567','信息技术','1'],['公司名称','项目名称','城市','区县','楼栋名称','房间名称','2000','123456','1234567','信息技术','2']],
}

p_page = {
    '公司名称':{"head":{"total":14,"current":1,"size":10},"body":{"city":None,"area":None,"companyName":"公司名称"}},
    '所在地区':{"head":{"total":1,"current":1,"size":10},"body":{"city":"0451","area":None}},
    '行政区':{"head":{"total":1,"current":1,"size":10},"body":{"city":"0451","area":"230103"}},
    '重置':{"head":{"total":0,"current":1,"size":10},"body":{"city":None,"area":None}},
}

p_query = {
    "重置":{"head":{"total":0,"current":1,"size":10},"body":{"city":None,"area":None}}
}

feild_upload_excel_1 = {"fileName": 'zspz.xlsx', "file": ('zspz.xlsx', open('{}/we_run/test_data/excel/zspz.xlsx'.format(os.getcwd()), 'rb'),
                                                        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}

feild_upload_excel = {"fileName": 'zspz2.xlsx',"file": ('zspz2.xlsx',open('{}/we_run/test_data/excel/zspz2.xlsx'.format(os.getcwd()), 'rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}