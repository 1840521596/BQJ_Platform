import os
import time
from common import methods
from page.BasePage import Page
from selenium.webdriver.common.by import By


class CreateCopyrightCredit(Page):
    client_detail_loc = (By.CLASS_NAME, 'client_detail_btn')
    delete_no_submit_btn_loc = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[1]/div[2]/button[1]')
    continue_edit_btn_loc = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[1]/div[2]/button[2]')
    ant_upload_loc = (By.CLASS_NAME, 'ant-upload')
    next_step_btn_loc = (By.CSS_SELECTOR, '#root>div>div>div>div:nth-child('
                                          '2)>div>form>div.all-btn.clearfix>button.ant-btn.ant-btn-primary.next-btn')
    confirm_info_loc = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/p')
    PATH = methods.project_path

    def click_client_detail_btn(self):
        """
        点击立即存证按钮
        :return:返回异常原因
        """
        try:
            self.click(self.client_detail_loc)
        except Exception as msg:
            return u"异常原因%s" % msg

    def click_delete_no_submit_btn(self):
        """
        点击删除未提交内容
        :return:返回异常原因
        """
        try:
            self.click(self.delete_no_submit_btn_loc)
        except Exception as msg:
            return u"异常原因%s" % msg

    def click_continue_edit_btn(self):
        """
        点击继续编辑按钮
        :return:返回异常原因
        """
        try:
            self.click(self.continue_edit_btn_loc)
        except Exception as msg:
            return u"异常原因%s" % msg

    def click_ant_upload_btn(self):
        """
        点击继续编辑按钮
        :return:返回异常原因
        """
        try:
            self.click(self.ant_upload_loc)
            # 调用upfile.exe上传程序
            os.system(self.PATH+r"\autoit.exe")
            time.sleep(3)
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

    def click_next_step_btn(self):
        """
        点击下一步按钮
        :return:返回异常原因
        """
        try:
            self.click(self.next_step_btn_loc)
        except Exception as msg:
            return u"异常原因%s" % msg

    def user_create_copyright_credit(self):
        self.click_client_detail_btn()
        self.click_ant_upload_btn()
        self.scroll_to_bottom()
        self.click_next_step_btn()

