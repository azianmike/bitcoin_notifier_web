from django.test import TestCase
from django.test import Client


class RegisterTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_unsuccessful_email_does_not_exist(self):
        response = self.c.post('/submitAlertJSON/', {'email':'test'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, '{"success": 1}')

    def test_unsuccessful_successful(self):
        response = self.c.post('/submitAlertJSON/', {'email':'test'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, '{"success": 1}')
