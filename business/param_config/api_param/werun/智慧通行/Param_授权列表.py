#新增
from common.Common_Base import getByte
import os

#新增
p_add = {
    '园区':{"propertyId":"20997","userType":1,"mobile":"13081782443","authStartDate":"","authEndDate":"","remark":"remarkremark01","faceUrl":"562322291501826048","cardList":[],"authType":1,"userId":3348,"neverExpires":1,"userName":"nickNamea747f70451c7","buildingId":7732,"facIdList":[],"tagList":[{"facTagId":64,"facTagName":"通行tag7ca40a5d-fef6-42d9-a4fe-e25664c34ffc"}]},
    '企业':{"propertyId":"36869","userType":2,"mobile":"13538450911","authStartDate":1648828800000,"authEndDate":1780156800000,"remark":"remarkremark","faceUrl":"575995592396767232","cardList":[{"cardId":"12354","cardStatus":None}],"authType":1,"userId":1045,"userName":"昵称8d780633-a262-492a-8fb3-9b66df52e2e6","neverExpires":0,"companyId":1797},
}
#上传授权照片
p_upload = {
    '01':{'file':('autotest.jpg', getByte('{}/we_run/test_data/auto_image/autotest.jpg'.format(os.getcwd()))),'classify':'gate','bizPath':'face'},
}
#企业通行规则
p_txgz = {
    '01':{"passageRuleVo":{"passageType":1,"propertyId":21263,"authType":1,"businessId":654,"buildingId":7845,"supplierPerson":"联系人94644926-6269-40f3-8ea4-b1ec8b3f4961","mobil":"13375727783","authStartDate":1648828800000,"authEndDate":1780156800000,"remark":"remark0101"},"facIdList":[],"tagList":[{"facTagId":70,"facTagName":"通行tagab99ebd3-358f-447b-8605-d4c0061da561"}]},
}
#分页查询授权信息
p_page = {
    '授权人员':{"head":{"current":1,"size":10,"total":1},"body":{"city":None,"area":None,"userName":"nickName"}},
    '园区':{"head":{"current":1,"size":10,"total":1},"body":{"city":None,"area":None,"userType":1}},
    '企业':{"head":{"current":1,"size":10,"total":1},"body":{"city":None,"area":None,"userType":2}},
    '访客':{"head":{"current":1,"size":10,"total":1},"body":{"city":None,"area":None,"userType":3}},
    '重置':{"head":{"current":1,"size":10,"total":0},"body":{"city":None,"area":None}},
}
#编辑修改授权信息
p_upd = {
    '01':{"propertyId":21274,"userType":1,"mobile":"13912238903","authStartDate":"","authEndDate":"","remark":"备注465c6db8-20c4","cardList":[],"authType":1,"userId":3401,"neverExpires":1,"userName":"nickNamef7cc976342e6","buildingId":7856,"facIdList":[],"tagList":[{"facTagId":81,"facTagName":"通行tag50d487c0-bab9-41ee-a87a-89fdd5de9cc2"}],"id":473},
}