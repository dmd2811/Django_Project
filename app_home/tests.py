from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home_page_status(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)