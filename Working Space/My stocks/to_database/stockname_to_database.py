import pandas as pd
import tushare as ts
import datetime
from sqlalchemy import create_engine


def get_connection():
    engine = create_engine('mysql+pymysql://root:Qw-1477517@localhost:3306/test?charset=utf8')
    con = engine.connect()  # 创建连接
    print("数据库创建连接成功")
    return con


def df_to_sql_replace(dataframe, tablename):
    con = get_connection()
    dataframe.to_sql(tablename, con, index=False, if_exists='replace')
    con.close()
    print("数据储存成功" + tablename + "\n" + datetime.datetime.now().strftime("%Y%m%d"))


def tushare_to_json():
    token = '6d55067438b3eddc5bb24bd687a5ad92a432f3b9086201e8e3701561'  # 输入你的token
    pro = ts.pro_api(token)
    df = pro.stock_basic(exchange='', list_status='L')
    codes = df.ts_code.values
    names = df.name.values
    stock = dicts(zip(names, codes))
    index = {'上证综指': 'sh.000001',
             '深证成指': 'sz.399001',
             '沪深300': 'sz.000300',
             '创业板指': 'sz.399006',
             '上证50': 'sh.000016',
             '中证500': 'sh.000905',
             '中小板指': 'sz.399005',
             '上证180': 'sh.000010'}
    stock_index = dicts([('指数', index), ('股票', stock)])
    print("获取tushare数据成功")
    return stock_index


def process_stocks_to_df(dicts):
    list_name1 = list(dicts["指数"].keys())
    list_name2 = list(dicts["股票"].keys())
    list_code1 = list(dicts["指数"].values())
    list_code2 = list(dicts["股票"].values())
    list_name1.extend(list_name2)
    list_code1.extend(list_code2)
    dataframe = pd.DataFrame(zip(list_name1, list_code1), columns=["name", "code"])
    dataframe["import_time"] = datetime.datetime.now().strftime("%Y-%m-%d")
    print("组装dataframe成功")
    return dataframe


if __name__ == '__main__':
    dicts = tushare_to_json()
    df = process_stocks_to_df(dicts)
    df_to_sql_replace(df, "stock_name")
