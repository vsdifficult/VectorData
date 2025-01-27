import faiss
import numpy as np

class VectorIndexer:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)

    def add_vectors(self, vectors):
        self.index.add(np.array(vectors, dtype=np.float32))

    def search(self, query_vector, k=5):
        distances, indices = self.index.search(np.array([query_vector], dtype=np.float32), k)
        return indices[0], distances[0]