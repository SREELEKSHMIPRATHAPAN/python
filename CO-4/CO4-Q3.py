class Rectangle:
    __length=0
    __width=0
    __area=0
    def __init__(self,l,w):
        self.__length=l;
        self.__width=w;
    def area(self):
        return self.__length*self.__width
    def __lt__(self,other):
        if(self.__area<other.__area):
            return True
        else:
            return False
obj1=Rectangle(2,3)
obj2=Rectangle(1,2)
if(obj1.area()<obj2.area()):
    print("obj1 is smaller in area")
else:
    print("obj2 is smaller in area")
        




