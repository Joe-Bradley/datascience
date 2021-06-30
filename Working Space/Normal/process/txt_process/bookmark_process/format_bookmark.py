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


def write_list(filename, mode, list):
    with open(filename, mode) as f:
        f.writelines(list)
    f.close()


if __name__ == '__main__':
    lines = read_txt("added_bookmarks.txt")
    lines_for_update = read_txt("bookmarks_6_28_21.html")
    for i in lines:
        address = i[8:-1]
        number = i[5:7]
        line = """            <DT><A HREF="{}/" ADD_DATE="1518413448"\
        >List{}</A> """.format(address, number)
        lines_for_update.insert(11, line + "\n")
        print(line)
    write_list("out.html", "w+", lines_for_update)
