from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.utils import timezone

from girox.event.models import Event


class EventDetailGet(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title='Evento 1',
            description='Descrição do evento...',
            date=timezone.now(),
            date_limit_subscription=timezone.now()
        )
        self.resp = self.client.get(r('events:event_detail', self.event.pk))

    def test_get(self):
        """ GET /eventos/1/ must return status code 200 """
        self.assertEqual(200, self.resp.status_code)
