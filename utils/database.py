from pymongo import MongoClient
from config import Config

def get_db():
    client = MongoClient(Config.MONGO_URI)
    db = client.get_default_database('expense_sharing_app')
    return db
