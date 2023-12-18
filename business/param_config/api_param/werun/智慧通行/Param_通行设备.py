

#新增
p_add = {
    '01':{"tagType":"fac_passage","propertyId":5,"tagName":"abcd"},
}
#修改标签
p_upd = {
    '01':{"tagType":"fac_passage","propertyId":5,"tagName":"abcde","id":27},
}
#打标签
p_dbq={
    '01':{"facIdList":[5091],"tagIdList":[30]},
}
#移除标签
p_ycbq = {
    '01':{"facIdList":[5091],"tagIdList":[30]},
}
#通过标签查询
p_tag_page = {
    '01':{"head":{"current":1,"size":10,"total":1},"body":{"tagId":30,"assetStatus":"","tagType":"fac_passage"}},
}