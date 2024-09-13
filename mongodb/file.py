from pymongo import MongoClient


# car brands and models
dict_1 = {
    'BMW': 'X5',
    'Audi': 'A8',
    'Mercedes': 'C200',
    'Toyota': 'Camry',
    'Honda': 'Civic'
}


def get_database():
    
    CONNECTION_STRING = "mongodb://localhost:27017/"
    
    client = MongoClient(CONNECTION_STRING)
    
    return client[]