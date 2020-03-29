import unittest
from bs4 import BeautifulSoup
class ADD(unittest.TestCase):
    def setUp(self):
        print('********************加法运算，开始啦*************************')


    def test_jia1(self):
        '''加法运算1'''
        a = 10
        b = 7
        result = a + b
        ex = 15
        self.assertEqual(result, ex)

    def test_jiaa(self):
        '''加法运算2'''
        a = 10
        b = 6
        result = a + b
        ex = 16
        self.assertEqual(result, ex)

    def tearDown(self):
        print('----------------------加法运算，结束啦-------------------------------------')


if __name__ == "__main__":
    unittest.main()