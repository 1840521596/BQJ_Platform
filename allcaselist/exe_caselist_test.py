# coding=utf-8
from testcase.register_test import Test1UserRegister
from testcase.verify_real_name_test import Test2VerifyRealName
from testcase.copyright_credit_test import Test3CreateCopyrightCredit
from testcase.certificate_verify_test import Test4CertificateVerify
from testcase.service_login_test import Test5ServiceLogin
from testcase.service_quit_test import Test6ServiceQuit


def test_all_cases_list():
    Test1UserRegister()
    Test2VerifyRealName()
    Test3CreateCopyrightCredit()
    Test4CertificateVerify()
    Test5ServiceLogin()
    Test6ServiceQuit()

