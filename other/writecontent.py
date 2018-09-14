# coding:utf-8


def write_num():
    for i in range(1, 1001):
        # print("tp" + str(i) + '\n')
        with open(r"D:\BQJ_Platform\other\num.txt", 'a+') as fp:
            fp.write("".join(str(i) + 'tp' + '\n'))


if __name__ == '__main__':
    write_num()
