import os
import re
import hashlib
from pathlib import Path
from typing import List

import faiss
import numpy as np
from dotenv import load_dotenv


load_dotenv()

PROJECT_NAME = os.getenv("PROJECT_NAME", "AutoResearch AI")
TOP_K = int(os.getenv("TOP_K", 3))

DATA_FILE = Path("data/documents.txt")
EMBED_DIM = 64


def load_documents(file_path: Path) -> List[str]:
    if not file_path.exists():
        raise FileNotFoundError(f"Could not find file: {file_path}")

    with file_path.open("r", encoding="utf-8") as f:
        documents = [line.strip() for line in f if line.strip()]

    if not documents:
        raise ValueError("No documents found in documents.txt")

    return documents


def tokenize(text: str) -> List[str]:
    return re.findall(r"[a-zA-Z0-9]+", text.lower())


def token_to_vector(token: str, dim: int = EMBED_DIM) -> np.ndarray:
    digest = hashlib.sha256(token.encode("utf-8")).digest()
    seed = int.from_bytes(digest[:8], "big")
    rng = np.random.default_rng(seed)
    return rng.standard_normal(dim).astype("float32")


def text_to_embedding(text: str, dim: int = EMBED_DIM) -> np.ndarray:
    tokens = tokenize(text)
    if not tokens:
        return np.zeros(dim, dtype="float32")

    token_vectors = np.array([token_to_vector(token, dim) for token in tokens], dtype="float32")
    embedding = token_vectors.mean(axis=0)

    norm = np.linalg.norm(embedding)
    if norm > 0:
        embedding = embedding / norm

    return embedding.astype("float32")


def build_index(documents: List[str]) -> faiss.IndexFlatIP:
    embeddings = np.array([text_to_embedding(doc) for doc in documents], dtype="float32")
    index = faiss.IndexFlatIP(EMBED_DIM)
    index.add(embeddings)
    return index


def search_documents(index, documents, query, top_k):
    query_embedding = np.array([text_to_embedding(query)], dtype="float32")
    scores, indices = index.search(query_embedding, top_k)

    results = []
    for rank, (score, idx) in enumerate(zip(scores[0], indices[0]), start=1):
        if idx != -1:
            results.append({
                "rank": rank,
                "score": float(score),
                "document": documents[idx]
            })

    return results


def display_results(results):
    print("\n" + "="*50)
    print(f" Top {len(results)} Matches for your query")
    print("="*50)

    for item in results:
        print(f"\nResult {item['rank']}")
        print("-"*30)
        print(f"Score : {item['score']:.4f}")
        print(f"Text  : {item['document']}")

    print("\n" + "="*50)


def main():
    print(f"\n{PROJECT_NAME} - Semantic Search System")
    print("=" * 60)

    documents = load_documents(DATA_FILE)
    index = build_index(documents)

    print(f"Loaded {len(documents)} documents.")
    print("Knowledge base indexed successfully.")

    while True:
        query = input("\nEnter your question (or type 'exit' to quit): ").strip()

        if query.lower() == "exit":
            print("Exiting search system. Goodbye.")
            break

        if not query:
            print("Please enter a valid question.")
            continue

        results = search_documents(index, documents, query, TOP_K)
        display_results(results)


if __name__ == "__main__":
    main()