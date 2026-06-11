import unittest
from phase1.redophase1.shapes import Shape, Rectangle, Square


class MyTestCase(unittest.TestCase):


    def test_cal_rec_area(self):
        #arrange
        value=Rectangle(2,3)
        #act
        result=value.cal_area()
        #assert
        self.assertEqual(result,6)

    def test_cal_rec_perimeter(self):
        #arrange
        value=Rectangle(2,3)
        #act
        result=value.cal_perimeter()
        #assert
        self.assertEqual(result,10)

    def test_cal_squ_area(self):
        #arrange
        value=Square(2)
        #act
        result=value.cal_area()
        #assert
        self.assertEqual(result,4)

    def test_cal_squ_perimeter(self):
        #arrange
        value=Square(2)
        #act
        result=value.cal_perimeter()
        #assert
        self.assertEqual(result,8)



if __name__ == '__main__':
    unittest.main()
