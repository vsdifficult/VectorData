from flask import Flask, request, jsonify
from storage.document_manager import DocumentManager
from indexer.vector_indexer import VectorIndexer
from model.text_model import TextModel
from utils.logger import logger
from utils.validators import Validators
from config import Config

app = Flask(__name__)
document_manager = DocumentManager(Config.DATABASE_PATH)
vector_indexer = VectorIndexer()
text_model = TextModel()

# Caching for transformed vectors
vector_cache = {}

@app.route('/add', methods=['POST'])
def add_document():
    data = request.json
    try:
        doc_id = data['id']
        text = data['text']
        Validators.validate_text(text)
        
        # Validate unique document ID
        existing_ids = document_manager.get_all_documents()['id'].tolist()
        Validators.validate_document_id(doc_id, existing_ids)
        
        # Check cache for vector
        if text in vector_cache:
            vector = vector_cache[text]
        else:
            vector = text_model.transform([text])[0]
            vector_cache[text] = vector
        
        document_manager.add_documents([(doc_id, text, vector)])
        vector_indexer.add_vectors([vector], [doc_id])
        logger.info(f"Document {doc_id} added successfully.")
        return jsonify({"message": "Document added successfully."}), 201
    except Exception as e:
        logger.error(f"Error adding document: {e}")
        return jsonify({"error": str(e)}), 400

@app.route('/search', methods=['POST'])
def search():
    query = request.json['query']
    try:
        Validators.validate_text(query)
        
        # Check cache for query vector
        if query in vector_cache:
            query_vector = vector_cache[query]
        else:
            query_vector = text_model.transform([query])[0]
            vector_cache[query] = query_vector
        
        results, distances = vector_indexer.search(query_vector)
        return jsonify({"results": results, "distances": distances}), 200
    except Exception as e:
        logger.error(f"Error searching documents: {e}")
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
