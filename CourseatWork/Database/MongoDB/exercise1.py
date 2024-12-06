from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD_PASS")

URL=f"mongodb+srv://{USER}:{PASSWORD}@mongopythondb.2bkcb.mongodb.net/?retryWrites=true&w=majority&appName=MongoPythonDB"
try:
    conn_obj = MongoClient(URL)
except Exception as e:
    print(e)
    
try:  
    #Creating database object
    database_obj = conn_obj ['Demo']
    #Creating collection
    collection_obj = database_obj['Employee']
    
    # inserting initial values
    document_list = [
    {"EmpID":"1","Name":"Tim","Dept":"ETA","Salary":21990},
    {"EmpID":"2","Name":"John","Dept":"ADM","Salary":22900},
    {"EmpID":"3","Name":"James","Dept":"FIN","Salary":28100},
    {"EmpID":"4","Name":"Robert","Dept":"ETA","Salary":100000}
    ]
    collection_obj.insert_many(document_list)
    
    # employees earning more then 25000
    
    docs = collection_obj.find({'Salary':{'$gt':25000}})
    for doc in docs:
        print(doc)
    
    
    # employees whose name start with J or whose dept has A
    docs1 = collection_obj.find({'$or':[{'Name':{'$regex':'^J'}},{'Dept':{'$regex':'A'}}]})
    for doc in docs1:
        print(f"Found...{doc}")
    
    #update dept of Jogn as "DNA"
    collection_obj.update({'Name':'John'},{'$set':{'Dept':'DNA'}})
    
    # print collection
    docs2 = collection_obj.find()
    for doc in docs2:
        print(doc)
    
    #dropping collection
    collection_obj.drop() 
    
except Exception as e:
    print(e)
    