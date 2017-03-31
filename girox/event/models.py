from django.db import models
from django.shortcuts import resolve_url as r


class Event(models.Model):
    title = models.CharField('título', max_length=255)
    description = models.TextField('descrição')
    date = models.DateTimeField('data do evento')
    date_limit_subscription = models.DateTimeField('data limite de inscrição')

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'

    def __str__(self):
        return self.title


class Subscription(models.Model):
    name = models.CharField('nome', max_length=255)
    rg = models.CharField('RG', max_length=20)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    city = models.CharField('cidade-UF', max_length=255)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        ordering = ('-created_at',)
        unique_together = ("rg", "event")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('events:subscription_detail', self.event.pk, self.pk)
