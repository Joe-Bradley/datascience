import baostock as bs
import pandas as pd
import pymysql
from sqlalchemy import create_engine, VARCHAR, Float, Integer
import datetime
import time

HOST = "127.0.0.1"
USER = "root"
PASSWORD = "Qw-1477517"
NAME = "test"
CHARSET = "utf8"


# 方法一：用sqlalchemy连接mysql
def get_connection():
    engine = create_engine('mysql+pymysql://root:Qw-1477517@localhost:3306/test?charset=utf8')
    con = engine.connect()
    return con


# 方法二：用pymysql连接mysql
def get_connections():
    db = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=NAME,
        charset=CHARSET
    )
    return db


# 查询
def query_data(sqls):
    conn = get_connections()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sqls)
        return cursor.fetchall()
    finally:
        conn.close()


# 获取data
def get_yesterday_data(stockcode):
    lg = bs.login()
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)
    # 获取沪深A股历史K线数据
    # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。“分钟线”不包含指数。
    # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
    # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
    rs = bs.query_history_k_data_plus(stockcode,
                                      "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,"
                                      "tradestatus,pctChg,isST",
                                      start_date=(datetime.datetime.now() - datetime.timedelta(days=1)).strftime(
                                          "%Y-%m-%d"),
                                      end_date=(datetime.datetime.now() - datetime.timedelta(days=1)).strftime(
                                          "%Y-%m-%d"),
                                      frequency="d",
                                      adjustflag="3")
    print('query_history_k_data_plus respond error_code:' + rs.error_code)
    print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)

    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    conn = get_connection()
    dyadic = mapping_df_types(result)
    result.to_sql("stocks_daily_basics_1", conn, index=False, if_exists='append', dtype=dyadic)
    conn.close()
    print(result)
    bs.logout()


# 数据库ddl设置
def mapping_df_types(df):
    dtypedict = {}
    for i, j in zip(df.dtypes, df.columns):
        if "date" in str(j):
            dtypedict.update({j: VARCHAR(length=30)})
        if "code" in str(j):
            dtypedict.update({j: VARCHAR(length=30)})
        if "open" in str(j):
            dtypedict.update({j: VARCHAR(length=50)})
        if "high" in str(j):
            dtypedict.update({j: VARCHAR(length=50)})
        if "low" in str(j):
            dtypedict.update({j: VARCHAR(length=50)})
        if "close" in str(j):
            dtypedict.update({j: VARCHAR(length=50)})
        if "preclose" in str(j):
            dtypedict.update({j: VARCHAR(length=50)})
        if "volume" in str(j):
            dtypedict.update({j: VARCHAR(length=50)})
        if "amount" in str(j):
            dtypedict.update({j: VARCHAR(length=50)})
        if "adjustflag" in str(j):
            dtypedict.update({j: VARCHAR(length=50)})
        if "turn" in str(j):
            dtypedict.update({j: VARCHAR(length=50)})
        if "tradestatus" in str(j):
            dtypedict.update({j: VARCHAR(length=50)})
        if "pctChg" in str(j):
            dtypedict.update({j: VARCHAR(length=50)})
        if "isST" in str(j):
            dtypedict.update({j: VARCHAR(length=50)})
    return dtypedict


if __name__ == '__main__':
    sql = "select code from stock_name order by code"
    stock_list = query_data(sql)
    # 股票
    for i in list(stock_list[0:-8]):
        j = i["code"][-2:].lower() + i['code'][-3] + i['code'][0:-3]
        get_yesterday_data(j)
        print(j+"已完成")
        time.sleep(0.01)
    # 指数
    for i in list(stock_list[-8:]):
        get_yesterday_data(i["code"])
        print(i["code"]+"已完成")
        time.sleep(0.01)
