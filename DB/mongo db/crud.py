from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['masss']
collection = db['reals']

def create_document():
    name = input("Enter name: ")
    email = input("Enter email: ")
    age = int(input("Enter age: "))
    doc = {'name': name, 'email': email, 'age': age}
    result = collection.insert_one(doc)
    print(f"Document inserted with ID: {result.inserted_id}")

def read_document():
    r_name = input("Enter name to search: ")
    doc = collection.find_one({'name': r_name})
    if doc:
        print(f"Found: {doc}")
    else:
        print("No document found.")

def update_document():
    name = input("Enter name to update: ")
    new_age = int(input("Enter new age: "))
    result = collection.update_one({'name':   name}, {'$set': {'age': new_age}})
    print(f"Modified count: {result.modified_count}")

def delete_document():
    name = input("Enter name to delete: ")
    result = collection.delete_one({'name': name})
    print(f"Deleted count: {result.deleted_count}")

def show_all_documents():
    print("All documents:")
    for doc in collection.find():
        print(doc)

while True:
    print("\n=== CRUD Menu ===")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Show All")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")
    
    if choice == '1':
        create_document()
    elif choice == '2':
        read_document()
    elif choice == '3':
        update_document()
    elif choice == '4':
        delete_document()
    elif choice == '5':
        show_all_documents()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

client.close()