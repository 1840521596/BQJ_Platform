# coding=utf-8
import json
import random
import requests
from pylab import *
from PIL import Image
import urllib.parse as uz
import urllib.request as ul
import http.cookiejar as cookielib
from pytesseract import pytesseract
import os
import sys
sys.path.append('image')
# dirPath = os.path.dirname(os.path.realpath(__file__))
# dirPath2 = os.getcwd()
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
c = cookielib.MozillaCookieJar(project_path + "\Cookie.txt")
# 先把cookie对象存储为cookiejar的对象
cookie = ul.HTTPCookieProcessor(c)  # 把cookiejar对象转换为一个handle(句柄)
opener = ul.build_opener(cookie)  # 建立一个模拟浏览器，需要handle作为参数
ul.install_opener(opener)  # 安装全局模拟浏览器
# 先写个头，表示我这是浏览器用户登录而不是代码登录，如果不写，代码默认用
headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 "
                  "Safari/537.36 "}

result = []
images = []
pictures = []
pic_more = []
resInfo = []


def verify_code():
    """
    获取验证码
    :return: 验证码求和后的值
    """
    num = random.choice(['0.']) + "".join(random.choice("0123456789") for i in range(17))
    # num = random.choice(['159']) + "".join(random.choice("0123456789") for i in range(8))
    # print(num)
    img_url = "https://passport.bqj.cn/image/validate/login?" + num
    image_path = r'D:/image'
    ul.urlretrieve(img_url, image_path)
    img_str = pytesseract.image_to_string(Image.open(image_path))
    get_sum = int(img_str[0]) + int(img_str[2])
    return get_sum


def login():
    """
    登录版全家网页版
    :return:
    """
    global result
    result = []
    data = {
        'username': '15810346836',
        'password': '111111q',
        'imageCode': verify_code(),
        'backurl': 'http://www.bqj.cn/sso/afterLogin',
        'emailLogin': 'false',
        'mobileLogin': 'true',
        '_ref': 'http://www.bqj.cn/sso/afterLogin'
    }
    # Post的数据必须是bytes或者iterable of bytes，不能是str，因此需要进行encode（）编码
    data = uz.urlencode(data).encode()
    req = ul.Request("https://passport.bqj.cn/sso/login", data, headers)
    # print("Header:%s" % req.header_items())
    html = opener.open(req).read().decode()
    result.append(html)
    print(result)
    c.save(ignore_discard=True, ignore_expires=True)
    # print(c)
    # for item in c:
    #     print('Name=' + item.name)
    #     print('Value = ' + item.value)
    # print("登录结果：%s" % result)

    # 获取接口返回的地址，请求后完成登录
    resp = json.loads(html)
    ssoCode = resp['backurl'].split('=')[1].split('&')[0]
    registerId = resp['backurl'].split('=')[1].split('&')[1]
    back_url = 'http://www.bqj.cn/sso/afterLogin?ssoCode=' + ssoCode + '&registerId=' + registerId
    req = ul.Request(back_url)
    # print("Header:%s" % req.header_items())
    html = opener.open(req).read().decode()
    print("打印登录成功后的页面：%s" % html)


def get_cookies():
    """
    获取cookie
    :return:
    """
    s = requests.session()
    dic = json.loads(result[0])
    parameters = {
        "ssoCode": dic['backurl'].split('=')[1].split('&')[0],
        "registerId": dic['backurl'].split('=')[1].split('&')[1]
    }
    response = s.get("https://passport.bqj.cn/sso/login", params=parameters)
    cookies = response.cookies.get_dict()
    print("获取Cookies:%s" % cookies)
    return cookies
    # headers = response.headers
    # print(response.request.headers)
    # print(response.text)


def get_img_path(path):
    """
    读取特定文件夹下的png格式图像
    :param path: 存储文件的路径
    :return: 返回列表中文件路径
    """
    image_list = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]
    return image_list


def get_image():
    """
    存储切割后的png格式文件到列表中
    :return: 返回列表中文件
    """
    global images
    images = []
    for pic in get_img_path(project_path + '\image'):
        image = pic.split("\\")
        images.append(image[3])
    return images


def choose_pp():
    """
    获取 "userPowerVOList" 字段值
    :return:返回请求后的"userPowerVOList"
    """
    dic = json.loads(result[0])
    req = requests.get("https://www.bqj.cn/order/original/choosePp?registerId=" + dic['user']['registerId'])
    response = req.json()
    # print(response["userPowerVOList"][0])
    return response


def get_order_seq_num():
    """
    获取"orderSeqNo" 字段值
    :return:返回请求后的"orderSeqNo"
    """
    req = requests.get("https://www.bqj.cn/order/original/orderId")
    response = req.json()
    # print("获取Seq_No:%s" % response)
    return response["orderSeqNo"]


def up_pic():
    """
    上传测试图片
    :return: 得到服务器返回的路径
    """
    global pic_more
    pic_more = []
    dic = json.loads(result[0])
    for j in range(len(images)):
        # if images.pop(j) is not None:
        pict = images.pop(j)
        pic_more.append(pict)
        print(len(images))
        data = {'registerId': dic['user']['registerId']}
        file = {
            'fileUpload': ('%s' % pict, open(project_path + '\image\%s' % pict, 'rb'))
        }
        print(file)
        response = requests.post("https://www.bqj.cn/order/original/fileUpload",
                                 data=data, files=file, cookies=get_cookies())
        req = response.json()
        print("上传测试图片:%s" % req)
        return req, pic_more


def up_pic_more():
    """
     上传多张测试图片
     :return: 得到服务器返回的路径
     """
    global pictures
    pictures = []
    get_image()
    for im in range(3):
        pictures.append(up_pic())
    return pictures


def get_require_value():
    """
    获取需要的数值
    :return:返回图片名称，上传到服务器的路径
    """
    global resInfo
    resInfo = []
    for i in range(3):
        getvalue = pictures
        image = getvalue[i][1][0]
        dic = getvalue[i][0]
        fileUrl = dic['fileUrl']
        resInfo.append(image)
        resInfo.append(fileUrl)
    return resInfo


def save_copyright_info():
    orderSeqNo = get_order_seq_num()
    get_copyright_credit = choose_pp()
    dic = json.loads(result[0])
    getValue = resInfo
    data = {'registerId': int("%s" % dic['user']['registerId']),
            "orderId": "",
            "orderSeqNo": "%s" % orderSeqNo,
            "attachments": "%s,%s,%s" % (getValue[1], getValue[3], getValue[5]),
            "attachmentNames": "%s,%s,%s" % (getValue[0], getValue[2], getValue[4]),
            "poNames": "%s" % get_copyright_credit['userPowerVOList'][0]['name'],
            "authorNames": "%s" % get_copyright_credit['userPowerVOList'][0]['name'],
            "poIds": int("%s" % get_copyright_credit['userPowerVOList'][0]['id']),
            "authorIds": int("%s" % get_copyright_credit['userPowerVOList'][0]['id']),
            "copyrightStatements": "未经合法授权，任何单位和个人不得进行辅助、转载、改编或其它侵权行为。",
            "workFullname": "1",
            "completeDateBegin": '',
            "completeDateEnd": '',
            "modifiCount": 0,
            "completeCountry": "无",
            "completeProvince": "无",
            "completeCity": "无",
            "publishStatus": 0,
            "publishDate": "",
            "publishPlatform": "无",
            "certificationFileUrl": "",
            "copyrightType": 1
            }
    # print(data)
    # response = requests.post("https://www.bqj.cn/order/original/save", cookies=get_cookies(), data=data)
    # html = response.json()
    # print(html)
    # Post的数据必须是bytes或者iterable of bytes，不能是str，因此需要进行encode（）编码
    data = uz.urlencode(data).encode()
    req = ul.Request("https://www.bqj.cn/order/original/save", data=data, headers=headers)
    # print("Header:%s" % req.header_items())
    html = opener.open(req).read().decode()
    # result = json.loads(html)
    print(html)


def upload_pics():
    login()
    up_pic_more()
    get_require_value()
    save_copyright_info()


if __name__ == '__main__':
    upload_pics()

