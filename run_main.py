# coding:utf-8
import unittest, os, time
import HTMLTestRunner
#from common import HTMLTestRunner_pic    #导入公用模块

class math4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass初始化操作：用例开始前只执行一次")

    @classmethod
    def tearDownClass(cls):
     print("tearDownClass收尾清理操作：用例结束时候只执行一次")


def all_case(case="testcase"):
    '''加载指定目录下的所有的用例'''
    # 待执行用例的目录
    case_dir = os.getcwd() + "\\" + case
    #加载测试用例
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)

    #discover方法筛选出来的用例循环添加到测试套件中。

    print(discover)       # 打印测试用例，如果要执行该语句必须进行函数调用
    return discover


if __name__ == "__main__":
    all_case()
    # 返回实例,测试结果是文本格式
    runner = unittest.TextTestRunner()
    runner.run(all_case())

    # 测试报告的路径
    report_path = os.getcwd()+'\\report\\'+time.strftime('%Y_%m_%d_%H_%M_%S')+'_report.html'

    fp = open(report_path, 'wb')           #wb表示以二进制数据写入html文件中
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title=u'接口自动化测试报告',description=u'用例执行情况：')
    # verbosity: 2 显示测试用例函数描述
    runner.run(all_case())
    fp.close()
