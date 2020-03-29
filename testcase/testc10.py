import unittest
class DEVISION(unittest.TestCase):
    def setUp(self):
        print('********************除法运算，开始啦*************************')


    def test_chuQ(self):
        '''除法运算7'''
        a = 10
        b = 5
        result = a / b
        ex = 2
        self.assertEqual(result, ex)

    def test_chuq(self):
        '''除法运算8'''
        a = 10
        b = 6
        result = a / b
        ex = 2
        self.assertEqual(result, ex)

    def tearDown(self):
        print('----------------------除法运算，结束啦-------------------------------------')


if __name__ == "__main__":
    unittest.main()