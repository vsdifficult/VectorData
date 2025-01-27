import pandas as pd
import os

class VectorDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        if os.path.exists(db_path):
            self.data = pd.read_csv(db_path)
        else:
            self.data = pd.DataFrame(columns=['id', 'text', 'vector'])

    def add_document(self, doc_id, text, vector):
        self.data = self.data.append({'id': doc_id, 'text': text, 'vector': vector}, ignore_index=True)
        self.save()

    def save(self):
        self.data.to_csv(self.db_path, index=False)

    def get_all_documents(self):
        return self.data