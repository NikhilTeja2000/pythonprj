import unittest

from  phase1.redophase1.odd_even_checker import OddEvenChecker



class MyTestCase(unittest.TestCase):
  # add assertion here

    def test_even_number(self):
        checker=OddEvenChecker(4)
        result=checker.check()
        self.assertEqual(result,"Even")

    def test_odd_number(self):
        checker=OddEvenChecker(5)
        result=checker.check()
        self.assertEqual(result,"Odd")






if __name__ == '__main__':
    unittest.main()
