from flask import Flask, render_template,send_file,Response,jsonify
import os
import logging
import datetime
import mysql.connector
from mysql.connector import pooling
#from datetime import datetime
import json
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 获取当前日期，格式化成字符串
today = datetime.date.today().strftime('%Y%m%d')
# 构造模版文件的路径
templates_path = os.path.join('/var/lib/jenkins/workspace/flask/report', 'templates')
# 在模版文件路径不存在的情况下，创建该路径
if not os.path.exists(templates_path):
    os.makedirs(templates_path)

# 设置模版文件路径为app的模版文件夹
app.template_folder = templates_path

@app.route('/')
def index():
    html_files = [f for f in os.listdir(app.template_folder) if f.endswith('.html')]
    links = []
    for f in html_files:
        links.append('<a href="/html/{0}">{0}</a>'.format(f))
    logging.info("打印所有链接%s"%links)
    return '<br>'.join(links)

@app.route('/html/<filename>')
def html_page(filename):
    return render_template(filename)


@app.route('/data', methods=['GET'])
def get_data():
    # 初始化数据库连接池
    db_conn_pool = pooling.MySQLConnectionPool(
        pool_name='mypool',
        pool_size=10,
        host='172.27.0.64',
        port='3306',
        database='iot',
        user='root',
        password='Webuild@666',
        auth_plugin="mysql_native_password"
    )
    # 从连接池中获取数据库连接
    conn = db_conn_pool.get_connection()
    cur=conn.cursor()
    cur.execute('SELECT * FROM iot.auto_report')
    results = cur.fetchall()
    print("results: %s" %results)
    # # 将查询结果转换为 JSON
    response_data = json.dumps(results, default=str)
    conn.close()
    return Response(response=response_data, status=200, mimetype='application/json')


def generate_report():
    # 建立数据库连接
    connection = pymysql.connect(
        host='172.27.0.64',
        user='root',
        port=3306,
        password='Webuild@666',
        db='iot',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        # 执行SQL查询
        with connection.cursor() as cursor:
            # DATE_FORMAT(date_time, '%Y-%m') AS month  统计月数据
            sql = "SELECT project_name, DATE_FORMAT(date_time, '%Y-%m') AS month , SUM(err_count) AS total_err_count FROM auto_report GROUP BY project_name, month"
            cursor.execute(sql)
            results = cursor.fetchall()
    finally:
        # 关闭数据库连接
        connection.close()
    #统计数据
    data_dict = {}
    # 获取所有的月份列表
    months = set([item['month'] for item in results])
    for item in results:
        project_name = item['project_name']
        total_err_count = int(item['total_err_count'])
        month = item['month']
        if project_name in data_dict:
            if month in data_dict[project_name]:
                data_dict[project_name][month].append(total_err_count)
            else:
                # 如果该月份不存在则创建一个空列表
                data_dict[project_name][month] = [total_err_count]
        else:
            # 初始化项目名称的字典
            data_dict[project_name] = {month: [total_err_count]}

    # 补充缺少的月份并且赋值为0
    for project_data in data_dict.values():
        for month in months:
            if month not in project_data:
                project_data[month] = [0]
    print(data_dict)
    #对data_dict再次进行过滤
    filtered_data = {}
    for project, data in data_dict.items():
        filtered_data[project] = []
        for month, counts in data.items():
            filtered_data[project].extend(counts)

    # 构建报告字典
    report = {
        'project_names': list(set(item['project_name'] for item in results)),
        'monthly_err_count': results,
        'months': list(set(item['month'] for item in results)),
        "month_statistical_error": filtered_data,
        "month_statistical_details":data_dict
    }
    return report

@app.route('/generate_report', methods=['GET'])
def get_report():
    # 调用生成报告的函数
    report = generate_report()
    # 以JSON格式返回报告
    return jsonify(report)





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8863,debug=True)
