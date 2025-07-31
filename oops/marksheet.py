class raj:
     def __init__(self):
          pass
     def fun(self):
            print("bank number is",obj1.a)
            print("name is",obj1.name)
            print("age is",obj1.age)    
            print("address is",obj1.ad)
            
     def raj(self):
            print("amount is",obj1.amount)
            print("interest is",obj1.interest)
            print("total amount is",obj1.amount+obj1.interest)
a=int(input("enter a bank number: "))
name=input("Enter name: ")
age=int(input("Enter age: "))
ad=input("Enter address of bank: ")
amount=int(input("Enter the amount: "))
interest=int(input("Enter the interest: "))
obj1=raj()
obj1.a=a
obj1.name=name
obj1.age=age
obj1.ad=ad
obj1.amount=amount
obj1.interest=interest
obj1.fun()
obj1.raj()
print("bank number is",obj1.a)
print("name is",obj1.name)
print("age is",obj1.age)    
print("address is",obj1.ad)
print("amount is",obj1.amount)
print("interest is",obj1.interest)
print("total amount is",obj1.amount+obj1.interest)