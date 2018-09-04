# coding:utf-8
import os
import random
import time
from page.BasePage import Page
from selenium.webdriver.common.by import By
# Get relative path
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))


class CommonMethod(Page):
    main_loc = (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/header/div/ul/li[1]/a')
    protection_client_loc = (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/header/div/ul/li[2]/a')
    copyright_show_loc = (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/header/div/ul/li[3]/a')
    bqj_main_url = u'https://www.bqj.cn/index.html#/'
    main_title = '版权家-版权服务专家'

    @staticmethod
    def rand_phone_num():
        """
        # 获取随机手机号
        :return: 返回随机生成159开头的手机号
        """
        num = random.choice(['159']) + "".join(random.choice("0123456789") for i in range(8))
        return num

    def open_main_url(self):
        """
        打开版全家首页
        :return:
        """
        self.verify_open(self.bqj_main_url, self.main_title)

    def click_main_page(self):
        """
        # 点击首页
        :return: 返回异常原因
        """
        try:
            self.click(self.main_loc)
        except Exception as msg:
            return u"异常原因%s" % msg

    def click_protection_client_page(self):
        """
        # 点击创作保护客户端
        :return: 返回异常原因
        """
        try:
            self.click(self.protection_client_loc)
        except Exception as msg:
            return u"异常原因%s" % msg

    def click_copyright_credit_page(self):
        """
        # 点击版权存证
        :return: 返回异常原因
        """
        try:
            self.click(self.copyright_show_loc)
            time.sleep(1)
        except Exception as msg:
            return u"异常原因%s" % msg

    def click_main_nav_jump(self):
        """
        # 统一点击主页导航跳转
        """
        self.open_main_url()
        self.click_protection_client_page()
        time.sleep(1)
        self.click_copyright_credit_page()
        time.sleep(1)
        self.click_main_page()
        time.sleep(1)
