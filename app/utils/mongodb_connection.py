from pymongo import MongoClient
from app.utils.models import Category, CategoryExample


class MongoDBConnection:
    def __init__(self, uri="mongodb://localhost:27017/", database_name="knowledge_base", collection_name="knowledge_base"):
        self.client = MongoClient(uri)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def fetch_data(self):
        return self.collection.find()

    def load_data(self):
        dataset = self.fetch_data()

        dataset_pyd = {}

        for entry in dataset:
            category = entry.pop("category")
            if category not in dataset_pyd:
                dataset_pyd[category] = []

            examples = entry.pop("examples")
            examples_pyd = [CategoryExample(**item) for item in examples]

            category_entry = Category(
                **entry, examples=examples_pyd
            )
            dataset_pyd[category].append(category_entry)

        return dataset_pyd
