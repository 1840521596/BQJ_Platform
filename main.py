# coding:utf-8
import os
import sys
import unittest
from common import send_mail
from HtmlTestRunner import HTMLTestRunner
import time
sys.path.append("./testcase")
sys.path.append("./driver")


def startup():
    cmd = "java -jar ./driver/selenium-server-standalone-3.14.0.jar"
    content = os.popen(cmd).read()
    print(content)


def get_log_name():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    return filename


def out_put_report(arg):
    # version = get_version()
    log_name = get_log_name()
    startup()
    fp = open(log_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='ServicePlatform Test Report',
        description='Report_description')
    runner.run(arg)
    fp.close()

    # import allcaselist  # 测试用例数据文件
    # alltestnames = allcaselist.caselist()
    # suite = unittest.TestSuite()
    # for caseItem in alltestnames:
    #     suite.addTest(unittest.defaultTestLoader.loadTestsFromName(caseItem))
    #     print('ERROR: \Skipping tests from "%s".' % caseItem)
    # unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    # 指定测试用例为当前文件夹下的testcase目录
    os.startfile("startup.bat")
    test_dir = './testcase'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
    time.sleep(2)
    # 输出报告
    out_put_report(discover)
    # os.system("taskkill /f /im cmd.exe")
    time.sleep(5)
    # send_mail.send_report()
