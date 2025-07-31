from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017')
db=client['data1']
collection=db['data']
def book():
    name=input("enter the name:")
    age=int(input("etner the age of the person"))
    noc=int(input("enter the no of ceat"))
    price=(noc*100)
    for i in range(1,noc):
        ceat=int(input("enter the ceat no want"))
    doc={'name':name,'name':name,'noc':noc,'ceat':ceat,'price':price}
    result=collection.insert_one(doc)
    print(f"documetn inserted with id{result.inserted_id}")
def view():
    name=input("enter the name to view the details")
    doc=collection.find({'name':name})
    if doc:
        print(f"found:{doc}")
    else:
        print("no bookikng list is found")
def change():
    name=input("enter the name of person for update the ceat details")
    new_ceat=int(input("enter the new cdeat no"))
    doc=collection.update_one({'name':name},{'$set':{'ceat':new_ceat}})
    print(f"modified count:{doc.modified_count}")

def cancel():
    name=input("enter the name of the user for delete the booked ticked")
    doc=collection.delete_one({'name':name})
    print(f"deleted count:{doc.deleted_count}")
while True:
    print(" bus ticket")
    print("1.booking")
    print("2.viewing")
    print("3.changing the ceat no")
    print("4.cancelling the boooking ticket")
    print("5.exit form the booking the ticket")
    choice=input("enter choice (1-6):")
    if choice=='1':
        book() 
    elif choice=='2':
        view()
    elif choice=='3':
        change()
    elif choice=='4':
        cancel()
    elif choice=='5':
        print("exit from the ticket booking")
        break

client.close()
