print("super market details");
sno=int(input("enter the serial no"))
cname=input("enter the customer name")
noproduct=int(input("enter the no of product"))
total=int(input("enter the total value"))
discount=total/50
newvalue=total-discount
print("sno is",sno)
print("cname is",cname)
print("noproduct is",noproduct)
print("discount value is",discount)
print("newvalue is",newvalue)