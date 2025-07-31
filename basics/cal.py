print("1.add")
print("2.sub")
print("3.multi")
print("4.div")
print("5.exit")
choice=int(input("enter the choice"))
if (choice>1 and choice<4):
    a=int(input("enter the first number:"))
    b=int(input("etner the first number:"))
    if choice==1:
        c=a+b
        print("addition of two number is",c)
    elif choice==2:
        c=a-b
        print("aubtraction of two number is",c)
    elif choice==3:
        c=a*b
        print("multiplication of two number is",c)
    elif choice==4:
        c=a/b
        print("divition of two number is",c)
else:
    print("please enter the correct choice between the 1 to 4")