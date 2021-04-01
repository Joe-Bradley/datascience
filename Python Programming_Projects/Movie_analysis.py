# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:20:28 2019

@author: lenovo
"""

from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import wordcloud
import PIL

########################################################
# 数据处理
plt.rcParams['savefig.dpi'] = 150
plt.rcParams['figure.dpi'] = 150
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']
df = pd.read_csv("18MovieMarket.csv", encoding="gb18030")

movie_name = []
movie_days_count = []
movie_rank_count = []
movie_rates_count = []
movie_money_count = []
movie_people_watching_count = []

for i in range(880):
    a = df.iat[i, 2]
    if a not in movie_name:
        movie_name.append(a)

for i in range(len(movie_name)):
    m = 0
    for j in range(880):
        if movie_name[i] == df.iat[j, 2]:
            m = m + 1
    movie_days_count.append(m)

for i in range(len(movie_name)):
    m = 0
    for j in range(880):
        if movie_name[i] == df.iat[j, 2]:
            m = m + df.iat[j, 10]
    movie_rank_count.append(m)

for i in range(len(movie_name)):
    m = 0
    for j in range(880):
        if movie_name[i] == df.iat[j, 2]:
            if df.iat[j, 8] == 0:
                m = m + 3.89
            else:
                m = m + df.iat[j, 8]
    movie_rates_count.append(m)

for i in range(len(movie_name)):
    m = 0
    for j in range(880):
        if df.at[j, 'name'] == movie_name[i]:
            m = m + df.at[j, 'day_amount']
    movie_money_count.append(m)

for i in range(len(movie_name)):
    m = 0
    for j in range(880):
        if df.at[j, 'name'] == movie_name[i]:
            m = m + df.at[j, 'day_amount'] / df.at[j, 'avg_price']
    movie_people_watching_count.append(m)

a_array = np.array(
    [movie_days_count, movie_money_count, movie_people_watching_count, movie_rank_count, movie_rates_count])
a_df = pd.DataFrame(a_array.T, columns=['days', 'money', 'watching', 'rank', 'rates']).astype("float")
a_df.insert(0, 'name', movie_name)
###############################################################
# 统计上映天数
b1_df = a_df[a_df['days'] > 22].sort_values(by='days')
c1_df = pd.DataFrame()
c1_df['total days'] = b1_df['days']
c1_df.index = b1_df['name']
c1_df.plot(kind="bar")
plt.xlabel("电影名字")
plt.ylabel("上映时间(天)")
plt.title("TOP10上映天数")
#############################################################
# 统计平均票房
b2_df = a_df[a_df['money'] > 26000].sort_values(by='money')
c2_df = pd.DataFrame()
c2_df['total money'] = b2_df['money']
c2_df.index = b2_df['name']
c2_df.plot(kind="bar")
plt.xlabel("电影名字")
plt.ylabel("票房收入(万元)")
plt.title("TOP10电影票房")
##########################################################
# 实际观影人数
b3_df = a_df[a_df['watching'] > 700].sort_values(by='watching')
c3_df = pd.DataFrame()
c3_df['total watching'] = b3_df['watching']
c3_df.index = b3_df['name']
c3_df.plot(kind="bar")
plt.xlabel("电影名字")
plt.ylabel("观看人次(万次)")
plt.title("TOP10电影观看人次")
########################################################
# 上映时间 vs 票房收入
b4_df = a_df[a_df['days'] > 15].sort_values(by='days')
c4_df = pd.DataFrame()
c4_df['total money'] = b4_df['money']
c4_df['total days'] = b4_df['days']
c4_df.index = b4_df['name']

data = b4_df
name = b4_df['name']
VI = b4_df['money']
VC = b4_df['days']

w = 1
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.spines['top'].set_color('none')
ax1.set_ylim(0, max(VC) + 10)
ax1.xaxis.set_ticks_position('bottom')
ax1.spines['bottom'].set_position(('data', 0))
ax1.set_xticks(np.arange(0, len(name) * 3, 3))
ax1.set_xticklabels(name, ha='center', fontsize=9, rotation=90)
plt.xlabel("电影名字")
plt.ylabel("上映时间(天)")
idx = np.arange(w, len(name) * 3 + w, 3)
plt.bar(idx - 0.5, VC, width=w, color='red')

ax2 = ax1.twinx()
ax2.spines['bottom'].set_position(('data', 0))
ax2.set_ylim(0, max(VI) + 10000)
ax2.set_xticks(np.arange(0, len(name) * 3, 3))
ax2.set_xticklabels(name, ha='center', fontsize=9, rotation=90)
plt.xlabel("电影名字")
plt.ylabel("观看人次(万次)")
plt.bar(idx - 1.5, VI, width=w)
plt.title("上映时间 VS 票房收入")
plt.show()
##################################################################
# 上映时间 VS 观看人次
b4_df = a_df[a_df['days'] > 15].sort_values(by='days')
c4_df = pd.DataFrame()
c4_df['total watching'] = b4_df['watching']
c4_df['total days'] = b4_df['days']
c4_df.index = b4_df['name']

data = b4_df
name = b4_df['name']
VI = b4_df['watching']
VC = b4_df['days']

w = 1
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.spines['top'].set_color('none')
ax1.set_ylim(0, max(VC) + 10)
ax1.xaxis.set_ticks_position('bottom')
ax1.spines['bottom'].set_position(('data', 0))
ax1.set_xticks(np.arange(0, len(name) * 3, 3))
ax1.set_xticklabels(name, ha='center', fontsize=9, rotation=90)
plt.xlabel("电影名字")
plt.ylabel("上映时间(天)")
idx = np.arange(w, len(name) * 3 + w, 3)
plt.bar(idx - 0.5, VC, width=w, color='red')

ax2 = ax1.twinx()
ax2.spines['bottom'].set_position(('data', 0))
ax2.set_ylim(0, max(VI) + 1000)
ax2.set_xticks(np.arange(0, len(name) * 3, 3))
ax2.set_xticklabels(name, ha='center', fontsize=9, rotation=90)
plt.xlabel("电影名字")
plt.ylabel("观看人次(万次)")
plt.bar(idx - 1.5, VI, width=w)

plt.title("上映时间 VS 观看人次")
plt.show()
#############################################################
# 统计累计票房图
df = pd.read_csv("MovieMarket.csv", encoding="gb18030")
movie_name = ['海王', '影', '无名之辈', '嗝嗝老师', '找到你', '毒液：致命守护者', '无双']
t = movie_name  # [-1:0:-1]
fig = plt.figure(figsize=(10, 6))
for i in range(7):
    df1 = df[df['name'] == t[i]]
    lenth = len(df1['name'])
    plt.plot(np.arange(lenth), df1['total'])
    plt.text(lenth, df1.iat[lenth - 1, 5], t[i], ha='center', va='bottom', fontsize=15)
plt.xlabel("累计上映时间(天)", fontsize=15)
plt.ylabel("累计票房(万元)", fontsize=15)
plt.title("累计票房统计", fontsize=15)
plt.show()
############################################################
# 生成词云
b5_df = a_df[a_df['watching'] > 300].sort_values(by='watching')
c5_df = pd.DataFrame()
c5_df['total watching'] = b5_df['watching']
c5_df['total rank'] = b5_df['rank']
c5_df['total rates'] = b5_df['rates']
c5_df['days'] = b5_df['days']
c5_df['name'] = b5_df['name']
f = 0.327
a = c5_df['days']
a1 = c5_df['total rank'] * (1 - f) * 0.15
a2 = c5_df['total rates'] * f * 0.15
a3 = c5_df['total watching'] / 300 * 0.7
aa = (a1 + a2 + a3) / 34 * 50 // 1
c5_df['final'] = aa
aaa = dict(zip(c5_df['name'], c5_df['final']))

ss = []
for i in range(len(aa)):
    a = c5_df.iat[i, 4]
    b = int(c5_df.iat[i, 5])
    for i in range(b):
        ss.append(a)

image1 = PIL.Image.open('911.jpg')
MASK = np.array(image1)
WC = wordcloud.WordCloud(font_path='C:\\Windows\\Fonts\\msyh.ttc', max_words=2000, mask=MASK, height=400, width=400,
                         background_color='white', repeat=False, mode='RGBA')
con = WC.generate_from_frequencies(aaa)
plt.imshow(con)
plt.axis("off")
############################################################
