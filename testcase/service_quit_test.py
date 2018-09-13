# encoding=utf-8
import configparser
import sys
import unittest
import time
from common import myunit, methods
from page.QuitPage import Quit
sys.path.append("./page")


class Test6ServiceQuit(myunit.MyTest, Quit):
    PATH = methods.project_path
    cf = configparser.ConfigParser()
    cf.read(PATH + "\\login_conf.ini")
    user = cf.get("correct_input", "user")
    pwd = cf.get("correct_input", "pwd")

    def test_quit_success(self):
        """退出成功测试"""
        self.user_login(self.user, self.pwd)
        self.user_quit()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
