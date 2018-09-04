# coding=utf-8
import sys
import unittest
from common import methods, myunit
from page.RegisterPage import Register
import configparser
sys.path.append("./page")
sys.path.append("./image")


class Test1UserRegister(myunit.MyTest, Register):
    path = methods.project_path
    cf = configparser.ConfigParser()
    cf.read(path + "\\login_conf.ini")

    @unittest.skip('跳过测试用户注册失败')
    def test_user_register_fail(self):
        """测试用户注册失败"""
        phone = self.cf.get('register_input', 'user')
        password = self.cf.get('register_input', 'pwd')
        self.user_register(phone, password)
        # verify.verifyEqual(self, self.bqj_agreement, "立即注册")

    def test_user_register_success(self):
        """测试用户注册成功"""
        phone = self.cf.get('unregister_input', 'user')
        password = self.cf.get('unregister_input', 'pwd')
        self.user_register(phone, password)


if __name__ == '__main__':
    unittest.main()
