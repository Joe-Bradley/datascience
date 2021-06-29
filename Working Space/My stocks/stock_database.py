import db_stocks
import tushare as ts
import pandas as pd
import json
import time

#
# def creat_table():
#     conn = db_stocks.get_connection()
#     c = conn.cursor()
#     c.execute('''CREATE TABLE SZ000002
#                    (ID           INT PRIMARY KEY   NOT NULL,
#                    TIME          TEXT    NOT NULL,
#                    CODE          TEXT    NOT NULL,
#                    HIGH          REAL,
#                    LOW           REAL,
#                    CLOSE         REAL,
#                    OPEN          REAL,
#                    DESCRIPTION CHAR(50));''')
#     conn.commit()
#     conn.close()
#
#
# def insert_sqls():
#     db_stocks.insert_or_update_data("INSERT INTO SZ000002 (ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
#                   VALUES (1, '2019-1-1', 000002, 10.12, 10.12, 10.12, 10.12,'Buy Signal' )")
#
#     db_stocks.insert_or_update_data("INSERT INTO SZ000002 (ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
#                   VALUES (2, '2019-1-2', 000002, 10.13, 10.13, 10.13, 10.13,'Sell Signal' )")
#
#     db_stocks.insert_or_update_data("INSERT INTO SZ000002 (ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
#                   VALUES (3, '2019-1-3', 000002, 10.14, 10.14, 10.14, 10.14,'Buy Signal' )")
#
#     db_stocks.insert_or_update_data("INSERT INTO SZ000002 (ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
#                   VALUES (4, '2019-1-4', 000002, 10.15, 10.15, 10.15, 10.15,'Sell Signal' )")
#
#
# def query_sqls():
#     db_stocks.query_data("select * from SZ000002")
#
#
# def update_sql():
#     db_stocks.insert_or_update_data("UPDATE SZ000002 set DESCRIPTION = 'None' where ID=1")


# engine = create_engine('mysql+pymysql://root:Qw-1477517@localhost:3306/pandas2mysql?charset=utf8')
# con = engine.connect()#创建连接
# token = '6d55067438b3eddc5bb24bd687a5ad92a432f3b9086201e8e3701561'  # 输入你的token
# pro = ts.pro_api(token)  # 初始化pro接口
# df_gldq = pro.daily(ts_code='000651.SZ', start_date='20190101', end_date='20190201')
# print(df_gldq.head())
# df_gldq.to_sql(name='STOCK000651',
#               con=con,
#               index=False,
#               index_label='id',
#               if_exists='append')