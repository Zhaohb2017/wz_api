
import Configs


#登陆
p_login = {
    'iot':{'LoginName':'admin','LoginPwdPageConfirm':'Bp123@iot9','validateCode':'','X-Requested-With':'XMLHttpRequest'},
    'gateway':{'LoginName':'admin','LoginPwd':'Bp123@gw','Authorization':''},
}
#新增子系统
p_add_zxt = {
    '01':{'EditType':'Add','SysCode':'autotestCode','SysName':'autotestName','SysDesc':'autotestRemark'},
}
#通过code删除子系统
p_delete_iotZxt = {
    '01':{'sysCode':'SysCode89127067','_':'1657522177986'},
}
#新增模板
p_add_md = {
    '01':{'ID':'','DeviceType':'autotest','used':'0'},
}
#通过id删除设备模版
p_delete_iotMd = {
    '01':{'id':'69','deviceType':'MoBan96154734','_':'1657519958572'},
}
#新增设备服务
p_add_fw = {
    'InfoService':{'ID':'','DeviceType':'MoBandcc9449e','ServiceType':'InfoService','Description':'infoService remark'},
}
#通过id删除设备服务
p_delete_iotFw = {
    '01':{'id':'137','serviceId':'InfoService','_':'1657519958571'},
}
#新增设备属性
p_add_sx = {
    '01':{'ID':'0','Method':'RW','Required':'','DeviceType':'MoBandcfd4e19','ServiceId':'InfoService','PropertyName':'autotestsx','DataType':'int','Min':'0','Max':'20000','Step':'','Unit':'','MaxLength':'','EnumList':'',},
}
#通过id删除设备属性
p_delete_iotSx = {
    '01':{'id':'450','tmp':'0','name':'autotestsx','_':'1657519958570'},
}
#分页查询iot子系统
p_page_iotzxt = {
    '01':{'projectID':'1','SysCode':'','SysName':'SysName','_search':'false','nd':'1656405328769','rows':'15','page':'1','sidx':'SysCode','sord':'desc'},
}
#分页查询模板
p_page_mb = {
    '01':{'projectID':'1','Name':'MoBan5774497d','_search':'false','nd':'1657524156118','rows':'15','page':'1','sidx':'ID','sord':'desc'},
}
#分页查询设备服务
p_page_fw = {
    '01':{'projectID':'1','deviceType':'MoBan5774497d','_search':'false','nd':'1657524511363','rows':'0','page':'1','sidx':'ServiceId','sord':'desc'},
}
#分页查询设备属性id
p_page_sx = {
    '01':{'projectID':'1','deviceType':'MoBan5774497d','serviceId':'InfoService','_search':'false','nd':'1657524613636','rows':'0','page':'1','sidx':'ID','sord':'desc'},
}
#添加产品
p_add_cp = {
    '01':{'ProductName':'chanpinauto','ProductType':'NORMAL','DeviceType':'MoBandcfd4e19','ManufacturerId':'changshangid12','ManufacturerName':'changshangName12','Model':'ChanPinXingHao123','ProtocolType':'','Version':'','Remark':'',},
}
#分页查询产品
p_page_cp = {
    '01':{'projectID':'1','ProductName':'ChanPinName972b77e8','ProductType':'','_search':'false','nd':'1657504647720','rows':'15','page':'1','sidx':'ID','sord':'desc'},
}
#删除产品
p_delete_iotCp = {
    '01':{'id':'75','_':'1657519958566'},
}
#新增iot注册设备
p_add_zcsb = {
    # '01':{'gwType':'','ID':'','SensorId':'','Name':'shebeiName','Description':'SheBeiMiaoShu','gw':'0','gatewayType':'Basepoint','GateWayId':'','Subsystem':'','ProductId':'1ce7ca7d-fe3c-4952-9acd-0c4c3ef94a8d','Mac':'MACAddress','GroupId':'','Location':'','DeviceType':'MoBan96822436','Model':'ChanPinXingHao96822436','ProtocolType':'','ManufacturerId':'ChangShangId96822436','ManufacturerName':'ChangShangName96822436'},
    '01':{'gwType':'','ID':'','SensorId':'','Name':'SheBeiName','Description':'MiaoShu','gw':'1','gatewayType':'Basepoint','GateWayId':f'{Configs.env_c.get("iot_gateway_id")}','Subsystem':'SysCode9409779f','ProductId':'8f2f12c1-d9d1-45d2-9736-ea605957b934','Mac':'MacAddress','GroupId':'','Location':'weizhi','DeviceType':'MoBan9409779f','Model':'ChanPinXingHao9409779f','ProtocolType':'','ManufacturerId':'ChangShangId9409779f','ManufacturerName':'ChangShangName9409779f'},
}
#删除iot注册设备
p_delete_iotDev = {
    '01':{'id':'129','sensorId':'0e1d23de-aeb0-4bd8-8e68-e63fb72d8a3b','gateWayId':'95ee8ec2-744a-4ed1-a5c3-3419ebaa974f','gwType':'1','name':'SheBeiName8aee08e1','deviceType':'MoBan8aee08e1','mac':'Mac8aee08e1','_':'1657618805145'},
}
#分页查询注册设备
p_page_zcsb = {
    '01':{'projectID':'1','sName':'SheBeiNameff191247','sgwType':'','sProduct':'','sDeviceType':'','Model':'','sSubsystem':'','Gateway':'','sGroup':'','_search':'false','nd':'1657506839072','rows':'15','page':'1','sidx':'CreateTime','sord':'desc'},
}
#新增网关子系统
p_add_gtzxt = {
    # '01':{'SubSystemID':'','SubSystemName':'autotest_system','IsEnabled':'true','IsReport':'true','IsTimerReport':'true','TimerReportSec':'10','IOCollectType':'ModbusTcp','IOCollectConfigJson':f'%7B%22ServerIP%22%3A%22{Configs.env_c.get("modbus_ip")}%22%2C%22ServerPort%22%3A{Configs.env_c.get("modbus_port")}%2C%22ModeType%22%3A%222%22%2C%22ReadTimeout%22%3A3000%2C%22ReadMaxCount%22%3A125%2C%22ReadWaitMs%22%3A0%2C%22ConnectedWaitMs%22%3A0%2C%22IsOneGroup%22%3A%22true%22%2C%22IsExReconnect%22%3A%22true%22%2C%22IOCollectRate%22%3A5%2C%22IsDebug%22%3A%22true%22%7D','Authorization':'bearer a53a33b077284573a8d7a7167a69b151'},
    '01':{'SubSystemID':'','SubSystemName':'autotest_system','IsEnabled':'true','IsReport':'true','IsTimerReport':'true','TimerReportSec':'10','IOCollectType':'ModbusTcp','IOCollectConfigJson':str({"ServerIP":Configs.env_c.get("modbus_ip"),"ServerPort":Configs.env_c.get("modbus_port"),"ModeType":"2","ReadTimeout":3000,"ReadMaxCount":125,"ReadWaitMs":0,"ConnectedWaitMs":0,"IsOneGroup":"true","IsExReconnect":"true","IOCollectRate":1,"IsDebug":"true"}),'Authorization':'bearer+a53a33b077284573a8d7a7167a69b151'},
}
#分页查询网关子系统
p_page_gtzxt = {
    '01':{'page':'1','limit':'20'},
}
#网关-分页查询iot需要导入的设备
p_page_import = {
    '01':{'page':'1','limit':'50','subSystemID':'SysCode1660bba3','deviceType':'','bound':'0'},
}
#网关从iot导入设备
p_load_sb = {
    '01':{'DeviceID':'','DeviceName':'SheBeiName1660bba3','DeviceReportCode':'f20b32e6-9349-4383-89e5-3f601df9574d','SubSystemID':'07','IsDeviceReport':'true'},
}
#分页查询网关子系统设备
p_page_gtsb = {
    '01':{}
}
#添加监控点位
p_add_jkdw = {
    '01':{'DeviceID':'0600001','DeviceName':'SheBeiName4dc12493','DeviceReportCode':'a3947e53-9a4b-4bf6-8eb0-97e748eb7ba9','SubSystemID':'06','IsDeviceReport':'true'},
}
#编辑更新网关点位数据
p_upd_gt_dw = {
    '01':{'TagName':'FuWu977d84e7_ShuXin977d84e7','TagCollectType':'1','TagDataType':'2','TagAccessRight':'2','CommItem':'1.40100.3','CommItemWrite':'','LogicItem':'','SignalId':'','SignalName':'','SubSystemID':'07','DeviceID':'0700001','TagID':'07000010001','TagCollectTypeName':'DictData_TagCollectType_IOCollect','TagDataTypeName':'DictData_TagDataType_Long','TagAccessRightName':'DictData_TagAccessRight_ReadWrite','Authorization':'bearer+e3f25410b26244af83cf4313ce188037'},
}
#分页查询监控点位
p_page_gtdw = {
    '01':{'DeviceID':'0700001','page':'1','limit':'20','tagName':''},
}
#分页查询监控点位
p_page_jkdw = {
    '01':{'DeviceID':'0700001','page':'1','limit':'20','tagName':''},
}
#重启子系统
p_reset_zxt = {
    '01':{'SubSystemID':'09','SubSystemName':'GSystemNamee1801be2'},
}
#重启网关
p_reset_gt = {

}
#更换项目
p_change_p = {
    '01':{'newPID':'1'},
}
#通过id删除点位
p_delete_gtdw = {
    '01':{'TagID':'06000010001','Authorization':'bearer+e3f25410b26244af83cf4313ce188037'},
}
#通过id删除设备
p_delete_gtsb = {
    '01':{'DeviceID':'0600001','Authorization':'bearer+e3f25410b26244af83cf4313ce188037'},
}
#通过id删除子系统
p_delete_gtzxt = {
    '01':{'SubSystemID':'06','Authorization':'bearer+e3f25410b26244af83cf4313ce188037'},
    '02':{'SubSystemID':'06'},
}