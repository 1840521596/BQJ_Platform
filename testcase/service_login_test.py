# coding=utf-8
import sys
import unittest
import time
from common import methods, myunit
from common.methods import CommonMethod
from page.LoginPage import Login
import configparser
sys.path.append("./page")


class Test5ServiceLogin(myunit.MyTest, Login, CommonMethod):
    PATH = methods.project_path
    cf = configparser.ConfigParser()
    cf.read(PATH + "\\login_conf.ini")
    user = cf.get("Infinite_time_purchase", "user")
    pwd = cf.get("Infinite_time_purchase", "pwd")

    @unittest.skip("跳过登录失败用例")
    def test_login_fail(self):
        """用户名、密码错误"""
        self.user_login(self.user, self.pwd)
        time.sleep(3)
        print(self.find_layer(self.login_btn_loc))

    def test_login_success(self):
        """登录成功"""
        self.user_login(self.user, self.pwd)
        # verify.verifyEqual(self, self.login_message, u"消息")

    def test_main_nav_jump(self):
        """导航栏跳转测试"""
        self.click_main_nav_jump()
