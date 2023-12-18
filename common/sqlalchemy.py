import logging
import mysql.connector
from mysql.connector import pooling
from datetime import datetime
from common.Encryption_AES import decrypt, md5_encode
from Configs import sign

password_aes = b'9Tl47yR90UsuMLb9BJR1ig=='
username_aes = b'3dDjOr6INW5PmGfHVgA09w=='
host_aes = b'A9E8ML4mD2XVvCjOh1eSmQ=='
secret_key = md5_encode(sign)
password = decrypt(encoded_text=password_aes, key=secret_key)
username = decrypt(encoded_text=username_aes, key=secret_key)
host_new = decrypt(encoded_text=host_aes, key=secret_key)
# formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
formatted_date = datetime.now().strftime("%Y-%m-%d")

class SQLMain:
    def __init__(self):
        # 初始化数据库连接池
        self.db_conn_pool = pooling.MySQLConnectionPool(
            pool_name='mypool',
            pool_size=10,
            host=host_new.decode('utf-8'),
            port='3306',
            database='iot',
            user=username.decode('utf-8'),
            password=password.decode('utf-8'),
            auth_plugin="mysql_native_password"
        )
        # 初始化日志配置
        logging.basicConfig(
            filename='application.txt',
            filemode='a',
            format='%(asctime)s %(levelname)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.INFO
        )

    def sql_main(self, project_name):
        logging.info('MyScript started')
        # 从连接池中获取数据库连接
        conn = self.db_conn_pool.get_connection()
        cur = conn.cursor()
        try:
            # 查询 b 数据库表，判断是否有数据
            query_sql = 'SELECT COUNT(*) FROM iot.auto_report WHERE project_name = %s AND date_time = %s'
            logging.info('query_sql %s' % query_sql)
            cur.execute(query_sql, (project_name, formatted_date))
            count = cur.fetchone()[0]
            print(count)

            if count == 0:
                # 如果没有数据，则进行写入
                # 如果没有数据，则进行写入
                insert_sql = "INSERT INTO iot.auto_report(project_name, date_time, err_count) VALUES ('%s', '%s', 1);" % (
                    project_name, formatted_date)
                cur.execute(insert_sql)
                conn.commit()
                logging.info('Data inserted into table auto_report')
        except Exception as e:
            logging.error(f'Error occurred while writing data: {e}')
            conn.rollback()

        finally:
            # 释放数据库连接回连接池
            conn.close()
            logging.info('MyScript finished')


if __name__ == '__main__':
    main()
