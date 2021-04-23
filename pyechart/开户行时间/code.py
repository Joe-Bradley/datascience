import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar3D


def read_csv(i):
    df1 = pd.read_csv(i, encoding="utf-8")
    return df1


def print_data(j, df1):
    df1 = df1[df1["开户行所在省"] == j]
    df1 = df1.reset_index(drop=True)
    a = "["
    for i in range(len(df1) - 1):
        a = a + "('" + str(df1["月份"][i]) + "'," + str(df1["账户数量"][i]) + "),"
    a = a + "('" + str(df1["月份"][i + 1]) + "'," + str(df1["账户数量"][i + 1]) + ")"
    a = a + "]"
    return a


def print_variable(i, df2):
    str = print_data(i, df2)
    print("data_" + i + "=" + str)


if __name__ == '__main__':
    df = read_csv("data.csv")
    data = np.array(df)
    data = [[d[0] - 1, d[1]-1, d[2]] for d in data]
    Month = ["20Jan", "20Feb", "20Mar", "20Apr", "20May", "20Jun", "20Jul", "20Aug", "20Sep", "20Oct", "20Nov", "20Dec", "21Jan", "21Feb", "21Mar"]
    Area = ["广东", "江苏", "浙江", "深圳", "福建"]
    (
        Bar3D(init_opts=opts.InitOpts(width="1600px", height="800px")).add(
            series_name="",
            data=data,
            xaxis3d_opts=opts.Axis3DOpts(type_="category", data=Month),
            yaxis3d_opts=opts.Axis3DOpts(type_="category", data=Area),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="分行TOP5-查控次数随时间分布图"),
            visualmap_opts=opts.VisualMapOpts(
                max_=320000,
                range_color=[
                    "#313695",
                    "#4575b4",
                    "#74add1",
                    "#abd9e9",
                    "#e0f3f8",
                    "#ffffbf",
                    "#fee090",
                    "#fdae61",
                    "#f46d43",
                    "#d73027",
                    "#a50026",
                ],
            )
        )
            .render("out.html")
    )
