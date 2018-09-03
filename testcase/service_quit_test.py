# encoding=utf-8
import configparser
import sys
import unittest
import time
from common import myunit, methods, verify
from page.QuitPage import Quit
sys.path.append("./page")


class TestServiceQuit(myunit.MyTest, Quit):
    PATH = methods.project_path
    cf = configparser.ConfigParser()
    cf.read(PATH + "\\login_conf.ini")
    user = cf.get("correct_input", "user")
    pwd = cf.get("correct_input", "pwd")

    def test_quit_success(self):
        """退出成功测试"""
        self.user_login(self.user, self.pwd)
        self.user_quit()
        # verify.verifyEqual(self, self.register_enter_btn_loc, "注册")
        time.sleep(3)
        # 关闭窗口
        # self.driver.close()


if __name__ == '__main__':
    unittest.main()
