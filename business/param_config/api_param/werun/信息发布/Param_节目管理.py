

#新增节目
p_add_program = {
    '图片':{"materials":[{"materialId":88}],"programName":"图片节目","resolution":"3840*2160","playInterval":"1","remark":"图片节目"},
    '音频':{"materials":[{"materialId":88}],"programName":"音频节目","resolution":"3840*2160","playInterval":"1","remark":"音频节目"},
    '视频':{"materials":[{"materialId":88}],"programName":"视频节目","resolution":"3840*2160","playInterval":"1","remark":"视频节目"},
}

p_upd_program = {
    "01": {"materials":[{"materialId":33}],"programName":"新增节目","resolution":"1366*768","playInterval":"1","remark":"1","id":19}
}
#分页查询素材
p_page = {
    '集合查询':{"head":{"current":1,"size":10,"total":3},"body":{"createdDateStart":"","createdDateEnd":"","programName":"新增节目"}},
    "默认查询": {"head":{"current":1,"size":10,"total":0},"body":{"createdDateStart":"","createdDateEnd":""}}
}



