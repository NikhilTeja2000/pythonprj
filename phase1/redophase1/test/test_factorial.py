import unittest

from phase1.redophase1.factorial import Factorial

class MyTestCase(unittest.TestCase):

    def test_5_factorial(self):
        value=Factorial(5)
        result=value.fact()
        self.assertEqual(result,120)

    def test_4_factorial(self):
        value=Factorial(4)
        result=value.fact()
        self.assertEqual(result,24)

    def test_5_rec_factotial(self):
        value=Factorial(5)
        result=value.recurssion_check()
        self.assertEqual(result,120)



if __name__ == '__main__':
    unittest.main()
