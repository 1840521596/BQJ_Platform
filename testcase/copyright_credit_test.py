# coding=utf-8
import sys
import unittest
import configparser
from common import methods, myunit
from page.LoginPage import Login
from page.CreateCopyrightCreditPage import CreateCopyrightCredit
sys.path.append("./page")


class Test3CreateCopyrightCredit(myunit.MyTest, methods.CommonMethod, Login, CreateCopyrightCredit):
    PATH = methods.project_path
    cf = configparser.ConfigParser()
    cf.read(PATH + "\\login_conf.ini")
    user = cf.get("Infinite_time_purchase", "user")
    pwd = cf.get("Infinite_time_purchase", "pwd")
    user1 = cf.get("correct_input1", "user")
    pwd1 = cf.get("correct_input1", "pwd")

    @unittest.skip("跳过VIP创建版权存证")
    def test_vip_create_copyright_credit_success(self):
        """测试VIP创建版权存证成功"""
        self.user_login(self.user, self.pwd)
        self.click_copyright_credit_page()
        self.vip_user_create_copyright_credit()
        self.assertEqual('信息审核', self.get_application_finish_info())

    @unittest.skip("跳过VIP购买环节验证")
    def test_purchase_vip_success(self):
        """测试VIP购买环节验证"""
        self.user_login(self.user1, self.pwd1)
        self.vip_user_create_copyright_credit()
        self.open_vip_user()
        self.assertEqual('￥298', self.get_vip_purchase_price())
        self.click_confirm_pay_btn()
        self.get_screen_shoot("请完成支付页面", self.timestamp)

    def test_create_copyright_credit_success(self):
        """注册用户测试创建版权存证成功"""
        self.user_login(self.user1, self.pwd1)
        self.click_copyright_credit_page()
        self.user_create_copyright_credit()
        self.assertEqual('信息审核', self.get_application_finish_info())


if __name__ == '__main__':
    unittest.main()
