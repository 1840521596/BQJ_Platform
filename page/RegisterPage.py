# coding:utf-8
import datetime
import time
from common import methods
from common.GetInterfaceValue import GetSms
from PIL import Image
from pytesseract import pytesseract
from page.BasePage import Page
from selenium.webdriver.common.by import By


class Register(Page):
    path = methods.project_path
    timestamp = datetime.datetime.now().strftime("%Y%m%d %H%M%S")
    bqj_register_url = u'https://passport.bqj.cn/register?backurl=https%3A%2F%2Ftsdev.bqj.cn%2Findex.html&sc=12589172'
    enterprise_register_loc = (By.XPATH, '/html/body/div/div/div/div/div/ul/li[2]')
    phone_loc = (By.ID, "account4Mobile")
    mail_loc = (By.ID, "account4Email")
    reg_img_loc = 'dynamic_code_person'
    verify_loc = (By.ID, "imageCode4Mobile")
    next_loc = (By.CSS_SELECTOR, "#signupForm>input")
    bqj_agreement = (By.XPATH, '//*[@id="signupForm"]/div[3]/div/a/span')
    bqj_create_success_loc = (By.CLASS_NAME, 'bqj_creat_suces')
    get_active_code_loc = (By.CSS_SELECTOR, '#signupForm>div.phone_write_code.clearfix>p.count_down.count_down_btn')
    sms_code_loc = (By.CSS_SELECTOR, '#verifyCode')
    psw_loc = (By.ID, 'password')
    psw2_loc = (By.ID, 'password2')
    quick_register_btn = (By.CLASS_NAME, 'form_btn')
    show_error_loc = (By.CLASS_NAME, 'show_error')
    enter_main_loc = (By.CSS_SELECTOR, 'body>div>div>div>div>div>button')
    page_title = '注册'
    original_img = path + r'\testImage\reg_test.png'
    image_path = path + r'\testImage\reg_login.png'

    def open_url(self):
        self.verify_open(self.bqj_register_url, self.page_title)

    def type_input_phone(self, phone):
        """
        :param phone: # 输入手机号
        :return: 返回异常原因
        """
        try:
            self.type_input(self.phone_loc, phone)
        except Exception as msg:
            return "异常原因%s" % msg

    def type_input_verify(self, verify_num):
        """
        :param verify_num: # 输入验证码
        :return: 返回异常原因
        """
        try:
            self.type_input(self.verify_loc, verify_num)
        except Exception as msg:
            return "异常原因%s" % msg

    def click_next_btn(self):
        """
        # 点击下一步按钮
        :return: 返回异常原因
        """
        try:
            self.click(self.next_loc)
        except Exception as msg:
            return "异常原因%s" % msg

    def click_active_code_btn(self):
        """
        # 点击获取动态码
        :return:  返回异常原因
        """
        try:
            self.click(self.get_active_code_loc)
        except Exception as msg:
            return "异常原因%s" % msg

    def type_input_sms_code(self, sms_code):
        """
        # 输入短信验证码
        :return:  返回异常原因
        """
        try:
            self.type_input(self.sms_code_loc, sms_code)
        except Exception as msg:
            return "异常原因%s" % msg

    def type_input_password(self, password):
        """
        # 输入密码
        :return:  返回异常原因
        """
        try:
            self.type_input(self.psw_loc, password)
            self.type_input(self.psw2_loc, password)
        except Exception as msg:
            return "异常原因%s" % msg

    def click_quick_register(self):
        """
        # 点击立即注册
        :return: 返回异常原因
        """
        try:
            self.click(self.quick_register_btn)
        except Exception as msg:
            return "异常原因%s" % msg

    def click_enter_main_page(self):
        """
        点击进入主页
        :return:
        """
        try:
            self.click(self.enter_main_loc)
        except Exception as msg:
            return "异常原因%s" % msg

    def click_enterprise_register_btn(self):
        """
        # 点击企业注册按钮
        :return:返回异常原因
        """
        try:
            self.click(self.enterprise_register_loc)
        except Exception as msg:
            return "异常原因%s" % msg

    def type_input_email(self, mail):
        """
        :param mail: # 输入企业邮箱
        :return: 返回异常原因
        """
        try:
            self.type_input(self.mail_loc, mail)
        except Exception as msg:
            return "异常原因%s" % msg

    def get_image_code(self):
        """
        获取验证码
        :return:返回验证码结果
        """
        self.driver.save_screenshot(self.original_img)
        element = self.driver.find_element_by_id(self.reg_img_loc)
        left = int(element.location['x'])
        top = int(element.location['y'])
        right = int(element.location['x'] + element.size['width'])
        bottom = int(element.location['y'] + element.size['height'])
        # print(top, right, bottom, left)
        # 通过Image处理图像
        im = Image.open(self.original_img)
        im = im.crop((left, top, right, bottom))
        im.save(self.image_path)
        img_str = pytesseract.image_to_string(Image.open(self.image_path))
        result = int(img_str[0]) + int(img_str[2])
        return str(result)

    @staticmethod
    def get_sms_code():
        """
        获取手机号验证码
        :return: 返回验证码结果
        """
        sms_code = GetSms().judgeCode()
        return sms_code

    def user_register_step1(self, phone):
        """
        # 定义个人注册入口
        :param phone: # 输入手机号
        :return:
        """
        self.open_url()
        verify_code = self.get_image_code()
        self.type_input_phone(phone)
        self.type_input_verify(verify_code)
        self.get_screen_shoot('注册首页', self.timestamp)
        self.click_next_btn()
        self.click_active_code_btn()

    def user_register_step2(self, password):
        """
        # 定义个人注册入口
        :param password: # 输入密码
        :return:
        """
        sms_code = self.get_sms_code()
        self.type_input_sms_code(sms_code)
        self.type_input_password(password)
        self.get_screen_shoot('注册账号页', self.timestamp)
        self.click_quick_register()
        time.sleep(1)
        self.get_screen_shoot('注册完成', self.timestamp)
        # self.click_enter_main_page()

    def enterprise_register(self, mail):
        """
        # 定义企业注册入口
        :param mail: # 输入企业邮箱
        :return:
        """
        self.open_url()
        self.click_enterprise_register_btn()
        verify_code = self.get_image_code()
        self.type_input_email(mail)
        self.type_input_verify(verify_code)
        time.sleep(1)
        self.click_next_btn()
        time.sleep(1)
