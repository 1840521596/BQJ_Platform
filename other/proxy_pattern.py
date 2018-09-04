# # 设计模式——代理模式
# # 送礼物接口
# class GiveGift(object):
#     # 送洋娃娃
#     def GiveDolls(self):
#         pass
#
#     # 送花
#     def GiveFlower(self):
#         pass
#
#     # 送巧克力
#     def GiveChocolate(self):
#         pass
#
# # 被追求者
# class SchoolTeacher(object):
#     def __init__(self, teacher):
#         self.teacher = teacher
#
# # 追求者
# class TestingEngineer(object):
#     def __init__(self, engineer):
#         self.engineer = engineer
#
# # 追求动作
# class Pursit(GiveGift):
#     def __init__(self, Girl, Boy):
#         self.Girl = Girl
#         self.Boy = Boy
#
#     def GiveDolls(self):
#         print(self.Girl.teacher,self.Boy.engineer,"".join( "送你洋娃娃"))
#
#     def GiveFlower(self):
#         print(self.Girl.teacher, self.Boy.engineer, "".join("送你花"))
#
#     def GiveChocolate(self):
#         print(self.Girl.teacher, self.Boy.engineer, "".join("送你巧克力"))
#
# class Proxy(GiveGift):
#     def __init__(self, Girl, Boy):
#         self.proxy = Pursit(Boy,Girl)
#
#     def GiveDolls(self):
#         self.proxy.GiveDolls()
#
#     def GiveChocolate(self):
#         self.proxy.GiveChocolate()
#
#     def GiveFlower(self):
#         self.proxy.GiveFlower()
#
# if __name__ == '__main__':
#     CJL = SchoolTeacher("陈佳丽")
#     PZ = TestingEngineer("潘泽")
#     proxy = Proxy(PZ, CJL)
#     proxy.GiveDolls()
#     proxy.GiveFlower()
#     proxy.GiveChocolate()
#
import time

from PIL import Image
from pytesseract import pytesseract
from selenium import webdriver

original_img = r'D:\BQJ_Platform\testImage\test.png'
image_path = r'D:\BQJ_Platform\testImage\login.png'
img_loc = 'dynamic_code_pw'
bqj_login_url = u"https://passport.bqj.cn/sso/login?backurl=http%3A%2F%2Fwww.bqj.cn%2Fsso%2FafterLogin&sc=12589172"


def get_image_code():
    driver = webdriver.Chrome()
    # 获取指定元素位置
    driver.get(bqj_login_url)
    driver.maximize_window()
    time.sleep(1)
    driver.save_screenshot(original_img)
    element = driver.find_element_by_id(img_loc)
    left = int(element.location['x'])
    top = int(element.location['y'])
    right = int(element.location['x'] + element.size['width'])
    bottom = int(element.location['y'] + element.size['height'])
    print(top, right, bottom, left)
    driver.quit()
    # 通过Image处理图像
    im = Image.open(original_img)
    im = im.crop((left, top, right, bottom))
    im.save(image_path)
    img_str = pytesseract.image_to_string(Image.open(image_path))
    result = int(img_str[0]) + int(img_str[2])
    return str(result)


def outer(a):
    b = 10

    def inner():
        print(a + b)

    return inner()


if __name__ == '__main__':
    # print(get_image_code())
    outer(5)
