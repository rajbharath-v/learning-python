from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017')
db=client['newdata']
collection=db['data']
def create():
    name=input("Enter the name:")
    accno=input("Enter the email: ")
    amount=int(input("enter the amount in the bank"))
    phno=int(input("enter the user phone number"))
    doc={'name':name,'accno':accno,'amount':amount,'phno':phno}
    result=collection.insert_one(doc)
    print(f"Document inserted with ID{result.inserted_id}")
def read():
    name=input("enter the name to search")
    doc=collection.find_one({'name':name})
    if doc:
        print(f"found:{doc}")
    else:
        print("No document found.")
def update():
    accno=input("enter account no to update:")
    choice=("1.account amount update /n 2. update the new phoneno ")
    if choice==1:
        insert_amount=int(input("enter the new amount to insert"))
        doc=collection.updated_one({'accno':accno},{'$set':{'amount':insert_amount}})
        print(f"modified count:{doc.modified_count}")
    elif choice==2:
        new_phno=int(input("enter the new phone no to chang in ur account"))
        doc=collection.updated_one({'accno':accno},{'$set':{'phno':new_phno}})
        print(f"modified count:{doc.modified_count}")
def delete():
    accno=input("enter the account no to delete")
    doc=collection.delete_one({'accno':accno})
    print(f"Deleted count:{doc.deleted_count}")
def showall():
    print("all document:")
    for doc in collection.find():
        print(doc)
while True:
    print("\n== CRUD Menu")
    print("1. Create ") 
    print("2.Read")
    print("3.update")
    print('4.delete')
    print("5.showall")
    print("6.exit")
    choice=input("enter choice (1-6):")
    if choice=='1': 
        create()
    elif choice=='2': 
        read()
    elif choice=='3': 
        update()
    elif choice=='4':
        delete() 
    elif choice=='5':
        showall() 
    elif choice=='6':
        print("goodbye") 
        break
client.close()
