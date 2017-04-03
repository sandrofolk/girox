from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEquals(200, self.response.status_code)


class ContactTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('contact'))

    def test_get(self):
        """GET /contato/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ Must use frontend/contact.html """
        self.assertTemplateUsed(self.resp, 'frontend/contact.html')
