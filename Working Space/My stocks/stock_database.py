import db_stocks
import tushare as ts
from sqlalchemy import create_engine
import pandas as pd
import json
import time


def creat_table():
    conn = db_stocks.get_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE SZ000002
                   (ID           INT PRIMARY KEY   NOT NULL,
                   TIME          TEXT    NOT NULL,
                   CODE          TEXT    NOT NULL,
                   HIGH          REAL,
                   LOW           REAL,
                   CLOSE         REAL,
                   OPEN          REAL,
                   DESCRIPTION CHAR(50));''')
    conn.commit()
    conn.close()


def insert_sqls():
    db_stocks.insert_or_update_data("INSERT INTO SZ000002 (ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
                  VALUES (1, '2019-1-1', 000002, 10.12, 10.12, 10.12, 10.12,'Buy Signal' )")

    db_stocks.insert_or_update_data("INSERT INTO SZ000002 (ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
                  VALUES (2, '2019-1-2', 000002, 10.13, 10.13, 10.13, 10.13,'Sell Signal' )")

    db_stocks.insert_or_update_data("INSERT INTO SZ000002 (ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
                  VALUES (3, '2019-1-3', 000002, 10.14, 10.14, 10.14, 10.14,'Buy Signal' )")

    db_stocks.insert_or_update_data("INSERT INTO SZ000002 (ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
                  VALUES (4, '2019-1-4', 000002, 10.15, 10.15, 10.15, 10.15,'Sell Signal' )")


def query_sqls():
    db_stocks.query_data("select * from SZ000002")


def update_sql():
    db_stocks.insert_or_update_data("UPDATE SZ000002 set DESCRIPTION = 'None' where ID=1")


def json_to_str():
    with open("stock_pool.json", 'r') as load_f:
        stock_index = json.load(load_f)
    return stock_index


def stock_to_sql_for(table_name, con_name, start='20190101', end='20190201'):
    stock_code = json_to_str()
    for code in stock_code['股票'].values():
        try:
            data = pro.daily(ts_code=code, start_date=start, end_date=end)
            time.sleep(0.2)
            data.to_sql(table_name, con_name, index=False, if_exists='append')
            print("right code is %s" % code)
        except:
            print("error code is %s" % code)


def get_connection():
    engine = create_engine('mysql+pymysql://root:Qw-1477517@localhost:3306/test?charset=utf8')
    con = engine.connect()  # 创建连接
    return con


token = '6d55067438b3eddc5bb24bd687a5ad92a432f3b9086201e8e3701561'  # 输入你的token
pro = ts.pro_api(token)  # 初始化pro接口
con = get_connection()
# stock_to_sql_for("stocks", con, start='20190101', end='20190201')
con.close()

