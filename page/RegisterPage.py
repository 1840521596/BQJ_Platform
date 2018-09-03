# coding:utf-8
import time
from PIL import Image
from pytesseract import pytesseract
from page.BasePage import Page
from selenium.webdriver.common.by import By


class Register(Page):
    bqj_register_url = u'https://tspassport.bqj.cn/register?backurl=https%3A%2F%2Ftsdev.bqj.cn%2Findex.html&sc=12589172'
    enterprise_register_loc = (By.XPATH, '/html/body/div/div/div/div/div/ul/li[2]')
    phone_loc = (By.ID, "account4Mobile")
    mail_loc = (By.ID, "account4Email")
    img_loc = 'dynamic_code_person'
    verify_loc = (By.ID, "imageCode4Mobile")
    next_loc = (By.CSS_SELECTOR, "#signupForm>input")
    bqj_agreement = (By.XPATH, '//*[@id="signupForm"]/div[3]/div/a/span')
    personal_register_loc = (By.XPATH, '/html/body/div/div/div/div/div/ul/li')
    page_title = '注册'
    original_img = r'D:\BQJ_Platform\testImage\test.png'
    image_path = r'D:\BQJ_Platform\testImage\login.png'

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
            return u"异常原因%s" % msg

    def type_input_verify(self, verify_num):
        """
        :param verify_num: # 输入验证码
        :return: 返回异常原因
        """
        try:
            self.type_input(self.verify_loc, verify_num)
        except Exception as msg:
            return u"异常原因%s" % msg

    def click_next_btn(self):
        """
        # 点击下一步按钮
        :return: 返回异常原因
        """
        try:
            self.click(self.next_loc)
        except Exception as msg:
            return u"异常原因%s" % msg

    def click_enterprise_register_btn(self):
        """
        # 点击企业注册按钮
        :return:返回异常原因
        """
        try:
            self.click(self.enterprise_register_loc)
        except Exception as msg:
            return u"异常原因%s" % msg

    def type_input_email(self, mail):
        """
        :param mail:  # 输入企业邮箱
        :return: 返回异常原因
        """
        try:
            self.type_input(self.mail_loc, mail)
        except Exception as msg:
            return u"异常原因%s" % msg

    def get_image_code(self):
        """
        获取验证码
        :return:
        """
        self.driver.save_screenshot(self.original_img)
        element = self.driver.find_element_by_id(self.img_loc)
        left = int(element.location['x'])
        top = int(element.location['y'])
        right = int(element.location['x'] + element.size['width'])
        bottom = int(element.location['y'] + element.size['height'])
        print(top, right, bottom, left)
        # 通过Image处理图像
        im = Image.open(self.original_img)
        im = im.crop((left, top, right, bottom))
        im.save(self.image_path)
        img_str = pytesseract.image_to_string(Image.open(self.image_path))
        result = int(img_str[0]) + int(img_str[2])
        return str(result)

    def user_register(self, phone):
        """
        # 定义个人注册入口
        :param phone: # 输入手机号
        :return:
        """
        self.open_url()
        verify_code = self.get_image_code()
        self.type_input_phone(phone)
        self.type_input_verify(verify_code)
        time.sleep(1)
        self.click_next_btn()
        time.sleep(1)
        # text = self.find_elem_text(self.personal_register_loc)
        # print(text)

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
        # text = self.find_elem_text(self.personal_register_loc)
        # print(text)
