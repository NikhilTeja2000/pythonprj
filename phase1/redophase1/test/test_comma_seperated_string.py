import unittest
from phase1.redophase1.comma_seperated_string import  CommaSeperatedString

class MyTestCase(unittest.TestCase):

    def test_right_no_of_lines(self):
        value=CommaSeperatedString("hi,how,are,you,doing")
        answer=value.seperate()
        self.assertEqual(answer,5)




if __name__ == '__main__':
    unittest.main()
