import pandas as pd
import json


# write dataframe to excel
def df_to_excel(df, filename):
    try:
        with pd.Excel(filename) as writer:
            df.to_excel(writer)
    finally:
        df.to_excel(filename)


# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
# 'U'       universal newline mode (deprecated)
# write str
def write_str(filename, mode, str):
    with open(filename, mode) as f:
        f.write(str)
    f.close()


# write list
def write_list(filename, mode, list):
    with open(filename, mode) as f:
        f.writelines(list)
    f.close()


# write Json
def list_to_json(dict):
    with open("stock_pool.json", "w", encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4)

# dict = [{'指数':
#                         {'上证综指': 'sh.000001',
#                          '深证成指': 'sz.399001',
#                          '沪深300': 'sz.000300',
#                          '创业板指': 'sz.399006',
#                          '上证50': 'sh.000016',
#                          '中证500': 'sh.000905',
#                          '中小板指': 'sz.399005',
#                          '上证180': 'sh.000010'}},
#                    {'股票':
#                         {'格力电器': '000651.SZ',
#                          '平安银行': '000001.SZ',
#                          '同花顺': '300033.SZ',
#                          '贵州茅台': '600519.SH',
#                          '浙大网新': '600797.SH'}}]


