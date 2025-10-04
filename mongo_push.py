import json
from pymongo import MongoClient

# Your MongoDB URI
MONGODB_URI = "mongodb+srv://parthdedhia04:parthdedhia04@cvedata.mca72ww.mongodb.net/?retryWrites=true&w=majority&appName=cvedata"
DB_NAME = "nlp"
COLLECTION_NAME = "cve_collection"

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def insert_into_mongo(data):
    client = MongoClient(MONGODB_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    
    # Optional: Clear collection before inserting
    collection.delete_many({})

    if isinstance(data, list):
        batch_size = 100  # adjust if needed
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]
            collection.insert_many(batch)

        print(f"✅ Inserted {len(data)} documents into '{COLLECTION_NAME}'")
    else:
        collection.insert_one(data)
        print("✅ Inserted 1 document.")

if __name__ == "__main__":
    data = load_data("final_data.json")
    insert_into_mongo(data)
