class Rectangle:
    def __init__(self, length = 1, width = 1):
        self.length = length
        self.width = width

    def getPerimeter(self):
        return 2 * (self.length + self.width)

    def getArea(self):
        return self.length * self.width

    def setWidth(self, width):
        self.width = width

    def setLength(self, length):
        self.length = length

def main():

    rectangle1 = Rectangle()
    print("area", rectangle1.getArea())
    print("perimeter", rectangle1.getPerimeter())

    rectangle2 = Rectangle(10, 20)
    print("area", rectangle2.getArea())
    print("perimeter", rectangle2.getPerimeter())
    

main()
