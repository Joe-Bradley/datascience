import pymysql

HOST = "127.0.0.1"
USER = "root"
PASSWORD = "Qw-1477517"
NAME = "test"
CHARSET = "utf8"


def get_connection():
    db = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=NAME,
        charset=CHARSET
    )
    return db


def query_data(sql):
    conn = get_connection()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        print(cursor.fetchall())
        return cursor.fetchall()
    finally:
        conn.close()


def insert_or_update_data(sql):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()
