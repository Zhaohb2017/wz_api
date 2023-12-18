

#新增
p_add = {
    '设备报单':{"workOrderType":1,"handleTime":1,"timelyRate":5,"orderName":"工单名称","orderContent":"工单内容123","expectedStartTime":1651075200000,"facCateId":26837,"facName":"设备名称2b160b55-c345-4abb-a498-5d80fec41647","facId":"8666","dispatchUserId":4818,"dispatchUserName":"nickNameaa2f9a98-8af6-48b7-bd8b-535fc8a9cef0","workOrderInOut":0,"buildingFloorSpaceId":None,"handleId":1817,"handleName":"lichang1"},
    '非设备报单':{"workOrderType":2,"handleTime":1,"timelyRate":5,"orderName":"工单名称123","orderContent":"工单内容123321","expectedStartTime":1651075200000,"facCateId":None,"dispatchUserId":4822,"dispatchUserName":"nickName641dfea8-bac6-448c-b1be-3aad3575733b","workOrderInOut":0,"buildingFloorSpaceId":None,"handleId":1817,"handleName":"lichang1"},
    '不限时外部工单':{"workOrderType":2,"handleTime":"","timelyRate":"50","orderName":"工单名称123","orderContent":"asdadsfasfd","expectedStartTime":1651075200000,"proposeUserName":"提单人123123","proposeUserContact":"18812341234","facCateId":None,"dispatchUserId":4824,"dispatchUserName":"nickNamef135423d-5db7-4527-9679-f5363df066d9","workOrderInOut":1,"buildingFloorSpaceId":None,"handleId":1817,"handleName":"lichang1"},
}


p_page = {
    '设备报单':{"head":{"current":1,"size":10},"body":{"totalCount":1,"workOrderType":"1","startDate":"","endDate":"","userId":"1817"}},
    '非设备报单':{"head":{"current":1,"size":10},"body":{"totalCount":0,"workOrderType":"2","startDate":"","endDate":"","userId":"1817"}},
    '内部工单':{"head":{"current":1,"size":10},"body":{"totalCount":1,"workOrderInOut":"0","startDate":"","endDate":"","userId":"1817"}},
    '外部工单':{"head":{"current":1,"size":10},"body":{"totalCount":1,"workOrderInOut":"1","startDate":"","endDate":"","userId":"1817"}},
    '待分派':{"head":{"current":1,"size":10},"body":{"totalCount":1,"state":"1","startDate":"","endDate":"","userId":"1817"}},
    '工单名称':{"head":{"current":1,"size":10},"body":{"totalCount":1,"orderInfo":"工单","startDate":"","endDate":"","userId":"1817"}},
    '接单人':{"head":{"current":1,"size":10},"body":{"totalCount":1,"pickUpPersonUserId":4826,"startDate":"","endDate":"","userId":"1817"}},
}

