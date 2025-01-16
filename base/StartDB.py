import numpy as np

class Base: 
    def __init__(self):
        self.vectors = {} 
        self.index = {}

    def search(self, query_vector, k=1): 
        similarities = {} 
        for i, vector in enumerate(self.vectors): 
            similarity = np.dot(query_vector, vector) / (np.linalg.norm(query_vector) * np.linalg.norm(vector))
            similarities.append((similarity, i))
        similarities.sort(reverse=True)
        return [self.vectors[i] for _, i in similarities[:k]]
    
    def select(self, id): 
        index = self.index[id] 
        return self.vectors[index]

    def insert(self, vector, id):  
        if vector is not None: 
            self.vectors.append(vector) 
            self.index[id] = len(self.vectors) - 1 

    def delete(self, id): 
        index = self.index[id] 
        del self.vectors[index] 
        del self.index[id]
