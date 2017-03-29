from django.test import TestCase

from girox.event.models import Event


class EventModelTest(TestCase):
    def setUp(self):
        self.title = 'Evento 1'
        self.event = Event.objects.create(
            title=self.title,
            description='Descrição do Evento...'
        )

    def test_create(self):
        self.assertTrue(Event.objects.exists())

    def test_str(self):
        self.assertEqual(self.title, str(self.event))