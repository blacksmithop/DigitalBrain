from pymongo import MongoClient
from json import load
from app.utils.models import Category, CategoryExample

DATABASE_NAME = "knowledge_repo"
COLLECTION_NAME = "domain_specific"

class MongoDB:
    def __init__(
        self,
        uri="mongodb://localhost:27017/",
    ):
        self.client = MongoClient(uri)
        self.database = self.client[DATABASE_NAME]
        collection_exists = self._check_if_collection_exists()
        if not collection_exists:
            self._populate_collection()
        
    def _check_if_collection_exists(self):
        collections = self.database.list_collection_names()
        if COLLECTION_NAME not in collections:
            self.collection = self.database[COLLECTION_NAME]
            return False
        self.collection = self.database[COLLECTION_NAME]
        return True
    
    def _populate_collection(self):
        with open("./static/reference/knowledge_base_data.json") as f:
            data = load(f)
        print(f"Loaded sample collection data ({len(data)})")
        self.collection.insert_many(data)
        print("Inserted sample collection data")
    
    def _fetch_data(self, exclude_id: bool = True):
        if exclude_id:
            return self.collection.find({}, {'_id': False})
        return self.collection.find()
    
    def get_domain_knowledge(self):
        data = self._fetch_data()
        return list(data) # use next for processing

    # def load_data(self):
    #     dataset = self.fetch_data()

    #     dataset_pyd = {}

    #     for entry in dataset:
    #         category = entry.pop("category")
    #         if category not in dataset_pyd:
    #             dataset_pyd[category] = []

    #         examples = entry.pop("examples")
    #         examples_pyd = [CategoryExample(**item) for item in examples]

    #         category_entry = Category(**entry, examples=examples_pyd)
    #         dataset_pyd[category].append(category_entry)

    #     return dataset_pyd
