from django.test import TestCase
from django.utils import timezone
from django.shortcuts import resolve_url as r

from girox.event.models import Event


class RegulationReprintGet(TestCase):
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

        self.resp = self.client.get(r('events:subscription_regulation', self.event.pk))

    def test_get(self):
        """ GET /eventos/regulamento/1/ must return status code 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ Must use event/subscription_regulation.html """
        self.assertTemplateUsed(self.resp, 'event/subscription_regulation.html')

    def test_html(self):
        """ Html must contain input tags """
        tags = (
            ('<form', 1),
            ('<input', 2),
            ('type="number"', 1),
            ('type="submit"', 1)
        )
        for text, count, in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """ Html must contain csrf """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


class RegulationReprintPostValid(TestCase):
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
        self.cpf = self.event.subscription_set.first().cpf

        data = dict(cpf=self.cpf, event=self.event.pk)

        self.resp = self.client.post(r('events:subscription_regulation', self.event.pk), data)

    def test_post(self):
        """Valid POST should redirect to /static/pdf/Termo_de_Responsabilidade.pdf/"""
        # 302 = redirect
        self.assertEqual(302, self.resp.status_code)
