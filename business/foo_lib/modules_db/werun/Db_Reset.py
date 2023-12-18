import pymysql

from Configs import env_c


class DbReset(object):

    @classmethod
    def db_reset(cls):
        #拿到env_c
        #keys
        #判断如果values的type=='list'
        #进去执行sql
        for db_key in env_c.keys():
            if 'list' in str(type(env_c.get(db_key))):
                db = pymysql.connect(*env_c.get(db_key))
                cursor = db.cursor()
                cursor.execute(f"select table_name from information_schema.tables where table_schema='{db_key}'")
                tables = cursor.fetchall()
                for table in tables:
                    if table[0] not in 'sys_dict sys_province sys_city sys_area global_area_code sys_chart_order_api sys_chart_order fac_category oauth_client_details sys_menu sys_resource xxl_job_user xxl_job_group fac_attribute fac_facilities':
                        cursor.execute(f"truncate table {table[0]}")
                    if table[0] == 'sys_chart_order':
                        cursor.execute(f"delete from {table[0]} where template != 1")
                    if table[0] == 'fac_category':
                        cursor.execute(f"delete from {table[0]} where default_flag != 1")
                    if table[0] == 'fac_category':
                        cursor.execute(f"delete from {table[0]} where default_flag != 1")
                    if table[0] == 'fac_attribute':
                        cursor.execute(f"delete from {table[0]} where property_id != 7116")
                    if table[0] == 'fac_facilities':
                        cursor.execute(f"delete from {table[0]} where property_id != 7116")
                cursor.execute("commit;")
                cursor.close()
                db.close()
                pass




if __name__ == '__main__':
    # Db设备智管.db_插入设备执行动作('5','sad','60')
    DbReset.db_reset()
    pass