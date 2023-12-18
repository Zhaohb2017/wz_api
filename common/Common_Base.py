import base64
import datetime
import json
import logging
import random
import string
import time
import uuid

import xlwt
from xlutils.copy import copy
from unittest import mock

import xlrd
from Crypto.Cipher import AES
from dateutil.relativedelta import relativedelta
from selenium import webdriver

# 因为每个用例模块中,都需要获取浏览器,而浏览器总共有3个.
# 如果手动切换,那么有多少个模块,就需要改多少次
# 所以封装一个函数,作为统一修改浏览器的操作入口
from selenium.webdriver.chrome.options import Options


# 将指定字段替换成唯一值
def replace_unique_param(original_value: str, replace_part: str):
    # 定义一个随机变量
    randomStr = str(int(time.time() * 10000))
    original_value = original_value.replace(replace_part, randomStr)
    return original_value


def is_json(myjson):
    """
    判断是否是Json格式
    :param myjson:
    :return:
    """
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


def get_pack_header(header: dict):
    """
    获取 request Tid Headers
    :param header:
    :return:
    """
    tid = {'tid': str(uuid.uuid4())}
    head = header.copy()
    head.update(tid)
    return head


def date_change(dates: str, years: int = 0, months: int = 0, days: int = 0, hours: int = 0, minutes: int = 0,
                seconds: int = 0):
    """
    在dates日期上做日期或时间的前后变更
    :type dates: 字符类型的“2020-07-24 15:00:00”
    :return:
    """
    d = datetime.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
    date_str = (d + relativedelta(years=years, months=months, days=days, hours=hours, minutes=minutes,
                                  seconds=seconds)).strftime('%Y-%m-%d %H:%M:%S')
    return date_str


def is_number(s):
    """
    判断字符串是否是数字
    :param s:
    :return:
    """
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def traverse_replace_dict_value(data, field, value):
    """替换全部字典参数中的值
    :param data: 嵌套字典列表
    :param field: 列表，某些字段
    :param value: 返回的值
    :return: 列表
    """
    if isinstance(data, list):
        for i in data:
            traverse_replace_dict_value(i, field, value)
    elif isinstance(data, dict):
        if field in data.keys():
            data[field] = value

        for key, value in data.items():
            traverse_replace_dict_value(value, field, value)
    return data


def get_browser(browser_name: str = None, is_local: bool = True, user_agent: str = None):
    logging.info("获取浏览器对象")
    driver = None
    if is_local:
        if browser_name is None:
            driver = webdriver.Chrome()
        elif browser_name == 'chrome':
            driver = webdriver.Chrome()
        elif browser_name == 'firefox':
            driver = webdriver.Firefox()
        elif browser_name == 'app':
            chrome_options = Options()
            chrome_options.add_argument(user_agent)
            driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        options = Options()
        options.add_argument('-headless')
        options.add_argument('-disable-gpu')
        options.add_argument('-no-sandbox')
        if browser_name is None:
            driver = webdriver.Chrome(options=options)
        elif browser_name == 'chrome':
            driver = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            driver = webdriver.Firefox(options=options)
        elif browser_name == 'app':
            options.add_argument(user_agent)
            driver = webdriver.Chrome(options=options)

    logging.info("设置窗口大小1920,1080")
    driver.set_window_rect(
        x=10,
        y=20,
        width=1920,
        height=1080
    )
    logging.info("设置隐式等待10s")
    driver.implicitly_wait(10)
    return driver  # 浏览器获取完毕后,需要返回


# 读取测试数据
def read_txt(filePath):
    resultList = []
    with open(filePath, "r", encoding="utf-8") as file:
        # 遍历文件的每一行
        for line in file:
            # 无效数据,就不加了
            if line[0] == "#":  # #号开头的注释文字不要
                continue
            if line == '\n':  # 这一行为\n不要
                continue
            if line[-1] == "\n":  # 去除最后的\n
                line = line[:-1]
            resultList.append(line.split("|"))  # 每一行都加入列表中
    return resultList  # 返回列表


# 模拟服务器返回数据
def mock_return(request_data, url, method, response_data):
    """
    用于模拟接口返回数据
    :param request_data: 请求数据
    :param url: 请求地址
    :param method: 请求类型“POST” or "GET"
    :param response_data:返回数据
    :return:返回数据response_data
    """
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url, method, request_data)
    return res


# 通过excel文件地址获取excel文件内容,返回为list列表
def get_excel_datas(fileAddr: str) -> list:
    """
    通过excel文件地址获取excel文件内容(所有内容)
    :param fileAddr: 文件地址
    :return: list内容
    """
    rDatas = []
    fileData = xlrd.open_workbook(fileAddr)
    sheetLen = len(fileData.sheets())
    for i in range(sheetLen):
        datas = []
        sheet = fileData.sheets()[i]
        for item in range(sheet.nrows):
            if item == 0:
                continue
            datas.append(sheet.row_values(item))
        rDatas.append(datas)
    return rDatas


# 通过excel文件地址获取excel文件内容,返回为list列表
def get_excel_data(fileAddr: str) -> list:
    """
    通过excel文件地址获取excel文件内容(仅第一个sheet的内容)
    :param fileAddr: 文件地址
    :return: list内容
    """
    datas = []
    fileData = xlrd.open_workbook(fileAddr)
    sheet = fileData.sheets()[0]
    for i in range(sheet.nrows):
        if i == 0:
            continue
        datas.append(sheet.row_values(i))
    return datas


def write_excel_xmhmc(path, value):
    """
    变更项目花名册的项目名称
    :param path:
    :param value:
    :return:
    """
    xlwt.Workbook(encoding='utf-8')
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, 5):
        new_worksheet.write(1, i, value[i])
    new_workbook.save(path)  # 保存工作簿


def write_excel(path, values_list: list):
    """
    变更项目花名册的项目名称
    :param path:
    :param values_list:
    :return:
    """
    xlwt.Workbook(encoding='utf-8')
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(len(values_list)):
        j_length = len(values_list[i])
        for j in range(j_length):
            new_worksheet.write(i + 1, j, values_list[i][j])
    new_workbook.save(path)  # 保存工作簿


# 通过json文件获取json数据
def getJsonFromFile(files: str):
    """
    通过json文件获取json数据
    :param files: 文件地址
    :return: dict 数据字典
    """
    datas = {}
    with open(files, "r", encoding="utf-8") as fp:
        datas = json.load(fp)
    return datas


# 漂亮打出Json字符
def pprint_json(jsony, msg=""):
    json1 = json.dumps(jsony, sort_keys=True, indent=4, separators=(',', ': '))
    logging.info(msg + json1)


# 获取几天前的日期
def get_date_ago(days: int):
    # 先获得时间数组格式的日期
    date_ago = (datetime.datetime.now() - datetime.timedelta(days=days))
    # 转换为其他字符串格式
    return date_ago.strftime("%Y-%m-%d")


# 首先将图片读入
# 由于要发送json，所以需要对byte进行str解码
def getByte(path):
    with open(path, 'rb', ) as f:
        img_byte = base64.b64encode(f.read())
    img_str = img_byte.decode('ascii')
    return img_str


# 设置偏移量
def pkcs7_padding(data, blocksize=32):
    length = len(data)
    pad = blocksize - (length % blocksize)
    data = data + chr(pad) * pad
    return data.encode('ascii')


# 加密函数
def encrypt():
    text = str(time.time()).split('.')[0]
    key = 'GtoBDQxYXdn1rSxd'.encode('utf-8')
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, key)
    text = pkcs7_padding(text, 16)
    cipher_text = cryptos.encrypt(text)
    return base64.b64encode(cipher_text)


# 打印接口参数
def logging_api_info(api_name: str, api_address: str, api_header: str, api_response: str = None, api_param: str = None,
                     request_method=None):
    logging.info(f'{api_name} 接口：{api_address}')
    logging.info(f'{api_name} 请求方法：{request_method}')
    logging.info(f'{api_name} 请求头：{api_header}')
    logging.info(f'{api_name} 请求参数：{api_param}')
    logging.info(f'{api_name} 返回结果：{api_response}')
    logging.info("=" * 100 + "\n")


def logging_api_error(err, api_name: str, api_address: str, api_header: str, api_response_code: str = None,
                      api_param: str = None, request_method=None):
    logging.error(f'请求报错了：{err}\n,详细信息如下: \n')
    logging.error(f'{api_name} 接口：{api_address}')
    logging.error(f'{api_name} 请求方法：{request_method}')
    logging.error(f'{api_name} 请求头：{api_header}')
    logging.error(f'{api_name} 请求参数：{api_param}')
    logging.error(f'{api_name} 返回状态码：{api_response_code}')


# 替换Json中某个字段的值，数据传递，机构开户有使用
def replace_dict_values(o_dict: dict, keys: list, values: list):
    for i in range(len(keys)):
        if o_dict.get(keys[i]) is not None:
            o_dict[keys[i]] = values[i]
    return o_dict
    pass


# 将字典内数据转换成Multipart可识别的参数
def multipart_list_transition(o_dict: dict):
    new_dict = {}
    for k, v in o_dict.items():
        if isinstance(v, list):
            result_dict = {}
            for i in range(len(v)):
                result_dict.setdefault(f'{k}[{i}]', v[i])
            new_dict.update(result_dict)
        else:
            new_dict.setdefault(k, v)
    return new_dict
    pass


# 创建随机手机号
def create_phone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


# 创建随机邮箱
def create_email():
    email_len = random.randint(6, 12)  # 指定一个范围随机取整数
    email_end = random.choice(('@163.com', '@qq.com', '@sina.com', '@126.com'))  # 随机取一个元素
    # 在小写、大写、特殊字符、数字里分别每样取一个字符，长度为4
    email_s = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(
        string.digits)
    # 剩下的2-8个字符在大小写、特殊字符、数字中随机取出来
    str = string.digits + string.ascii_letters
    str_len = email_len - 4
    email_e = random.sample(str, str_len)  # 随机选取几个元素，返回list
    email_start = list(email_s) + email_e  # 字符串转list
    random.shuffle(email_start)  # 打乱列表，返回值为空
    email = ''.join(email_start) + email_end  # 一个完整的邮箱号  list转字符串
    return email


def get_timestamp(hour=0, minute=0, second=0, microsecond=0):
    """获取时间搓"""
    current_time = datetime.datetime.now()
    # 将当前时间的时、分、秒、微秒设置为0
    current_time = current_time.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)
    # 正常时间戳*1000，如果不需要删除*1000
    current_timestamp = int(current_time.timestamp() * 1000)
    return current_timestamp


if __name__ == '__main__':
    print(get_timestamp(hour=23, minute=59, second=59, microsecond=59))

