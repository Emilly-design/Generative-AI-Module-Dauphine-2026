import os
import configparser
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/twitter_data_clean_sample.csv")
CHROMA_PATH = os.path.join(BASE_DIR, "../chroma_db")

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB client
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(name="twitter_support")


def index_data():
    """Load CSV and index all tweets into ChromaDB (only if not already indexed)."""
    if collection.count() > 0:
        print(f"ChromaDB already indexed ({collection.count()} documents). Skipping.")
        return

    print("Indexing data into ChromaDB...")
    df = pd.read_csv(DATA_PATH)

    documents = df["customer_tweet"].tolist()
    metadatas = [
        {"company_tweet": row["company_tweet"], "company": row["company"]}
        for _, row in df.iterrows()
    ]
    embeddings = embed_model.encode(documents).tolist()
    ids = [f"doc_{i}" for i in range(len(documents))]

    collection.add(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids,
    )
    print(f"Indexed {len(documents)} documents.")


def search(query: str, company: str, n_results: int = 3) -> list[dict]:
    """Search for similar past interactions for a given company."""
    query_embedding = embed_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results * 2,  # fetch more to filter by company
        include=["documents", "metadatas", "distances"],
    )

    # Filter by company
    filtered = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        if meta["company"].lower() == company.lower():
            filtered.append({
                "customer_tweet": doc,
                "company_tweet": meta["company_tweet"],
                "distance": dist,
            })
        if len(filtered) >= n_results:
            break

    return filtered
