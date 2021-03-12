import unittest
import requests

WEB_URL = "http://web:8080"


class BasicTests(unittest.TestCase):
    def test_pages_respond_200(self):
        pages = [
            "/",
            "/forms/email-subscription",
            "/forms/more",
            "/forms/signin",
            "/forms/signin-email",
            "/forms/signup",
            "/other",
            "/readability",
            "/urls",
            "/slow-client-loading",
            "/replace-state",
        ]

        for page in pages:
            req = requests.get(WEB_URL + page)
            self.assertEqual(
                req.status_code, 200, '"{}" should respond 200'.format(page)
            )


if __name__ == "__main__":
    unittest.main()
