import sqlite3
import tushare as ts

conn = sqlite3.connect('stock-data.db')
c = conn.cursor()

# c.execute('''CREATE TABLE SZ000002
#                (ID           INT PRIMARY KEY   NOT NULL,
#                TIME          TEXT    NOT NULL,
#                CODE          TEXT    NOT NULL,
#                HIGH          REAL,
#                LOW           REAL,
#                CLOSE         REAL,
#                OPEN          REAL,
#                DESCRIPTION CHAR(50));''')
# conn.commit()

# c.execute("PRAGMA table_info(SZ000002)")
# print(c.fetchall())

# # 插入表
# c.execute("INSERT INTO SZ000002 (ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
#       VALUES (1, '2019-1-1', 000002, 10.12, 10.12, 10.12, 10.12,'Buy Signal' )")
#
# c.execute("INSERT INTO SZ000002 (ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
#       VALUES (2, '2019-1-2', 000002, 10.13, 10.13, 10.13, 10.13,'Sell Signal' )")
#
# c.execute("INSERT INTO SZ000002 (ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
#       VALUES (3, '2019-1-3', 000002, 10.14, 10.14, 10.14, 10.14,'Buy Signal' )")
#
# c.execute("INSERT INTO SZ000002 (ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
#       VALUES (4, '2019-1-4', 000002, 10.15, 10.15, 10.15, 10.15,'Sell Signal' )")
# conn.commit()

# # 查询表内容
# c.execute("select * from SZ000002")
# print(c.fetchall())

# # 更新表
# c.execute("UPDATE SZ000002 set DESCRIPTION = 'None' where ID=1")
# conn.commit()
# c.execute("select * from SZ000002")
# print(c.fetchall())

# # 选择表
# cursor = conn.execute("SELECT id, time, code, description from SZ000002 where HIGH < 10.15 and HIGH > 10.12")
# for row in cursor:
#     print("ID = {}; TIME = {}; CODE = {}; description = {};".format(row[0],row[1],row[2],row[3]))

# # 删除表数据
# c.execute("DELETE from SZ000002 where ID=2;")
# conn.commit()
# c.execute("select * from SZ000002")
# print(c.fetchall())

# # 删除一个表
# c.execute("drop table SZ000002")
# conn.commit()
# conn.close()

