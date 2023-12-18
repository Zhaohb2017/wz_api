import pymysql

from Configs import env_c


class Db设备智管(object):

    @classmethod
    def db_变更线上巡检任务开始时间(cls, plan_name:str,start_time: int):
        db = pymysql.connect(*env_c.get('werun_inspect_online'))
        cursor = db.cursor()
        #通过模糊查询inspect_task_name查询到并修改
        cursor.execute(f"select id from inspect_task WHERE inspect_task_name like '%{plan_name}%'")
        task_id = cursor.fetchone()[0]
        #通过id修改时间
        cursor.execute(f"UPDATE inspect_task SET inspect_plan_start = {str(start_time)} WHERE id='{task_id}'")
        cursor.execute("commit;")
        cursor.close()
        db.close()

    @classmethod
    def db_插入设备执行动作(cls, property_id:str,fac_cate_code: str,fac_cate_id:str,action_id:str=None,attr_code:str=None):
        """
        db_插入设备执行动作
        :param property_id: 项目id
        :param fac_cate_code: 设备编码
        :param fac_cate_id: 设备id
        :param action_id: 执行动作id
        :param attr_code: 执行动作代码
        :return:
        """
        #连接assert库,插入设备执行动化
        db = pymysql.connect(*env_c.get('wz_assets'))
        cursor = db.cursor()
        if action_id is None:
            action_id = '88888'
        if attr_code is None:
            attr_code = 'ZNZMXT_ZMHL_AUTOTEST'
        cursor.execute(f"INSERT INTO fac_attribute VALUES ({action_id},null, '{property_id}', '{fac_cate_code}', '{fac_cate_id}', '开关状态', null, '{attr_code}',null, 'attr', 'int', '', 'RW', '', null, null, null, null, null,'0-关闭、1-开启', '0', null, null, null, null, null, null)")
        cursor.execute("commit;")
        cursor.close()
        db.close()

    @classmethod
    def db_插入设备执行动作数据链路(cls, p_id:str,fac_cate_code: str,fac_cate_id:str,attr_name:str,attr_code:str,access_mode:str,sevice_type:str):
        """
        db_插入设备执行动作
        :param p_id: 项目id
        :param fac_cate_code: 设备编码
        :param fac_cate_id: 设备id
        :param attr_name: 执行动作名称
        :param attr_code: 执行动作代码
        :param access_mode: 执行模式 RO:只读 RW:可读可写
        :param sevice_type: 服务类型 SetService设置参数 InfoService读取服务 AlarmService告警上报
        :return:
        """
        #连接assert库,插入设备执行动化
        db = pymysql.connect(*env_c.get('wz_assets'))
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO wz_assets.fac_attribute (property_id,fac_cate_code,fac_cate_id,attr_name,attr_code,attr_type,data_type,access_mode,iot_service) values({p_id},'{fac_cate_code}',{fac_cate_id},'{attr_name}','{attr_code}','attr','int','{access_mode}','{sevice_type}')")
        cursor.execute("commit;")
        cursor.close()
        db.close()

    @classmethod
    def db_删除设备执行动作(cls, fac_cate_id:str):
        """
        db_删除设备执行动作
        :param fac_cate_id:
        :return:
        """
        #连接assert库,删除设备执行动化
        db = pymysql.connect(*env_c.get('wz_assets'))
        cursor = db.cursor()
        cursor.execute(f"select * FROM fac_attribute WHERE fac_cate_id = '{fac_cate_id}'")
        search_data = cursor.fetchall()
        if search_data != ():
            cursor.execute(f"DELETE FROM fac_attribute WHERE fac_cate_id = '{fac_cate_id}'")
        cursor.execute("commit;")
        cursor.close()
        db.close()
        pass

    @classmethod
    def db_变更线下巡检记录状态(cls, faclog_id:str,log_status: str):
        db = pymysql.connect(*env_c.get('werun_inspect_offline'))
        cursor = db.cursor()
        cursor.execute(f"UPDATE tb_schedule_fac_log SET sch_eqt_log_status = '{log_status}' WHERE id='{faclog_id}'")
        cursor.execute("commit;")
        cursor.close()
        db.close()

    @classmethod
    def db_变更保养任务开始时间(cls, plan_name:str,start_time: int):
        db = pymysql.connect(*env_c.get('werun_maintenance'))
        cursor = db.cursor()
        #通过模糊查询inspect_task_name查询到并修改
        cursor.execute(f"select id from tb_maintenance_task WHERE maintenance_task_name like '%{plan_name}%'")
        task_id = cursor.fetchone()[0]
        #通过id修改时间
        cursor.execute(f"UPDATE tb_maintenance_task SET term_of_validity_start = {str(start_time)} WHERE id='{task_id}'")
        cursor.execute(f"UPDATE tb_maintenance_task SET maintenance_task_status = 4 WHERE id='{task_id}'")
        cursor.execute("commit;")
        cursor.close()
        db.close()



if __name__ == '__main__':
    # Db设备智管.db_插入设备执行动作('5','sad','60')
    Db设备智管.db_删除设备执行动作('60')
    pass