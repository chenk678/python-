import unittest
class SUB(unittest.TestCase):
    def setUp(self):
        print('********************减法运算，开始啦*************************')


    def test_jianP(self):
        '''减法运算3'''
        a = 10
        b = 7
        result = a - b
        ex = 15
        self.assertEqual(result, ex)

    def test_jianb(self):
        '''减法运算4'''
        a = 10
        b = 6
        result = a - b
        ex = 4
        self.assertEqual(result, ex)

    def tearDown(self):
        print('----------------------减法运算，结束啦-------------------------------------')


if __name__ == "__main__":
    unittest.main()