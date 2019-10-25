from django.test import TestCase

API = '/api/v1/'

class ManTest(TestCase):

    def test_man_get_list(self):
        res = self.client.get(API+'man/')
        self.assertEqual([], res.json())

    def test_man_create_err(self):
        res = self.client.post(API+'man/', {})
        self.assertEqual(400, res.status_code)

    def test_man_create_err_invalid_data(self):
        res = self.client.post(API+'man/', {"first_name":1})
        self.assertEqual(400, res.status_code)

    def test_man_create_success(self):
        res = self.client.post(
            API+'man/',
            {
                "first_name":"Test",
                "last_name":"Test",
            }
        )
        print(res.json())
        self.assertEqual(201, res.status_code)