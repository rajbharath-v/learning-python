atmno=int(input("enter the atm number"))
pin=int(input("enter the pin no:"))
amount=int(input("enter the amount:"))
pin1=1324
balance=10000
if pin<10000:
    if pin1==pin:
        print("the entered pin right")
        if balance>amount:
              print("u have efficient amount to withdraw in your account ")       
        else :
                print("u dont have enough balance to withdraw the amont in the bank")
    else:
        print("the entered pin is wrong")            