

import os
#新增物料分类
from common.Common_Base import getByte

p_add_wf = {
    '01':{"warningNum":1,"spareTypeName":"dfasdfsdaf","spareTypeCode":"FDSAFDS"},
}
#物料分页分页查询
p_page_wlfl = {
    '重置':{"head":{"current":1,"size":10,"total":1},"body":{}},
}

#新增物料入库
p_add_rk = {
    '01':{"quantity":30,"annexUrl":"534026482691866624","unitPrice":999,"spareName":"名称123","brand":"品牌123","spareCode":"DFSAFSD","remark":"备注备注","spareTypeId":8},
}

#分页查询入库列表
p_page_rk = {
    '备件名称':{"head":{"current":1,"size":10,"total":4},"body":{"startDate":"","endDate":"","spareName":"名称"}},
    '物料分类':{"head":{"current":1,"size":10,"total":1},"body":{"startDate":"","endDate":"","spareTypeId":8}},
    '重置':{"head":{"current":1,"size":10,"total":0},"body":{"startDate":"","endDate":""}},
}

#图片上传参数
p_pic_upload = {
    '01':{'file':('autotest.jpg', getByte('{}/we_run/test_data/auto_image/autotest.jpg'.format(os.getcwd()))),'classify':'materiel','bizPath':'bill'}
    # 'out':{'file':('autotest.jpg', getByte('test_data/auto_image/autotest.jpg')),'classify':'materiel','bizPath':'out'}
}

#出库
p_add_ck = {
    '01':{"annexUrl":"534308308484358144","spareCodes":["XWL-20211224000"],"changeQuantitys":[5],"spareUseType":1,"orderId":77,"spareUseId":330},
}

#出入库历史分页查询
p_page_ls = {
    '备品分类':{"head":{"current":1,"size":10,"total":2},"body":{"startDate":"","endDate":"","spareTypeId":37}},
    '出库':{"head":{"current":1,"size":10,"total":2},"body":{"startDate":"","endDate":"","operateType":0}},
    '入库':{"head":{"current":1,"size":10,"total":1},"body":{"startDate":"","endDate":"","operateType":1}},
    '名称':{"head":{"current":1,"size":10,"total":2},"body":{"startDate":"","endDate":"","spareTypeId":"","operateType":"","brand":"","spareName":"名称"}},
}