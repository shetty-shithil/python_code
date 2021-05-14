import math
class Abc:
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return(math.pi*(self.rad**2))
a=Abc(int(input('Enter radius of a circle:')))
print('Area of a circle is ',a.area())
