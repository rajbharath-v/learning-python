sno=int(input("Enter the no:"))
sname=input("Enter the sname:")
saddress=input("Enter the saddress:")
tamil=int(input("Enter the tamil mark:"))
english=int(input("Enter the english mark:"))
maths=int(input("Enter the maths mark:"))
science=int(input("Enter the science mark:"))
social=int(input("Enter the social mark:"))
total=tamil+english+maths+science+social
avg=total/5
if tamil<35 or english<35 or maths<35 or science<35 or social<35:
    print("resul= fail")
else:
    print("result=pass")
if (total<250):
    print("poor in all subject")
elif(total<300):
    print("below avg")
elif(total<350):
    print("average mark in all subject")
elif(total<400):
    print("goood at all subject")
print("sno is",sno)
print("sname is",sname)
print("saddress is:",saddress)
print("tamil mark is", tamil)
print("english mark is", english)
print("maths mark is", maths)
print("science mark is", science)
print("social mark is", social)
print("total mark is ",total)
print("avg mark is",avg)