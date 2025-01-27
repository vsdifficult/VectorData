import unittest
import json
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_document(self):
        response = self.app.post('/add', json={'id': '1', 'text': 'Sample document text.'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Document added successfully.', response.get_data(as_text=True))

    def test_add_duplicate_document(self):
        self.app.post('/add', json={'id': '1', 'text': 'Sample document text.'})
        response = self.app.post('/add', json={'id': '1', 'text': 'Another document text.'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Document ID must be unique.', response.get_data(as_text=True))

    def test_search_document(self):
        self.app.post('/add', json={'id': '2', 'text': 'Another sample document.'})
        response = self.app.post('/search', json={'query': 'Another sample document.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
