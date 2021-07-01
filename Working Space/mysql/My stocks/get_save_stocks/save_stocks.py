import json
import tushare as ts


# List to Json
def list_to_json():
    stock_index = [{'指数':
                        {'上证综指': 'sh.000001',
                         '深证成指': 'sz.399001',
                         '沪深300': 'sz.000300',
                         '创业板指': 'sz.399006',
                         '上证50': 'sh.000016',
                         '中证500': 'sh.000905',
                         '中小板指': 'sz.399005',
                         '上证180': 'sh.000010'}},
                   {'股票':
                        {'格力电器': '000651.SZ',
                         '平安银行': '000001.SZ',
                         '同花顺': '300033.SZ',
                         '贵州茅台': '600519.SH',
                         '浙大网新': '600797.SH'}}]
    json_str = json.dumps(stock_index)
    with open("to_database/stock_pool.json", "w", encoding='utf-8') as f:
        json.dump(stock_index, f, ensure_ascii=False, indent=4)


# Tushare to Json
def tushare_to_json():
    token = '6d55067438b3eddc5bb24bd687a5ad92a432f3b9086201e8e3701561'  # 输入你的token
    pro = ts.pro_api(token)

    # 获取数据
    df = pro.stock_basic(exchange='', list_status='L')

    # 取ts_code，name这两列
    codes = df.ts_code.values
    names = df.name.values
    stock = dict(zip(names, codes))
    index =  {'上证综指': 'sh.000001',
                 '深证成指': 'sz.399001',
                 '沪深300': 'sz.000300',
                 '创业板指': 'sz.399006',
                 '上证50': 'sh.000016',
                 '中证500': 'sh.000905',
                 '中小板指': 'sz.399005',
                 '上证180': 'sh.000010'}
    # stock_index = [('指数', index), ('股票', stock)] 也可
    stock_index = dict([('指数', index), ('股票', stock)])
    with open("to_database/stock_pool.json", "w", encoding='utf-8') as f:
        json.dump(stock_index, f, ensure_ascii=False, indent=4)
