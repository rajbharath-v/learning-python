class vehicle:
    def __init__(self,a):
        self.a=a
        pass
    def  raj(self):
        print("superclass method")
class car(vehicle):
    def tam(self):
        print("child class method")
        print(self.a)
obj1=car("fghj")
obj1.raj()
obj1.tam()
    
