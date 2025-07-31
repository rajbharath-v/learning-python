#multilevel
class multilev:
    def raj(self):
        print("grandfather")
class bi(multilev):
    def raj1(self):
        print("father")
class sing(bi):
    def raj2(self):
        print("son")
obj=sing()
obj1=bi()
obj.raj2()
obj.raj1()
obj1.raj()
