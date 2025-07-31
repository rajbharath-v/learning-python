#multiple inheritance
class car:
    def raj(self):
        print("car is runing")
class bike:
    def speed(self):
        print("bike is runnning")
class vehicle(car,bike):
    def travel(self):
        print("vehicle used to travel all around the world")
obj=vehicle()
obj.travel()
obj.speed()
obj.raj()
