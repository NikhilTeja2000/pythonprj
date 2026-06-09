class OddEvenChecker:

    def __init__(self,number):
        self.number=number

    def check(self):
        if self.number%2==0:
            return "Even"
        else:
            return "Odd"