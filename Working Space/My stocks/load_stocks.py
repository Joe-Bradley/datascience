import json


def json_to_str():
    # load: 将文件中的字符串变换为数据类型
    with open("stock_pool.json", 'r') as load_f:
        stock_index = json.load(load_f)
    print(stock_index)  # <class 'dict'>
    # {'指数': {'上证综指': '000001.SH', ..... '上证180': '000010.SH'}, '股票': {'平安银行': '000001.SZ', '万科A': '000002.SZ', .....}}
    print(type(stock_index)) # <class 'dict'>
    print(stock_index['指数']['上证综指']) # sh.000001
    print(stock_index['股票']['平安银行']) # 000001.SZ
    return stock_index

json_to_str()