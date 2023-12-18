from Configs import env_c

p_login = {
    '登录':{'userName': env_c.get('xxl_job_login').get('username'), 'password':env_c.get('xxl_job_login').get('password'), 'ifRemember': 'on'},
}
#生成任务
p_trigger = {
    # '生成线上巡检任务':{'id':env_c.get('xxl_job_mission').get('线上巡检').get('createTomorrowInspectTask'),'executorParam':'','addressList':''},
    # '定时更新线上巡检任务状态':{'id':env_c.get('xxl_job_mission').get('线上巡检').get('updateInspectTaskStatus'),'executorParam':'','addressList':''},
    # '生成视频巡逻任务':{'id':env_c.get('xxl_job_mission').get('视频巡逻').get('createTomorrowPatrolTask'),'executorParam':'','addressList':''},
    # '定时更新巡逻任务':{'id':env_c.get('xxl_job_mission').get('视频巡逻').get('updatePatrolTaskStatus'),'executorParam':'','addressList':''},
    # '定时更新车辆登记状态':{'id':env_c.get('xxl_job_mission').get('停车管理').get('updateCarAuthStatus'),'executorParam':'','addressList':''},
    '其它任务':{'id':'123','executorParam':'','addressList':''},
}
#列表查询
p_list = {
    '查询保养列表':{'jobGroup':'2','triggerStatus':'-1','jobDesc':'%E8%AE%A1%E5%88%92%E5%90%8D%E7%A7%B0%E4%BB%BB%E5%8A%A1','executorHandler':'','author':'','start':'0','length':'10'},
    '线下巡检定时任务列表':{'jobGroup':'3','triggerStatus':'-1','jobDesc':'%E5%B7%A1%E6%A3%80%E8%AE%A1%E5%88%92%E4%BB%BB%E5%8A%A1','executorHandler':'','author':'','start':'0','length':'10'},
    '通过GROUPID查询列表': {'jobGroup': '2', 'triggerStatus': '-1', 'jobDesc': '', 'executorHandler': '', 'author': '','start': '0', 'length': '10'},
}