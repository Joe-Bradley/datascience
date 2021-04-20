from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd

def read_csv(i):
    df1 = pd.read_csv(i, encoding="utf-8")
    return df1

def map_china(data) -> Map:
    c = (
        Map()
            .add(series_name="查询次数", data_pair=data, maptype="china", zoom=1, center=[105, 38])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="查询次数分布图"),
            visualmap_opts=opts.VisualMapOpts(max_=50000, is_piecewise=True,
                                              pieces=[{"max": 100, "min": 0, "label": "0-9", "color": "#FFE4E1"},
                                                      {"max": 999, "min": 100, "label": "100-999", "color": "#FF7F50"},
                                                      {"max": 5999, "min": 1000, "label": "1000-5999", "color": "#F08080"},
                                                      {"max": 9999, "min": 6000, "label": "6000-9999", "color": "#CD5C5C"},
                                                      {"max": 99999, "min": 10000, "label": ">=10000", "color": "#8B0000"}]
                                              )
        )
    )
    return c

def print_data():
    data = read_csv("2.csv")
    for i in range(len(data)):
        print("('"+data["开户行所在省"][i]+"',"+str(data["账户数量"][i])+"),")
if __name__ == '__main__':
    #data = read_csv("2.csv")
    print_data()
    # data = [('湖北', 4658), ('浙江', 7605), ('广东', 27829), ('河南', 493), ('湖南', 463),
    #         ('安徽', 340), ('江西', 333), ('重庆', 275), ('江苏', 236), ('四川', 231),
    #         ('山东', 230), ('北京', 191), ('上海', 182), ('福建', 159), ('陕西', 116),
    #         ('广西', 111), ('云南', 105), ('河北', 104), ('黑龙江', 95), ('辽宁', 69),
    #         ('海南', 64), ('新疆', 21), ('内蒙古', 21), ('宁夏', 28), ('青海', 11),
    #         ('甘肃', 40), ('西藏', 1),('贵州', 38), ('山西', 56), ('吉林', 23),
    #         ('台湾', 10), ('天津', 48), ('香港', 14), ('澳门', 8)]

    data = [('安徽',3331),('湖北',4658),('海南',1520),('江苏',8284),('内蒙古',838),
            ('浙江',7605),('云南',4117),('新疆',1788),('青海',145),('四川',4882),
            ('陕西',2268),('广东',27829),('福建',8544),('湖南',4861),('天津',1200),
            ('山东',3680),('青岛',937),('西藏',29),('河南',5238),('山西',1671),
            ('重庆',1995),('黑龙江',1668),('吉林',1130),('宁夏',254),('辽宁',2539),
            ('江西',3750),('甘肃',530),('广西',3044),('上海',3275),('贵州',1135),
            ('北京',4049),('河北',3907)]
    d_map = map_china(data)
    d_map.render("china_gdp_from_1993_to_2018.html")

