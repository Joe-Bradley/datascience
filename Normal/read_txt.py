def read_txt(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            for line in f:
                file_lines = f.readlines()
    except:
        with open(file_name, encoding="gbk") as f:
            for line in f:
                file_lines = f.readlines()
    return file_lines

if __name__ == '__main__':
    lines = read_txt("list.txt")
    for i in lines:
        aa = i[5:7]
        a = """<DT><A HREF="{}/" ADD_DATE="1518413448">List{}</A> """.format(i[8:-1],aa)
        print(a)

