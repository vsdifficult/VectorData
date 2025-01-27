from storage.database import VectorDatabase

class DocumentManager:
    def __init__(self, db_path):
        self.database = VectorDatabase(db_path)

    def add_documents(self, documents):
        self.database.add_documents(documents)

    def get_all_documents(self):
        return self.database.get_all_documents()
