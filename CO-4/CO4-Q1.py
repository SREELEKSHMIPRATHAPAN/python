class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length* self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

    def compare(R1,R2):
        if R1.area()>R2.area():
            print("\n Rectangles 1 is bigger")
        else:
            print("\nRectangle 2 is bigger")

        return

a=int(input("Enter length of 1st rectangle:"))
b=int(input("Enter length of 1st rectangle:"))
c=int(input("Enter length of 2nd rectangle:"))
d=int(input("Enter length of 2nd rectangle:"))
R1=Rectangle(a,b)
R2=Rectangle(c,d)
print("\nArea of 1st Rectangle :",R1.area())
print("\nPerimeter of 1st Rectangle:",R1.perimeter())
print("\nArea of 2nd Rectangle:",R2.area())
R1.compare(R2)
