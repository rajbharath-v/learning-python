class vehicle:
    def raj(self):
        print("superclass")
class car(vehicle):
    def bhar(self):
        print("subclass")
obj=car()
obj.raj()
obj.bhar()
