
from app import create_app
import unittest
import requests


app = create_app()


class TestApi(unittest.TestCase):
    URL = "http://127.0.0.1:5000/post"

    #check if respnse is 200
    # def test_index(self):
    #     tester = app.test_client(self)
    #     response=tester.get("/register")
    #     statuscode = response.status_code
    #     self.assertEqual(statuscode,200)

    def test_post(self):
        resp = requests(self.URL)
        self.assertEqual(resp.status_code,200)


    


if __name__ == "__main__":
    unittest.main()
