# coding:utf-8
import datetime
import os
import time
from common import methods
from page.BasePage import Page
from selenium.webdriver.common.by import By


class CreateRealName(Page):
    client_detail_loc = (By.CLASS_NAME, 'client_detail_btn')
    go_real_name_loc = (By.CSS_SELECTOR, 'body>div:nth-child(14)>div>div.ant-modal-wrap>div>div.ant-modal-content>div.ant-modal-body>div>a>button')
    upload_front_loc = (By.CSS_SELECTOR, '#root>div>div>div>div.account.clearfix>div.account-content>div>div>div:nth-child(2)>div>div>div:nth-child(2)>div.ant-col-18>div:nth-child(1)>div>span>div')
    upload_back_loc = (By.CSS_SELECTOR, '#root>div>div>div>div.account.clearfix>div.account-content>div>div>div:nth-child(2)>div>div>div:nth-child(2)>div.ant-col-18>div:nth-child(2)>div>span>div')
    quick_auth_btn = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[5]/button')
    real_name_success_loc = (By.CSS_SELECTOR, '#root > div > div > div > div.account.clearfix > div.account-content > div > div > div.margin-top-20.font14')
    PATH = methods.project_path
    timestamp = datetime.datetime.now().strftime("%Y%m%d %H%M%S")

    def click_client_detail_btn(self):
        """
        点击立即存证按钮
        :return:返回异常原因
        """
        try:
            self.click(self.client_detail_loc)
        except Exception as msg:
            return u"异常原因%s" % msg

    def click_go_real_name_btn(self):
        """
        点击前往实名按钮
        :return:返回异常原因
        """
        try:
            self.click(self.go_real_name_loc)
        except Exception as msg:
            return u"异常原因%s" % msg

    def upload_credentials(self):
        """
        上传证件
        :return:返回异常原因
        """
        try:
            # 正面证件
            self.click(self.upload_front_loc)
            os.system(self.PATH + r"\front1.exe")
            time.sleep(5)
            # 背面证件
            self.click(self.upload_back_loc)
            os.system(self.PATH + r"\back1.exe")
            time.sleep(5)
        except Exception as msg:
            return u"异常原因%s" % msg

    def scroll_to_bottom(self):
        """
        滑动到底部
        :return:返回异常原因
        """
        try:
            js = "var q=document.documentElement.scrollTop=100000"
            self.script(js)
        except Exception as msg:
            return u"异常原因%s" % msg

    def click_quick_auth_btn(self):
        """
        点击立即认证按钮
        :return:返回异常原因
        """
        try:
            self.click(self.quick_auth_btn)
        except Exception as msg:
            return u"异常原因%s" % msg

    def get_real_name_success_info(self):
        """
        获取认证成功文字信息
        :return:
        """
        try:
            content = self.find_elem_text(self.real_name_success_loc)
            return content
        except Exception as msg:
            return u"异常原因%s" % msg

    def create_real_name_verify(self):
        # self.get_screen_shoot('立即存证', self.timestamp)
        self.click_client_detail_btn()
        # self.get_screen_shoot('未实名认证弹窗', self.timestamp)
        self.click_go_real_name_btn()
        self.upload_credentials()
        # self.get_screen_shoot('上传证件', self.timestamp)
        self.scroll_to_bottom()
        self.click_quick_auth_btn()
        time.sleep(1)
        # self.get_screen_shoot('认证成功', self.timestamp)

    # def click_ant_upload_btn(self):
    #     """
    #     点击继续编辑按钮
    #     :return:返回异常原因
    #     """
    #     try:
    #         self.click(self.upload_front_loc)
    #         # 调用upfile.exe上传程序
    #         os.system(self.PATH + r"\copyright.exe")
    #         time.sleep(3)
    #     except Exception as msg:
    #         return u"异常原因%s" % msg
