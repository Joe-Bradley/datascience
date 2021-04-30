from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd


def read_csv(i):
    df1 = pd.read_csv(i, encoding="utf-8")
    return df1


def map_china(data1) -> Map:
    c = (
        Map()
            .add(series_name="查询次数", data_pair=data1, maptype="china", zoom=1, center=[105, 38])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="查询次数分布图"),
            visualmap_opts=opts.VisualMapOpts(max_=50000, is_piecewise=True,
                                              pieces=[{"max": 100, "min": 0, "label": "0-9", "color": "#FFE4E1"},
                                                      {"max": 999, "min": 100, "label": "100-999", "color": "#FF7F50"},
                                                      {"max": 5999, "min": 1000, "label": "1000-5999",
                                                       "color": "#F08080"},
                                                      {"max": 9999, "min": 6000, "label": "6000-9999",
                                                       "color": "#CD5C5C"},
                                                      {"max": 99999, "min": 10000, "label": ">=10000",
                                                       "color": "#8B0000"}]
                                              )
        )
    )
    return c


def print_data(df1):
    a = "["
    for i in range(len(df1) - 1):
        a = a + "('" + df1["开户行所在省"][i] + "'," + str(df1["账户数量"][i]) + "),"
    a = a + "('" + df1["开户行所在省"][i + 1] + "'," + str(df1["账户数量"][i + 1]) + ")"
    a = a + "]"
    print(a)


if __name__ == '__main__':
    #df = read_csv("data.csv")
    #df["开户行所在省"] = df.apply(lambda x: x["开户行所在省"][4:6], axis=1)
    #print_data(df)
    data = [('安徽', 3331), ('湖北', 4658), ('海南', 1520), ('江苏', 8284), ('内蒙古', 838),
            ('浙江', 7605), ('云南', 4117), ('新疆', 1788), ('青海', 145), ('四川', 4882),
            ('陕西', 2268), ('广东', 27829), ('福建', 8544), ('湖南', 4861), ('天津', 1200),
            ('山东', 3680), ('青岛', 937), ('西藏', 29), ('河南', 5238), ('山西', 1671),
            ('重庆', 1995), ('黑龙江', 1668), ('吉林', 1130), ('宁夏', 254), ('辽宁', 2539),
            ('江西', 3750), ('甘肃', 530), ('广西', 3044), ('上海', 3275), ('贵州', 1135),
            ('北京', 4049), ('河北', 3907)]
    d_map = map_china(data)
    d_map.render("out.html")
