# coding:utf-8
import time

from PIL import Image
from pytesseract import *
from common import methods
from page.BasePage import Page
from selenium.webdriver.common.by import By


class Login(Page):
    path = methods.project_path
    username_loc = (By.ID, 'usernameInSignInForm')
    password_loc = (By.ID, 'passwordInSignInForm')
    image_code_loc = (By.NAME, 'imageCode')
    original_img = path + r'/testImage/test.png'
    image_path = path + r'/testImage/login.png'
    img_loc = 'dynamic_code_pw'
    bqj_login_url = u"https://passport.bqj.cn/sso/login?backurl=http%3A%2F%2Fwww.bqj.cn%2Fsso%2FafterLogin&sc=12589172"
    login_btn_loc = (By.CSS_SELECTOR, '#signInForm>input.form_btn')
    login_title = '登录'
    login_message = (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/header/div/ul/li[5]/a/span[1]')

    def open_login_url(self):
        """
        打开版全家登录页
        :return:
        """
        self.verify_open(self.bqj_login_url, self.login_title)

    def type_input_username(self, username):
        """
        :param username: # 输入用户名
        :return: 返回异常原因
        """
        try:
            self.type_input(self.username_loc, username)
        except Exception as msg:
            return "异常原因%s" % msg

    def type_input_password(self, password):
        """
        :param password: # 输入密码
        :return: 返回异常原因
        """
        try:
            self.type_input(self.password_loc, password)
        except Exception as msg:
            return "异常原因%s" % msg

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
        # print(top, right, bottom, left)
        # 通过Image处理图像
        im = Image.open(self.original_img)
        im = im.crop((left, top, right, bottom))
        # im = im.convert('RGB')
        im.save(self.image_path)
        img_str = pytesseract.image_to_string(Image.open(self.image_path))
        result = int(img_str[0]) + int(img_str[2])
        return str(result)

    def type_input_verify_code(self, verify_code):
        """
        :param verify_code: 验证码
        :return: 返回异常原因
        """
        try:
            self.type_input(self.image_code_loc, verify_code)
        except Exception as msg:
            return "异常原因%s" % msg

    def click_login_btn(self):
        """
        # 点击登录按钮
        :return: 返回异常原因
        """
        try:
            self.click(self.login_btn_loc)
        except Exception as msg:
            return "异常原因%s" % msg

    def user_login(self, username, password):
        """
        # 定义统一登录
        :param username: # 输入用户名
        :param password: # 输入密码
        """
        self.open_login_url()
        verify_code = self.get_image_code()
        self.type_input(self.username_loc, username)
        self.type_input(self.password_loc, password)
        # print(verify_code)
        self.type_input_verify_code(verify_code)
        self.click_login_btn()
        time.sleep(3)








