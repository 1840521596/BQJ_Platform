# coding=utf-8
import sys
import unittest
import configparser
from common import methods, verify, myunit
from page.LoginPage import Login
from page.CreateCopyrightCreditPage import CreateCopyrightCredit
sys.path.append("./page")


class TestCreateCopyrightCredit(myunit.MyTest, methods.CommonMethod, Login, CreateCopyrightCredit):
    PATH = methods.project_path
    print(PATH)
    cf = configparser.ConfigParser()
    cf.read(PATH + "\\login_conf.ini")
    user = cf.get("correct_input", "user")
    pwd = cf.get("correct_input", "pwd")

    def test_create_copyright_credit_success(self):
        """测试创建版权存证成功"""
        self.user_login(self.user, self.pwd)
        self.click_copyright_credit_page()
        self.user_create_copyright_credit()
        verify.verifyEqual(self, self.confirm_info_loc, "信息确认")


if __name__ == '__main__':
    unittest.main()
