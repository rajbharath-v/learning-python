from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017/')
db=client['raj']
collection=db['']
document={
    'name':'goodmorning',
    'email':'rajbharath@mail.com',
    'age':41
}
insert_result=collection.insert_one(document)
print(f"inserted document id:{insert_result.inserted_id}")

found_doc=collection.find_one({'name':'goodmorning'})
print(f'found document:{found_doc}')

update_result=collection.update_one(
    {'name':'goodmorning'},{'$set':{'age':31}})
print(f'update document {update_result.modified_count}')

delete_result=collection.delete_one({'name':'goodmorning'})
print(f'deleted documents: {delete_result.deleted_count}')

print('all documents:')
for doc in collection.find():
    print(doc)
client.close()