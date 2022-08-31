class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        P =  2*(self.length + self.width)
        return P

    def Area(self):
        A = self.length * self.width
        return A

    def display(self):
        print('Length = ', self.length)
        print('Width = ', self.width)
        print('Perimeter = ', self.Perimeter())
        print('Area = ', self.Area())

class Parallelepiped(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def Volume(self):
        V = self.Area() * self.height
        return V

    def display(self):
        print('Volume = ', self.Volume())
        
        
r = Rectangle(13,6)
r.display()

p = Parallelepiped(13,6,10)
p.display()

