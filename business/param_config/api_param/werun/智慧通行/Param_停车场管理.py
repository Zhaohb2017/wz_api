from common.Common_Base import getByte
import os
#新增停车场
p_add = {
    '单区域单出入口':{"parkingSpaceAreaList":[{"parkingSpaceArea":"车位区域1","parkingSpaceNum":"123"}],"parkingEntranceList":["入口1"],"parkingExitList":["出口1"],"propertyId":"27915","propertyName":"项目104c81b8-c123-11ec-9dc5-fc017c01a764","parkingSpaceSum":123,"parkingName":"停车场名称1","buildingSpaceId":"139510,139511,139512","parkingArea":"1","parkingGuideList":[{"entranceName":"入口1","spaceAreasName":"车位区域1","guideImg":"569485939374555136"}]},
    '多区域多出入口':{"parkingSpaceAreaList":[{"parkingSpaceArea":"车位区域1","parkingSpaceNum":"306"},{"parkingSpaceArea":"车位区域2","parkingSpaceNum":"305"}],"parkingEntranceList":["入口1","入口2"],"parkingExitList":["出口1","出口2"],"propertyId":"27925","propertyName":"项目a63a06fc-c14d-11ec-8e94-fc017c01a764","parkingSpaceSum":611,"parkingName":"停车场名称2","buildingSpaceId":"139640,139641,139642","parkingArea":"2","parkingGuideList":[{"entranceName":"入口1","spaceAreasName":"车位区域1","guideImg":"569562169394331648"},{"entranceName":"入口2","spaceAreasName":"车位区域2","guideImg":"569562200801280000"}]},
}
#上传引导图片
p_upload = {
    '01':{'file':('autotest.jpg', getByte('{}/we_run/test_data/auto_image/autotest.jpg'.format(os.getcwd()))),'classify':'parking','bizPath':'guide'},
}
#停车场分页查询
p_page = {
    '关键字':{"head":{"total":18,"current":1,"size":10},"body":{"parkingName":"停车场名称"}},
    '重置':{"head":{"total":0,"current":1,"size":10},"body":{}},
}
#停车场编辑更新
p_upd = {
    '01':{"id":54,"createdBy":1817,"createdDate":None,"lastUpdatedBy":None,"lastUpdatedDate":None,"parkingName":"停车场名称3bd3d7da-6238-4b9a-961f-4d4c672d9829","buildingId":None,"buildingFloorId":None,"buildingSpaceId":"139825,139826,139827","parkingArea":1,"parkingSpaceSum":102,"parkingSpaceAreas":None,"parkingAreaSum":1,"parkingEntrances":"入口95933af3-8f6a-4682-a238-7a22d667bf65","parkingEntrancesSum":1,"parkingExits":"出口623bab82-bdbf-426b-b759-ff213fa72af0","parkingExitsSum":1,"parkingCode":None,"propertyId":27939,"delFlag":0,"remark":None,"tenantId":None,"revision":None,"parkingSpaces":"楼栋b0bfaef9-c164-11ec-9b2e-fc017c01a764--3,楼栋b0bfaef9-c164-11ec-9b2e-fc017c01a764--2,楼栋b0bfaef9-c164-11ec-9b2e-fc017c01a764--1","parkingSpaceAreaList":[{"id":65,"createdBy":1817,"createdDate":None,"lastUpdatedBy":None,"lastUpdatedDate":None,"parkingLotId":54,"parkingSpaceArea":"车位区域abc","parkingSpaceNum":"102","propertyId":27939,"delFlag":0,"remark":None,"tenantId":None,"revision":None,"strId":"None","bizName":"PARKING_SPACE_AREA"}],"parkingEntranceList":["入口95933af3-8f6a-4682-a238"],"parkingExitList":["出口623bab82-bdbf-426b-b759"],"parkingGuideList":[{"id":66,"createdBy":1817,"createdDate":None,"lastUpdatedBy":None,"lastUpdatedDate":None,"parkingLotId":54,"entranceName":"入口95933af3-8f6a-4682-a238","spaceAreasName":"车位区域abc","guideImg":"569603161044549632","propertyId":27939,"delFlag":0,"remark":None,"tenantId":None,"revision":None,"strId":"None","bizName":"PARKING_LOGUIDE"}],"strId":"None","bizName":"PARKING_LOT_VO"},
}
#停车记录分页查询
p_page_tcjl = {
    '车牌号码':{"head":{"total":0,"current":1,"size":10},"body":{"parkingLotId":56,"carNumber":"E123"}},
    '重置':{"head":{"total":0,"current":1,"size":10},"body":{"parkingLotId":56}},
}

p_add_cldj = {
    '01':{"authEndDate":1650699461000,"authStartDate":1650613061000,"parkingLotId":83,"authAmount":1,"carAuthId":53,"carAuthorizationName":"授权类型e9f5e46a-9ecf-4a21-910c-7b0cb2acded5","auhtPeriod":1,"auhtPeriodUnit":"日","carNumber":"京A345678","carOwnerName":"李大大","carOwnerTel":"18812345678","companyId":1022}
}

p_page_cldj = {
    '重置':{"head":{"total":0,"current":1,"size":10},"body":{}},
    '车辆类型':{"head":{"total":1,"current":1,"size":10},"body":{"carAuthId":65}},
    '授权状态_所有':{"head":{"total":1,"current":1,"size":10},"body":{"authStatus":None}},
    '授权状态_登记':{"head":{"total":1,"current":1,"size":10},"body":{"authStatus":1}},
    '授权状态_使用中':{"head":{"total":0,"current":1,"size":10},"body":{"authStatus":2}},
    '授权状态_临期':{"head":{"total":0,"current":1,"size":10},"body":{"authStatus":3}},
    '授权状态_到期停用':{"head":{"total":1,"current":1,"size":10},"body":{"authStatus":4}},
    '授权状态_冻结':{"head":{"total":0,"current":1,"size":10},"body":{"authStatus":5}},
    '车牌号码':{"head":{"total":1,"current":1,"size":10},"body":{"carNumber":"京A3456"}},
}
#编辑修改车辆登记
p_upd_cldj = {
    '01':{"authEndDate":1650699461000,"authStartDate":1650613061000,"parkingLotId":83,"authAmount":1,"carAuthId":53,"carAuthorizationName":"授权类型e9f5e46a-9ecf-4a21-910c-7b0cb2acded5","auhtPeriod":1,"auhtPeriodUnit":"日","carNumber":"京A345678","carOwnerName":"李大大","carOwnerTel":"18812345678","companyId":1022},
}
#编辑修改停车场
p_upd_tcc = {
    '01':{"id":104,"createdBy":1817,"createdDate":None,"lastUpdatedBy":None,"lastUpdatedDate":None,"parkingName":"停车场名称aa584eef-50cc-44dd-bda1-f00a363b1006","buildingId":None,"buildingFloorId":None,"buildingSpaceId":"147964,147965","parkingArea":1,"parkingSpaceSum":223,"parkingSpaceAreas":None,"parkingAreaSum":1,"parkingEntrances":"入口84c684be-b9b0-4516-997f-e68028777810","parkingEntrancesSum":1,"parkingExits":"出口1e7bd96e-bd84-473e-83da-2517f6fc28ff","parkingExitsSum":1,"parkingCode":None,"propertyId":29094,"delFlag":0,"remark":None,"tenantId":None,"revision":None,"parkingSpaces":"楼栋eeb3c308-c3b1-11ec-8c53-fc017c01a764--3,楼栋eeb3c308-c3b1-11ec-8c53-fc017c01a764--2,楼栋eeb3c308-c3b1-11ec-8c53-fc017c01a764--1","parkingSpaceAreaList":[{"id":115,"createdBy":1817,"createdDate":None,"lastUpdatedBy":None,"lastUpdatedDate":None,"parkingLotId":104,"parkingSpaceArea":"车位区域141e1e99","parkingSpaceNum":"223","propertyId":29094,"delFlag":0,"remark":None,"tenantId":None,"revision":None,"strId":"None","bizName":"PARKING_SPACE_AREA"}],"parkingEntranceList":["入口84c684be"],"parkingExitList":["出口1e7bd96e"],"parkingGuideList":[{"id":116,"createdBy":1817,"createdDate":None,"lastUpdatedBy":None,"lastUpdatedDate":None,"parkingLotId":104,"entranceName":"入口84c684be-b9b0-4516-997f-e68028777810","spaceAreasName":"车位区域141e1e99-881a-4e2c-96bd-e09c262451ac","guideImg":"570664223969902592","propertyId":29094,"delFlag":0,"remark":None,"tenantId":None,"revision":None,"strId":"None","bizName":"PARKING_LOGUIDE"}],"strId":"None","bizName":"PARKING_LOT_VO"},
}
