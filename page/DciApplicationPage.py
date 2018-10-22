# coding=utf-8
import datetime
import time
from page.BasePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class DciApplicationPage(Page):
    other_service_loc = (By.CSS_SELECTOR, '#root > div > div > div > div:nth-child(1) > div > header > div > ul > li:nth-child(5)')
    application_registration_works_loc = (By.CSS_SELECTOR, '#root > div > div > div > div:nth-child(1) > div > header > div > div.tip.headTip.other-services > div.tipContent > p:nth-child(1)')
    registration_application_loc = (By.XPATH, '//*[@id="app"]/div[1]/div/ul/li[1]')
    select_work_loc = (By.CSS_SELECTOR, '#app > div.infoCheck > div.infoCenter > div.choose > div.worksShow > div')
    next_step_loc = (By.CSS_SELECTOR, '#app > div.infoCheck > div.infoCenter > div.choose > div.limitBtns > div > button.el-button.el-button--primary.is-round > span')
    work_type_loc = (By.CSS_SELECTOR, '#app > div.infoCheck > div.infoCenter > div:nth-child(5) > form > div:nth-child(2) > div > button > span')
    novel_work_loc = (By.CSS_SELECTOR, "#app > div.infoCheck > div.infoCenter > div:nth-child(5) > form > div.el-dialog__wrapper > div > div.el-dialog__body > div.limit-elUi.limit-elUi2 > form:nth-child(1) > div:nth-child(1) > div > button:nth-child(1) > span")
    confirm_btn_loc = (By.CSS_SELECTOR, '#app > div.infoCheck > div.infoCenter > div:nth-child(5) > form > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button')
    time_loc = (By.CSS_SELECTOR, '#app > div.infoCheck > div.infoCenter > div:nth-child(7) > form > div:nth-child(1) > div > div > input')
    select_available_today_loc = (By.CSS_SELECTOR, 'body > div.el-picker-panel.el-date-picker.el-popper > div.el-picker-panel__body-wrapper > div > div.el-picker-panel__content > table.el-date-table > tbody > tr:nth-child(5) > td.available.today')
    time_loc2 = (By.CSS_SELECTOR, '#app > div.infoCheck > div.infoCenter > div:nth-child(7) > form > div:nth-child(3) > div > div > input')
    select_available_today_loc2 = (By.CSS_SELECTOR, 'body > div:nth-child(5) > div.el-picker-panel__body-wrapper > div > div.el-picker-panel__content > table.el-date-table > tbody > tr:nth-child(5) > td.available.today')
    creation_place_loc = (By.CSS_SELECTOR, '#app > div.infoCheck > div.infoCenter > div:nth-child(7) > form > div.el-form-item.citySelect.citySelect20.is-required > div > div:nth-child(1) > div > input')
    select_china_loc = (By.CSS_SELECTOR, 'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)')
    provinces_loc = (By.CSS_SELECTOR, '#app > div.infoCheck > div.infoCenter > div:nth-child(7) > form > div.el-form-item.citySelect.citySelect20.is-required > div > div:nth-child(2) > div > input')
    select_beijing_loc = (By.CSS_SELECTOR, 'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(34) > span')
    creation_intention_loc = (By.CSS_SELECTOR, '#app > div.infoCheck > div.infoCenter > div.limitTab.limitPos > form > div:nth-child(1) > div > div.el-textarea > textarea')
    originality_works_loc = (By.CSS_SELECTOR, '#app > div.infoCheck > div.infoCenter > div.limitTab.limitPos > form > div:nth-child(3) > div > div.el-textarea > textarea')
    commit_btn_loc = (By.CSS_SELECTOR, '#app > div.infoCheck > div.infoCenter > div:nth-child(12) > div > button.el-button.el-button--primary.is-round')
    get_order_detail_loc = (By.CSS_SELECTOR, '#app > div.production-check > div > div.infoCenter > span > span')
    timestamp = datetime.datetime.now().strftime("%Y%m%d %H%M%S")

    def click_application_registration_works(self):
        """
        点击作品登记证书申请
        :return:返回异常原因
        """
        try:
            self.click_and_hold(self.other_service_loc)
            self.click(self.application_registration_works_loc)
            self.switch_to_window()
            time.sleep(2)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def click_registration_application_btn(self):
        """
        点击登记申请按钮
        :return:返回异常原因
        """
        try:
            self.click(self.registration_application_loc)
            self.refresh_current_page()
            time.sleep(2)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def select_application_work(self):
        """
        选择要申请的作品
        :return:返回异常原因
        """
        try:
            self.click(self.select_work_loc)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def click_next_step(self):
        """
        点击下一步按钮
        :return: 返回异常原因
        """
        try:
            self.click(self.next_step_loc)
            time.sleep(1)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def click_work_type(self):
        """
        点击作品类型
        :return: 返回异常原因
        """
        try:
            self.click(self.work_type_loc)
            time.sleep(1)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def select_novel_work(self):
        """
        选择小说作品
        :return: 返回异常原因
        """
        try:
            self.click(self.novel_work_loc)
            self.scroll_to_bottom()
            time.sleep(1)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def click_confirm_btn(self):
        """
        点击确定按钮
        :return: 返回异常原因
        """
        try:
            self.click(self.confirm_btn_loc)
            time.sleep(2)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def select_start_time(self):
        """
        选择创作开始日期
        :return: 返回异常原因
        """
        try:
            self.scroll_to_more_bottom()
            self.click(self.time_loc)
            time.sleep(1)
            self.click(self.select_available_today_loc)
            time.sleep(1)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def select_end_time(self):
        """
        选择创作完成日期
        :return: 返回异常原因
        """
        try:
            self.click(self.time_loc2)
            time.sleep(1)
            self.click(self.select_available_today_loc2)
            time.sleep(1)
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def select_creation_place(self):
        """
        选择创作地点
        :return: 返回异常原因
        """
        try:
            self.click(self.creation_place_loc)
            time.sleep(1)
            self.click(self.select_china_loc)
            time.sleep(1)
            self.click(self.provinces_loc)
            time.sleep(1)
            self.click(self.select_beijing_loc)
            time.sleep(1)
            self.scroll_to_bottom()
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def type_input_creative_intention_info(self):
        """
        填写创作意图信息
        :return: 返回异常原因
        """
        try:
            self.type_input(self.creation_intention_loc, '请为作品补充填写对应的“创作意图”和“作品独创性”说明，我们将会以此内容为你生成《创作过程说明书》并将作品样本、身份证信息 及根据你的作品基本信息生成的其他相关声明一同提交至中国版权保护中心进行审核。审核周期为7—10个工作日，请认真填写。')
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def type_input_originality_work_info(self):
        """
        填写作品独特性信息
        :return: 返回异常原因
        """
        try:
            self.type_input(self.originality_works_loc, '请为作品补充填写对应的“创作意图”和“作品独创性”说明，我们将会以此内容为你生成《创作过程说明书》并将作品样本、身份证信息 及根据你的作品基本信息生成的其他相关声明一同提交至中国版权保护中心进行审核。审核周期为7—10个工作日，请认真填写。')
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def click_commit_btn(self):
        """
        点击提交按钮
        :return:返回异常原因
        """
        try:
            self.click(self.commit_btn_loc)
            self.scroll_to_top()
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def get_order_detail_info(self):
        """
        点击提交按钮
        :return:返回异常原因
        """
        try:
            content = self.find_elem_text(self.get_order_detail_loc)
            return content
        except NoSuchElementException as msg:
            return "异常原因%s" % msg

    def user_registration_works_application(self):
        """
        统一作品登记证书申请
        :return:
        """
        self.click_application_registration_works()
        self.click_registration_application_btn()
        self.select_application_work()
        self.click_next_step()
        self.click_work_type()
        self.select_novel_work()
        self.click_confirm_btn()
        self.select_start_time()
        self.select_end_time()
        self.select_creation_place()
        self.type_input_creative_intention_info()
        self.type_input_originality_work_info()
        self.click_commit_btn()
