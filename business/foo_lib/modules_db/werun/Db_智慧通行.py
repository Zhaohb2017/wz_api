import pymysql

from Configs import env_c


class Db智慧通行(object):

    @classmethod
    def db_插入停车记录(cls, lot_id:str,propertyId:str):
        db = pymysql.connect(*env_c.get('werun_parking'))
        cursor = db.cursor()
        #通过模糊查询inspect_task_name查询到并修改
        cursor.execute(f"INSERT INTO parking_record VALUES ('1', '{lot_id}', 'E123123', '1', null, null, null, null, null, null, null, '{propertyId}', '0', null, null, null, null, null, null, null);")
        cursor.execute("commit;")
        cursor.close()
        db.close()

    @classmethod
    def db_删除停车记录(cls, lot_id:str):
        db = pymysql.connect(*env_c.get('werun_parking'))
        cursor = db.cursor()
        cursor.execute(f"select * FROM parking_record WHERE parking_lot_id = '{lot_id}'")
        search_data = cursor.fetchall()
        if search_data != ():
            cursor.execute(f"DELETE FROM parking_record WHERE parking_lot_id = '{lot_id}'")
        cursor.execute("commit;")
        cursor.close()
        db.close()

    @classmethod
    def db_插入通行记录(cls, phone:str,propertyId:str):
        db = pymysql.connect(*env_c.get('wz_passage'))
        cursor = db.cursor()
        #通过模糊查询inspect_task_name查询到并修改
        cursor.execute(f"INSERT INTO `passage_access_record` VALUES ('8888', '14196', '2', '584505339391508480', '{phone}', null, '0', '4', '1654092933229', null, '1654092933229', '{propertyId}');")
        cursor.execute("commit;")
        cursor.close()
        db.close()

    @classmethod
    def db_删除通行记录(cls, propertyId:str):
        db = pymysql.connect(*env_c.get('wz_passage'))
        cursor = db.cursor()
        cursor.execute(f"select * FROM passage_access_record WHERE property_id = '{propertyId}'")
        search_data = cursor.fetchall()
        if search_data != ():
            cursor.execute(f"DELETE FROM passage_access_record WHERE property_id = '{propertyId}'")
        cursor.execute("commit;")
        cursor.close()
        db.close()
