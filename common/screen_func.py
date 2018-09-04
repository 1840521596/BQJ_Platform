# coding=utf-8
import datetime
import sys
sys.path.append('./image')


def get_screen_shot_name(file_name):
    """
    截图方法
    :param file_name: 图片名称
    :return: 返回截图
    """
    # 截图函数
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S_')
    filename = './image/' + timestamp + file_name
    return filename
    # if __name__ == '__main__':
    #     driver = webdriver.Chrome()
    #     driver.get("https://www.baidu.com")
    #     take_screen_shot(driver, "baidu.png")
    #     time.sleep(3)
    #     driver.quit()
