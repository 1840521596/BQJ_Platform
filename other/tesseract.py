# -*- coding: UTF-8 -*-
from pytesseract import *
from PIL import Image
from selenium.webdriver.common.by import By
from page.BasePage import Page
from selenium import webdriver


class GetVerifyPic(Page):
    img_loc = (By.ID, "dynamic_code_pw")
    login_title = '登录'
    image_path = r'D:\BQJ_Platform\testImage\code.png'
    bqj_login_url = u"https://passport.bqj.cn/sso/login?backurl=http%3A%2F%2Fwww.bqj.cn%2Fsso%2FafterLogin&sc=12589172"
    driver = webdriver.Chrome()

    def open_url(self):
        self.verify_open(self.bqj_login_url, self.login_title)

    def get_image_code(self):
        # 获取指定元素位置
        self.get_screen_shoot(self.image_path)
        element = self.find_element(self.img_loc)
        left = int(element.location['x'])
        top = int(element.location['y'])
        right = int(element.location['x'] + element.size['width'])
        bottom = int(element.location['y'] + element.size['height'])
        # print(top, right, bottom, left)
        # 通过Image处理图像
        im = Image.open(self.image_path)
        im = im.crop((left, top, right, bottom))
        im.save(self.image_path)
        img_str = pytesseract.image_to_string(Image.open(self.image_path))
        result = int(img_str[0])+int(img_str[2])
        return result

    @staticmethod
    def randomCodeOcr(filename):
        image = Image.open(filename)
        ltext = image_to_string(image=image)
        print(u'[%s]识别到验证码:[%s]!!!' % (filename, ltext))
        image.save(filename)
        result = int(ltext[0]) + int(float(ltext[2]))
        print(int(result))
        return ltext



