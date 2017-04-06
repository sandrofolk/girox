from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.utils import timezone

from girox.event.models import Event


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title='Evento 1',
            description='Descrição do evento...',
            date=timezone.now(),
            date_limit_subscription=timezone.now()
        )
        self.event.subscription_set.create(
            name='Participante 1',
            rg='1234567890',
            cpf='12345678901',
            email='email@email.com',
            phone='(012) 3 4567-8900',
            date_of_birth=timezone.now().date(),
            address='Rua teste',
            city='Apucarana-PR'
        )
        self.resp = self.client.get(r('events:subscription_detail', self.event.pk, self.event.subscription_set.first().pk))

    def test_get(self):
        """ GET /eventos/inscricao/1/1/ must return status code 200 """
        self.assertEqual(200, self.resp.status_code)
