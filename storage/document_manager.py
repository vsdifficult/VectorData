from storage.database import VectorDatabase

class DocumentManager:
    def __init__(self, db_path):
        self.database = VectorDatabase(db_path)

    def add_document(self, doc_id, text, vector):
        self.database.add_document(doc_id, text, vector)

    def get_all_documents(self):
        return self.database.get_all_documents()