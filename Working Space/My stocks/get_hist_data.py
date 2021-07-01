import baostock as bs
import pandas as pd
import json
from sqlalchemy import create_engine


def get_connection():
    engine = create_engine('mysql+pymysql://root:Qw-1477517@localhost:3306/test?charset=utf8')
    con = engine.connect()  # 创建连接
    return con


def get_hist_data(stockcode):
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    #### 获取沪深A股历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。“分钟线”不包含指数。
    # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
    # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
    rs = bs.query_history_k_data_plus(stockcode,
                                      "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                      start_date='2021-06-01',
                                      end_date='2021-06-30',
                                      frequency="d",
                                      adjustflag="3")
    print('query_history_k_data_plus respond error_code:' + rs.error_code)
    print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    conn = get_connection()
    result.to_sql("stocks", conn, index=False, if_exists='append')
    conn.close()
    print(result)
    #### 登出系统 ####
    bs.logout()


def json_to_str():
    with open("stock_pool.json", 'r') as load_f:
        stock_code = json.load(load_f)
    return stock_code


if __name__ == '__main__':
    # stock_list = json_to_str()
    # for i in list(stock_list):
    #     get_hist_data(i)
    stocks = json_to_str()
    list_name = list(stocks["指数"].keys()).extend(list(stocks["股票"].keys()))
    list_code = list(stocks["指数"].values()).extend(list(stocks["股票"].values()))
    df = pd.DataFrame([[list_name,list_code]],columns=["name","code"])
    print(df)
