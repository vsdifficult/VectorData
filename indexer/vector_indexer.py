import numpy as np
from model.text_model import TextModel

class VectorIndexer:
    def __init__(self):
        self.vectors = []
        self.documents = []
        self.text_model = TextModel()

    def add_vectors(self, vectors, documents):
        self.vectors.extend(vectors)
        self.documents.extend(documents)

    def search(self, query, k=5):
        query_vector = self.text_model.transform([query])[0]
        distances = [np.linalg.norm(np.array(vec) - np.array(query_vector)) for vec in self.vectors]
        indices = np.argsort(distances)[:k]
        return [self.documents[i] for i in indices], [distances[i] for i in indices]
