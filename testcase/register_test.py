# coding=utf-8
import sys
import unittest
from common import methods, verify, myunit
from page.RegisterPage import Register
import configparser
sys.path.append("./page")


class TestServiceLogin(myunit.MyTest, Register):
    PATH = methods.project_path
    cf = configparser.ConfigParser()
    cf.read(PATH + "\\login_conf.ini")

    def test_user_register_fail(self):
        """测试用户注册失败"""

        phone = self.cf.get('register_input', 'user')
        self.user_register(phone)
        verify.verifyEqual(self, self.bqj_agreement, "立即注册")

    def test_user_register_success(self):
        """测试用户注册成功"""
        phone = self.cf.get('unregister_input', 'user')
        self.user_register(phone)
        verify.verifyEqual(self, self.personal_register_loc, u"个人注册")


if __name__ == '__main__':
    unittest.main()
