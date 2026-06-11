class Shape:
    def cal_area(self):
        pass

    def cal_perimeter(self):
        pass



class Rectangle(Shape):

    def __init__(self,l,b):
        self.l=l
        self.b=b


    def cal_area(self):
        return self.l * self.b

    def cal_perimeter(self):
        return 2 * self.l + 2 * self.b

class Square(Rectangle):

    def __init__(self,side):
        super().__init__(side,side)



if __name__ == '__main__':

    obw=Rectangle(2,3)
    print(obw.cal_perimeter())
    obe=Square(2)
    print(obe.cal_area())








