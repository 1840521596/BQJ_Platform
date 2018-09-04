# coding:utf-8
import os
import sys
import unittest
from common import send_mail
from HtmlTestRunner import HTMLTestRunner
import time
# sys.path.append("./testcase")
sys.path.append("./driver")
sys.path.append("./allcaselist")


def startup():
    cmd = "java -jar ./driver/selenium-server-standalone-3.8.1.jar"
    content = os.popen(cmd).read()
    print(content)


def get_log_name():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_TestReport.html'
    return filename


def out_put_report(arg):
    # version = get_version()
    log_name = get_log_name()
    # startup()
    fp = open(log_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='Bqj ServicePlatform Test Report',
        description='Report_description')
    runner.run(arg)
    fp.close()


if __name__ == '__main__':
    # 指定测试用例为当前文件夹下的testcase目录
    os.startfile("startup.bat")
    time.sleep(2)
    os.system("ntsd -c q -pn cmd.exe")
    test_dir = './allcaselist'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
    time.sleep(2)
    # 输出报告
    out_put_report(discover)
    time.sleep(2)
    # send_mail.send_report()
    # os.system("taskkill /f /t /im cmd.exe")
