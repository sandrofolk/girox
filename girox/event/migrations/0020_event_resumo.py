# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0019_auto_20170416_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='resumo',
            field=models.TextField(blank=True, null=True, verbose_name='resumo'),
        ),
    ]
