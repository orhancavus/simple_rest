import sys
import unittest
import json

#sys.path.append('..')  # Add parent directory to path

from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello from Python Flask")

    def test_get_data(self):
        response = self.client.get('/api/data')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'John')
        self.assertEqual(data['age'], 30)
        self.assertEqual(data['city'], 'New York')       

if __name__ == '__main__':
    unittest.main() 