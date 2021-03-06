# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'foto', 'verbose_name_plural': 'fotos'},
        ),
        migrations.AlterField(
            model_name='album',
            name='cover_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='gallery.Photo', verbose_name='foto de capa'),
        ),
        migrations.AlterField(
            model_name='album',
            name='order',
            field=models.PositiveIntegerField(default=9999, verbose_name='ordem'),
        ),
    ]
