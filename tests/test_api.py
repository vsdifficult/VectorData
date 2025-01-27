import unittest
import json
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_document(self):
        response = self.app.post('/add', json={'id': 1, 'text': 'Тестовый документ.'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Document added successfully.', response.get_data(as_text=True))

    def test_search_document(self):
        self.app.post('/add', json={'id': 2, 'text': 'Другой тестовый документ.'})
        response = self.app.post('/search', json={'query': 'тестовый'})
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(json.loads(response.get_data(as_text=True))['results']), 0)

if __name__ == '__main__':
    unittest.main()