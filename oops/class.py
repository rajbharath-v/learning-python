class area:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        pass
    def square(self):
        area=self.a*self.a
        perimeter=4*self.a
        print("area of square",area)
        print("perimeter of square",perimeter)
    def rectangle(self):
        area=self.a*self.b
        perimeter=2*(self.a+self.b)
        print("area of rectangle",area)
        print("perimeter of rectangle",perimeter)
    def triangle(self):
        area=0.2*self.a*self.b
        perimeter=a.self+b.self+c.self
        print("area of triangle",area)
        print("perimeter of triangle",perimeter)
    def circle(self):
        area=3.14*a.self*a.self
        perimeter=2*3.14*a.self
        print("area of circle is",area)
        print("perimeter of circle",perimeter)
        
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
obj=area(a,b,c)
obj.square()
obj.rectangle()
obj.triangle()
obj.circle()