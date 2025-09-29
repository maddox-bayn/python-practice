yclass Circle:
    pi = 3.14 # class object  attribut
    def __init__(self, radius) -> None:
        self.radius=radius
        self.area = self.pi * radius * radius
    def circumferace(self):
        circum = 2*self.pi*self.radius
        return circum
circle = Circle(4)
print(circle.circumferace())
print(circle.area)

class Rectangle:
    def __init__(self, lenght, breght) -> None:
        self.lenght = lenght
        self.breght = breght
    def get_area(self):
        return self.lenght * self.breght
ractangle = Rectangle(4, 8)
print(ractangle.get_area())