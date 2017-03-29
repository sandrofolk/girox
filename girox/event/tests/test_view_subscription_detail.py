from django.test import TestCase
from django.shortcuts import resolve_url as r

from girox.event.models import Event


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title='Evento 1',
            description='Descrição do evento...'
        )
        self.event.subscription_set.create(
            name='Participante 1',
            rg='1234567890',
            email='email@email.com',
            phone='(012) 3 4567-8900',
            city='Apucarana-PR'
        )
        self.resp = self.client.get(r('events:subscription_detail', self.event.subscription_set.first().pk))
