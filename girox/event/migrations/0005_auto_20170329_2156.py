# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 21:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_subscription_event'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([('rg', 'event')]),
        ),
    ]
