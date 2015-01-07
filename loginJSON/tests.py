from django.test import TestCase
from django.test import Client
from registerJSON.models import Person
import json
# Create your tests here.


class LoginTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_successful_login(self):
        response = self.c.post('/registerJSON/', {'email':'test', 'password':'test hash pw'})
        response = self.c.post('/loginJSON/', {'email':'test', 'password':'test hash pw'})
        self.assertEquals(response.status_code, 200)
        returnJSON = json.loads(response.content)
        self.assertEquals(1, returnJSON['success'])

    def test_unsuccessful_login_user_does_not_exist(self):
        response = self.c.post('/loginJSON/', {'email':'not a valid email', 'password':'wrong password'})
        self.assertEquals(response.status_code, 200)
        returnJSON = json.loads(response.content)
        self.assertEquals(0, returnJSON['success'])


    def test_unsuccessful_login_wrong_password(self):
        response = self.c.post('/registerJSON/', {'email':'test', 'password':'test hash pw'})
        response = self.c.post('/loginJSON/', {'email':'test', 'password':'wrong password'})
        self.assertEquals(response.status_code, 200)
        returnJSON = json.loads(response.content)
        self.assertEquals(0, returnJSON['success'])
