# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('rg', models.CharField(max_length=20, verbose_name='RG')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('phone', models.CharField(max_length=20, verbose_name='telefone')),
                ('city', models.CharField(max_length=255, verbose_name='cidade-UF')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'inscrição',
                'verbose_name_plural': 'inscrições',
            },
        ),
    ]
