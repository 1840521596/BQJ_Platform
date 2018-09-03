# # coding=utf-8
# import sys
# import time
# from HTMLTestRunner import HTMLTestRunner
# import unittest
# sys.path.append("./main")
# # 指定测试用例为当前文件夹下的main目录
# test_dir = './main'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
#
# if __name__ == '__main__':
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     file_name = './report/' + now + '_result.html'
#     fp = open(file_name, 'wb')
#     runner = HTMLTestRunner(stream=fp,
#                             title=u'ServicePlatform Test Report',
#                             description=u'Implementation Example with:')
#     runner.run(discover)
#     fp.close()
