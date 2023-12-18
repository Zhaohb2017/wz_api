


#新增分组
p_add_group={
    '电量统计':{"statisticsName":"电量统计"}
}
#通过id查询分组
p_search_group={
    '电量统计':{"head":{"current":1,"size":10,"total":1},"body":{"groupId":20}}
}

#修改分组信息
p_upd = {
    '01':{"statisticsName":"电量统计-修改","id":20}
}
#能耗统计图表查询
p_energy_tj = {
    '分项时':{'date%5B0%5D':'2022-06-22','date%5B1%5D':'2022-06-22','start':'2022-06-22','end':'2022-06-22','energyType':'electricity','dimension':'item','cycle':'1','id':'21','partitionType':'building'},
    '分项天':{'date%5B0%5D':'2022-06-22','date%5B1%5D':'2022-06-30','start':'2022-06-22','end':'2022-06-30','energyType':'electricity','dimension':'item','cycle':'3','id':'21','partitionType':'building'},
    '分项周':{'date%5B0%5D':'2022-06-06','date%5B1%5D':'2022-08-05','start':'2022-06-06','end':'2022-08-05','energyType':'electricity','dimension':'item','cycle':'2','id':'21','partitionType':'building'},
    '分项月':{'date%5B0%5D':'2022-07-01','date%5B1%5D':'2022-10-31','start':'2022-07-01','end':'2022-10-31','energyType':'electricity','dimension':'item','cycle':'4','id':'21','partitionType':'building'},
    '分区楼栋时':{'date%5B0%5D':'2022-06-22','date%5B1%5D':'2022-06-22','start':'2022-06-22','end':'2022-06-22','energyType':'electricity','dimension':'partition','cycle':'1','id':'6682','partitionType':'building'},
    '分区楼栋天':{'date%5B0%5D':'2022-06-22','date%5B1%5D':'2022-06-30','start':'2022-06-22','end':'2022-06-30','energyType':'electricity','dimension':'partition','cycle':'3','id':'6682','partitionType':'building'},
    '分区楼栋周':{'date%5B0%5D':'2022-06-01','date%5B1%5D':'2022-08-06','start':'2022-06-01','end':'2022-08-06','energyType':'electricity','dimension':'partition','cycle':'2','id':'6682','partitionType':'building'},
    '分区楼栋月':{'date%5B0%5D':'2022-06-01','date%5B1%5D':'2022-10-27','start':'2022-06-01','end':'2022-10-27','energyType':'electricity','dimension':'partition','cycle':'4','id':'6682','partitionType':'building'},
    '分区楼层时':{'date%5B0%5D':'2022-06-22','date%5B1%5D':'2022-06-22','start':'2022-06-22','end':'2022-06-22','energyType':'electricity','dimension':'partition','cycle':'1','id':'86452','partitionType':'floor'},
    '分区楼层天':{'date%5B0%5D':'2022-06-22','date%5B1%5D':'2022-07-01','start':'2022-06-22','end':'2022-07-01','energyType':'electricity','dimension':'partition','cycle':'3','id':'86452','partitionType':'floor'},
    '分区楼层周':{'date%5B0%5D':'2022-06-01','date%5B1%5D':'2022-08-26','start':'2022-06-01','end':'2022-08-26','energyType':'electricity','dimension':'partition','cycle':'2','id':'86452','partitionType':'floor'},
    '分区楼层月':{'date%5B0%5D':'2022-06-01','date%5B1%5D':'2022-09-30','start':'2022-06-01','end':'2022-09-30','energyType':'electricity','dimension':'partition','cycle':'4','id':'86452','partitionType':'floor'},
    '新增分区时':{'date%5B0%5D':'2022-06-22','date%5B1%5D':'2022-06-22','start':'2022-06-22','end':'2022-06-22','energyType':'electricity','dimension':'partition','cycle':'1','id':'100','partitionType':'custom'},
    '新增分区天':{'date%5B0%5D':'2022-06-22','date%5B1%5D':'2022-06-30','start':'2022-06-22','end':'2022-06-30','energyType':'electricity','dimension':'partition','cycle':'3','id':'100','partitionType':'custom'},
    '新增分区周':{'date%5B0%5D':'2022-06-01','date%5B1%5D':'2022-09-16','start':'2022-06-01','end':'2022-09-16','energyType':'electricity','dimension':'partition','cycle':'2','id':'100','partitionType':'custom'},
    '新增分区月':{'date%5B0%5D':'2022-06-01','date%5B1%5D':'2022-09-30','start':'2022-06-01','end':'2022-09-30','energyType':'electricity','dimension':'partition','cycle':'4','id':'100','partitionType':'custom'},
}
