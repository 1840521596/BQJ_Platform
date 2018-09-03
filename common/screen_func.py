# coding=utf-8
import os
import time
from selenium import webdriver

# def take_screen_shot(driver, file_name):
#     # 截图函数
#     base_dir = os.path.dirname(os.path.dirname(__file__))
#     base_dir = str(base_dir)
#     base_dir = base_dir.replace('/', '\\')
#     base = base_dir.split('\\report')[0]
#     file_path = base + '\\report\\image\\' + file_name
#     driver.get_screenshot_as_file(file_path)

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com")
#     take_screen_shot(driver, "baidu.png")
#     time.sleep(3)
#     driver.quit()