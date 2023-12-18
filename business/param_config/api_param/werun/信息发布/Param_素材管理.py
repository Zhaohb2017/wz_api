import os
from common.Common_Base import getByte

#上传素材
p_upload = {
    '图片':{'file':('autotest.jpg', getByte('{}/we_run/test_data/auto_image/autotest.jpg'.format(os.getcwd()))),'classify':'publish','bizPath':'img'},
    '音频':{'file':('autotest.mp3', open('{}/we_run/test_data/auto_audio/autotest.mp3'.format(os.getcwd()),'rb'),'audio/mpeg'),'classify':'publish','bizPath':'audio'},
    '视频':{'file':('autotest.mp4', open('{}/we_run/test_data/auto_video/autotest.mp4'.format(os.getcwd()),'rb'),'text/plain'),'classify':'publish','bizPath':'video'},
}

#新增素材
p_add = {
    '图片':[{"materialName":"图片","fileId":"566588921413107712","fileName":"autotest.jpg","fileSize":630,"fileWidth":1920,"fileHeight":1080,"fileType":"img"}],
    '音频':[{"materialName":"音频","fileId":"566589593218973696","fileName":"autotest.mp3","fileSize":8570324,"fileWidth":1920,"fileHeight":1080,"fileType":"audio"}],
    '视频':[{"materialName":"视频","fileId":"566590064839098368","fileName":"autotest.mp4","fileSize":314758,"fileWidth":1920,"fileHeight":1080,"fileType":"video"}],
}

#集合查询
p_set = {
    "默认": {"body":{"fileType":"img"},"head":{"total":14,"size":10,"current":1}}
}

#分页查询素材
p_page = {
    '查询图片':{"body":{"fileType":"img","materialName":"冰墩墩","createdDateStart":"","createdDateEnd":""},"head":{"total":0,"size":10,"current":1}},
    '查询音频':{"body":{"fileType":"audio","materialName":"冰墩墩","createdDateStart":"","createdDateEnd":""},"head":{"total":0,"size":10,"current":1}},
    '查询视频':{"body":{"fileType":"video","materialName":"冰墩墩","createdDateStart":"","createdDateEnd":""},"head":{"total":0,"size":10,"current":1}},
}



