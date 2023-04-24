

import unittest
from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()#передача контекста
        self.ctx.push()#использует вызванный контекст
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()#прекращает использовать вызванный контекст

    def test_form(self):
        response = self.client.post("/qb", data={"num_1": "3"})
        assert response.status_code == 200

    def test_form1(self):
        response = self.client.post("/bq", data={"num_2": "2", "num_3": "3"})
        assert response.status_code == 200

    def test_form2(self):
        response = self.client.post("/prizma", data={"num_7": "7", "num_8": "9"})
        assert response.status_code == 200

    def test_form3(self):
        response = self.client.post("/pyramid", data={"num_9": "7", "num_10": "9", "num_11": "11"})
        assert response.status_code == 200

    def test_form4(self):
        response = self.client.post("/cilindr", data={"num_12": "12", "num_13": "13", "num_14": "3"})
        assert response.status_code == 200

    def test_form5(self):
        response = self.client.post("/shar", data={"num_15": "15", "num_16": "1"})
        assert response.status_code == 200


if __name__ == "__main__":
    unittest.main()