# coding=utf-8
import sys
import unittest
import configparser
from common import methods, myunit
from page.LoginPage import Login
from page.CertificateVerifyPage import CertificateVerifyPage
sys.path.append("./page")


class Test4CertificateVerify(myunit.MyTest, methods.CommonMethod, Login, CertificateVerifyPage):
    PATH = methods.project_path
    cf = configparser.ConfigParser()
    cf.read(PATH + "\\login_conf.ini")
    user = cf.get("Infinite_time_purchase", "user")
    pwd = cf.get("Infinite_time_purchase", "pwd")
    user1 = cf.get("unregister_input", "user")
    pwd1 = cf.get("unregister_input", "pwd")

    # def test_vip_certificate_content_verify(self):
    #     """测试VIP证书内容核验"""
    #     self.verify_copyright_pass()
    #     self.user_login(self.user, self.pwd)
    #     self.user_certificate_verify()
    #     self.assertEqual(self.cdData[0], self.sha256())
    #
    # def test_vip_trusted_time_verify(self):
    #     """测试VIP可信时间凭证核验"""
    #     self.user_login(self.user, self.pwd)
    #     self.user_trusted_time_verify()
    #     self.assertIn(self.get_certificate_id(), self.get_trusted_time_verify_result())
    #
    # def test_vip_digital_signature_verify(self):
    #     """测试VIP用户数字签名核验"""
    #     self.user_login(self.user, self.pwd)
    #     self.user_digital_signature_verify()
    #     self.assertEqual('1.本次签名有效', self.get_signature_result())
    #
    # def test_vip_copyright_block_chain_verify(self):
    #     """测试VIP版权区块链联盟核验"""
    #     self.user_login(self.user, self.pwd)
    #     self.user_copyright_block_chain_verify()
    #     self.assertEqual(self.get_certificate_value(), self.get_hash_value())

    def test_certificate_content_verify(self):
        """测试证书内容核验"""
        self.verify_copyright_pass()
        self.user_login(self.user1, self.pwd1)
        self.user_certificate_verify()
        self.assertEqual(self.cdData[0], self.sha256())

    def test_trusted_time_verify(self):
        """测试可信时间凭证核验"""
        self.user_login(self.user1, self.pwd1)
        self.user_trusted_time_verify()
        self.assertIn(self.get_certificate_id(), self.get_trusted_time_verify_result())

    def test_digital_signature_verify(self):
        """测试用户数字签名核验"""
        self.user_login(self.user1, self.pwd1)
        self.user_digital_signature_verify()
        self.assertEqual('1.本次签名有效', self.get_signature_result())

    def test_copyright_block_chain_verify(self):
        """测试版权区块链联盟核验"""
        self.user_login(self.user1, self.pwd1)
        self.user_copyright_block_chain_verify()
        self.assertEqual(self.get_certificate_value(), self.get_hash_value())


if __name__ == '__main__':
    unittest.main()
