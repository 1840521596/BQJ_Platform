# coding=utf-8
import sys
import unittest
from common import methods, myunit
from page.RealNamePage import CreateRealName
from page.LoginPage import Login
from page.RegisterPage import Register
import configparser
sys.path.append("./page")


class Test2VerifyRealName(myunit.MyTest, methods.CommonMethod,  Login, CreateRealName, Register):
    PATH = methods.project_path
    cf = configparser.ConfigParser()
    cf.read(PATH + "\\login_conf.ini")
    user = cf.get("unreal_name_input", "user")
    pwd = cf.get("unreal_name_input", "pwd")

    def test_real_name_verify_success(self):
        """测试实名认证成功"""
        self.user_login(self.user, self.pwd)
        self.click_copyright_credit_page()
        self.create_real_name_verify()


if __name__ == '__main__':
    unittest.main()
