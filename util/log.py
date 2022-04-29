# coding:utf-8

import sys
import os
import traceback

from util import const


class Log:
    def __init__(self, filename=None):
        self.log_to_file = True
        self.log_to_screen = True
        self.out = sys.stdout
        self.log_filename = filename
        if self.log_filename is None:
            self.log_filename = const.LOG_DEFAULT_FILENAME
        dirs = os.path.dirname(self.log_filename)
        if not os.path.exists(dirs):
            os.makedirs(dirs)

    def write(self, message):
        if self.log_to_screen:
            self.out.write(message)
        if self.log_to_file:
            mk_file = open(self.log_filename, 'a')
            mk_file.writelines(message)
            mk_file.close()

    def flush(self):
        pass


if __name__ == '__main__':
    sys.stdout = Log()
    print("this a test msg")