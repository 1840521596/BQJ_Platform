# coding=utf-8
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import common.methods


def find_element(self, *loc):
    """
    :param self: 传参固定为self
    :param loc: 元素id
    :return: 返回元素位置
    """
    try:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        return self.driver.find_element(*loc)
    except AssertionError:
        print("%s 页面中未能找到%s元素" % (self, loc))


def find_elem_text(self, loc):
    """
    :param self: 传参固定为self
    :param loc: 元素id
    :return: 返回元素所在的文本信息
    """
    return self.find_element(*loc).text


def verifyEqual(self, element_id, exp_result):
    """
    :param self: 传参固定为self
    :param element_id: 元素id
    :param exp_result: 预期结果
    :return:
    """
    global act_result
    try:
        act_result = self.find_elem_text(element_id)
        self.assertEqual(act_result, exp_result)
    except AssertionError:
        print("[ERROR]:%s is not equal to %s" % (act_result, exp_result))
        self.driver.get_screenshot_as_file(common.methods.project_path + "\\image\\" + act_result+'.png')


def verifyIn(self, element_id, exp_result):
    """
    :param self: 传参固定为self
    :param element_id: 元素id
    :param exp_result: 预期结果
    :return:
    """
    global act_result
    try:
        act_result = self.find_elem_text(element_id)
        self.assertIn(act_result, exp_result, "[ERROR]:expected is not contain actual")
        time.sleep(1)
    except AssertionError:
        self.driver.get_screenshot_as_file(common.methods.project_path + "\\image\\" + act_result+'.png')


def verifyEqualNum(self, actual, expected, img_name):
    """
    :param self:传参固定为self
    :param actual: 实际结果
    :param expected: 预期结果
    :param img_name: 屏幕截图命名
    :return:
    """
    if actual == expected:
        pass
    else:
        print("[ERROR]:" + str(actual) + "......is not equal to....." + str(expected))
        self.driver.get_screenshot_as_file(common.methods.project_path + "\\image\\" + img_name)



