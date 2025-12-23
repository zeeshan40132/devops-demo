import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        # Create a test client for our Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # Send a GET request to the homepage
        response = self.app.get('/')
        # Assert that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        # Send a GET request
        response = self.app.get('/')
        # Assert that the word "Hello" is in the response text
        self.assertIn('Welcome', response.data.decode('utf-8'))

if __name__ == "__main__":
    unittest.main()