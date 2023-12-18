import os
#新增资料库
from common.Common_Base import getByte

p_add_zlk = {

    '顶级':{"folderName":"我是脚本"},
    '下级':{"folderName":"afddsafdsaf","parentId":17},
}
#新增项目资料
p_add_xmzl = {
    '01':{"folderId":18,"filePath":"543431610305871872","fileFormat":"jpg","fileOriginalName":"123","fileSize":2326,"fileName":"asdf","fileVersion":"sdf","remark":"dsf"},
}
#上传项目资料文件
p_upload = {
    '01':{'file':('autotest.jpg', getByte('{}/we_run/test_data/auto_image/autotest.jpg'.format(os.getcwd()))),'classify':'device','bizPath':'database'},
}
#项目资料分页查询
p_page_xmzl = {
    '重置':{"body":{},"head":{"current":1,"size":10,"total":0}},
    '名称':{"body":{"fileName":"名称"},"head":{"current":1,"size":10,"total":0},"page":1,"rows":10,"pages":1,"total":3},
}

