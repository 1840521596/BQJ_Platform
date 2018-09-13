# coding:utf-8
import logging
import os
import os.path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common import globalparameter as gl
from common.log import Logger

__author__ = 'panze'
'''description:邮件发送最新的测试报告'''


# 定义邮件内容
def email_init(report, report_name):
    with open(report, 'rb')as f:
        mail_body = f.read()
    my_log = Logger("error_log.log", logging.WARNING, logging.DEBUG)
    # 创建一个带附件的邮件实例
    msg = MIMEMultipart('mixed')
    # 以测试报告作为邮件正文
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
    report_file = MIMEText(mail_body, 'html', 'utf-8')
    # 定义附件名称（附件的名称可以随便定义，你写的是什么邮件里面显示的就是什么）
    report_file["Content-Disposition"] = 'attachment; filename=' + report_name
    msg.attach(report_file)  # 添加附件
    msg['Subject'] = '版权存证网站自动化测试报告:' + report_name  # 邮件标题
    msg['From'] = gl.email_name  # 发件人
    msg['To'] = ";".join(gl.email_To)  # 收件人列表
    try:
        server = smtplib.SMTP()
        server.connect(gl.smtp_sever, 25)
        server.login(gl.email_name, gl.email_password)
        server.sendmail(gl.email_name, gl.email_To, msg.as_string())
        server.quit()
    except smtplib.SMTPException:
        my_log.error(u'邮件发送测试报告失败 at ' + __file__)


def send_report():
    # 找到最新的测试报告
    report_list = os.listdir(gl.report_path)
    report_list.sort(
        key=lambda fn: os.path.getmtime(gl.report_path + fn) if not os.path.isdir(gl.report_path + fn) else 0)
    new_report = os.path.join(gl.report_path, report_list[-1])
    # 发送邮件
    email_init(new_report, report_list[-1])


if __name__ == '__main__':
    send_report()
