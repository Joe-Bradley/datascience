import pandas as pd
import pandas_datareader.data as web
import baostock as bs
import tushare as ts
import datetime


pd.set_option('display.expand_frame_repr', False)  # False不允许换行
pd.set_option('display.max_rows', 10)  # 显示的最大行数
pd.set_option('display.max_columns', 6)  # 显示的最大列数
pd.set_option('precision', 2)  # 显示小数点后的位数


# 获取上证综指行情数据 pandas-datareade模块data.DataReader()方法
def pd_data_000001SS():
    df_stockload = web.DataReader("000001.SS", "yahoo", datetime.datetime(2009, 1, 1), datetime.datetime(2019, 6, 1))
    # 查看前几行
    print(df_stockload.head())
    # 查看末尾几行
    print(df_stockload.tail())
    # 查看行索引信息
    print(df_stockload.index)
    # 查看列索引信息
    print(df_stockload.columns)
    # 查看形状
    print(df_stockload.shape)
    # 查看各列数据描述性统计
    print(df_stockload.describe())
    # 查看缺失及每列数据类型
    print(df_stockload.info())


# Tushare Org
def ts_data_sh_hist():
    df_sh_hist = ts.get_hist_data('sh', start='2009-01-01', end='2019-06-01')
    print(df_sh_hist.head())
    print(df_sh_hist.tail())
    print(df_sh_hist.info())
    print(df_sh_hist.axes)


token = '6d55067438b3eddc5bb24bd687a5ad92a432f3b9086201e8e3701561'  # 输入你的token
pro = ts.pro_api(token)  # 初始化pro接口


# Tushare Pro
def ts_data_pro_daily():
    # 获取格力电器日线行情数据
    df_gldq = pro.daily(ts_code='000651.SZ', start_date='20090101', end_date='20190601')
    print(df_gldq.head())
    print(df_gldq.tail())
    print(df_gldq.info())
    print(df_gldq.axes)

    # 行索引时间格式规整化 方法一
    # df_gldq.index = pd.to_datetime(df_gldq.trade_date)
    # df_gldq.drop(axis=1, columns='trade_date', inplace=True)
    # print(df_gldq.head())

    # 行索引时间格式规整化 方法二
    # df_gldq.trade_date = pd.DatetimeIndex(df_gldq.trade_date)
    # df_gldq.set_index("trade_date", drop=True, inplace=True)
    # print(df_gldq.head())

    # 查看行的轴标签
    # df_gldq.sort_index(inplace=True)
    # print(df_gldq.index)

    # 查看行的轴标签
    # df_gldq.index = df_gldq.index.set_names('Date')
    # print(df_gldq.index)

    # 取某几行
    # recon_data = {'High': df_gldq.high, 'Low': df_gldq.low, 'Open': df_gldq.open, 'Close': df_gldq.close, \
    #               'Volume': df_gldq.vol}
    # df_recon = pd.DataFrame(recon_data)
    # print(df_recon.columns)
    # print(df_recon.head())
    # print(df_recon.tail())


# Baostock
def bs_data_sh():
    # 登陆系统
    lg = bs.login()
    # 获取历史行情数据
    fields = "date,open,high,low,close,volume"

    # frequency="d"取日k线，adjustflag="3"默认不复权，1：后复权；2：前复权
    df_bs = bs.query_history_k_data("sh.000001",
                                    fields,
                                    start_date='2009-01-01',
                                    end_date='2019-06-01',
                                    frequency="d",
                                    adjustflag="2")

    data_list = []
    while (df_bs.error_code == '0') & df_bs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(df_bs.get_row_data())
    result = pd.DataFrame(data_list, columns=df_bs.fields)
    result.close = result.close.astype('float64')
    result.open = result.open.astype('float64')
    result.low = result.low.astype('float64')
    result.high = result.high.astype('float64')
    result.volume = result.volume.astype('int')
    result.index = pd.to_datetime(result.date)

    print(result.head())
    print(result.tail())
    print(result.info())
    print(result.axes)

    bs.logout()


