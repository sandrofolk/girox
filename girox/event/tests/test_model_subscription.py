from django.test import TestCase
from datetime import datetime
from django.shortcuts import resolve_url as r

from girox.event.models import Event, Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        # self.event = Event.objects.create(
        #     title='Evento 1',
        #     description='Descrição do Evento...'
        # )
        # self.name = 'Participante 1'
        # self.event.subscription_set.create(
        #     name=self.name,
        #     rg='1234567890',
        #     email='email@email.com',
        #     phone='(012) 3 4567-8900',
        #     city='Apucarana-PR'
        # )

        self.name = 'Participante 1'
        self.subscription = Subscription.objects.create(
            name=self.name,
            rg='1234567890',
            email='email@email.com',
            phone='(012) 3 4567-8900',
            city='Apucarana-PR'
        )

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """ Subscription must have an auto created_at attr. """
        self.assertIsInstance(self.subscription.created_at, datetime)

    def test_str(self):
        # self.assertEqual(self.name, str(self.event.subscription_set.first()))
        self.assertEqual(self.name, str(self.subscription))

    def test_get_absolute_url(self):
        url = r('events:subscription_detail', self.subscription.pk)
        self.assertEqual(url, self.subscription.get_absolute_url())
