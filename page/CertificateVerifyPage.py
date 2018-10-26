# coding=utf-8
import datetime
import hashlib
import json
import time
import requests
from page.LoginPage import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.GetInterfaceValue import VerifyCopyrightPass


class CertificateVerifyPage(Page):
    position_path_loc = (By.CSS_SELECTOR, '#root > div > div > div > div:nth-child(1) > div > header > div > ul > li.header-images > a')
    img_container_loc = (By.CSS_SELECTOR, '#root>div>div>div>div.account.clearfix>div.account-content>div>section>ul>li>div>div:nth-child(2)>div')
    certificate_verify_loc = (By.CSS_SELECTOR, '#root > div > div > div > div.content > div > div.detailsLeftBox > div.content > section > div:nth-child(4) > div > div > article:nth-child(1) > div.creation-details-certificate-info > div > div > a:nth-child(2) > button')
    type_check_num_loc = (By.CSS_SELECTOR, '#code')
    confirm_loc = (By.CSS_SELECTOR, 'body > div:nth-child(14) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > form > button > span')
    verify_value_loc = (By.XPATH, '//*[@id="public_text"]')
    copy_content_loc = (By.CSS_SELECTOR, '#root > div > div > div > div.ordercommon > div.vmain-content > div:nth-child(2) > div:nth-child(7) > div.marginLeft60 > button')
    confirm_copy_content_loc = (By.CSS_SELECTOR, 'body > div:nth-child(14) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div.text-center.margin15.margin-top-60 > button')
    hash_link = 'http://www.jsons.cn/sha/'
    hash_link_title = "在线SHA加密-SHA1加密-SHA256加密-SHA512加密-Json在线解析格式化工具"
    secret_content_loc = (By.CSS_SELECTOR, '#message_source')
    paste_btn_loc = (Keys.CONTROL, 'v')
    SHA256_secret_loc = (By.CSS_SELECTOR, '#form1 > div:nth-child(2) > div > button:nth-child(2)')
    certificate_content_loc = (By.XPATH, '.orderContent-center > div:nth-child(4)>textarea:nth-child(1)')
    time_verify_link_loc = (By.CSS_SELECTOR, '#root > div > div > div > div.ordercommon > div.vmain-content > div:nth-child(3) > div.astyle > form > a > input[type="button"]')
    trusted_time_certificate_loc = (By.CLASS_NAME, 'el-icon-search')
    trusted_time_verify_result_loc = (By.CSS_SELECTOR, '#app > div > div.main > div.content > div > div > div.success-desc > p')
    certificate_id_loc = (By.CSS_SELECTOR, '#app > div > div.main > div.content > div > div > div.content > div.succ-aid > div.aid-desc')
    iTrustChina_loc = (By.CSS_SELECTOR, '#root > div > div > div > div.ordercommon > div.vmain-content > div:nth-child(4) > div.astyle > div > form > input[type="submit"]:nth-child(4)')
    quick_verify_loc = (By.CSS_SELECTOR, 'body > div.certificate_inquiry_box > div.certificate_inquiry_content > div > div > a')
    signature_result_loc = (By.CSS_SELECTOR, '#result')
    copyright_block_chain_loc = (By.CSS_SELECTOR, '#root > div > div > div > div.ordercommon > div.vmain-content > div:nth-child(5) > div:nth-child(10) > a')
    certificate_content_verify_loc = (By.CSS_SELECTOR, '#app > div > div.w1200 > div:nth-child(4) > table > tr:nth-child(1) > td:nth-child(2)')
    hash_certificate_content_verify_loc = (By.CSS_SELECTOR, '#app > div > div.w1200 > div.copyPub.nobor.copyPubDetail > table > tr > td:nth-child(2)')
    timestamp = datetime.datetime.now().strftime("%Y%m%d %H%M%S")
    cdData = []
    primitiveTscCaData = []

    @staticmethod
    def verify_copyright_pass():
        vcp = VerifyCopyrightPass()
        vcp.copyright_verify_pass()

    def click_user_portrait(self):
        """
        点击用户头像
        :return:异常原因
        """
        try:
            self.click(self.position_path_loc)
            time.sleep(2)
        except Exception as msg:
            return "异常原因%s" % msg

    def click_user_work(self):
        """
        点击用户作品
        :return:异常原因
        """
        try:
            self.click(self.img_container_loc)
            # print("打印当前地址：" + self.get_current_url())
            time.sleep(3)
        except Exception as msg:
            return "异常原因%s" % msg

    def get_bqj_check_num(self):
        """
        获取版全家核验码
        :return:异常原因
        """
        try:
            url = self.get_current_url()
            work_id = str(url.split('/')[-1])
            # print("打印作品ID：" + work_id)
            param = {'registerId': 'null'}
            rq = requests.get('https://www.bqj.cn/order/original/info/' + work_id, params=param)
            result = rq.text
            number = json.loads(result)
            check_num = number['copyright']['bqjCheckNum']
            # print("数字" + number['copyright']['bqjCheckNum'])
            return check_num
        except Exception as msg:
            return "异常原因%s" % msg

    def click_certificate_verify_btn(self):
        """
        点击证书核验
        :return:异常原因
        """
        try:
            self.scroll_to_less_middle()
            self.click(self.certificate_verify_loc)
            time.sleep(2)
        except Exception as msg:
            return "异常原因%s" % msg

    def type_input_check_num(self):
        """
        输入核验码
        :return:异常原因
        """
        try:
            self.type_input(self.type_check_num_loc, self.get_bqj_check_num())
            self.click(self.confirm_loc)
            time.sleep(5)
        except Exception as msg:
            return "异常原因%s" % msg

    # def click_verify_certificate_btn(self):
    #     """
    #     点击核验证书按钮
    #     :return: 异常原因
    #     """
    #     try:
    #         self.click(self.verifyBtn_loc)
    #         time.sleep(3)
    #     except Exception as msg:
    #         return "异常原因%s" % msg

    def get_certificate_content_verify(self):
        """获取证书内容完整性效验值
        :return: 异常原因
        """
        try:
            url = self.get_current_url()
            work_id = str(url.split('/')[-1])
            # print("打印作品ID：" + work_id)
            param = {'registerId': 'null',
                     'stamp': '0.5909795341286705'}
            rq = requests.get('https://www.bqj.cn/order/original/infoGet/' + work_id, params=param)
            result = rq.text
            number = json.loads(result)
            # print("caData:" + number['copyright']['ca']['caData'])
            return number['copyright']['ca']['caData']
        except Exception as msg:
            return "异常原因%s" % msg

    def click_copy_content_btn(self):
        """
        点击复制内容
        :return: 异常原因
        """
        try:
            self.click(self.copy_content_loc)
            self.click(self.confirm_copy_content_loc)
            time.sleep(1)
        except Exception as msg:
            return "异常原因%s" % msg

    def open_hash_link(self):
        """
        打开内容核验链接
        :return: 异常原因
        """
        try:
            self.verify_open(self.hash_link, self.hash_link_title)
            time.sleep(1)
        except Exception as msg:
            return "异常原因%s" % msg

    def SHA256_secret_content(self):
        """
        粘贴并SHA256加密内容
        :return: 异常原因
        """
        try:
            self.type_input(self.secret_content_loc, self.paste_btn_loc)
            self.click(self.SHA256_secret_loc)
            time.sleep(2)
        except Exception as msg:
            return "异常原因%s" % msg

    def get_certificate_main_content(self):
        """
        获证书摘取的主要内容
        :return: 异常原因
        """
        try:
            url = self.get_current_url()
            work_id = str(url.split('/')[-1])
            # print("打印作品ID：" + work_id)
            param = {'registerId': 'null',
                     'stamp': '0.5909795341286705'}
            rq = requests.get('https://www.bqj.cn/order/original/infoGet/' + work_id, params=param)
            result = rq.text
            number = json.loads(result)
            # print("primitiveTscCaData:" + number['copyright']['primitiveTscCaData'])
            content = number['copyright']['primitiveTscCaData']
            return content
        except Exception as msg:
            return "异常原因%s" % msg

    def sha256(self):
        """
        sha256加密
        return:加密结果转成16进制字符串形式
        """
        sha256 = hashlib.sha256()
        sha256.update(self.primitiveTscCaData[0].encode("utf-8"))
        # print(sha256.hexdigest())
        return sha256.hexdigest()

    def open_time_center(self):
        """
        打开中国科学院国家授时中心
        :return: 异常原因
        """
        try:
            self.click(self.time_verify_link_loc)
            self.switch_to_window()
            time.sleep(1)
        except Exception as msg:
            return "异常原因%s" % msg

    def click_trusted_time_certificate_btn(self):
        """
        点击查验可信时间凭证
        :return:异常原因
        """
        try:
            self.click(self.trusted_time_certificate_loc)
            time.sleep(5)
        except Exception as msg:
            return "异常原因%s" % msg

    def get_trusted_time_verify_result(self):
        """
        获取可信时间验证结果
        :return:异常原因
        """
        try:
            content = self.find_elem_text(self.trusted_time_verify_result_loc)
            time.sleep(1)
            return content
        except Exception as msg:
            return "异常原因%s" % msg

    def get_certificate_id(self):
        """
        获取凭证编号
        :return: 异常原因
        """
        try:
            content = self.find_elem_text(self.certificate_id_loc)
            time.sleep(1)
            return content
        except Exception as msg:
            return "异常原因%s" % msg

    def click_iTrustChina_btn(self):
        """
        点击天威诚信按钮
        :return: 异常原因
        """
        try:
            self.click(self.iTrustChina_loc)
            self.switch_to_window()
            time.sleep(1)
        except Exception as msg:
            return "异常原因%s" % msg

    def click_quick_verify_btn(self):
        """
        点击立即核验按钮
        :return: 异常原因
        """
        try:
            self.click(self.quick_verify_loc)
            time.sleep(2)
        except Exception as msg:
            return "异常原因%s" % msg

    def get_signature_result(self):
        """
        获取签名结果
        :return: 异常原因
        """
        try:
            content = self.find_elem_text(self.signature_result_loc)
            time.sleep(1)
            return content
        except Exception as msg:
            return "异常原因%s" % msg

    def click_copyright_chain_block_btn(self):
        """
        点击版权区块链联盟核验按钮
        :return: 异常原因
        """
        try:
            self.click(self.copyright_block_chain_loc)
            self.switch_to_window()
            time.sleep(1)
        except Exception as msg:
            return "异常原因%s" % msg

    def get_certificate_value(self):
        """
        获取证书内容完整性校验值
        :return:
        """
        try:
            content = self.find_elem_text(self.certificate_content_verify_loc)
            time.sleep(1)
            return content
        except Exception as msg:
            return "异常原因%s" % msg

    def get_hash_value(self):
        """
        获取查验公示Hash中,证书内容完整性校验值
        :return:
        """
        try:
            content = self.find_elem_text(self.hash_certificate_content_verify_loc)
            time.sleep(1)
            return content
        except Exception as msg:
            return "异常原因%s" % msg

    def user_certificate_verify(self):
        """
        用户证书核验
        :return:
        """
        self.click_user_portrait()
        # self.get_screen_shoot("我的创作首页", self.timestamp)
        self.click_user_work()
        self.refresh_current_page()
        # self.get_screen_shoot("作品详情页", self.timestamp)
        self.click_certificate_verify_btn()
        # self.get_screen_shoot("证书核验页", self.timestamp)
        self.type_input_check_num()
        self.get_screen_shoot("1.证书内容信息截图", self.timestamp)
        self.cdData.append(self.get_certificate_content_verify())
        self.primitiveTscCaData.append(self.get_certificate_main_content())
        self.click_copy_content_btn()
        self.open_hash_link()
        # self.get_screen_shoot("SHA加密首页", self.timestamp)
        self.SHA256_secret_content()
        self.get_screen_shoot("2.内容核验截图", self.timestamp)

    def user_trusted_time_verify(self):
        """
        用户授时可信时间核验
        :return:
        """
        self.click_user_portrait()
        # self.get_screen_shoot("我的创作首页", self.timestamp)
        self.click_user_work()
        # self.get_screen_shoot("作品详情页", self.timestamp)
        self.click_certificate_verify_btn()
        # self.get_screen_shoot("证书核验页", self.timestamp)
        self.type_input_check_num()
        # self.get_screen_shoot("证书内容完整性展示页", self.timestamp)
        self.scroll_to_less_middle()
        self.open_time_center()
        # self.get_screen_shoot("中国科学院国家授时中心页", self.timestamp)
        self.click_trusted_time_certificate_btn()
        self.get_screen_shoot("3.授时时间核验截图", self.timestamp)

    def user_digital_signature_verify(self):
        """
        用户数字签名核验
        :return:
        """
        self.click_user_portrait()
        # self.get_screen_shoot("我的创作首页", self.timestamp)
        self.click_user_work()
        # self.get_screen_shoot("作品详情页", self.timestamp)
        self.click_certificate_verify_btn()
        # self.get_screen_shoot("证书核验页", self.timestamp)
        self.type_input_check_num()
        # self.get_screen_shoot("证书内容完整性展示页", self.timestamp)
        self.scroll_to_more_bottom()
        self.click_iTrustChina_btn()
        # self.get_screen_shoot("诚信签验签页", self.timestamp)
        self.click_quick_verify_btn()
        self.get_screen_shoot("4.签名核验截图", self.timestamp)

    def user_copyright_block_chain_verify(self):
        """
        版权区块链联盟核验
        :return:
        """
        self.click_user_portrait()
        # self.get_screen_shoot("我的创作首页", self.timestamp)
        self.click_user_work()
        # self.get_screen_shoot("作品详情页", self.timestamp)
        self.click_certificate_verify_btn()
        # self.get_screen_shoot("证书核验页", self.timestamp)
        self.type_input_check_num()
        # self.get_screen_shoot("证书内容完整性展示页", self.timestamp)
        self.scroll_to_bottom()
        self.click_copyright_chain_block_btn()
        self.scroll_to_middle()
        self.get_screen_shoot("5.区块链核验截图", self.timestamp)
