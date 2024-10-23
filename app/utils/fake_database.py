from json import load
from app import CategoryExample, Category
from mongodb_connection import MongoDBConnection


def load_knowledge_data():
    # Use the MongoDBConnection class instead of reading from JSON
    # You can modify URI or database/collection names if needed
    mongo_conn = MongoDBConnection()
    return mongo_conn.load_data()
