# coding=utf-8
import json
import time
import urllib.parse as uz
import urllib.request as ul
import http.cookiejar as cookielib
import requests
import os
import sys

sys.path.append('image')
# dirPath = os.path.dirname(os.path.realpath(__file__))
# dirPath2 = os.getcwd()
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
c = cookielib.MozillaCookieJar()
# 先把cookie对象存储为cookiejar的对象
cookie = ul.HTTPCookieProcessor(c)  # 把cookiejar对象转换为一个handle(句柄)
opener = ul.build_opener(cookie)  # 建立一个模拟浏览器，需要handle作为参数
ul.install_opener(opener)  # 安装全局模拟浏览器
# 先写个头，表示我这是浏览器用户登录而不是代码登录，如果不写，代码默认用
headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"}


class CopyrightVerifyPass:
    url = 'https://www.bqj.cn/order/original/getOrderListForMulti'

    def copyright_verify_pass(self):
        """
        登录版全家
        :return:
        """
        data = {'emailLogin': 'true',
                'password': 'abc123',
                'username': 'panze@anne.com.cn'
                }
        # Post的数据必须是bytes或者iterable of bytes，不能是str，因此需要进行encode（）编码
        data = uz.urlencode(data).encode()
        req = ul.Request("https://backendtp.bqj.cn/a/login", data, headers)
        # print("Header:%s" % req.header_items())
        opener.open(req).read().decode()
        # c.save(ignore_discard=True, ignore_expires=True)

        req = ul.Request("https://backendtp.bqj.cn/a?login")
        # print("Header:%s" % req.header_items())
        opener.open(req).read().decode()
        # print(html)
        url = "https://backendtp.bqj.cn/a/order/orderCommon"
        req = ul.Request(url)
        # print("Header:%s" % req.header_items())
        opener.open(req).read().decode()
        # print(html)

        data = {'authorName': '',
                'endTime': '',
                'endUpdateTime': '',
                'memberStatus': '',
                'orderSeqNo': '',
                'pageNo': '1',
                'pageSize': '20',
                'startTime': '',
                'startUpdateTime': '',
                'terminal': '',
                'userTye': '',
                'workFullname': '测试数据，勿动'}
        # Post的数据必须是bytes或者iterable of bytes，不能是str，因此需要进行encode（）编码
        data = uz.urlencode(data).encode()
        req = ul.Request("https://backendtp.bqj.cn/a/order/orderCommon/", data, headers)
        # print("Header:%s" % req.header_items())
        opener.open(req).read().decode()

        req = ul.Request(
            "https://backendtp.bqj.cn/a/orderSop/copyrightDepositCertificateForm?id=" + self.get_copyright_id())
        # print("Header:%s" % req.header_items())
        opener.open(req).read().decode()
        # print(response)

        # 版权存证审核通过
        req = ul.Request(
            "https://backendtp.bqj.cn/a//orderSop/copyrightDepositCertificateVerify?orderId=" +
            self.get_copyright_id() + "&auditType=filing_identify")
        # print("Header:%s" % req.header_items())
        opener.open(req).read().decode()
        time.sleep(5)
        # print(response)
        # number = json.loads(result)
        # print("caData:" + number['copyright']['ca']['caData'])
        # return number['copyright']['id']

    def get_copyright_id(self):
        """
        获取版权存证id
        :return: 异常原因
        """
        try:
            data = {'certType': 'all',
                    'keyword': '',
                    'period': 'all',
                    'pageSize': '9',
                    'pageNo': '1',
                    'workType': 'all',
                    'status': 'all',
                    'loading': 'true',
                    'registerId': '143556'}
            rq = requests.post(self.url, data=data)
            result = rq.text
            number = json.loads(result)
            # print("caData:" + number['copyright']['ca']['caData'])
            return number['copyrights'][0]['id']
        except Exception as msg:
            return "异常原因%s" % msg


if __name__ == '__main__':
    CopyrightVerifyPass().copyright_verify_pass()
