import pymysql
from Configs import env_c


def del_caseinfo_by_accountid_for_rate(account_id:str):
    """
    删除本条用例需要清除的数据示例
    :param account_id:
    :return:
    """
    #删除cms
    db = pymysql.connect(*env_c.get('db_addr_werun'))
    cursor = db.cursor()
    cursor.execute(f"delete from account_interest where id='{account_id}'")
    cursor.execute(f"delete from flow_interest where id='{account_id}'")
    cursor.execute(f"delete from flow_interest_setting where id='{account_id}'")
    cursor.execute("commit;")
    cursor.close()
    db.close()


def get_client_info_update_approve_id(accountid:str):
    """
    获取数据库数据示例
    :return:
    """
    db = pymysql.connect(*env_c.get('db_addr_werun'))
    cursor = db.cursor()
    cursor.execute(f"select id,business_no from client_update where accountid='{accountid}'")
    index = cursor.description
    column_name = []
    for i in range(len(index)):
        column_name.append(index[i][0])
    row = cursor.fetchone()
    value = dict(zip(column_name, row))
    cursor.close()
    db.close()
    return value