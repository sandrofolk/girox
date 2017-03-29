from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTeste(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEquals(200, self.response.status_code)
