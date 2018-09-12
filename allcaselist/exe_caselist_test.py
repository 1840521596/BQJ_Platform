# coding=utf-8
from testcase.register_test import Test1UserRegister
from testcase.verify_real_name_test import Test2VerifyRealName
from testcase.copyright_credit_test import Test3CreateCopyrightCredit
from testcase.service_login_test import Test4ServiceLogin
from testcase.service_quit_test import Test5ServiceQuit
from testcase.certificate_verify_test import Test6CertificateVerify


def test_all_cases_list():
    Test1UserRegister().test_user_register_success()
    Test2VerifyRealName().test_real_name_verify_success()
    Test3CreateCopyrightCredit().test_create_copyright_credit_success()
    Test3CreateCopyrightCredit().test_purchase_vip_success()
    Test4ServiceLogin().test_login_success()
    Test4ServiceLogin().test_main_nav_jump()
    Test5ServiceQuit().test_quit_success()
    Test6CertificateVerify().user_certificate_verify()
    Test6CertificateVerify().user_trusted_time_verify()
    Test6CertificateVerify().user_digital_signature_verify()
    Test6CertificateVerify().user_copyright_block_chain_verify()
