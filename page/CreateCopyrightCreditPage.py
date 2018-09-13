# coding:utf-8
import datetime
import os
import time
from common import methods
from page.BasePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class CreateCopyrightCredit(Page):
    client_detail_loc = (By.CLASS_NAME, 'client_detail_btn')
    delete_no_submit_btn_loc = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[1]/div[2]/button[1]')
    continue_edit_btn_loc = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[1]/div[2]/button[2]')
    ant_upload_loc = (By.CLASS_NAME, 'ant-upload')
    copyright_name_loc = (By.CLASS_NAME, 'copyright-name')
    next_step_btn_loc = (By.CSS_SELECTOR, '#root>div>div>div>div:nth-child('
                                          '2)>div>form>div.all-btn.clearfix>button.ant-btn.ant-btn-primary.next-btn')
    confirm_info_loc = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/p')
    commit_confirm_info_loc = (
        By.CSS_SELECTOR, '#root>div>div>div>div:nth-child(2)>div>div.operation_box>div>button:nth-child(2)')
    get_application_finish_info_loc = (By.CSS_SELECTOR,
                                       '#root>div>div>div>div:nth-child(2)>div>div.copyright.copyright_detail>div>div>div.schedule-text.clearfix>div:nth-child(3)>p')
    select_vip_purchase_type_loc = (By.CSS_SELECTOR, '#root>div>div>div>div:nth-child('
                                                     '2)>div>div.charge>div.charge-child>div>div.charge-vip.charge-all.border-fff>div'
                                                     ':nth-child(1)')
    open_vip_commit_loc = (
        By.CSS_SELECTOR, '#root>div>div>div>div:nth-child(2)>div>div.charge>div.operation_box>div>a>button')
    get_vip_price_loc = (By.CSS_SELECTOR,
                         '#root>div>div>div>div.account.clearfix>div.account-content>div>div>div.walletOpenMember>div.OpenMemberPriceBox>ul>li:nth-child(3)>div>span:nth-child(2)')
    confirm_pay_loc = (By.CLASS_NAME, 'btn_pay')
    PATH = methods.project_path
    timestamp = datetime.datetime.now().strftime("%Y%m%d %H%M%S")

    def click_client_detail_btn(self):
        """
        点击立即存证按钮
        :return:返回异常原因
        """
        try:
            self.click(self.client_detail_loc)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def click_delete_no_submit_btn(self):
        """
        点击删除未提交内容
        :return:返回异常原因
        """
        try:
            self.click(self.delete_no_submit_btn_loc)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def click_continue_edit_btn(self):
        """
        点击继续编辑按钮
        :return:返回异常原因
        """
        try:
            self.click(self.continue_edit_btn_loc)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def click_ant_upload_btn(self):
        """
        上传测试图片
        :return: 得到服务器返回的路径
        """
        try:
            self.click(self.ant_upload_loc)
            os.system(self.PATH + r"\copyright.exe")
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def type_input_work_name(self):
        """
        输入作品名称
        :return:
        """
        try:
            self.type_input(self.copyright_name_loc, '测试数据，勿动')
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def click_next_step_btn(self):
        """
        点击下一步按钮
        :return:返回异常原因
        """
        try:
            self.click(self.next_step_btn_loc)
            time.sleep(3)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def click_confirm_info_btn(self):
        """
        点击确认信息并提交按钮
        :return: 返回异常原因
        """
        try:
            self.click(self.commit_confirm_info_loc)
            time.sleep(1)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def get_application_finish_info(self):
        """
        获取申请完成的信息
        :return:返回异常原因
        """
        try:
            get_application_info = self.find_elem_text(self.get_application_finish_info_loc)
            time.sleep(1)
            # print(type(get_application_info))
            # print(get_application_info)
            return get_application_info
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def select_vip_type(self):
        """
        选择vip类型
        :return:返回异常原因
        """
        try:
            self.click(self.select_vip_purchase_type_loc)
            time.sleep(1)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def click_open_vip_commit_btn(self):
        """
        选择vip购买
        :return:返回异常原因
        """
        try:
            self.click(self.open_vip_commit_loc)
            time.sleep(1)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def get_vip_purchase_price(self):
        """
        获取vip购买价格
        :return:返回异常原因
        """
        try:
            get_vip_price = self.find_elem_text(self.get_vip_price_loc)
            # print(type(get_vip_price))
            # print(str(get_vip_price))
            time.sleep(1)
            return get_vip_price
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def click_confirm_pay_btn(self):
        """
        点击确认支付按钮
        :return:返回异常原因
        """
        try:
            self.click(self.confirm_pay_loc)
            time.sleep(1)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def user_create_copyright_credit(self):
        self.click_client_detail_btn()
        self.get_screen_shoot("点击立即存证", self.timestamp)
        self.click_ant_upload_btn()
        self.get_screen_shoot("上传作品", self.timestamp)
        self.scroll_to_middle()
        self.type_input_work_name()
        self.get_screen_shoot("输入作品名称", self.timestamp)
        self.scroll_to_bottom()
        self.click_next_step_btn()
        self.get_screen_shoot('确认信息页', self.timestamp)
        self.scroll_to_bottom()
        self.click_confirm_info_btn()
        self.get_screen_shoot('信息审核页', self.timestamp)
        self.scroll_to_top()

    def open_vip_user(self):
        self.click_client_detail_btn()
        self.get_screen_shoot("点击立即存证", self.timestamp)
        self.click_ant_upload_btn()
        self.get_screen_shoot("上传作品", self.timestamp)
        self.scroll_to_middle()
        self.type_input_work_name()
        self.get_screen_shoot("输入作品名称", self.timestamp)
        self.scroll_to_bottom()
        self.click_next_step_btn()
        self.get_screen_shoot('确认信息页', self.timestamp)
        self.select_vip_type()
        self.get_screen_shoot("个人VIP会员购买", self.timestamp)
        self.click_open_vip_commit_btn()
        self.switch_to_window()
        self.get_screen_shoot("开通VIP会员", self.timestamp)
        self.scroll_to_bottom()
