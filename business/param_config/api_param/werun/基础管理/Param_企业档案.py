import os

#新增企业
p_add = {
    '01':{"globalAreaCodeId":1,"contactInformation":"13823466541","spaceId":"45576,160,7795,45575","businessName":"测试大佬","contactPerson":"zhb","enterTime":1678982400000},
}
#分页查询
p_page = {
    '关键字':{"head":{"current":1,"size":10},"body":{"totalCount":0,"total":0,"businessName":"公司名称"}},
    '所在区域':{"head":{"current":1,"size":10},"body":{"totalCount":0,"total":11,"spaceId":1451}},
    "默认":{"head":{"current":1,"size":10},"body":{"totalCount":0,"total":0}},
    '重置':{"head":{"current":1,"size":10},"body":{"total":0}},
}
#编辑修改企业
p_upd = {
    '01':{"spaceId":"1454","id":55,"businessName":"公司名称0eabc218-8fcf-4362-823","contactPerson":"联系人c1db9280-f4a3-4fd0-","globalAreaCodeId":"86","contactInformation":"14760775244","enterTime":1644336000000,"remark":"备注f07724b5-e727-47a1","sort":None,"delFlag":0,"createdBy":329,"createdDate":1644397797212,"lastUpdatedBy":329,"lastUpdatedDate":1644397797212,"propertyId":3983,"tenantId":None,"revision":None,"employNum":None,"spaceVos":[{"spaceId":1454,"buildingId":1562,"buildingFloorId":19510,"buildingFullName":"楼栋0c9297b0-8988-11ec-8229-fc017c01a764--3-room 0ca5ab4b-8988-11ec-bc20-fc017c01a764"}],"createdName":None},
}
#添加员工
p_add_yg = {
    '01':{"sword":"Efc1u5Mg/IOTjE1B0iiwILs8zwTKam5NeLI44TU4N0yydq6s+p3CUVRHa9bImUbrwAARmsQleBUyAFXs8z9/WjCVZqHAPOVXOYznMxKayojer3tuCG1H3HSxlrUplzid+gDvkXdVu/Q4f0TzV130zNLfLPwzJWkpBKrSRWMoDPc0cBcO6HWat80VayNShPHuovruoqgUqt0PWfKb1AdhyEFvdXLw6Qq22XYFfDXwGGKbPDZn270+i17HwWjxlvxG1s4ORUKcfRhdLV9a1PhS4H2cBK6z6AiluZ7kh8GXbZqviseRyuaNoBZL9E5njuYeizMKc4QchrMkkd319sYU+A==","confirmSword":"CUe2BQQUwr+0NpqT5PONDyeUQyd/VhIrniXleyQRzE48T5WksS6exGiQLmSOvZPCITgfCZNww0fkENuvzmnOlB8eYeqOAIyF4DDueNMlC2BTlGo8pYhOhmfvg65rdEYKIIgVWM0UjygkU7ZT3W+sOLObVEXBXQR/VVvOxnjzOLJQnVo3ypULMRzNORG2Z3tCSOaUs0r86EmGdyvzx8nF6kBW9vQ0Y183A3NK8q3VR2a0eIRVdXjjDLqgXwKYJxo+sFaSSpashOrAnGwaoSxLiClvETegMH7QUJcOvIt5n88PHRF1fGlY76QYp+qfz/JaXgJuIu9dNW1SPFBhxWFDFw==","nickName":"sbsbsbs","businessId":50,"businessUserType":"3","scabbard":"coencoen","mobile":"18545641234","email":"123456@qq.com"},
}
#业主端登录
p_login_yz = {
    '01':{"loginType":"app-client","scabbard":"coencoen","sword":"hNOVeonWZo9JMgRDAv8MF5PkBJvwp7ZOX/t/g138wJxUDF6GQC/XegR31yPsG3eUctIquSxLSWk0ad54yamtoVTieI3QoQL1VQv2G74eGeBq83WuVFe8mX6ALrofRhk1cS6SSoQPgsBijuvqZgOWO3BfZz0vyIKiHXPj9W0IjpFlqgv95noUA+9pR48ONwRKr3zj/uJ6MwIzFEHAg0B6JtIqkAf0u6jWbbJ8Frox9CSPrZqBP0YUCoMfxOrmAUmW3HuwnbJh+IDMGiY0o4Hwqa4DAkqEefojewwzQGG2bmucc/fSIG0LirCU1W4vvBvQy/VXnzMvmSjmljeiJRJ3SA==","userType":1},
}
#导入企业
p_import = {
    '01':['微筑', '杭州市', '下城区', '孙悟空', '13888888888', '客服', '2021/1/1 16:20:37', '2021/12/10 16:20:37'],
}

file_data = {
    "01": {"fileName": 'xmhmc.xlsx',
                            "file": ('xmhmc.xlsx', open('{}/we_run/test_data/excel/xmhmc.xlsx'.format(os.getcwd()), 'rb'),
                                     'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')},
    "02": '{}/we_run/test_data/excel/xmhmc.xlsx'.format(os.getcwd())
}