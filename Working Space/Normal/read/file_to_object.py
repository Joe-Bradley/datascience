import pandas as pd
import os


# xls to dataframe
def read_xls(filename, sheet):
    df = pd.read_excel(filename, encoding="utf-8", sheet_name=sheet)
    return df


# csv to dataframe
def read_csv(filename):
    df = pd.read_csv(filename, encoding="utf-8")
    return df


# txt to list
def read_txt(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                file_lines = f.readlines()
    except:
        with open(filename, encoding="gbk") as f:
            for line in f:
                file_lines = f.readlines()
    return file_lines


# read file name list
def read_file_name_list():
    path_list = os.listdir()
    return path_list


# make direction
def mkdir(path):
    isExits = os.path.exists(path)
    if not isExits:
        os.makedirs(path)
        print(path + "创建成功")
        print("文件将放在" + path)
    else:
        print(path + "目录已存在")
        print("文件将放在" + path)
