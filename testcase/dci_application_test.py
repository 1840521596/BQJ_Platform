# coding=utf-8
import sys
import unittest
import configparser
from common import methods, myunit
from page.LoginPage import Login
from page.DciApplicationPage import DciApplicationPage
sys.path.append("./page")


class Test5DciApplication(myunit.MyTest, methods.CommonMethod, Login, DciApplicationPage):
    PATH = methods.project_path
    cf = configparser.ConfigParser()
    cf.read(PATH + "\\login_conf.ini")
    user1 = cf.get("unregister_input", "user")
    pwd1 = cf.get("unregister_input", "pwd")

    def test_dci_application(self):
        self.user_login(self.user1, self.pwd1)
        self.user_registration_works_application()
        self.assertEqual(self.get_order_detail_info(), '作品登记证书（电子版）订单详情')


if __name__ == '__main__':
        unittest.main()
