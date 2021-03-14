#To find area of square
square=lambda x: x*x
side=int(input("enter length of a side of square"))
print("Area of square is ",square(side))

#To find area of rectangle
rectangle=lambda a,b: a*b
a=int(input("enter length of rectangle"))
b=int(input("enter breadth of rectangle"))
print("Area of rectangle is ",rectangle(a,b))

#To find area of triangle
triangle=lambda b,h: 0.5*b*h
b=int(input("enter base length of triangle"))
h=int(input("enter height of triangle"))
print("Area of triangle is ",triangle(b,h))