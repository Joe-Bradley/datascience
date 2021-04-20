import pandas as pd


def read_csv(i):
    df1 = pd.read_csv(i, encoding="gb18030")
    return df1


if __name__ == '__main__':
    df = pd.read_csv("1.csv", encoding="utf-8")
    df["开户行所在省"] = df.apply(lambda x: x["开户行所在省"][4:6] ,axis = 1)
    print(df)
    df.to_csv("2.csv",encoding="utf-8",index=False)
