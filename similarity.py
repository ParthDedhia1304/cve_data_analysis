from transformers import AutoTokenizer, AutoModel
import torch
import warnings
import os
from dotenv import load_dotenv
from pinecone import Pinecone
from pymongo import MongoClient

# Suppress warnings
warnings.filterwarnings("ignore")

# Load env
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Pinecone setup
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("cveindex")

# MongoDB setup
client = MongoClient(MONGODB_URI)
db = client["nlp"]
collection = db["cve"]  # ✅ Correct collection

class SimilaritySearch:
    def __init__(self):
        """Initialize with MiniLM model + tokenizer (384-dim)."""
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
        self.model = AutoModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def search(self, query, top_k=5):
        """Search for similar CVEs based on query."""
        # Encode query
        inputs = self.tokenizer(query, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            model_output = self.model(**inputs)

        # Mean pooling
        token_embeddings = model_output.last_hidden_state
        attention_mask = inputs["attention_mask"]
        mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        sum_embeddings = torch.sum(token_embeddings * mask_expanded, 1)
        sum_mask = torch.clamp(mask_expanded.sum(1), min=1e-9)
        query_embedding = sum_embeddings / sum_mask

        query_vector = query_embedding[0].tolist()

        # Query Pinecone
        response = index.query(namespace="ns1", vector=query_vector, top_k=top_k)

        results = []
        for res in response["matches"]:
            result = collection.find_one({"id": res["id"]})  # ✅ correct lookup
            description = result.get("description", "Not Available") if result else "Not Available"

            results.append({
                "cve_id": res["id"],
                "description": description,
                "similarity_score": round(res["score"]*2 , 4)
            })

        return results


# Initialize once
search_engine = None

def get_search_engine():
    global search_engine
    if search_engine is None:
        search_engine = SimilaritySearch()
    return search_engine
