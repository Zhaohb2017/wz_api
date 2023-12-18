
#用电能流图
p_ydnlt = {
    '今日':{'cycle':'1','availableTime%5B0%5D':'2022-06-23%2000%3A00%3A00','availableTime%5B1%5D':'2022-06-23%2023%3A59%3A59','start':'2022-01-01%2000%3A00%3A00','end':'2022-12-31%2023%3A59%3A59'},
    '本周':{'cycle':'2','availableTime%5B0%5D':'2022-06-20%2000%3A00%3A00','availableTime%5B1%5D':'2022-06-26%2023%3A59%3A59','start':'2022-01-01%2000%3A00%3A00','end':'2022-12-31%2023%3A59%3A59'},
    '本月':{'cycle':'3','availableTime%5B0%5D':'2022-06-01%2000%3A00%3A00','availableTime%5B1%5D':'2022-06-30%2023%3A59%3A59','start':'2022-01-01%2000%3A00%3A00','end':'2022-12-31%2023%3A59%3A59'},
    '本年':{'cycle':'4','availableTime%5B0%5D':'2022-01-01%2000%3A00%3A00','availableTime%5B1%5D':'2022-12-31%2023%3A59%3A59','start':'2022-01-01%2000%3A00%3A00','end':'2022-12-31%2023%3A59%3A59'},
}
#用能统计
p_yntj = {
    '今日':{'propertyId':'497','energyType':'electricity','cycle':'1'},
    '本周':{'propertyId':'497','energyType':'electricity','cycle':'2'},
    '本月':{'propertyId':'497','energyType':'electricity','cycle':'3'},
    '本年':{'propertyId':'497','energyType':'electricity','cycle':'4'},
}
#单方能耗统计
p_dfnhtj = {
    '今日':{'propertyId':'497','energyType':'electricity','cycle':'1'},
    '本周':{'propertyId':'497','energyType':'electricity','cycle':'2'},
    '本月':{'propertyId':'497','energyType':'electricity','cycle':'3'},
    '本年':{'propertyId':'497','energyType':'electricity','cycle':'4'},
}
#能耗折碳排放趋势
p_nhztpfcs = {
    '01':{'propertyId':'497','energyType':'electricity','cycle':'2'}
}
#能耗折标煤趋势
p_nhzbmqs = {
    '01':{'propertyId':'497','energyType':'electricity','cycle':'2'},
}
#分区用电占比
p_fqydzb = {
    '今日':{'propertyId':'497','energyType':'electricity','cycle':'1'},
    '本周':{'propertyId':'497','energyType':'electricity','cycle':'2'},
    '本月':{'propertyId':'497','energyType':'electricity','cycle':'3'},
    '本年':{'propertyId':'497','energyType':'electricity','cycle':'4'},
}
#分项用电占比
p_fxydzb = {
    '今日':{'propertyId':'497','energyType':'electricity','cycle':'1'},
    '本周':{'propertyId':'497','energyType':'electricity','cycle':'2'},
    '本月':{'propertyId':'497','energyType':'electricity','cycle':'3'},
    '本年':{'propertyId':'497','energyType':'electricity','cycle':'4'},
}
#分区用电趋势
p_fqydqs = {
    '01':{'propertyId':'497','energyType':'electricity','cycle':'2','id':'180','partitionType':'custom'},
}
#分项用电趋势
p_fxydqs = {
    '01':{'propertyId':'497','energyType':'electricity','cycle':'2','groupId':'','id':'12','partitionType':'custom'},
}
#分区用电排名
p_fqydpm = {
    '楼栋今日':{"head":{"current":1,"size":5},"body":{"total":16,"page":1,"rows":5,"cycle":1,"partitionType":"building","pages":4}},
    '楼栋本周':{"head":{"current":1,"size":5},"body":{"total":16,"page":1,"rows":5,"cycle":2,"partitionType":"building","pages":4}},
    '楼栋本月':{"head":{"current":1,"size":5},"body":{"total":16,"page":1,"rows":5,"cycle":3,"partitionType":"building","pages":4}},
    '楼栋今年':{"head":{"current":1,"size":5},"body":{"total":16,"page":1,"rows":5,"cycle":4,"partitionType":"building","pages":4}},
    '房间今日':{"head":{"current":1,"size":5},"body":{"total":3,"page":1,"rows":5,"cycle":1,"partitionType":"room","pages":1}},
    '房间本周':{"head":{"current":1,"size":5},"body":{"total":3,"page":1,"rows":5,"cycle":2,"partitionType":"room","pages":1}},
    '房间本月':{"head":{"current":1,"size":5},"body":{"total":3,"page":1,"rows":5,"cycle":3,"partitionType":"room","pages":1}},
    '房间今年':{"head":{"current":1,"size":5},"body":{"total":3,"page":1,"rows":5,"cycle":4,"partitionType":"room","pages":1}},
}