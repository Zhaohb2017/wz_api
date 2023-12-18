import os

import xlrd


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

# 通过excel文件地址获取excel文件内容,返回为list列表
def read_excel_datas(fileAddr: str, firstSheet: bool = False) -> list:
    """
    通过excel文件地址获取excel文件内容(所有内容)
    :param firstSheet: 是否仅读第一个sheet
    :param fileAddr: 文件地址
    :return: list内容
    """
    rDatas = []
    fileData = xlrd.open_workbook(fileAddr)
    if firstSheet is True:
        sheet = fileData.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            rDatas.append(sheet.row_values(i))
        pass
    else:
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
def read_excel_by_folder(folder_addr: str) -> list:
    """
    通过excel文件夹地址获取excel文件内容(所有内容)
    :param folder_addr: 文件夹地址
    :return: list内容
    """
    datas=[]
    file_list = os.listdir(folder_addr)
    for file_name in file_list:
        datas.extend(read_excel_datas(f'{folder_addr}{file_name}', True))
    return datas
