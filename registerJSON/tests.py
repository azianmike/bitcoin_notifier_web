from django.test import TestCase
from django.test import Client
from registerJSON.models import Person
# Create your tests here.


class RegisterTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_successful_register(self):
        response = self.c.post('/registerJSON/', {'email':'test', 'password':'test hash pw'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, '{"success": 1}')

    def test_unsuccessful_register(self):
        response = self.c.post('/registerJSON/', {'email':'test', 'password':'test hash pw'})
        response = self.c.post('/registerJSON/', {'email':'test', 'password':'test hash pw'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, '{"success": 0}')
        
