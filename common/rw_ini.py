#config  配置
#parser  解析器
from configparser import ConfigParser
def read_config(config_file_path:str):
    '''读取配置文件

    :param config_file_path: 路径
    :return:  配置文件对象
    '''
    rc = ConfigParser()  #配置文件对象
    rc.read(config_file_path) #读配置文件
    return rc

def write_config(filePath:str,section,option,value=None):
    '''修改配置文件

    :param filePath:   文件路径
    :param section:    段   [browser]
    :param option:    选项  name
    :param value:     值  chrome
    :return:   None
    '''
    rc = ConfigParser()
    rc.read(filePath)
    s = rc.get(section, option)
    rc.set(section, option, value)
    rc.write(open(filePath, "w", encoding="utf-8"))

# rc = read_config(r"C:\Users\liu\Desktop\代码_liu_q\day9\browser.ini")
# result = rc.getboolean("local","local_browser")
# result = rc.getint("local","wait_time")
# result = rc.get("browser","name")

#如果配置文件读不到,那么使用备用值
# result = rc.get("browser","aaa",fallback="666")
# print(result)