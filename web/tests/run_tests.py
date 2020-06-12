import unittest
import requests

WEB_URL = "http://web:8080/"

class BasicTests(unittest.TestCase):
    def test_index_page_responds_200(self):
        req = requests.get(WEB_URL)
        self.assertEqual(req.status_code, 200, "main page should respond 200")
        
    def test_urls_page_responds_200(self):
        req = requests.get(WEB_URL + "urls")
        self.assertEqual(req.status_code, 200, "main page should respond 200")

if __name__ == "__main__":
    unittest.main()
