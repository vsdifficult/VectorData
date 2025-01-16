import numpy as np
from sklearn.neighbors import NearestNeighbors

class Index:
    def __init__(self, index_type):
        self.index_type = index_type
        if index_type == 'brute_force':
            self.index = BruteForceIndex()
        elif index_type == 'ann':
            self.index = ANNIndex()
        else:
            raise ValueError('Invalid index type')

    def insert(self, vector, id):
        self.index.insert(vector, id)

    def search(self, query_vector, k=1):
        return self.index.search(query_vector, k)

    def delete(self, id):
        self.index.delete(id)

    def update(self, vector, id):
        self.index.update(vector, id)

class BruteForceIndex:
    def __init__(self):
        self.vectors = []
        self.ids = []

    def insert(self, vector, id):
        self.vectors.append(vector)
        self.ids.append(id)

    def search(self, query_vector, k=1):
        similarities = []
        for i, vector in enumerate(self.vectors):
            similarity = np.dot(query_vector, vector) / (np.linalg.norm(query_vector) * np.linalg.norm(vector))
            similarities.append((similarity, self.ids[i]))
        similarities.sort(reverse=True)
        return [self.vectors[i] for _, i in similarities[:k]]

    def delete(self, id):
        index = self.ids.index(id)
        del self.vectors[index]
        del self.ids[index]

    def update(self, vector, id):
        index = self.ids.index(id)
        self.vectors[index] = vector

class ANNIndex:
    def __init__(self):
        self.index = NearestNeighbors(n_neighbors=1, algorithm='brute')

    def insert(self, vector, id):
        self.index.fit([vector])

    def search(self, query_vector, k=1):
        distances, indices = self.index.kneighbors([query_vector])
        return [self.index.data[i] for i in indices[0]]

    def delete(self, id):
        raise NotImplementedError

    def update(self, vector, id):
        raise NotImplementedError