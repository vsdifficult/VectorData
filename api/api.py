from flask import Flask, request, jsonify
from storage.document_manager import DocumentManager
from indexer.vector_indexer import VectorIndexer
from model.text_model import TextModel
from utils.logger import logger
from utils.validators import Validators
from config import Config

app = Flask(__name__)
document_manager = DocumentManager(Config.DATABASE_PATH)
vector_indexer = VectorIndexer(dimension=Config.VECTOR_DIMENSION)
text_model = TextModel()

@app.route('/add', methods=['POST'])
def add_document():
    data = request.json
    try:
        doc_id = data['id']
        text = data['text']
        Validators.validate_text(text)
        vector = text_model.transform([text])[0]
        document_manager.add_document(doc_id, text, vector)
        vector_indexer.add_vectors([vector])
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
        query_vector = text_model.transform([query])[0]
        indices, distances = vector_indexer.search(query_vector)
        results = document_manager.database.data.iloc[indices]
        return jsonify({"results": results.to_dict(orient='records'), "distances": distances.tolist()}), 200
    except Exception as e:
        logger.error(f"Error searching documents: {e}")
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)