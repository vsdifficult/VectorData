import numpy as np
from .index import Index
from .storage import Storage

class VectorDB:
    def __init__(self, index_type='brute_force', storage_type='in_memory'):
        self.index = Index(index_type)
        self.storage = Storage(storage_type)

    def insert(self, vector, id):
        self.storage.insert(vector, id)
        self.index.insert(vector, id)

    def search(self, query_vector, k=1):
        return self.index.search(query_vector, k)

    def delete(self, id):
        self.storage.delete(id)
        self.index.delete(id)

    def update(self, vector, id):
        self.storage.update(vector, id)
        self.index.update(vector, id)

    def get_all_vectors(self):
        return self.storage.get_all_vectors()

    def get_all_ids(self):
        return self.storage.get_all_ids()