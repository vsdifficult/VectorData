import numpy as np 

class Storage: 
    def __init__(self, storage_type):
        self.storage_type = storage_type 
        if storage_type == "in_memory": 
              self.storage = InMemoryStorage() 
        elif storage_type == "on_disk": 
            self.storage = OnDiskStorage() 
            
    def insert(self, vector, id):
        self.storage.insert(vector, id)

    def delete(self, id):
        self.storage.delete(id)

    def update(self, vector, id):
        self.storage.update(vector, id)

    def get_all_vectors(self):
        return self.storage.get_all_vectors()

    def get_all_ids(self):
        return self.storage.get_all_ids()

class OnDiskStorage:
    def __init__(self):
        self.file_name = 'vectors.db'

    def insert(self, vector, id):
        with open(self.file_name, 'a') as f:
            f.write(f"{id},{','.join(map(str, vector))}\n")

    def delete(self, id):
        lines = []
        with open(self.file_name, 'r') as f:
            lines = f.readlines()
        with open(self.file_name, 'w') as f:
            for line in lines:
                if not line.startswith(f"{id},"):
                    f.write(line)

    def update(self, vector, id):
        lines = []
        with open(self.file_name, 'r') as f:
            lines = f.readlines()
        with open(self.file_name, 'w') as f:
            for line in lines:
                if line.startswith(f"{id},"):
                    f.write(f"{id},{','.join(map(str, vector))}\n")
                else:
                    f.write(line)

    def get_all_vectors(self):
        vectors = []
        with open(self.file_name, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                vectors.append(np.array(list(map(float, parts[1:]))))
        return vectors

    def get_all_ids(self):
        ids = []
        with open(self.file_name, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                ids.append(int(parts[0]))
        return ids
    
class InMemoryStorage:
    def __init__(self):
        self.vectors = []
        self.ids = []

    def insert(self, vector, id):
        self.vectors.append(vector)
        self.ids.append(id)

    def delete(self, id):
        index = self.ids.index(id)
        del self.vectors[index]
        del self.ids[index]

    def update(self, vector, id):
        index = self.ids.index(id)
        self.vectors[index] = vector

    def get_all_vectors(self):
        return self.vectors

    def get_all_ids(self):
        return self.ids