from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD_PASS")

URL=f"mongodb+srv://{USER}:{PASSWORD}@mongopythondb.2bkcb.mongodb.net/?retryWrites=true&w=majority&appName=MongoPythonDB"
try:
    conn_obj = MongoClient(URL)
    print("Connection established")
    print("################################################################################")
   
    #Creating database object
    database_obj = conn_obj ['ETA']
    
    #Creating collection object
    collection_obj = database_obj['student']
    document = {'Name':'John','Regd_id':'1','Age':20,'Sex':'M'}
    returnval = collection_obj.insert_one(document)
    print(returnval.inserted_id)
    print("################################################################################")

    #inserting many
    document_list = [
    {'Name':'Kelley','Regd_id':'2','Age':21,'Sex':'M'},
    {'Name':'Hannah','Regd_id':'3','Age':18,'Sex':'F'},
    {'Name':'Ravi','Regd_id':'4','Age':22,'Sex':'M'},
    {'Name':'Rachel','Regd_id':'5','Age':26,'Sex':'F'},
    {'Name':'Esther','Regd_id':'6','Age':19,'Sex':'F'}
    ]
    
    returnval = collection_obj.insert_many(document_list)
    print(returnval.inserted_ids)

    #Fetching the first document
    print('Find One Document:')
    doc = collection_obj.find_one()
    print(doc)
    print("################################################################################")

    #Fetching all the documents
    print('Find All Documents:')
    docs = collection_obj.find()
    for doc in docs:
        print(doc)
    print("################################################################################")

    #filtering based on condition
    docs1 = collection_obj.find({'Sex':'F'})
    for doc in docs1:
        print(doc)
    print("################################################################################")
    # students whose age is greater than 21
    docs2 = collection_obj.find({'Age':{'$gt':21}})
    for doc in docs2:
        print(doc)

    # Regex - fetch all the students whose name begins with ‘R’.
    docs4 = collection_obj.find({'Name':{'$regex':'^R'}})
    for doc in docs4:
        print(doc)

    # display student records with only name and age rather than all the columns such as _id, name, regd_id, age, and sex.
    docs5 = collection_obj.find({},{'_id':0,'Name':1,'Age':1})
    for doc in docs5:
        print(doc)
    print("################################################################################")    
        
    # sort documents based on age.
    docs6 = collection_obj.find({}).sort('Age',1)
    for doc in docs6:
        print(doc)

    print("################################################################################")    

    # To limit the number of documents to be displayed, use limit() method of cursor class. Also, pass the number of documents to be displayed as an argument to limit() method.
    docs6 = collection_obj.find({}).limit(2)
    for doc in docs6:
        print(doc)
        
    
    #Delete one record
    collection_obj.delete_one({'Regd_id':'1'})
    #Delete many records
    collection_obj.delete_many({'Regd_id':{'$gt':'4'}})
    
    #Dropping the collection
    collection_obj.drop()   
    
    
    #Fetches the list of databases
    db_list = conn_obj.list_database_names()
    print(db_list)
    print("################################################################################")    
    #Fetches the list of collections under 'ETA' database
    col_list = database_obj.list_collection_names()
    print(col_list)
        
except Exception as e:
    print(e)


