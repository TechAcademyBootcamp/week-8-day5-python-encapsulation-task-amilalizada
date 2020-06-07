class Shape():
    def __init__(self,color,filled):
        self.color=color
        if filled==True:
            self.filled='filled'
        else:
            self.filled='not filled'
    def toString(self):
        return f'A Shape with color of {self.color} and {self.filled}'
shape=Shape('red',True)
print(shape.toString())

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        return f'Area circle -{self.radius}'

    def getPerimetr(self):
        return f'perimetr circle - {self.radius*3.14}'

    def toString(self):
        return f'A Circle with radius={self.radius}, which is a subclass of {super().toString()}'

class Rectangle(Shape):
    def __init__(self,width,length):
        
        self.width=width
        self.length=length

    def getArea(self):
        return self.width * self.length
    def getPerimetr(self):
        return 2*(self.width + self.length)
    
    def toString(self):
        return f'A Rectangle with width={self.width} and length={self.length}, which is a subclass of {super(Rectangle,self).toString()}'

class Square(Rectangle):
    def __init__(self,a):

        super().__init__(a,a)
square = Square(2)
print(square.getArea())
print(square.getPerimetr())



