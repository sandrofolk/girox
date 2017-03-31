from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.utils import timezone

from girox.event.forms import SubscriptionForm
from girox.event.models import Event, Subscription


class SubscriptionNewGet(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title='Evento 1',
            description='Descrição do evento...',
            date=timezone.now(),
            date_limit_subscription=timezone.now()
        )
        self.resp = self.client.get(r('events:subscription_new', self.event.pk))

    def test_get(self):
        """ GET /eventos/inscricao/ must return status code 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ Must use event/subscription_form.html """
        self.assertTemplateUsed(self.resp, 'event/subscription_form.html')

    def test_html(self):
        """ Html must contain input tags """
        tags = (
            ('<form', 1),
            ('<input', 8),
            ('type="hidden"', 1),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1)
        )
        for text, count, in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """ Html must contain csrf """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have subscription form """
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscriptionsNewPostValid(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title='Evento 1',
            description='Descrição do evento...',
            date=timezone.now(),
            date_limit_subscription=timezone.now()
        )
        self.rg = '12345678901'
        data = dict(name='Participante 1', rg=self.rg,
                    email='email@email.com', phone='(012) 3 4567-8900',
                    city='Apucarana-PR', event=self.event.pk)
        self.resp = self.client.post(r('events:subscription_new', self.event.pk), data)

    def test_post(self):
        """Valid POST should redirect to /eventos/inscricao/1/"""
        # 302 = redirect
        self.assertEqual(302, self.resp.status_code)
        self.assertRedirects(self.resp, r('events:subscription_detail', self.event.pk, 1))

    # def test_send_subscribe_email(self):
    #     self.assertEqual(1, len(mail.outbox))
    #
    # def test_save_subscription(self):
    #     self.assertTrue(Subscription.objects.exists())
