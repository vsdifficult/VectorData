import json
import numpy as np
from sentence_transformers import SentenceTransformer
import chromadb
import logging

logging.basicConfig(level=logging.INFO)

class VectorDatabase:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(name="text_collection")

    async def add_texts(self, new_texts):
        """Adds new texts to the database and updates vectors."""
        embeddings = self.model.encode(new_texts)
        
        self.collection.add(
            embeddings=embeddings.tolist(),
            documents=new_texts,
            ids=[str(i) for i in range(len(new_texts))]
        )

    async def search(self, query, top_n=5):
        """Searches for the most similar texts based on the query."""
        query_embedding = self.model.encode([query]).tolist()
        logging.info(f"Searching for query: {query} with embedding: {query_embedding}")
        results = self.collection.query(query_texts=[query], n_results=top_n)  # Updated line
        logging.info(f"Search results: {results}")
        return results

    async def load_texts(self, filepath):
        """Loads texts from a file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                texts = json.load(f)
                if texts:  # Check if texts are not empty
                    await self.add_texts(texts)
                else:
                    logging.info("The texts file is empty. No texts loaded.")
        except FileNotFoundError:
            logging.warning("The texts file was not found. Database will be empty.")

    async def save_texts(self, filepath):
        """Saves texts to a file."""
        texts = []  # Placeholder for retrieving all documents
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(texts, f)
