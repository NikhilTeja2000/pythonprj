class Factorial:

    def __init__(self,number):

        self.number=number

    def fact(self):
        count=1

        for a in range(self.number,1,-1):
            count=count*a
        return count

    def recurssion_check(self):

        if self.number==1:
            return 1
        current=self.number
        self.number=self.number-1
        return current * self.recurssion_check()
