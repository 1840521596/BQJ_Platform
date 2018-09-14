# coding:utf-8
import os
import sys
import unittest
from common import send_mail
from HtmlTestRunner import HTMLTestReportCN
import time
# sys.path.append("./testcase")
sys.path.append("./driver")
sys.path.append("./allcaselist")


def get_log_name():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_TestReport.html'
    return filename


def out_put_report(arg):
    # version = get_version()
    log_name = get_log_name()
    # startup()
    fp = open(log_name, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='版全家网站3.3.0版本测试报告',
        description='详细测试用例结果',
        tester=u'潘泽')
    runner.run(arg)
    fp.close()


if __name__ == '__main__':
    # 指定测试用例为当前文件夹下的testcase目录
    os.startfile("startup.bat")
    time.sleep(2)
    # os.system("ntsd -c q -pn cmd.exe")
    test_dir = './allcaselist'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
    time.sleep(2)
    # 输出报告
    out_put_report(discover)
    time.sleep(2)
    # send_mail.send_report()
    # os.system("taskkill /f /t /im cmd.exe")
