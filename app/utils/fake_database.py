from json import load
from app import CategoryExample, Category
# from mongodb_connection import MongoDBConnection



# TODO: Use the MongoDBConnection class instead of reading from JSON
# You can modify URI or database/collection names if needed
# mongo_conn = MongoDBConnection()
# return mongo_conn.load_data()

def load_knowledge_data():
    with open("./static/reference/knowledge_base_data.json") as f:
        dataset = load(f)
        
    dataset_pyd = {}
    
    for category, values in dataset.items():
        dataset_pyd[category] = []
        
        for value in values:
            examples = value.pop("examples")
            examples_pyd = [CategoryExample(**item) for item in examples]
            
            entry = Category(
                **value, examples=examples_pyd
            )
            dataset_pyd[category].append(entry)
            
    return dataset_pyd


