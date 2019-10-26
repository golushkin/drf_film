from django.test import TestCase

API = '/api/v1/'

USER_DATA = {
    'username':'test_user',
    'password':'test_password123A'
}

class ManTest(TestCase):

    def get_token(self):
        res = self.client.post(API+'user/', {**USER_DATA})
        return 'Token {}'.format(res.json()['auth_token'])

    def test_man_get_list(self):
        res = self.client.get(API+'man/')
        self.assertEqual([], res.json())

    def test_man_create_err_unauthenticated(self):
        res = self.client.post(API+'man/', {})
        self.assertEqual(401, res.status_code)

    def test_man_create_err_invalid_data(self):
        res = self.client.post(
            API+'man/',
            {"first_name":1},
            HTTP_AUTHORIZATION=self.get_token()
        )
        self.assertEqual(400, res.status_code)

    def test_man_create_success(self):
        res = self.client.post(
            API+'man/',
            {
                "first_name":"Test",
                "last_name":"Test",
            },
            HTTP_AUTHORIZATION=self.get_token()
        )
        self.assertEqual(201, res.status_code)


class ManDetailTest(TestCase):

    def get_token(self, user_data=USER_DATA):
        res = self.client.post(API+'user/', {**user_data})
        return 'Token {}'.format(res.json()['auth_token'])       

    def test_man_detail_get_person_empty(self):
        res = self.client.get(API+'man/')
        self.assertEqual([], res.json())

    def test_man_detail_get_person(self):
        self.client.post(
            API+'man/',
            {
                "first_name":"Test",
                "last_name":"Test",
            },
            HTTP_AUTHORIZATION=self.get_token()
        )
        res = self.client.get(API+'man/')
        self.assertEqual(1, len(res.json()))

    def test_man_detail_delete_person_err(self):
        self.client.post(
            API+'man/',
            {
                "first_name":"Test",
                "last_name":"Test",
            },
            HTTP_AUTHORIZATION=self.get_token()
        )

        res = self.client.delete(API+'man/1/')
        self.assertEqual(401, res.status_code)

    def test_man_detail_delete_person_forbidden(self):
        self.client.post(
            API+'man/',
            {
                "first_name":"Test",
                "last_name":"Test",
            },
            HTTP_AUTHORIZATION=self.get_token()
        )

        res = self.client.delete(
            API+'man/1/',
            HTTP_AUTHORIZATION=self.get_token(
                {"username":"test1","password":"test123A"}
            )
        )
        self.assertEqual(403, res.status_code)

    def test_man_detail_delete_person_success(self):
        token = self.get_token()
        self.client.post(
            API+'man/',
            {
                "first_name":"Test",
                "last_name":"Test",
            },
            HTTP_AUTHORIZATION=token
        )
        res = self.client.delete(API+'man/1/',HTTP_AUTHORIZATION=token)
        self.assertEqual(204, res.status_code) 


class UserTest(TestCase):

    def test_create_err_method(self):
        res = self.client.get(API+'user/')
        self.assertEqual(405, res.status_code)

    def test_create_err_data(self):
        res = self.client.post(API+'user/', {})
        self.assertEqual(400, res.status_code)

    def test_create_success(self):
        res = self.client.post(
            API+'user/',
            {
                'username':'test',
                'password':'test'
            }
        )
        self.assertEqual(201, res.status_code)