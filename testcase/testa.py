import unittest
class PLUS(unittest.TestCase):
    def setUp(self):
        print('********************乘法运算，开始啦*************************')


    def test_plus9(self):
        '''乘法运算5'''
        a = 10
        b = 7
        result = a * b
        ex = 80
        self.assertEqual(result, ex)

    def test_pluss(self):
        '''乘法运算6'''
        a = 10
        b = 6
        result = a * b
        ex = 60
        self.assertEqual(result, ex)

    def tearDown(self):
        print('----------------------乘法运算，结束啦-------------------------------------')


if __name__ == "__main__":
    unittest.main()