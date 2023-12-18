import pymysql

from Configs import env_c


class Db智慧安防(object):

    @classmethod
    def db_变更视频巡逻任务开始时间(cls, plan_name:str,start_time: int):
        db = pymysql.connect(*env_c.get('werun_patrol_video'))
        cursor = db.cursor()
        #通过模糊查询inspect_task_name查询到并修改
        cursor.execute(f"select id from patrol_task WHERE patrol_task_name like '%{plan_name}%'")
        task_id = cursor.fetchone()[0]
        #通过id修改时间
        cursor.execute(f"UPDATE patrol_task SET task_plan_start = {str(start_time)} WHERE id='{task_id}'")
        cursor.execute("commit;")
        cursor.close()
        db.close()
