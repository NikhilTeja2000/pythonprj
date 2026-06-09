import unittest

from phase1.redophase1.temperature_converter import TemperatureConverter

class MyTestCase(unittest.TestCase):

    def test_cel_to_feh(self):
        #Arrange
        value=TemperatureConverter(0)
        #Act
        result=value.calculate_cel_to_feh()
        #Assert
        self.assertEqual(result,32)

    def test_feh_to_cel(self):
        #arrange
        value=TemperatureConverter(32)
        #Act
        answer=value.calcualte_feh_to_cel()
        #assert
        self.assertEqual(answer,0)



if __name__ == '__main__':
    unittest.main()
