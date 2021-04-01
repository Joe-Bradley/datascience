# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:42:49 2019

@author: lenovo
"""

import tushare as ts
import time
import pandas as pd

pro = ts.pro_api('6d55067438b3eddc5bb24bd687a5ad92a432f3b9086201e8e3701561')

# 获取18年数据
date1 = []
df1 = pro.bo_daily(date='20181001')
for i in range(10, 13):
    for j in range(1, 32):
        if i < 10:
            m1 = '0' + str(i)
        else:
            m1 = str(i)
        if j < 10:
            m2 = '0' + str(j)
        else:
            m2 = str(j)
        if i in [1, 3, 5, 7, 8, 10, 12]:
            mm = '2018' + m1 + m2
            date1.append(mm)
        if i in [4, 6, 9, 11] and j < 31:
            mm = '2018' + m1 + m2
            date1.append(mm)
        if i == 2 and j < 29:
            mm = '2018' + m1 + m2
            date1.append(mm)
for i in range(2, 93):
    df11 = pro.bo_daily(date=date1[i])
    df1 = df1.append(df11)
    time.sleep(2.5)
    print(i)
df1 = pd.DataFrame(df1)

# 获取19年数据
date2 = []
df2 = pro.bo_daily(date='20190101')
for i in range(1, 6):
    for j in range(1, 32):
        if i < 10:
            m1 = '0' + str(i)
        else:
            m1 = str(i)
        if j < 10:
            m2 = '0' + str(j)
        else:
            m2 = str(j)
        if i in [1, 3, 5, 7, 8, 10, 12]:
            mm = '2019' + m1 + m2
            date2.append(mm)
        if i in [4, 6, 9, 11] and j < 31:
            mm = '2019' + m1 + m2
            date2.append(mm)
        if i == 2 and j < 29:
            mm = '2019' + m1 + m2
            date2.append(mm)
for i in range(2, 151):
    df21 = pro.bo_daily(date=date2[i])
    df2 = df2.append(df21)
    time.sleep(2.5)
    print(i)
df2 = pd.DataFrame(df2)

# 合并数据
df = df1.append(df2)
df.drop("Unnamed: 0", axis=1, inplace=True)
df1.to_csv("18MovieMarket.csv", encoding="gb18030")
df2.to_csv("19MovieMarket.csv", encoding="gb18030")
df.to_csv("MovieMarket.csv", encoding="gb18030")
