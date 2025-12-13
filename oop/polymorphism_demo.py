import math 
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the method area()")
<<<<<<< HEAD
    
    class Circle(Shape):
        def __init__(self,radius):
            self.radius = radius
    def area(self):
       return math.pi * (self.radius) ** 2

=======
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
       return math.pi * (self.radius) ** 2
>>>>>>> 53791f627d7adc1c922f618a8ab852ee4c3aad70

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
<<<<<<< HEAD
    
=======
>>>>>>> 53791f627d7adc1c922f618a8ab852ee4c3aad70

    
