#hierarchy inheritance
class hier:
    def car(self):
        print("car hav edifferent parts")
class wheel(hier):
    def wheel(self):
        print("wheel is used to sprinting")
class ceat(hier):
    def ceat(self):
        print("ceat used to sit in the car")
obj=ceat()
obj.ceat()
obj.car()
