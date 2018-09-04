# _*_ coding: utf-8 _*_
import configparser
import os
import re
from urllib import request
from PIL import Image
from pytesseract import pytesseract
import urllib.parse as uz
import urllib.request as ul
import http.cookiejar as cookielib
from common import methods

project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
c = cookielib.MozillaCookieJar(project_path + "\Cookie.txt")
# 先把cookie对象存储为cookiejar的对象
cookie = ul.HTTPCookieProcessor(c)  # 把cookiejar对象转换为一个handle(句柄)
opener = ul.build_opener(cookie)  # 建立一个模拟浏览器，需要handle作为参数
ul.install_opener(opener)  # 安装全局模拟浏览器
# 先写个头，表示我这是浏览器用户登录而不是代码登录，如果不写，代码默认用
headers = {
    "Referer": "http://www.106818.com/loginFront.aspx",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"}


class GetSms:
    url = 'http://www.106818.com/codehandler.ashx'
    path = methods.project_path
    cf = configparser.ConfigParser()
    cf.read(path + "\\login_conf.ini")
    phone = cf.get('unregister_input', 'user')

    def get_verify(self):

        # 调用接口
        request.urlretrieve(self.url, self.path + r'\testImage\sms.png')
        # img = Image.open(path + r'\testImage\login.jpg')
        # imgry = img.convert('L')  # 图像加强，二值化
        # sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
        # sharp_img = sharpness.enhance(2.0)
        # sharp_img.save(path + r'\testImage\login.jpg')
        img_code = pytesseract.image_to_string(Image.open(self.path + r'\testImage\sms.png'))
        return img_code

    def login(self):
        # 参数写入
        data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '/wEPDwUKLTUzNTA0NDkzNw9kFgJmD2QWAgIDD2QWAgIBD2QWAgIGDxYCHglpbm5lcmh0bWwFgwHniYjmnYPkv6Hmga/vvJpF5LyB5L+h6YCaLeS8geS4muiQpemUgOS/oeaBr+ezu+e7nyAmbmJzcDsgSUNQ5aSH5qGI77yaPGEgaHJlZj0iaHR0cDovL3d3dy5taWliZWlhbi5nb3YuY24iPuS6rElDUOWkhzEyMDIzMzUx5Y+3PC9hPmQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFFGN0bDAwJEhvbGRlcjEkSW1hZ2Ux1zmJ0XKwzzwvvRdeu4wrmIIa8vA=',
            '__EVENTVALIDATION': '/wEWBwKOoYT5CwL+wOqsCAL0/u7GDwLe59jTDQK51dqTCgLHy6GnCgLD+LOmCP4nVoq7LlUanvvu67Dgya3Wrr8M',
            'ctl00$Holder1$pwds': 'changyuan',
            'ctl00$Holder1$CorpID': 'SY0204',
            'ctl00$Holder1$Pwd': 'af4c4aabb77623e051c03b0217119cc8',
            'ctl00$Holder1$selectCookie': '0',
            'ctl00$Holder1$verifycode': self.get_verify(),
            'ctl00$Holder1$Image1.x': 56,
            'ctl00$Holder1$Image1.y': 9
        }
        # Post的数据必须是bytes或者iterable of bytes，不能是str，因此需要进行encode（）编码
        data = uz.urlencode(data).encode()
        req = ul.Request('http://www.106818.com/loginFront.aspx', data, headers)
        # print("Header:%s" % req.header_items())
        opener.open(req).read().decode()
        # print(result)
        c.save(ignore_discard=True, ignore_expires=True)
        # 获取接口返回的地址，请求后完成登录
        req = ul.Request('http://www.106818.com/Desk.aspx')
        # print("Header:%s" % req.header_items())
        opener.open(req).read().decode()
        # print("打印登录成功后的页面：%s" % html)

    def getcode(self):
        global code
        self.login()
        # 参数写入
        data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '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',
            '__EVENTVALIDATION': '/wEWCwLKto65BwLS2LaNCgKPya+TDQLa2rmZBwL1w9euAQK2i7exDgLX9fuEBwKH2tGhBQLH+pXeDwLLst7qDALLstbqDN/BDRFzjapHbv2SIp6le/7zXZPK',
            'ctl00$ctl00$Holder1$Holder2$Phone': self.phone,
            'ctl00$ctl00$Holder1$Holder2$sContent': '',
            'ctl00$ctl00$Holder1$Holder2$CreateDateKS': '',
            'ctl00$ctl00$Holder1$Holder2$CreateDateJS': '',
            'ctl00$ctl00$Holder1$Holder2$Number': '100000',
            'ctl00$ctl00$Holder1$Holder2$TB': 'vPX_SENDA_ALL',
            'ctl00$ctl00$Holder1$Holder2$Image1.x': '44',
            'ctl00$ctl00$Holder1$Holder2$Image1.y': '10',
            'ctl00$ctl00$Holder1$Holder2$AspNetPager1_input': '1',
            'ctl00$ctl00$Holder1$Holder2$AspNetPager2_input': '1'
        }
        # Post的数据必须是bytes或者iterable of bytes，不能是str，因此需要进行encode（）编码
        data = uz.urlencode(data).encode()
        req = ul.Request('http://www.106818.com/SmsQuery.aspx', data, headers)
        response = opener.open(req).read().decode()
        sms = response.find(self.phone)
        code = re.findall(u"验证码.(\d*)", response[sms:])
        return code
        # # 取出对应下标值
        # sms = response.text.find('15810346836')
        # # 取出对应验证码
        # code = re.findall(u"验证码.(\d*)", response.text[sms:])
        # return code[0]

    def judgeCode(self):
        """
        判断传入的验证码是否为空
        :return: 返回不为空的验证码
        """
        for i in range(30):
            array = self.getcode()
            # print(array)
            if len(array) is int(0):
                continue
            else:
                return array[0]


if __name__ == '__main__':
    get_sms = GetSms()
    print(get_sms.judgeCode())

