# coding=utf8

import sys

from util.log import Log


def main():
    sys.stdout = Log()  ## 让打印的log能输出到文件
    print("cpp analysis start...")


if __name__ == '__main__':
    main()