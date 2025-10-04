import torch
import json
import os
from dotenv import load_dotenv
from pinecone import Pinecone
from pinecone.exceptions import NotFoundException

# Load env
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Init Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "cveindex"

# 🔍 Get index info dynamically (so no hardcoding region)
indexes = pc.list_indexes().to_dict()["indexes"]
index_info = next((idx for idx in indexes if idx["name"] == index_name), None)

if not index_info:
    raise ValueError(f"Index '{index_name}' not found in Pinecone project!")

print(f"ℹ️ Using index '{index_name}' at host: {index_info['host']}")

# Connect to index
index = pc.Index(index_name, host=index_info["host"])

# ✅ Try reset namespace safely
try:
    print("⚠️ Clearing old namespace 'ns1'...")
    index.delete(delete_all=True, namespace="ns1")
    print("✅ Namespace 'ns1' cleared.")
except NotFoundException:
    print("ℹ️ Namespace 'ns1' not found — continuing fresh upload.")

# Load embeddings
embeddings = torch.load("embeddings.pt")
print("✅ Embeddings loaded:", embeddings.shape)

# Load CVE IDs
with open("data_for_vectordb.json", "r", encoding="utf-8") as f:
    records = json.load(f)

assert len(records) == embeddings.shape[0], f"❌ Mismatch: {len(records)} records vs {embeddings.shape[0]} embeddings"

# Prepare vectors
vectors = [
    {"id": records[i]["id"], "values": embeddings[i].tolist()}
    for i in range(len(records))
]

# Upload in batches
batch_size = 500
for i in range(0, len(vectors), batch_size):
    batch = vectors[i:i+batch_size]
    try:
        index.upsert(vectors=batch, namespace="ns1")
        print(f"✅ Uploaded batch {i//batch_size + 1} ({len(batch)} vectors)")
    except Exception as e:
        print(f"⚠️ Error uploading batch {i//batch_size + 1}: {e}")
        break

# Verify
stats = index.describe_index_stats()
print("📊 Final stats:", stats)
