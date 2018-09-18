# coding:utf-8
import time
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from common import methods
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s %(filename)s[line:%(lineno)d] '
#            '%(levelname)s %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     filename='log.log',
#     filemode='w'
# )
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)
#
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         info = func.__doc__
#         logging.info('testing at : %s' % info)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def errorLog(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except AssertionError:
#             logging.getLogger().exception('Exception')
#             exit()
#     return wrapper
#
#
# def consoleLog(info, level='INFO'):
#     if level is 'INFO':
#         logging.info(info)
#     elif level is 'WARNING':
#         logging.warning(info)
#     elif level is 'ERROR':
#         logging.error(info)


class Page(object):
    def __init__(self, driver, base_url, action, select, page_title, ):
        self.driver = driver
        self.base_url = base_url
        self.action = action
        self.select = select
        self.page_title = page_title

    def on_page(self, page_title):
        return page_title in self.driver.title

    def verify_open(self, base_url, page_title):
        # 使用get打开访问链接地址
        self.driver.get(base_url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page()方法
        assert self.on_page(page_title), u"打开开页面失败 %s" % base_url

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self.verify_open(self.base_url, self.page_title)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except AssertionError:
            print("%s 页面中未能找到%s元素" % (self, loc))

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except AssertionError:
            print("%s 页面中未能找到%s元素" % (self, loc))

    def find_layer(self, *loc):
        return self.find_element(loc)

    def find_elem_text(self, loc):
        return self.find_element(*loc).text

    def find_elem_attribute(self, loc):
        return self.find_element(*loc).get_attribute('innerHTML')

    # 定义script方法，用于执行js脚本
    def script(self, src):
        self.driver.execute_script(src)

    def type_input(self, loc, text):
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc))
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(text)
        except AssertionError:
            print("%s 页面中未能找到%s元素" % (self, loc))

    def click(self, loc):
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc))
            self.driver.find_element(*loc).click()
        except AssertionError:
            print("%s 页面中未能找到%s元素" % (self, loc))

    def get_screen_shoot(self, file_name, time_stamp):
        self.driver.get_screenshot_as_file(methods.project_path + '/image/%s %s.png ' % (file_name, time_stamp))
        time.sleep(1)

    def save_screen_shoot(self, file):
        self.driver.save_screenshot(file)

    def scroll_to_bottom(self):
        """
        滑动到底部
        :return:返回异常原因
        """
        try:
            js = "var q=document.documentElement.scrollTop=100000"
            self.script(js)
        except Exception as msg:
            return "异常原因%s" % msg

    def scroll_to_top(self):
        """
        滑动到顶部
        :return:返回异常原因
        """
        try:
            js = "var q=document.documentElement.scrollTop=0"
            self.script(js)
            time.sleep(2)
        except Exception as msg:
            return "异常原因%s" % msg

    def scroll_to_less_middle(self):
        """
        滑动到靠近顶部
        :return: 返回异常原因
        """
        try:
            js = "var q=document.documentElement.scrollTop=300"
            self.script(js)
            time.sleep(2)
        except Exception as msg:
            return "异常原因%s" % msg

    def scroll_to_middle(self):
        """
        滑动到中部
        :return:返回异常原因
        """
        try:
            js = "var q=document.documentElement.scrollTop=550"
            self.script(js)
            time.sleep(2)
        except Exception as msg:
            return "异常原因%s" % msg

    def scroll_to_more_bottom(self):
        """
        滑动到底部多点
        :return:返回异常原因
        """
        try:
            js = "var q=document.documentElement.scrollTop=1000"
            self.script(js)
            time.sleep(2)
        except Exception as msg:
            return "异常原因%s" % msg

    def switch_to_window(self):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != handles:
                self.driver.switch_to_window(handle)
            continue

    def select_options(self, loc, text):
        option_loc = self.find_element(*loc)
        sl = self.select(option_loc)
        sl.select_by_visible_text(text)

    def click_checkboxes(self, loc):
        checkboxes = self.find_elements(*loc)
        for check in checkboxes:
            check.click()
        print(len(checkboxes))

    def right_click(self, loc):
        loc = self.find_element(*loc)
        ActionChains(self.driver).context_click(loc).perform()

    def double_click(self, loc):
        loc = self.find_element(*loc)
        ActionChains(self.driver).double_click(loc).perform()

    def drag_and_drop(self, loc_source, loc_target):
        source = self.find_element(*loc_source)
        target = self.find_element(*loc_target)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def move_to_element(self, loc):
        loc = self.find_element(*loc)
        ActionChains(self.driver).move_to_element(loc).perform()

    def click_and_hold(self, loc):
        loc = self.find_element(*loc)
        ActionChains(self.driver).click_and_hold(loc).perform()

    def switch_to_alert(self):
        try:
            self.driver.switch_to_alert()
            return True
        except NoAlertPresentException:
            return False

    def get_title(self):
        return self.driver.title



