print("supermarket billing")
print("1.water 2. juice 3. choclate 4.'biscuit '5.milk ")
selected=int(input("enter the item are u want from market"))
unit=int(input("enter the no item u want"))
while True:
    if  selected==1:
        water=10
        price=water*unit
        print("the price of water of unit ",unit,"is",price)
        continue
    elif  selected==2:
        juice=35
        price=juice*unit
        print("the price of juice of unit ",unit,"is",price)
        continue
    elif  selected==3:
        choclate=40
        price=choclate*unit
        print("the price of choclate of unit ",unit,"is",price)
        continue
    elif  selected==4:
        biscuit=20
        price=biscuit*unit
        print("the price of biscuite of unit ",unit,"is",price)
        continue
    elif  selected==5:
        milk=31
        price=milk*unit
        print("the price of milk of unit ",unit,"is",price)
        continue
    elif selected==5:
        print("thankyou for selected the market **ALWAYS UR WELCOME")
        break
    else:
        print("enter the correct item in the list") 
        selected=int(input("enter the item are u want from market"))
        unit=int(input("enter the no item u want"))
        continue
